# 🗡️ Quest #0007: Average Marks with Namedtuple

Given a spreadsheet of student information, calculate the average marks of all students using Python’s `collections.namedtuple`.  
The spreadsheet’s column order can vary, but the column names are always: **ID**, **MARKS**, **CLASS**, and **NAME**.

## 📋 Details  
**Difficulty:** 🟡 Medium  

**Input Example:**  
```
5
ID MARKS NAME CLASS
1 97 Raymond 7
2 50 Steven 4
3 91 Adrian 9
4 72 Stewart 5
5 80 Peter 6
```

**Output Example:**  
```
78.00
```

**Constraints:**  
- The first line contains an integer `n` — the total number of students.  
- The second line contains the column names in any order.  
- The next `n` lines each contain the details of a student.  
- Column names and their spelling will not change.  
- Output the average marks rounded to **2 decimal places**.
