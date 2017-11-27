from typing import *
import reader
#from progkurs import *

T = TypeVar('T')

def generate_ngrams(seq: Tuple[T], n: int) -> List[Tuple[T]]: # Tuple: Inmutable
    # ngrams are sub-sequences of 'seq' of length 'n'.
    # For seq = ('a', 'b', 'c', 'd') and n = 2, the result would be
    # ngrams = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    ngrams = []
    for i in range(len(seq)):
        ngrams.append(seq[i:i+n])
    #print("n-grams: ", ngrams)
    return ngrams


def get_corpus_frequencies(seq: List[Tuple[T]]) -> Dict[Tuple[T], int]:
    # Counts how often each item occurs in 'seq' and returns
    # the frequencies in a dictionary.
    frequencies = {}
    for token in seq:
        if (token in frequencies):
            newFrequency = str(int(frequencies[token])+1)
            frequencies.update({token: newFrequency})
        else:
            frequencies.update({token: '0'})
    #print(frequencies)
    return frequencies


def print_most_frequent(type: str, token_frequencies: Dict[Iterable[str], int], n: int) -> None:
    print("\nThe ", n, " most frequent", type+"s", "in the given corpus:")
    print("Frequencies -> n-gram")
    for k, v in sorted(
            token_frequencies.items(),
            key=lambda x: x[1],
            reverse=True)[:n]:

        print("  ", k, "-> " , v)


def main():
    corpus = reader.read('hamlet.txt')

    unigrams = generate_ngrams(corpus, 1)
    bigrams = generate_ngrams(corpus, 2)
    trigrams = generate_ngrams(corpus, 3)

    unigram_frequencies = get_corpus_frequencies(unigrams)
    bigram_frequencies = get_corpus_frequencies(bigrams)
    trigram_frequencies = get_corpus_frequencies(trigrams)

    print_most_frequent("unigram", unigram_frequencies, 10) # 10 most frequent
    print_most_frequent("bigram", bigram_frequencies, 10)
    print_most_frequent("trigram", trigram_frequencies, 10)

main()
