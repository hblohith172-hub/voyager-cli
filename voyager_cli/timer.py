import time


def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\r⏱️  {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Timer done!")