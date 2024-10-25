# generate_death_horoscope.py
import sys
import datetime
import os
from artery import ArteryPrinter, ConfessionReceipt, ReceiptImage, ReceiptText
from death_horoscope import generate_horoscope, get_california_zodiac_sign

LOGO = "/usr/share/asterisk/agatephone/elysiumbell_receipt_logo.png"
COMPANY = "Elysium Bell"
MOTTO = "Connecting Voices Across Eternity"

image_dir = "/usr/share/asterisk/agatephone/ElysiumBell_DeathHoroscope_Zodiac"

# Logging function
def log_horoscope(month, day, horoscope, success):
    zodiac_sign = get_california_zodiac_sign(int(month), int(day))
    log_path = "/var/log/common/horoscope_log.txt"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    horoscope_lines_count = len(horoscope.splitlines())
    with open(log_path, "a") as log_file:
        log_file.write(f"{now} | Death date: {date_str} | Zodiac sign: {zodiac_sign} | Lines in horoscope: {horoscope_lines_count} | Success: {success}\n")

# Function to print the horoscope to the receipt
def print_horoscope_to_receipt(month, day, horoscope):
    zodiac_sign = get_california_zodiac_sign(int(month), int(day))

    printer = ArteryPrinter()

    # Define the image file paths for each sign
    image_files = {
        "California Condor": "EB_california_condor.png",
        "Common Raven": "EB_raven.png",
        "Starfish": "EB_starfish.png",
        "Turkey Vulture": "EB_turkey_vulture.png",
        "Western Gull": "EB_gull.png",
        "Isopod": "EB_isopod.png",
        "Dungeness Crab": "EB_dungeness_crab.png",
        "Pacific Octopus": "EB_octopus.png",
        "Grey Wolf": "EB_wolf.png",
        "Hagfish": "EB_hagfish.png",
        "Sea Cucumber": "EB_sea_cucumber.png",
        "Carrion Beetle": "EB_carrion_beetle.png"
    }

    # Initialize the receipt
    receipt = ConfessionReceipt(
        experience_text=horoscope,
        logo=LOGO,
        title="YOUR DESTINY IN THE AFTERLIFE",
        header=zodiac_sign.upper(),
        company=COMPANY,
        motto=MOTTO
    )

    # Add the image for the zodiac sign
    image_path = os.path.join(image_dir, image_files.get(zodiac_sign, ""))
    if image_path:
        printer.print_image(image_path)

    receipt.build_receipt()

    # Print the receipt
    for obj in receipt.receipt:
        #print(f"Processing object: {obj}")  # Add this line to see what objects are present
        if isinstance(obj, ReceiptImage):
            printer.print_image(obj.filepath)
        elif isinstance(obj, ReceiptText):
            printer.print_text(obj.text, **obj.to_dict())

    printer.finish()


def sanitize_text(text):
    # Replace non-standard punctuation with standard versions
    replacements = {
        "‘": "'", "’": "'",  # Curly single quotes to straight
        "“": '"', "”": '"',  # Curly double quotes to straight
        "–": "-", "—": "-",  # Dashes to hyphen
        "…" : "..."          # Ellipsis to three dots
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text



# Main function
if __name__ == "__main__":
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    else:
        date_str = input("Enter your birth date (MMDD): ")

    month = date_str[:2]
    day = date_str[2:]
    #print("Death date selected:", month, day)
    horoscope = generate_horoscope(date_str)
    horoscope = sanitize_text(horoscope)
    print_horoscope_to_receipt(month, day, horoscope) 
    log_horoscope(month, day, horoscope, success=True)

