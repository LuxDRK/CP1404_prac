import random

def main():

    num_min = 1
    num_max = 45
    column = 6

    row = int(input('How many "quick picks" you wish to generate? '))
    for i in range (0,row):
        matrix = []
        matrix.append(random.randint(num_min, num_max-column+1))
        for j in range (1,column):
            num = 0
            while num <= matrix[j-1]:
                num = random.randint(num_min, num_max-column+1+j)
            matrix.append(num)
        print(" ".join("{:2}".format(number) for number in matrix))
main()