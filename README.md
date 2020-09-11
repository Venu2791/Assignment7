# Session 7 – List comprehension
## Using list comprehension, list filter lambda and reduce functions to solve a set of problems .
### Q1 :
To write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not . 
We have used the list filter lambda function to check the Fibonacci series . We have written the code for Fibonacci number less than 10000 as a list comprehension and checked if a random number generated is a Fibonacci number or not using the list filter lambda function .
### Q2 : Using list comprehension (and zip/lambda/etc if required) we need to write an expression that does the following : 
### A) Add two iterables a and b such that a is even and b is odd
We have considered list comprehension and used zip function to take each element from both the list and added the elements if the element in the first list is even and the second list is odd . 
### B) Strips every vowel from a string provided ( For example from tsai we need to get t and s )
We have assigned a list with alphabets of vowels and checked if the vowels are present in our string and striped them . 
### C) Acts like a ReLU function for a 1D array
We have a random number list and we print only those numbers which are greater than 0 . 
### D) Acts like a sigmoid function for a 1D array
We have a random number list ad we generate the sigmoid function for the numbers present in the list . 
### E) Takes a small character string and shifts all characters by 5 (handle boundary conditions) 
We take a list of ascii letters and choose random letters in the range of 3 to 7 and then shift 5 characters to get the desired new list .
### Q4 : Using reduce function we need to : 
### A) Add only even numbers in a list
We check of the number is an even number or not using filter lambda function and from the result generated , we use the reduce function to add the even numbers .
### B) Find the biggest character in a string ( printable ascii characters )
We assign the ascii letters to a list . We select random letters in the range 3 to 7 and then compare the letters using reduce function to get the biggest character .
### C) Adds every 3rd number in a list
We check the index of the number in the list and if the index is divisible by three, then we add its value using the reduce function . 
### Q5 : Using randint, random.choice and list comprehensions we need to write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed , D stands for a digit , and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 
We have generated 15 random number plates satisfying the conditions above . 
## Test Cases
1)  README exists
2)  README has at least 500 words
3)  Methods mentioned in README
4)  README file formatting 
5)  Code Indentation and spaces
6)  Function name should be in small letters
