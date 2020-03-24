from itertools import tee


def pair(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)


class Record:
    def __init__(self, score, name=None):
        self.name = name
        self.set_score(score)
        pass

    def set_score(self, score):
        self._score = score
        self._calculate_grade()

    def _calculate_grade(self):
        ranges = [100, 80, 75, 70, 65, 60, 55, 50, 0]
        grades = [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
        for (upper_bound, lower_bound), grade in zip(pair(ranges), grades):
            if self.score >= lower_bound and self.score < upper_bound:
                self._grade = grade
                return
        raise IndexError("Score not in range.")

    @property
    def score(self):
        return self._score

    @property
    def grade(self):
        return self._grade
