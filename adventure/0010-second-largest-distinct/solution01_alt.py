n = int(input())
nums = [int(input()) for _ in range(n)]
u = sorted(set(nums))
print(u[-2] if len(u) >= 2 else "NA")