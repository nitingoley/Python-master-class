                   

#    Project: Text Analyzer 
# Yeh project user se ek sentence input lega aur usme kuch basic analysis karega jaise:
# ✅ Total characters
# ✅ Total words
# ✅ Vowel aur consonant count
# ✅ Reverse string
# ✅ Most frequent word  


text = input("Enter a sentence: ") 

char_count = len(text)
words_count = len(text.split()) 


print(f"Total Characters: {char_count}")
print(f"Total words: {words_count}")


vowels = "aeiouAEIOU" 

vowel_count = sum(1 for char in text if char in vowels) 
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)


print(f"Vowel Count: {vowel_count}")
print(f"Consoant count: {consonant_count}")


reversed_text = text[::-1]

print(f"Reversed text: {reversed_text}")



from collections import Counter 

words = text.split()

if words:
    most_common_words = Counter(words).most_common(1)[0][0]
    print(f"Most frequent word: {most_common_words}")
else:
    print("No words found!")