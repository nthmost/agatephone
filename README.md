# Elysium Bell: Connecting Voices Across Eternity

## The Agatephone project

Imagine a rotary phone whose base and handset are made mostly out of solid agate.

Now imagine this phone on a pedestal, surrounded by an ethereal glow.

First you're going to have to learn (or remember) how to dial a rotary phone.  Maybe you dial 0, which takes you "the operator".  Maybe you dial 666, which takes you...somewhere else...

![An ornately hand-lettered paper sign says "Dial any 3 numbers. Confused? Find an adult!"](https://github.com/nthmost/agatephone/blob/main/EB_photos/instructions.jpg)

The phone is a "portal" into an unseeable pocket universe, with its own rules, values, and priorities.

## For Artists and Patrons of the Arts

The Agatephone is an interactive art installation that invites participants to explore themes of mortality, rebirth, and identity through the lens of California's ecosystem. Using a rotary phone and a receipt printer, visitors are drawn into a poetic experience that blends folklore with dark humor, offering a personalized “death horoscope” as a memento of the encounter.

![A warm candle illuminates a printed strip of receipt paper containing a Starfish and a horoscope for March 14th.](https://github.com/nthmost/agatephone/blob/main/EB_photos/horoscope_yellow.jpg)

## For Engineers and Tech Art Enthusiasts

Agatephone combines a vintage rotary phone, Asterisk-powered telephony, and Python-driven dynamic horoscopes to create a captivating interactive piece. At its core, the project involves a unique "California Zodiac of Death," where customized horoscopes are generated based on participant input and printed on thermal receipt paper, blending analog devices with digital creativity.


### Hardware

* Minimal Linux box w/ low power draw
* [S100i (iaxy)](https://www.voipon.co.uk/documents/digium_iaxy_brochure.pdf)
* rotary phone
* Bluetti EB3A power station
* small USB thermal printer

### Software

* [Asterisk telephony OSS](https://www.asterisk.org/)
* [nthmost/artery-thermal](https://github.com/nthmost/artery-thermal) (github repo)
* generated voice prompts via OpenAI TTS

## Project Overview

The Agatephone Project is an interactive installation exploring life cycles and existential reflection through an evocative, morbid-humor-laden California-themed zodiac system. The experience is built around a reimagined astrological calendar—the “California Zodiac of Death”—where visitors receive a horoscope reflecting their “death sign,” personalized and printed on thermal paper for them to keep.

## Components

### Rotary Phone and Dialplan

A vintage rotary phone serves as the interactive portal for the experience. Visitors dial in and provide a “death day,” which the system processes to generate a unique horoscope.
An Asterisk dialplan collects the input, facilitates the call flow, and triggers the horoscope generation process in Python.

### Python Script (death_horoscope.py)

The death_horoscope.py script calculates the participant's California Zodiac of Death sign based on the input.
Using poetic prompts and elements, it generates a multi-layered horoscope, including identity advice, positive messages, love advice, and a reflective question.
California Zodiac of Death

Inspired by the carrion eaters and detritus dwellers of California, the zodiac features signs like the California Condor, Isopod, and Grey Wolf.
Each sign has a distinct identity with advice and character traits, exploring themes of transformation, resilience, and renewal.

### Thermal Receipt Printer

The participant’s horoscope is printed on thermal paper as a takeaway, bringing a physical dimension to the mystical interaction.
The use of receipt paper adds irony and humor to the experience, grounding existential themes in an everyday format.

### Technical Configuration (Asterisk, Variables, Sound Files)

The Asterisk dialplan manages the phone interaction, providing prompts through sound files and structuring the process to trigger the horoscope script.
Variables and configurations ensure smooth integration of sound files, dialplan variables, and script triggering.

### Poetic and Reflective Tone

The horoscopes combine dark humor, melancholy, and existential themes, encouraging contemplation and self-reflection.
Each reading balances wry humor with introspection, offering a unique and slightly whimsical perspective on life and death.

# Installation

## Hardware Setup

* Rotary phone (connected to an IAX or SIP adapter -- recommend the S100i if you can find one).
* Thermal receipt printer with Linux-compatible drivers.

## Software Requirements

* Asterisk PBX system for managing the call and input collection.
* Python 3.7+ for horoscope generation script.
* Linux with udev rules for printer setup and permissions.

## Configuration

* Set up Asterisk with custom sound files and dialplan configuration.
* Place death_horoscope.py in the appropriate directory and configure the AGI script trigger within Asterisk.
* Ensure thermal printer connectivity and test printing functionality.

## Interaction 

* Dial any 3 numbers on the rotary phone and follow the voice prompts to enter a “death day.”
* Receive a personalized California Zodiac of Death horoscope printed on receipt paper.

## Horoscope Customization

* Modify death_horoscope.py to add or adjust sign identity advice, prompts, and reflective questions for deeper customization.

# License

This project is licensed under the MIT License.

# Acknowledgments

Special thanks to those who inspired this project and the supportive community that brings interactive art installations to life.

