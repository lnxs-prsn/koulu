Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

An example of expected behaviour:

line(7, "%")
line(10, "LOL")
line(3, "")
Sample output
%%%%%%%
LLLLLLLLLL
***

1. input = 7, '%' > func > %*7 
2. input = 10, 'LOL' > func > 'LOL[0]*10
3. input = 3,'' > func > '*'*3


"What is this function's ONE job?"
   -   functions one job is to multiply

Can I describe its purpose in one simple sentence
   -   multiply str[0] * int or if no str[0] '*'*int

"What data does it need? What does it return?"
   -   it needs int and str > it returns str



my solution 
{
    def line(num, txt):
    num = int(num)
    if num and txt:
        print(txt[0]*num)
    elif len(txt) == 0:
        print('*'*num)
    elif num == 0:
        print(txt[0])
}

mooc solution
{
    def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
# Write your solution here
}

I have certain way of thinking 
    - ISSUE IS THIS 
      - man with hammer sees nails everywhere !