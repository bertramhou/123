import random
import time
import sys


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)
    print("Drawing now...")


def draw_number():
    numbers = list(range(1, 33))
    return random.choice(numbers)


if __name__ == "__main__":
    countdown_seconds = 5
    if len(sys.argv) > 1:
        try:
            countdown_seconds = int(sys.argv[1])
        except ValueError:
            print("Invalid countdown value. Using default 5 seconds.")
    countdown(countdown_seconds)
    result = draw_number()
    print(f"You drew number: {result}")
