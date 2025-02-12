def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1 
    return total
print(count_substring("xirillamamngla, man, man, man", "m"))