text = "HElLo WoRLd"

print("original:", text)
lowered = text.lower()
print("lowered:", lowered)
uppered = text.upper()
print("uppered:", uppered)

print("stripped:", text.strip())
print("replaced:", text.replace("HElLo", "Goodbye"))

#동시에하려면
print("replaced:", text.strip().replace("HElLo", "Goodbye").upper())