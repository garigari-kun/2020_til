import string

alpha = string.ascii_uppercase
nums = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
decoded = []

for i in nums:
    decoded.append(alpha[i - 1])

print("".join(decoded))


