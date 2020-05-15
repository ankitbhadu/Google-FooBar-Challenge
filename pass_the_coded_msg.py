"""
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Test cases
==========

Inputs:
    (int list) l = [3, 1, 4, 1]
Output:
    (int) 4311

Inputs:
    (int list) l = [3, 1, 4, 1, 5, 9]
Output:
    (int) 94311
"""
def solution( l): 
    flag = 0
    sum = 0
    n=len(l)
    for i in range(n): 
        sum += l[i] 

  
    else: 
        l.sort(reverse = True) 
  
        # if there is just one element 0 
        if (l[0] == 0):  
            return 0
          
        else: 
            flag = 0
            y = sum % 3
            if (y != 0): 
                  
                i = n - 1
                while(i >= 0): 
                    if (l[i] % 3 == y): 
                        l.remove(l[i]) 
                        flag = 1
                        break
                    i -= 1
                if (flag == 0): 
                    y = 3 - y 
                    cnt = 0
                    i = n - 1
                    while(i >= 0): 
                        if (l[i] % 3 == y): 
                            l.remove(l[i]) 
                            cnt += 1
  
                            if (cnt >= 2): 
                                break
                          
                        i -= 1
  
            if(len(l)==0):
                return 0
            ans="".join([str(elem) for elem in l])
            return ans
print(solution( [3,3,5,6,2,3,3,5,7,3]))