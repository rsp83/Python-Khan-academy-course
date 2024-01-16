# Language codes include "es" for Portuguese and "es" for Spanish.
language_code = "es"

subject = input("Please enter a Subject, subjects can be math, science, computing, or humanities.")

url = "https://" + language_code + ".khanacademy.org/" + subject

print("Navigate to the " + subject + " page below!")
print(url)