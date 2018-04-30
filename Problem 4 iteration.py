#start at a number n
def Collatz_Tree50(n):
    count = 0
    
    while n != 1:
        
    #if even
        if n % 2 == 0:
            n = n/2
            count += 1
        
        #if odd
        elif n % 2 == 1:
            n = ((3*n)+1)
            count += 1
    return count

print(Collatz_Tree50(2581383174241854160896))