is_member = True
purchase_total = 150

if is_member and purchase_total > 120:
    print ("Discount applied.")
else:
    print ("No discount applied.")


is_locked = False
if not is_locked:
    print("You can open the door.")
else:
    print("The door is locked.")


score = 84
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
else:
    print("You failed.")

