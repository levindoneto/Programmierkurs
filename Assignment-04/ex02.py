#!/usr/local/bin/python3


from typing import *
from progkurs import *

Count = int

class ProbabilisticLemmatizer:
    """
    Learns how to lemmatize according to token_lemma_counts
    (most common lemma per token should be used).
    
    Implement these methods by filling in the blanks (i.e. 'fill(____)').
    
    E.g. with: token_lemma_counts    = [('dogs', 'dog', 4), ('dogs', 'dogs', 1), ('cats', 'cat', 3)]
         then: self.token2lemma2prob = {'dog':{'dog':0.8, 'dogs':0.2}, 'cats':{'cat':1.0}}
    
    """
    def __init__(self, token_lemma_counts: Iterable[Tuple[str,str,Count]]) -> None:
        
        token2lemma2count: Dict[str,Dict[str,Count]] = {}
        token2count: Dict[str,Count] = {}
        for t, l, c in token_lemma_counts:
            lemma2count: Dict[str,Count] = token2lemma2count.get(t, {})
            lemma2count[l] = lemma2count.get(l, 0) + fill(____)
            token2count[t] = token2count.get(t, 0) + fill(____)
            token2lemma2count[t] = lemma2count
        
        token2lemma2prob: Dict[str,Dict[str,float]] = {}
        for t, l2c in token2lemma2count.items():
            if t not in token2lemma2prob: token2lemma2prob[t] = {}
            for l, c in l2c.items():
                token2lemma2prob[t][l] = c / token2count[t]
        
        self.token2lemma2prob = token2lemma2prob
    
    def lemmas(self, token: str) -> List[Tuple[str,float]]:
        lemma_probs: List[Tuple[str,float]] = []
        if token in self.token2lemma2prob:
            lemma2prob: Mapping[str,float] = self.token2lemma2prob[token]
            lemma_probs = list(lemma2prob.items())
        return lemma_probs

    def get_prob_lemma(self, token: str, lemma: str) -> float:
        prob: float = self.token2lemma2prob.get(token, {}).get(lemma, 0)
        return prob


def test():
    counts_fn = "ukwac-tok-lem.tok-len-4-6.subsel.sortNR.utf8"
    with open(counts_fn, encoding="utf8") as count_data:
        rows: Iterable[List[str]] = (line.split() for line in count_data)
        token_lemma_counts: Iterable[Tuple[str,str,Count]] = ((t, l, int(c)) for (c, t, l, p) in rows)
        prob_lem = ProbabilisticLemmatizer(token_lemma_counts)

    assert 1 > prob_lem.get_prob_lemma('bigger', 'big') > .99
    assert prob_lem.get_prob_lemma('easier', 'easy') > prob_lem.get_prob_lemma('easier', 'easier')
    assert prob_lem.get_prob_lemma('Tried', 'try') == .4
    assert prob_lem.get_prob_lemma('Throws', 'throw') == .25
    assert prob_lem.get_prob_lemma('Served', 'serve') == .12
    assert dict(prob_lem.lemmas('Stones')) == {'Stone': 0.5625, 'Stones': 0.3125, 'stone': 0.125}
    assert .7 < prob_lem.get_prob_lemma('WANTED', 'WANTED') < .8

if __name__ == '__main__':
    test()

