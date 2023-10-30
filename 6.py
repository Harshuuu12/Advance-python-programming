# Write a python program to find the longest words.

def find_longest_words(text):
    words = text.split()
    
    longest_words = []
    max_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            longest_words = [word]
            max_length = word_length
        elif word_length == max_length:
            longest_words.append(word)
    
    return longest_words

input_text = "This is an example sentence to find the longest words"
longest_words = find_longest_words(input_text)
print("Longest word(s):", longest_words)
print("Length of longest word(s):", len(longest_words[0]))  
