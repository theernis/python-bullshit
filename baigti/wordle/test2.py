file1 = open("filtered.txt","r")
file2 = open("sorted.txt","w")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
scores = [0 for i in letters]
placed_scores = [[0 for i in letters] for i in range(5)]

def word_val(word):
    return sum([placed_scores[i][letters.index(word[i])] for i in range(len(word.split("\n")[0]))]) / sum([scores[letters.index(letter)] for letter in word.split("\n")[0]]) * len([*set(word.split("\n")[0])])

text = file1.readlines()
for word in text:
    print(word)
    i = 0
    for letter in word.split("\n")[0]:
        scores[letters.index(letter)] += 1
        placed_scores[i][letters.index(letter)] += 1
        i += 1

print(scores)
sorted = []

for word in text:
    print(str(len(sorted)) + ":" + str(len(text)))
    if (len(sorted) == 0):
        sorted.insert(0, word)
    else:
        value = word_val(word)
        for i in range(len(sorted)):
            if (i == len(sorted)-1):
                sorted.insert(len(sorted), word)
            else:
                if (value < word_val(sorted[i])):
                    sorted.insert(i, word)
                    break

print(sorted)

file2.writelines(sorted)
file1.close()
file2.close()