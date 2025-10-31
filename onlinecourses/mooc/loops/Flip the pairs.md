Please write a program which asks the user to type in a number. 

The program then prints out all the positive integer values from 1 up to the number. 

However, the order of the numbers is changed so that each pair or numbers is flipped. 

That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.


what I need to do.
    - ask num print num
    - take num 
        - print all the positive interger values   from 1 to num
        - ! then pair of numbers order is flipped
            - so if num is 5 
            - first is print 2 then 1 then 4 then 3 then 5 

how I feel after above
    - I feel like experimenting first ideas that crossed the mind 
        - first ideas in general are wrong 
        - I should ignore first ideas and try to think it clearly about the problem

how do I model the solution / problem
    - problem is how do I switch the order of 
        - 1 and 2 
        -  and order of 3 and 4
    - solution1  would be like this 
        - print 1 + 1 print 2 - 1 and print 3 + 1 print 4 - 1 print 5 do nothing
        - I would need to check if num is even or odd if num is odd break loop when x is num
        if its even then keep switching until x is num
    - solution1 problem
        - it assumes that I get to print 1,2,3,4,5
        - but if I have to build everything from scratch it would be not so easy
        - the switch to decide when to add 1 and when to substract 1 would be too complex 
        despite problem being simple
    
    - solution2
        - outside the loop define x = 0
        if x == num break
        inside the loop start x += 1
        - when x is even - 1 print x 
        - when odd + 1 print x 
        
    - solution2 problem

        - if x == num break
            - what if num is even then there would be 
                2,1,4,3,6 break
            works if num is odd
    
    - solution3 
        - outside loop define x = 0
        - inside while loop
            - x += 1
            - if x == num and num is even
                - x -= 1
                - print(x)
            - elif x == num and num is odd
                - x += 1
                - print(x)

    - solutions3 problem
        - could be done easier with for loop

    - solution4 
        - for loop
            - x in range is num
            if x is even 
                 x - 1
            if x is odd 
                x + 1
    
    - solution4 problem
        - does not check if the 
        - last one digit is odd instead it tries to swithch it 
    
    - solution5
        - for loop 
        - x in range is num
            if x is even 
                 x - 1
            if x is odd and x != num
                x + 1
    - solution5 problem
        - does not print the last x 
    
    - solution
        - for loop 
        - x in range is num
            if x is even 
                 x - 1
            if x is odd and x != num
                x + 1
            else print x


solution provided by exercise maker 

number = int(input("Please type in a number: "))
 
index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2
 
if index <= number:
    print(index)