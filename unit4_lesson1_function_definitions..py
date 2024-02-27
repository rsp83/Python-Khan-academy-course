hours_played = 15

if hours_played >= 50:
    trophy_name = "Valiant Veteran"
elif hours_played >= 10:
    trophy_name = "Active Adventurer"
else:
    trophy_name = "Trainee Traveller"

print(trophy_name)
