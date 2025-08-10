# 🗡️ Quest #0013: Number Guessing Game

The computer randomly selects an integer between 1 and 100 (inclusive).  
The user tries to guess the number. After each guess, the program should print:  
- `"Higher"` if the guessed number is smaller than the target.  
- `"Lower"` if the guessed number is larger than the target.  
When the guess is correct, print `"Correct! Attempts: X"` where `X` is the number of guesses made.

## 📋 Details  
**Difficulty:** 🟢 Easy  

**Input Example:**  
```
50
75
62
70
68
69
```

**Output Example:**  
```
Higher
Lower
Higher
Lower
Higher
Correct! Attempts: 6
```

**Constraints:**  
- The target number is an integer between 1 and 100 inclusive.  
- The number of attempts can be any positive integer.
