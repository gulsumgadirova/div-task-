def count_words(text):
    words = text.lower().split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

text = input("Metni daxil edin: ")
result = count_words(text)
print(result)
max_word = ""

for word in result:
    if max_word == "" or result[word] > result[max_word]:
        max_word = word

if max_word !="":
    print("En cox tekrarlanan soz:", max_word)
        