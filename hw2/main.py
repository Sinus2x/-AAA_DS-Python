from itertools import chain


class CountVectorizer:

    def __init__(self, corpus: [[str]]):
        words = [sent.split() for sent in corpus]
        self.__features = list(set(chain.from_iterable(words)))

    def fit_transform(self):
        pass

    @property
    def get_feature_names(self):
        return self.__features


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer(corpus)
    # count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names)
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    # print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

