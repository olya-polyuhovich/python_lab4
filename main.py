import re
import pyuca


try:
    with open ('text.txt', 'r', encoding='utf-8') as file:
        text=file.read()
        sentences = re.findall(r"[^.!?]+", text)  # splitting sentences
        first_s = sentences[0]
        print("first sentence:", first_s)

        words = re.findall(r'\b\w+\b',first_s)  # detecting words and deleting punctuation marks
        first_count = len(words)
        print("word count:", first_count)

        words.sort(key=lambda x: x.lower())
        ukr_words = [word for word in words if re.match(r'^[А-Яа-яІіЇїЄєҐґ]+$', word)]
        eng_word = [word for word in words if re.match(r'^[A-Za-z]+$', word)]
        collator = pyuca.Collator()  # sorting non english chars correctly
        sorted_ukr = sorted(ukr_words, key=collator.sort_key)
        print("first sentence in alphabetical order:\n ukrainian:", sorted_ukr, "\n english:", eng_word)

except NameError:
    print('cant find given file')
except:
    print("an error occurred")


