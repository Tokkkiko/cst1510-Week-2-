# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try:
    with open("records.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: records.txt was not found.")