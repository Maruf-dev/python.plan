def count(str, target):
    total = 0
    index = 0
    while index < len(str):
        if str[index:index+len(target)] == target:
           total += 1
           index += len(target)
        else:  
            index += 1
    return total

print(count("AAAA", "AA"))           

