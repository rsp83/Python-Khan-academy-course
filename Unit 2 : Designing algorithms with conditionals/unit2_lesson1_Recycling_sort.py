material = input("What material is it? ")
length = float(input("What is its length in cm? "))

if material == "plastic" :
  waste_type = "recycling"
if material != "plastic" :
  waste_type = "trash"
if length < 7.5 :
    waste_type = "trash"



print("Please deposit your item in the " + waste_type + " bin.")
