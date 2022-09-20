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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer(corpus)
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names)
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
