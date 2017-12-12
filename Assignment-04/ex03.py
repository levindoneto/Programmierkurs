#!/usr/local/bin/python3


from typing import *
from progkurs import *
from ex02 import ProbabilisticLemmatizer

class ProbabilisticLemmatizerPlus(ProbabilisticLemmatizer):
    """
    Implement the lemmatize method by filling in the blank.
    """
    def lemmatize(self, token: str) -> Optional[str]:
        """
        Return most probable lemma -- if it exists, else None.
        """
        result: Optional[str] = None
        if token in self.token2lemma2prob:
            lemma2prob: Mapping[str,float] = self.token2lemma2prob[token]
            fill(____)
        
        return result



def test():
    counts_fn = "ukwac-tok-lem.tok-len-4-6.subsel.sortNR.utf8"
    with open(counts_fn, encoding="utf8") as count_data:
        rows: Iterable[List[str]] = (line.split() for line in count_data)
        token_lemma_counts: Iterable[Tuple[str,str,Count]] = ((t, l, int(c)) for (c, t, l, p) in rows)
        prob_lem = ProbabilisticLemmatizerPlus(token_lemma_counts)

    assert prob_lem.lemmatize('caught') == 'catch'
    assert prob_lem.lemmatize('desks') == 'desk'
    assert prob_lem.lemmatize('threw') == 'throw'
    assert prob_lem.lemmatize('bigger') == 'big'
    assert prob_lem.lemmatize('smaller') == None
    

if __name__ == '__main__':
    test()
