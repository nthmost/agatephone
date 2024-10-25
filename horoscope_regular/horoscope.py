import random
import datetime

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

# Stereotypical qualities and advice for each sign
sign_identity_advice = {
    "Aries": "All Aries are brave and impulsive, so remember that not every wall needs to be broken through—sometimes doors work too.",
    "Taurus": "All Taurus are stubborn and loyal, so consider letting someone else choose the restaurant for once—you might just love it.",
    "Gemini": "All Geminis are adaptable and curious, so resist the urge to start 17 new projects today—maybe just stick to 5.",
    "Cancer": "All Cancers are emotional and nurturing, so it's okay if not everyone wants a hug—offer snacks instead.",
    "Leo": "All Leos are confident and dramatic, so try to keep the soliloquies under five minutes this time—brevity is the soul of wit.",
    "Virgo": "All Virgos are practical and detail-oriented, so remember, sometimes a little chaos can be good—your to-do list doesn't need to include 'relax.'",
    "Libra": "All Libras are charming and indecisive, so flip a coin if you must, but make a decision before your coffee gets cold.",
    "Scorpio": "All Scorpios are intense and mysterious, so let someone in on one of your secrets today—just one, not all of them.",
    "Sagittarius": "All Sagittarius are adventurous and honest, so think before you speak—some truths don't need to be shared with the grocery cashier.",
    "Capricorn": "All Capricorns are ambitious and disciplined, so take a moment to appreciate what you've already accomplished—ambition is a journey, not a sprint.",
    "Aquarius": "All Aquarius are innovative and unpredictable, so write down your wildest idea today—just don't try to patent it... yet.",
    "Pisces": "All Pisces are dreamy and compassionate, so give yourself a break from saving everyone—maybe start with saving that leftover pizza."
}

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
    ]),
    ("The look on your face will be priceless when", [
        "you try to explain quantum physics to your dog.",
        "you find out the cake really *was* a lie.",
        "you realize you've been talking to a mannequin for 10 minutes."
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

# Positive phrases for something good on the horizon
positive_phrases = [
    "A new adventure is just around the corner.",
    "Good fortune is just around the corner.",
    "A pleasant surprise is just around the corner.",
    "An exciting opportunity is just around the corner.",
    "A creative breakthrough is just around the corner.",
    "A moment of clarity is just around the corner.",
    "A fun new friendship is just around the corner."
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

    # Identity statement with advice
    identity_advice = sign_identity_advice[zodiac_sign]
    horoscope_lines.append(identity_advice)

    # Generate two sentences by combining setups and matching endings
    for _ in range(2):
        setup, endings = random.choice(setup_endings_pairs)
        ending = random.choice(endings)
        horoscope_lines.append(f"{setup} {ending}")

    # Add positive phrase
    positive = random.choice(positive_phrases)
    horoscope_lines.append(positive)

    # Generate love advice
    love = random.choice(love_advice)
    horoscope_lines.append(love)

    return "\n".join(horoscope_lines)

# Print or send to receipt printer
horoscope = generate_horoscope()
print(horoscope)

# Optionally, use a function here to send the generated horoscope to a receipt printer
# def print_receipt(text):
#     # Example using a receipt printer
#     # Replace with actual code to interface with your specific printer
#     with open("/dev/usb/lp0", "w") as printer:
#         printer.write(text)

# print_receipt(horoscope)

