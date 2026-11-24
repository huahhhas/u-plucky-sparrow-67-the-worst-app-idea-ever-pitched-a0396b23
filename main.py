#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence (at most 240 characters) pitching the worst and
most useless app imaginable to /output/entry.txt.
"""
import os

PITCH = "ToastTalk is an AI app that translates your toaster's pops into personalised motivational speeches, so your breakfast can believe in itself before you butter it — because no slice of bread should face the day without a pep talk."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
