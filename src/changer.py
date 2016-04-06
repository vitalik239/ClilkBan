import svn_saver
import makegood
import file_loader

words = {}
file_loader.get()
for word in file_loader.badwords:
    words[word] = makegood.good(word)


svn_saver.save(words)
