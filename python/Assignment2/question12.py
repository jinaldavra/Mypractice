# 12. Count the occurrences of each character in a string using a loop.

string = "programming"
char_count = {}

for i in string:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for ch in char_count:
    print(f"{ch} : {char_count[ch]}")

