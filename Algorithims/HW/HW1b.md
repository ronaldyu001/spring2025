# Q0: Main Menu

## Details

A main menu was implemented to allow the user to access different functions.

## Output

1) Binary Search Number Guessing Game
2) Time Efficiency Function
3) Guessing Game
4) Collatz Sequence Generator
5) Extra Credit: Time Efficiency using decorator
6) Quit

# Q1: Number guessing game using Binary Search

## Details

The binary search algorithm was implemented to guess a randomly generated number between 1 - 1000.

This was repeated 10,000 times. The total guesses, as well as the average number of guesses were recorded.

This was also done for randomly generated numbers between 1-1000000

## Output

Enter Menu Option: 1
Numbers 1 - 1000: Total Guesses: 79789 Avg: 7.9789
Numbers 1 - 1000000: Total Guesses: 179577 Avg: 17.9577

# Q2: Writing a simple timer function

## Details

A function timeEfficiency() was implemented to receive a function as its input, and prints the start time, end time, and duration. The input function in this case is a prime number generator. The result of this function is also given.

## Output

Enter Menu Option: 2
Start Time: 1739059649.271872
End Time: 1739059649.2728372
Duration: 0.000965118408203125
Result: [2, 3, 5, 7, 11, ... ,971, 977, 983, 991, 997]

# Q3: Another guessing game

## Details

This second guessing game used a deterministic "brute force" approach. As well as a random approach.

## Output

Enter Menu Option: 3
Deterministic Brute Force approach:
        Number of tries: 10000
        Max number guesses: 1000
        Lowest number guesses: 1
        Average number of guesses: 499.8603

Random approach:
        Number of tries: 10000
        Max number guesses: 9552
        Lowest number guesses: 1
        Average number of guesses: 1007.4993


# Q4: Collatz 3n + 1 Algorithm

# Details

The collatz algorithm was implemented recursively. It starts with any positive integer, and based on if the number is even or odd, it will perform a mathematical function on the number. This is done until the number reaches one. The numbers calculated from the starting number to one make up the Collatz Sequence(including the starting number and one).

## Output

Enter Menu Option: 4

Top Ten Sequences:

1. Collatz sequence for 8400511 has 686 values, whose largest value is 159424614880
2. Collatz sequence for 8865705 has 668 values, whose largest value is 15208728208
3. Collatz sequence for 6649279 has 665 values, whose largest value is 15208728208
4. Collatz sequence for 9973919 has 663 values, whose largest value is 15208728208
5. Collatz sequence for 6674175 has 621 values, whose largest value is 125218704148
6. Collatz sequence for 7532665 has 616 values, whose largest value is 1017886660
7. Collatz sequence for 7332399 has 616 values, whose largest value is 150311737960
8. Collatz sequence for 5649499 has 613 values, whose largest value is 1017886660
9. Collatz sequence for 8474249 has 611 values, whose largest value is 1017886660
10. Collatz sequence for 6355687 has 608 values, whose largest value is 1017886660

# Q5: Extra credit Program

## Details

For the extra credit program, the time efficiency and prime number functions are used. However, this time it is implemented using a decorator. The decorator wrapper allows actions to be performed before and after running the inner function. In this case, the start time is printed before the function; the end time and duration is printed after the function.

## Output

Enter Menu Option: 5
Start Time: 1739060525.386996
End Time: 1739060525.388166
Duration: 0.0011699199676513672
Result: [2, 3, 5, 7, 11, ..., 971, 977, 983, 991, 997]
