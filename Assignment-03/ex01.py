from typing import *
import reader
from progkurs import *


T = TypeVar('T')

def generate_ngrams(seq: Tuple[T], n: int) -> List[Tuple[T]]:
    """Generates ngrams of length 'n' from the input sequence 'seq'.
    ngrams are sub-sequences of 'seq' of length 'n'.
    For seq = ('a', 'b', 'c', 'd') and n = 2, the result would be
    ngrams = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    """
    ngrams: list = []
    for i in range(fill(____)):
        ngrams.append(seq[i:i+n])
    return ngrams


def get_corpus_frequencies(seq: List[Tuple[T]]) -> Dict[Tuple[T], int]:
    """Counts how often each each item occurs in 'seq' and returns
    the frequencies in a dictionary.
    """
    frequencies: dict = {}
    for token in seq:
        fill(____)
    return frequencies


def print_most_frequent(token_frequencies: Dict[Iterable[str], int], n: int) -> None:
    print("freq\tngram")
    for k, v in sorted(
            token_frequencies.items(),
            key=lambda x: x[1],
            reverse=True)[:n]:
        print(f"{v}\t{' '.join(k)}")
    print()


def main():
    corpus = reader.read('hamlet.txt')

    unigrams = generate_ngrams(corpus, 1)
    bigrams = generate_ngrams(corpus, 2)
    trigrams = generate_ngrams(corpus, 3)

    unigram_frequencies = get_corpus_frequencies(unigrams)
    bigram_frequencies = get_corpus_frequencies(bigrams)
    trigram_frequencies = get_corpus_frequencies(trigrams)

    print_most_frequent(unigram_frequencies, 10)
    print_most_frequent(bigram_frequencies, 10)
    print_most_frequent(trigram_frequencies, 10)


if __name__ == '__main__':
    main()
