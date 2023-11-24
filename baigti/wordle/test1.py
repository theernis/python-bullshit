file1 = open("words.txt","r")
file2 = open("filtered.txt","w")

text = file1.readlines()
for word in text:
    if (len(word) == 6 and word.split("\n")[0].isalpha()):
        file2.write(word.lower())

file1.close()
file2.close()