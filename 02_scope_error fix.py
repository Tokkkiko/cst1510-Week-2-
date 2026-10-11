# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

check(87, 100)
status = check(87, 100)
print(status)
