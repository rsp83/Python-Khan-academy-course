footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
if has_pet == "yes": 
    footprint = footprint + 5
    meat = input("Does your pet’s food contains meat (yes/no)? ")
    if meat == "yes":
        footprint = footprint + 10
    else:
        pass
    

days = int(input("How many days a week do you commute to school or work? "))
if days > 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? ")
    if transport == "car":
        footprint += (8 * days)
    elif transport == "bus" or transport == "train":
        footprint += (4 * days)
    elif transport == "bike" or transport == "foot":
        footprint =+ days
    else:
        pass

print("Your environmental footprint score is " + str(footprint) + ".")
