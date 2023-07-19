def Printnum(num):
    if num==1:
        print(1,end=" ")
        return 1
    Printnum(num-1) # 1 to N -> change the two lines to N to 1
    print(num,end=" ")
if __name__ == '__main__':
    num=int(input())
    Printnum(num)
"""
You are given an integer A, print 1 to A using using recursion.

Note :- After printing all the numbers from 1 to A, print a new line.
"""