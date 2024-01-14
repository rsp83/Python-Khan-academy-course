# Language codes include "es" for Portuguese and "es" for Spanish.
language_code = "es"

print("Please enter a Subject, Subjects can be math, science, computing, or humanities.")

subject = input("Enter a subject: ")

url = "https://" + language_code + ".khanacademy.org/" + subject

print("Navigate to the page below!")
print(url)