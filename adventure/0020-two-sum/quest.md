# 🗡️ Quest #0020: two-sum

Given an integer array `nums` and an integer `target`, return the indices (0-based) of the two numbers such that they add up to `target`. If there are multiple solutions, return any one of them. If none exists, print `NA`.

**Input format**
- First line: integer `n` (array length)
- Second line: `n` space-separated integers
- Third line: integer `target`

**Output format**
- Two space-separated integers representing the indices, or `NA` if no valid pair exists.

**Rules & clarifications**
- Indices must be distinct.
- You may return indices in any order.

## 📋 Details  
**Difficulty:** 🟢 Easy

**Input Example:**  
```
4
2 7 11 15
9
```

**Output Example:**  
```
0 1
```

**Constraints:**  
- 2 ≤ n ≤ 10^5
- -10^9 ≤ nums[i] ≤ 10^9
- -10^9 ≤ target ≤ 10^9
