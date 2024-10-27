# death_horoscope.py
import random

# California Zodiac of Death signs with the same date ranges as traditional zodiac
def get_california_zodiac_sign(month, day):
    signs = [
        ("California Condor", (1, 19)), ("Common Raven", (2, 18)), ("Starfish", (3, 20)), 
        ("Turkey Vulture", (4, 19)), ("Western Gull", (5, 20)), ("Isopod", (6, 20)),
        ("Dungeness Crab", (7, 22)), ("Pacific Octopus", (8, 22)), ("Grey Wolf", (9, 22)),
        ("Hagfish", (10, 22)), ("Sea Cucumber", (11, 21)), ("Carrion Beetle", (12, 21)),
        ("California Condor", (12, 31))
    ]
    for sign, (m, d) in signs:
        if (month == m and day <= d) or (month < m):
            return sign
    return "California Condor"

# Stereotypical qualities and advice for each California Zodiac of Death sign
california_sign_identity_advice = {
    "California Condor": "All California Condors know the wind may carry you far, but home is where your homies are. Embrace the distance, but remember your tribe.",
    "Common Raven": "All Ravens are masters of survival. Laugh at the chaos, but don’t get too close to the flames; being clever is one thing, getting burnt is another.",
    "Starfish": "All Starfish regrow what's been lost. Painful, but proof you’re still here; just try not to grow too many heads at once, it gets confusing.",
    "Turkey Vulture": "All Vultures turn loss into gain. Take what you need, but leave the bones; a little seasoning never hurt, but don’t overdo it.",
    "Western Gull": "All Gulls know tides bring and take. Hold lightly; the sea doesn’t care, especially about your fries, but it’s still worth trying.",
    "Isopod": "All Isopods thrive in shadows. Your work is unseen but vital; cleaning up dead fish isn’t glamorous, but it’s necessary art.",
    "Dungeness Crab": "All Crabs grip tight. Let go of what's not worth the pinch; nobody likes a crabby crab, but they love a determined one.",
    "Pacific Octopus": "All Octopi wear many masks. Today, let a mask slip into the abyss; poets will be intrigued, and mystery is your strength.",
    "Grey Wolf": "All Wolves need packs but cherish solitude too. Trust both the group and your lone howl; balance is everything.",
    "Hagfish": "All Hagfish find purpose in the decay, carving beauty from the grotesque. Rest easy knowing slime-making counts as self-care.",
    "Sea Cucumber": "All Sea Cucumbers transform the worst into something useful. To create something like you, however, requires you to spill your guts.",
    "Carrion Beetle": "All Carrion Beetles find beauty in endings. Dig deep, share your findings; gross can be great, especially if it causes shifts in others."
}

# Pair setup phrases with matching endings for grammatical consistency
setup_endings_pairs = [
    ("The sea urchin boom in Monterey gives you a chance to", [
        "let go of what's gone and make room for growth; nothing good grows from holding onto rot.",
        "turn decay into new beginnings; make the most of what’s left behind.",
        "reflect on endings as starts; use them wisely, even if they’re prickly.",
        "build anew from what's fallen; just watch for spines—they sting."
    ]),
    ("Invasive ivy takes down yet another cypress tree in the Presidio; this the perfect moment to", [
        "use rot as fuel for your next chapter; dead things still nourish.",
        "embrace beauty in odd places, even if it’s not supposed to be there.",
        "let go and make space for something new without forgetting your values.",
    ]),
    ("Humpback whales migrating means it's time to", [
        "follow your instincts, even if it means a dramatic breach; the splash is worth it.",
        "focus on the journey, not the destination; splash along the way.",
        "let the tides push you forward; just don’t get stranded on the rocks.",
        "enjoy peaceful moments between long swims; snack breaks are essential."
    ]),
    ("The mushroom bloom in the damp forest suggests", [
        "turning rot into something fertile; decay feeds rebirth.",
        "past failures can nourish new ideas; let the spores spread.",
        "endings always feed beginnings; spores understand this better than most."
    ]),
    ("Hemlock blooms across forbidden places—an invitation to", [
        "embrace dark beauty; just don’t eat it, unless you like hospital visits.",
        "find strength in unlikely places; poison can still be pretty.",
        "tap into hidden power within; it’s often overlooked, but it’s always there."
    ]),
    ("The Pacific Plate pushes granite northwards in Point Reyes, signaling", [
        "for you to rediscover your past; just watch your step, some trails have dropped into the ocean.",
        "the right moment for you to question your foundations while realizing bedrock is still bedrock.",
    ]),
    ("Autumn fog settles in musty redwoods; take a moment to", [
        "mark the changing of the seasons by shopping at Target.",
        "reflect on what matters. Just try not to walk into anything solid.",
        "embrace the unclear path. The journey matters more than clarity sometimes.",
        "trust you’ll find your way. If you get lost, it’ll make a good story."
    ]),
    ("With the tides pulling back at sunset, it's time to", [
        "release what you cling to; just don’t get swept away yourself.",
        "see beauty in ebb and flow; sunsets make everything softer.",
        "step back, reassess, and prepare for return; avoid the sharp shells."
    ]),
    ("Now is not the time to", [
        "make promises you can’t keep; ghosts may forgive, but they remember.",
        "whisper secrets to ghosts; they’re bad at keeping them, and worse at forgetting.",
        "challenge eternity; it’s busy, and you’re not on its schedule."
    ])
]

