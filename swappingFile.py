def swapFiledata():
    sample1 = input("enter file to swap ")
    sample2 = input("enter file to swap ")

    with open(sample1,'r') as a:
        data_a = a.read()

    with open(sample2,'r') as b:
        data_b = b.read()
        
    with open(sample1,'w') as a:
        a.write(data_b)

    with open(sample2,'w') as b:
        b.write(data_a)



swapFiledata()
