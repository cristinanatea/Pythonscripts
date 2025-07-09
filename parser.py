
def parser():
    last_words=[]
    file_name = "/home/cristina/Downloads/logcat_applications.txt"
   # caractere = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    with open (file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            if words:
                last_word = words[-1].strip("!@#$%^&*()_+<>?:.,;{}[]").split(".")[-1]
            #if all (char in caractere for char in last_word):
               # last_words.append(last_word)
            if last_word.isalpha() and last_word.isprintable() and last_word.isascii():
                last_words.append(last_word)
    return last_words

result = parser()
print(result)