# Love advice (melancholy, yet wryly humorous)
love_advice = [
    "Romance is in the air, faint like a ghost; be gentle with the past—it breaks easily.",
    "Your partner may not get your dark side today; maybe save the taxidermy talk for later.",
    "Single? Enjoy old laughter; echoes hold warmth, and no one’s demanding anything from you.",
    "Share a sad story today; there’s beauty in honesty. It’s also a good way to filter out the weak.",
    "Don’t argue about who left first; agree to haunt each other forever—it’s less paperwork.",
    "Hold someone's hand through the fog; if it slips away, maybe it’s just a ghost making their rounds."
]

# Positive phrases (melancholy optimism)
positive_phrases = [
    "A quiet understanding waits around the corner; it might be hiding under a rock, but it’s there.",
    "A twist in your story may hold truth; at least it’s a twist worth exploring.",
    "An unexpected bond is near, though brief; forever’s overrated anyway.",
    "A fleeting comfort is near; hold it close, or let it drift away—both are okay.",
    "A forgotten memory waits to remind you of something; maybe it’s embarrassing, maybe it’s not.",
    "Calm acceptance is close; face it, or let it wait—it’s not in a hurry.",
    "An old friend is near; perhaps just in your heart, but that’s still something."
]

# Reflective questions (to add contemplation to the reading)
reflective_questions = [
    "What old habits can you let go of to make space for something new?",
    "Are you holding onto something that no longer serves you?",
    "What transformation have you been resisting, and how can you embrace it?",
    "How can you use today to nurture something you've been neglecting?",
    "What beauty can you find in the endings that surround you?"
]

# Generate a horoscope by combining phrases
def generate_horoscope(date_str):
    # Parse the birthdate as month and day only
    date_str = date_str.strip()
    month = int(date_str[:2])
    day = int(date_str[2:])

    # Determine California Zodiac of Death sign
    zodiac_sign = get_california_zodiac_sign(month, day)

    # Seed random generator with month and day for consistent uniqueness per person
    seed_value = month * 100 + day
    random.seed(seed_value)

    horoscope_lines = [f"Deathday: {month}-{day}"]

    horoscope_lines.append(f"Your sign is {zodiac_sign}.")

    # Identity statement with advice (dark, wry, and a little melancholy)
    identity_advice = california_sign_identity_advice[zodiac_sign]
    horoscope_lines.append(identity_advice)

    # Generate one sentence by combining setups and matching endings (not "Now is not the time to")
    setup, endings = random.choice(setup_endings_pairs[:-1])
    ending = random.choice(endings)
    horoscope_lines.append(f"{setup} {ending}")

    # Add positive phrase (melancholy optimism)
    positive = random.choice(positive_phrases)
    horoscope_lines.append(positive)

    # Add "Now is not the time to" sentence towards the end
    setup, endings = setup_endings_pairs[-1]
    ending = random.choice(endings)
    horoscope_lines.append(f"{setup} {ending}")

    # Generate love advice (dark humor, wry)
    love = random.choice(love_advice)
    horoscope_lines.append(love)

    # Add reflective question to encourage contemplation
    question = random.choice(reflective_questions)
    horoscope_lines.append(question)

    return "\n".join(horoscope_lines)

# Quick test if run directly
if __name__ == "__main__":
    date_str = input("Enter your birth date (MMDD): ")
    try:
        horoscope = generate_horoscope(date_str)
        print(horoscope)
    except Exception as e:
        print(f"An error occurred: {e}")
