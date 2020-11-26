name = input("Please input your name: ")
out_file = open('name.txt','w')
out_file.write(name)
out_file.close()

out_file = open('name.txt','r')
print("Your name is",out_file.readline())
out_file.close()

out_file = open('numbers.txt','w')
out_file.writelines(['17\n','42\n','400\n'])
out_file.close()
out_file = open('numbers.txt','r')
print(int(out_file.readline()) + int(out_file.readline()))
out_file.close()

out_file = open('numbers.txt','r')
finished = False
sum = 0
while not finished:
    try:
        sum = sum + int(out_file.readline())
    except:
        finished = True
print(sum)
out_file.close()
