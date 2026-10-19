"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.

label = input("Please enter a name/hostname/IP: ")
value = float(input("Please enter a value: "))
limit = float(input("Please enter a limit: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit
percent = (value/limit) * 100

# 3. Decide a status and store it in a variable called status.

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Value: {value}")
print(f" limit: {limit}")
print(f" difference: {difference}")
print(f" percent : {percent:.2f}%")
print(f" Status :{status}")


# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
