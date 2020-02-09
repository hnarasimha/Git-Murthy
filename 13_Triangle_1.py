def triangle_1 (n,ch):
    for i in range (n):
        k=n
        for j in range(1,i+1):
            print (ch, end = " ")
        print("\n")

def triangle_2 (n,ch):
    for i in range (n,0,-1):
        k=n
        for j in range(1,i+1):
            print (ch, end = " ")
        print("\n")

def triangle_3 (n,ch):
    for i in range (n):
        
        for j in range(1,i):
            if j == 1 or j == i-1:
                print (ch,end = " ")
            else:
                print (" ", end = " ")
        print("\n")
        if i == n-1:
            for k in range (int(n/2)+1):
                print(ch+ " ",end = " ")
n = int(input("Enter a number :"))
ch = input ("Enter a character :")
#triangle_1(n,ch)
#triangle_2(n,ch)
triangle_3(n,ch)
