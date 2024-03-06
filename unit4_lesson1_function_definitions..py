def get_time_trophy(hours_played):

    if hours_played >= 50:
        trophy_name = "Valiant Veteran"
    elif hours_played >= 10:
        trophy_name = "Active Adventurer"
    else:
        trophy_name = "Trainee Traveller"

    return trophy_name

hours_played = 2
trophy_Name = get_time_trophy(hours_played)
print(trophy_Name)

hours_played = 11
trophy_Name = get_time_trophy(hours_played)
print(trophy_Name)

hours_played = 33
trophy_Name = get_time_trophy(hours_played)
print(trophy_Name)

hours_played = 55
trophy_Name = get_time_trophy(hours_played)
print(trophy_Name)
