import json

f1 = open("data/file1.txt", "r" ,encoding="utf-8")
file1 = f1.read()
f2 = open("data/file2.txt", "r" ,encoding="utf-8")
file2 = f2.read()
f3 = open("data/file3.txt", "r" ,encoding="utf-8")
file3 = f3.read()


words1 = file1.split()
words2 = file2.split()
words3 = file3.split()
word_count = {}
# seen_words = set()

def process_file(words, source):
    for word in words:
        cleaned_word = word.replace('.', '').replace('،', '')
        if len(cleaned_word) >= 2:
            if cleaned_word in word_count:
                word_count[cleaned_word]['Count'] += 1
                if source not in word_count[cleaned_word]['Sources']:
                    word_count[cleaned_word]['Sources'].append(source)
            else:
                word_count[cleaned_word] = {'Count': 1, 'Sources': [source]}

def output_json(word_count):
    with open("output.json", "w", encoding="utf-8") as outfile:
        json.dump(word_count, outfile, ensure_ascii=False, indent=4)


process_file(words1, "file1")
process_file(words2, "file2")
process_file(words3, "file3")

output_json(word_count)
