# Problem 4
    
def Collatz_Tree1100(n, count = 0):
    
    if count == 1100 or n == 1:
        return n, count
    
    #if even
    elif n % 2 == 0:
        return Collatz_Tree1100(n/2, count+1)
    
    #if odd
    elif n % 2 == 1:
        return Collatz_Tree1100(((3*n)+1), count+1)    
    
def __main():
    #print(Collatz_Tree(340))
    n, ans1 = Collatz_Tree1100(2581383174241854160896)
    print(n, ans1)
    n, ans2 = Collatz_Tree1100(n)
    print(n, ans2)
    ans = ans1 + ans2
    print(ans)

    
    
if __name__ == '__main__':
    __main() 
        