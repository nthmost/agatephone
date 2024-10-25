from datetime import datetime
from artery import MockArteryPrinter, ArteryPrinter
from artery import ConfessionReceipt, ReceiptImage, ReceiptText, CrazyText

import random
import os

LOGO = "/usr/share/asterisk/agatephone/elysiumbell_receipt_logo.png"
COMPANY = "Elysium Bell"
MOTTO = "Connecting Voices Across Eternity"

POEM_DIR = "/usr/share/asterisk/agatephone/poems"


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


def pick_poem(confession_score):
    poems = os.listdir(POEM_DIR)
    text = open(os.path.join(POEM_DIR, random.choice(poems))).read()
    return text


def stripped_down_receipt(confession_score):
    poem = pick_poem(confession_score)
    receipt = ConfessionReceipt(experience_text=poem, logo=LOGO, title="YOUR PENANCE", 
                                header="YOUR PENANCE", company="Elysium Bell", motto=MOTTO)
    receipt.build_receipt()
    return receipt


# decided not to bother actually scoring confessions, just picking a random poem works well enough. :-)
print_receipt(stripped_down_receipt(100))

