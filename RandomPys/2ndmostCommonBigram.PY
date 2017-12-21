import nltk
#nltk.download('brown') # Just if it has not been installed yet
brown_words = set(nltk.corpus.brown.words())
#print (brown_words)
brown_word_freqs = nltk.FreqDist(nltk.corpus.brown.words())
#brown_word_freqs.most_common()[:20]

print("Second most common bigram in the corpus brown: ", nltk.FreqDist(nltk.bigrams(nltk.corpus.brown.words())).most_common()[1])