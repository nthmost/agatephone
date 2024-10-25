#!/usr/bin/env python3

import sys
import subprocess

import os
os.environ['TMPDIR'] = '/var/tmp/asterisk'


def main():
    # Fetch the UNIQUEID passed from Asterisk
    agi_exten = sys.argv[1]

    # Output AGI completion message to Asterisk (AGI protocol)
    print(f"VERBOSE \"Running generate_death_horoscope.py in the background for deathdate: {agi_exten}\" 1")
    sys.stdout.flush()  # Ensure the VERBOSE message is sent to Asterisk before proceeding

    # Construct the command to run the actual script in the background
    # venv = "/home/nthmost/.local/share/virtualenvs/agatephone-j4q6lhlk/bin/python"
    # pyfile = "/home/nthmost/projects/git/agatephone/generate_death_horoscope.py"
    venv = "/usr/share/asterisk/pyvm/bin/python3"
    pyfile = "/usr/share/asterisk/agatephone/generate_death_horoscope.py"

    command = [venv, pyfile, agi_exten]

    # Run the horoscope script in the background and log output
    with open("/var/log/common/generate_horoscope.log", "a") as log_file:
        log_file.write(f"Running command: {' '.join(command)}\n")
        try:
            subprocess.Popen(command, stdout=log_file, stderr=log_file)
        except Exception as e:
            log_file.write(f"Error occurred: {str(e)}\n")

if __name__ == "__main__":
    main()

