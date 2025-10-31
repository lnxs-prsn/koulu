Please write a program which asks the user to type in a number.

The program then prints out the positive integers between 1 and the number itself,

alternating between the two ends of the range as in the examples below.

what is the problem - num = 10 - print 1,10,2,9,3,8,4,7,5,6 - so I need to return 1 and then 9 and then 2 and then 8 - first is followed by last second is followed by second last etc

- isnt there simpler way to define the problem that could simplify the 
solution search
    - starting from beginning jumping to end  jumping back to begining and continueing from the begining jumping back to end continueing etc

- still not simple enough 
    - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    get first > last >second > second last>third >third last

- more explaining power
    - code takes numbers from both ends from beginning and and in turns
what do I feel about it - I feel like going to testing my idea of using for loop - feeling impatient, enjoying the new process

what is the solution / problem

- get from begining and the end in turns start from the beginning 

solution1
    - what do I need to do 
        - get number from the user
        - have an loop that ends  in case the loop goes more than the number user gave 
        - have number ingreasing like in while loop 
        - or the x in the for loop
        solution 
            - print x 
            - print num[-x]

 solution1 problem
    - num[-x] works on the list or str but not on int
    - idea is good implementation is lacking 

solution2
    - what do I need to do 
        - get number from the user
        - have an loop that ends  in case the loop goes more than the number user gave 
        - have number ingreasing like in while loop 
        - or the x in the for loop
        solution 
            - print x 
            - print num - 1
            how do I know when to stop the program
                - if num = 11
                - I need to know when the x < int(num / 2) + 1 if num is odd
                1,11,2,10,3,9,4,8,5,7,6
solution2 problem # got distracted had to do feel check
    - 
how do I feel - I feel am over complicating the process - feeling restless and uncomfortable - am likely in edge of my learining pushing further will lead to growth in my knowledge

solution2 problem
    - program is supposed to stop 
        - when x is less than 6
            - if so the last x will print is 5 and program ends 
            - this solution works only when its odd not when its even
    - how do I print the 
        the from top down
        that is not yet modeled clearly 


- solution3 
    - what do I need to do 
        - get number from the user
        - have an loop that ends  in case the loop goes more than the number user gave 
        - have number ingreasing like in while loop 
        - or the x in the for loop
        solution 
            - print x 
            - print num - x
            - x rises from one to num
                logiikka ongelma
                - 11 - 1 , 11-2, 11-3, 11-4

            how do I know when to stop the program
                - works for the odd number
                - if num = 11
                - I need to know when the x < int(num / 2) + 1 if num is odd
                1,11,2,10,3,9,4,8,5,7,6

- solution3 problem
    - print num - 1
        - ei toimi sen pitäisi ensin antaa num ja sen jälkeen 
         aloittaa num - x 
         - oletettavasti tarvitaan if else 
            eikö ole helpompaa keinoa 

- solution4 magic thinking 
    - what would be magic solution
        - I would have magical variable that would substract from num correct amount every round of iteration but would not be used in the first time 
        - like this x is 1  num is num then x is 2 and num-magic variable 
how do I feel - I feel that there is easier way to think about this but my present - capabilities are just not able to get me there yet - am presently just looping but I dont want to jump to just doing - as that would be same that I have done so far feelings discomfort, stuck, pressure.

how to go forward - do solutions until - solution6 if there is no new ideas - start experimenting but no mindless but focused and with purpose - with purpose means - look in to this file do not make fixing without updating the file so if after the solution six problems exist but no solution - try solution write down the process of thinking

- solution5 
    - take number roll up from begining and the end roll down in turns start from the beginning 
        - num = input
        -  num1 = num
        - for x in range(1, num)
                        -   print x                       XXXX!!!! not possible 
        - if x is not 1 and num1 != num
        -  print x
        - print(num1)
        -   num1 -= 1
        - if x <= int(num/2) + 1 and num%2 != 0
        - print x
        - if n%2 == 0 and x >= int(num/2):
        -  print num1

- solution5 problem 
    - jokaiselle x printaus pitää tapahtua
        - if statementin sisällä
        - Feeling that this way of doing is incorrect
    - feeling that this is some how too much repetition
    - or that something is not correct


- solution6 
    -      - num = input
        -  num1 = num
        - for x in range(1, num)
        - if x == 1 and num1 == num:
        -  print x
        - print(num1)
        -  num1 -= 1
        - if x is not 1 and num1 != num
        -  print x
        - print(num1)
        -   num1 -= 1
        - if x <= int(num/2) + 1 and num%2 != 0
        - print x
        - if n%2 == 0 and x >= int(num/2):
        -  print num1

- solution6 problem
    - cant find problem 
    - but I dont know how I decided why this should be for loop instead of while loop



- solution7
num = 10
num1 = num
for x in range(1, 10):
    if x ==1 and num1== num:
        print(x)
        print(num1)
        num-=1
    elif x <= int(num/2)+1 and num%2!=0:
        print(x)
        print(num1)
        num-=1
    elif num%2 == 0 and x <= int(num/2):
        print(x)
        print(num1)
        num-=1
    else: 
        print('not as I thought')
output expected: - 1,10,2,9,etc feeling that it wont be this out put - what will go wrong - I dont know but I feel it will print more than intended

solution 7 problem
    - it printed more than I intended when it printed odd nums range
    - issue is that there is no stopping printing x when x and num1 are equal

solution8 works ?? hindsight no it did not work
    - num = 5
num1 = num for x in range(1, 10): if x ==1 and num1== num: print(x) print(num1) num1-=1 elif x <= int(num/2)+1 and num%2!=0: if x != num1: print(x) print(num1) num1 -=1 elif num%2 == 0 and x <= int(num/2): print(x) print(num1) num1-=1

how am I feeling - dissatisfied that I could not get the solution I am feeling but cant think yet

solution8 problem
    - when if input is 1 then it prints it twice solution is another 
    if statement


solution9 works
num = 1
num1 = num for x in range(1, 10): if x ==1 and num1== num: print(x) if num > 1: print(num1) num1-=1 elif x <= int(num/2)+1 and num%2!=0: if x != num1: print(x) print(num1) num1 -=1 elif num%2 == 0 and x <= int(num/2): print(x) print(num1) num1-=1

solution9 problem

- here is the real solution from exercise
number = int(input("Please type in a number: "))

left = 1
right = number

while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1

if left == right:
    print(left)


questions feelings - why did I got stuck thinking for loop? - if forgot to look at this - how I feel after above - I feel like experimenting first ideas that crossed the mind - first ideas in general are wrong - I should ignore first ideas and try to think it clearly about the problem

over all - my solution works but its half longer than the ideal solution