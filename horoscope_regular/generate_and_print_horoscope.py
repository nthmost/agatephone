from datetime import datetime
from artery import MockArteryPrinter, ArteryPrinter
from artery import ConfessionReceipt, ReceiptImage, ReceiptText, CrazyText

import random
import datetime
import os


LOGO = "elysiumbell_receipt_logo.png"
COMPANY = "Community Capture Corporation"
MOTTO = "Connecting Voices Across Eternity"


# Function to print the receipt
def print_receipt(receipt):
    printer = ArteryPrinter()

    for obj in receipt.receipt:
        if isinstance(obj, ReceiptImage):
            printer.print_image(obj.filepath)
        elif isinstance(obj, ReceiptText):
            printer.print_text(obj.text, **obj.to_dict())
        elif isinstance(obj, CrazyText):
            printer.print_crazy_text(obj.text, **obj.to_dict())

    printer.finish()


# Zodiac sign determination based on birth date
def get_zodiac_sign(month, day):
    signs = [
        ("Capricorn", (1, 19)), ("Aquarius", (2, 18)), ("Pisces", (3, 20)), 
        ("Aries", (4, 19)), ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)), ("Virgo", (9, 22)),
        ("Libra", (10, 22)), ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (m, d) in signs:
        if (month == m and day <= d) or (month < m):
            return sign
    return "Capricorn"

# Pair setup phrases with matching endings for grammatical consistency
setup_endings_pairs = [
    ("Now is not a good time to", [
        "take a photocopy of your butt.",
        "challenge a raccoon to a dance-off.",
        "try to teach your cat how to play chess."
    ]),
    ("The stars advise you to avoid", [
        "reorganizing your sock drawer by astrological sign.",
        "starting a collection of antique toothbrushes.",
        "having a serious conversation with your toaster."
    ]),
    ("Consider postponing any plans to", [
        "declare yourself the ruler of the living room.",
        "dress up as a pirate and commandeer the neighbor's barbecue.",
        "convince your goldfish to run for public office."
    ]),
    ("Today is not ideal for", [
        "eating an entire cake just to prove a point.",
        "starting a new hobby involving jello sculptures.",
        "trying to communicate with pigeons using interpretive dance."
    ])
]

love_advice = [
    "Romance is in the air, but avoid grand gestures involving llamas.",
    "Your partner might not appreciate spontaneous karaoke, but do it anyway.",
    "Single? Now is the time to attract someone with your vast collection of bottle caps.",
    "Show love today by sharing your weirdest childhood story.",
    "Avoid arguments over whose imaginary friend was cooler as a kid.",
    "A heartfelt gesture could mean baking a cake, but don't use glitter this time."
]

# Get birthday input (for demo purposes, this can be hardcoded)
birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")

# Determine zodiac sign
zodiac_sign = get_zodiac_sign(birth_date.month, birth_date.day)

# Seed random generator with birth date for consistent uniqueness per person
random.seed(birth_date.toordinal())

# Generate a horoscope by combining phrases
def generate_horoscope():
    horoscope_lines = [f"Your sign is {zodiac_sign}."]

    # Generate the first three sentences by combining setups and matching endings
    for _ in range(3):
        setup, endings = random.choice(setup_endings_pairs)
        ending = random.choice(endings)
        horoscope_lines.append(f"{setup} {ending}")

    # Generate love advice
    love = random.choice(love_advice)
    horoscope_lines.append(love)

    return "\n".join(horoscope_lines)

def print_horoscope(horoscope):
    receipt = ConfessionReceipt(experience_text=horoscope, logo=LOGO, title="DEATH HOROSCOPE", 
                                header="DEATH HOROSCOPE", company="Elysium Bell", motto=MOTTO)
    receipt.build_receipt()
    return receipt


# Print or send to receipt printer
horoscope = generate_horoscope()
print(horoscope)


