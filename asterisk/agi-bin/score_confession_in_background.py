#!/usr/share/asterisk/pyvm/bin/python3 

import sys
import subprocess

def main():
    # Fetch the UNIQUEID passed from Asterisk
    agi_uniqueid = sys.argv[1]

    # Construct the command to run the actual scoring script in the background
    score_command = f"/var/lib/asterisk/agi-bin/score_confession.py {agi_uniqueid} &"

    # Run the scoring script in the background
    subprocess.Popen(score_command, shell=True)

    # Output AGI completion message to Asterisk (AGI protocol)
    print("VERBOSE \"Running score_confession.py in the background for uniqueid: {}\" 1".format(agi_uniqueid))

if __name__ == "__main__":
    main()

