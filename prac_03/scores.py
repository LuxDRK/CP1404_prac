"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    out_file = open('results.txt', 'w')
    import random
    score_num = int(input("How many scores you want?\n"))
    for i in range (0,score_num):
        score = int(random.randrange(1,100))
        if score < 0 or score > 100:
            print(score,"is Invalid score", file=out_file)
        elif score >= 90:
            print(score,"is Excellent", file=out_file)
        elif score >= 50:
            print(score,"is Passable", file=out_file)
        else:
            print(score,"is Bad", file=out_file)

main()
