"""
Progress Utility
"""

import time

def progress():

    for i in range(5):

        print(f"Processing {i+1}/5")

        time.sleep(0.2)
