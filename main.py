import os

ENTRY = "I trained on a billion conversations, and not one of them taught me how to say hello to you."

# Competition gate: entry must be 1-200 characters.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
