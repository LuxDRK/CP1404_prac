def main():
    ### change_type Ture means F->C, False means C->F
    change_type = True
    in_file = open('temps_input.txt','r+')
    out_file = open('temps_output.txt','w+')
    count = len(in_file.readlines())
    list = in_file.readlines()
    for i in range(1,count+1):
        if change_type:
            print((float(list[i])-28)/1.8, file=out_file)
        else:
            print(float(list[i])*1.8+28, file=out_file)

    in_file.close()
    out_file.close()

main()