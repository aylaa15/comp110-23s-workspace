"""Knock knock with conditionals"""

inter_cow: str = input("Do you want an interrputing cow? ")

print("Knock knock")
if (inter_cow == "yes"):
    print("...who's there?")
    print("Interrputing cow.")
    print("...interrupting cow wh---")
    print("MOO!!!")
else:
    print("Oh... okay... :(")
    if (inter_cow == "you're not funny"):
        print("Wow... that hurts my feelings. :(") 