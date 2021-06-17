# Chapter 3 - Exercise 3.3
# program prompts for a score between 0.0 and 1.0
# if score is out of range, print error message
# use below table for input value

#    Table
#   --------------------
#       Score    Grade
#   --------------------
#       >= 0.9    A
#       >= 0.8    B
#       >= 0.7    C
#       >= 0.6    D
#       <  0.6    F
#   ---------------------

prompt = "Enter score: "

score = input(prompt)

# print(type(score))
try:

    scorefloat = float(score)

    if scorefloat >= 0.9 and scorefloat <= 1.0:
        print('A')
    elif scorefloat >= 0.8 and scorefloat <= 0.89:
        print('B')
    elif scorefloat >= 0.7 and scorefloat <= 0.79:
        print('C')
    elif scorefloat >= 0.6 and scorefloat <= 0.69:
        print('D')
    elif scorefloat < 0.6:
        print('F')
    else:
        print('Bad score')
except:
    print('Bad score')


# if scorefloat >= 0.9 and scorefloat <= 1.0:
#    print('A')
# elif scorefloat >= 0.8 and scorefloat <= 0.89:
#    print('B')
# elif scorefloat >= 0.7 and scorefloat <= 0.79:
#    print('C')
# elif scorefloat >= 0.6 and scorefloat <= 0.69:
#    print('D')
# elif scorefloat < 0.6:
#    print('F')
# else:
#    print('Bad score')
