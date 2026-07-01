"""Recommends a Khan Academy course based on grade and subject preferences."""

# Course options to choose from for our recommendation.
fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"
cpro = "C-Programming"
basichis = "Basic history"
isl = "Islamiaat"
alg = "Algebra"
trig = "Trigonometric"
cs1 = "CS100"
cal = "Calculus"
mech = "Mechanics"
cs2 = "CS200"
bio = "BIO 101"
cal2 = "Calculus II"
mod = "Modern Physics"


# Collect user attributes to inform our recommendation.
grade = int(input("What grade are you in? "))
difficulty = input("Which difficulty level do you " +
                    "prefer(Easy, Medium, Hard)? ")
favorite_subject = input("What is your favorite subject? ")

# Make a course recommendation based on the user's attributes.
rec = ""
rec2 = ""
rec3 = ""
rec4 = ""
rec5 = ""
if grade < 6:
    # Course caters to younger learners.
    rec = grammar
    rec2 = cpro
    rec3 = basichis
    rec4 = isl
    rec5 = alg
else:
    if favorite_subject == "computing" or favorite_subject == "art":
        rec = pixar
        rec2 = cal
        rec3 = mech
        rec4 = trig
        rec5 = cs1
    else:
        # Most broadly relevant and approachable subject.
        rec = fin_lit
        rec2 = cal2
        rec3 = mod
        rec4 = bio
        rec5 = cs2

print("We recommend the Khan Academy course: " + rec + ", " + rec2 + ", " + 
      rec3 + ", " + rec4 + " and " + rec5)
