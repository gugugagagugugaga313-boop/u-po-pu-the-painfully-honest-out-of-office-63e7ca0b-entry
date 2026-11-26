"""Write one painfully honest out-of-office reply to /output/entry.txt.

The reply is a fixed string: no randomness, no clock, no network, so
every run writes byte-identical output.
"""
import os


REPLY = (
    "I am out of the office until Monday, and honestly I am using this "
    "holiday to avoid an inbox I cannot face, but I promise your message "
    "will be the first I read with a clear head when I return."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
