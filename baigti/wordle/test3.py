import os
file = open("sorted.txt","r")

greens = input("greens (_ = not green): ") + "_"*5
yellows = input("yellows: ")
greys = input("greys: ")

words = []

text = file.readlines()
for word in text:
    print(len(words))

    if (len(yellows) > sum([(i in word) for i in yellows]) or sum([(i in word) for i in greys])):
        continue

    for i in range(len(word.split("\n")[0])):
        if (not(greens[i] == "_" or greens[i] == word[i])):
            break
    else:
        words.append(word)

print(words)

file.close()
os.system("pause")