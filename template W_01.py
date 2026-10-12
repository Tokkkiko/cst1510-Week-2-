"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
host_name = input("Enter system hostname: ")
failed_logins = int(input("Enter number of failed login attempts: "))
login_limit = int(input("Enter maximum allowed failed attempts: "))

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

remaining_chances = login_limit - failed_logins  # replace with your calculation

percent = (failed_logins / login_limit) * 100

if percent >= 100:
    status = "Wrong-you have finished your login attempts (please check your logins)"
elif percent >= 90:
    status = "Warning- you are almost out of login attempts (please check your logins)"
else:
    status = "Your login attempts are within the limit"

print()
print("=" * 34)
print(f"  CYBER SECURITY LOGIN CHECK - {host_name}")
print("=" * 34)

print(f"  Failed attempts : {failed_logins:>10}")
print(f"  Security limit  : {login_limit:>10}")
print(f"  Remaining       : {remaining_chances:>+10}")
print(f"  Limit used      : {percent:>10.2f}%")

print("=" * 34)
print(f" Status is: {status}")
print("=" * 34)




# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
