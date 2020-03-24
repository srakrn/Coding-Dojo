from itertools import tee


def pair(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)


class Record:
    def __init__(self, score, name=None):
        self.score = score
        self.name = name
        pass

    def calculate_grade(self):
        ranges = [100, 80, 75, 70, 65, 60, 55, 50, 0]
        grades = [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
        for (upper_bound, lower_bound), grade in zip(pair(ranges), grades):
            if self.score >= lower_bound and self.score < upper_bound:
                return grade
        raise IndexError("Score not in range.")
