def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

# Input
s = input("Enter a string: ")

# Output
print("String after removing duplicates:", remove_duplicates(s))
