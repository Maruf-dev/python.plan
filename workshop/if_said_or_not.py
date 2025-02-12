def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words
no_repeating()