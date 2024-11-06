s = input()
flag = False
for i in range(len(s) - 1):
    for j in range(i, len(s)):
        if (s[i] + s[j] == '()') or (s[i] + s[j] == '{}') or (s[i] + s[j] == '[]'):
            flag = True
        else:
            flag = False

print(flag)