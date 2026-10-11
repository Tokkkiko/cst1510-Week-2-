"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_label(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:10.2f}")
    print(f"  Total       : {limit:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def main():
    over_limit_count = 0

    while True:
        hostname = input("Please enter the hostname (or type 'stop' to exit the program): ")
        if hostname == "stop":
            break
        value = float(input("Please enter the used capacity : "))
        limit = float(input("Please enter the total capacity : "))

        difference, percent = check(value, limit)
        status = status_of(percent)
        print_label(hostname, value, limit, difference, percent, status)

        if status == "OVER LIMIT":
            over_limit_count += 1

        print(f"the records counted that are over limit are: {over_limit_count}")


if __name__ == "__main__":
    main()

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
