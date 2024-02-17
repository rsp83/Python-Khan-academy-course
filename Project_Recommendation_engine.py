"""Recommends a Khan Academy course based on grade and subject preferences."""

# Course options to choose from for our recommendation.
fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"
documentaries = "Documentaries"
nature_shows = "Nature shows"
human_interest_stories ="Human interest stories"
science = "Science"

# Collect user attributes to inform our recommendation.
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? ")
learning_pace = input("What is your learning pace like ? ")

# Make a course recommendation based on the user's attributes.
rec = ""
if grade < 6:
    # Course caters to younger learners.
    rec = grammar
elif learning_pace == "slow":
    rec = "Time Management Strategies"
else:
    if favorite_subject == "computing" or favorite_subject == "art":
        rec = pixar

    elif favorite_subject == "engineering" or favorite_subject == "physics":
        rec = science

    elif favorite_subject == "history" or favorite_subject == "literature":
        rec = documentaries

    elif favorite_subject == "biology" or favorite_subject == "ecology":
        rec = nature_shows

    elif favorite_subject == "psychology" or favorite_subject == "sociology":
        rec = human_interest_stories
    else:
        # Most broadly relevant and approachable subject.
        rec = fin_lit

print("We recommend the Khan Academy course: " + rec)
