from itertools import chain


class CountVectorizer:

    def __init__(self, corpus: [str], lowercase=True):
        sentences = [sent.lower().split() if lowercase else sent.split() for sent in corpus]
        self.__features = list(set(chain.from_iterable(sentences)))
        self.__n_features = len(self.__features)

    def fit_transform(self, corpus: [str], lowercase=True) -> [[int]]:
        tdm = []
        counters = [dict.fromkeys(self.__features, 0) for _ in corpus]
        counters = zip(counters, corpus)
        for c, sent in counters:
            tokens = sent.lower().split() if lowercase else sent.split()
            for w in tokens:
                if w in self.__features:
                    c[w] += 1
            tdm.append(list(c.values()))
        return tdm

    @property
    def get_feature_names(self) -> [str]:
        return self.__features

