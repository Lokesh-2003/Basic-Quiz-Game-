def count_words(text):
    word_list = text.split()
    return len(word_list)

# Example usage:
text_input = "bindu rani."
word_count = count_words(text_input)
print(f"The number of words in the text is:{word_count}")
