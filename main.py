"""One Star for Monday — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The review: Monday served cold coffee, reheated dread, and a meeting that could have been an email.
TEXT = "One star. Monday served cold coffee, reheated dread, and a meeting that could have been an email. I will not be returning."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
