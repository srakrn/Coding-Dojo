from itertools import tee


def pair(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)


class GradeRange:
    def __init__(self, ranges, grades):
        self.ranges = ranges
        self.grades = grades

    def __str__(self):
        return "GradeRange of {} grades at {}".format(len(self.grades), hex(id(self)))

    def info(self):
        descriptions = []
        for (upper, lower), grade in zip(pair(self.ranges), self.grades):
            descriptions.append("{} <= x < {}\t=> {}".format(lower, upper, grade))
        return "\n".join(descriptions)


thai_grade_range = GradeRange(
    [100, 80, 75, 70, 65, 60, 55, 50, 0], [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
)


class Record:
    def __init__(self, score, name=None, criteria=thai_grade_range):
        self.name = name
        self.criteria = criteria
        self.set_score(score)
        pass

    @property
    def score(self):
        return self._score

    @property
    def grade(self):
        return self._grade

    def set_score(self, score):
        self._score = score
        self._calculate_grade()

    def _calculate_grade(self):
        ranges = self.criteria.ranges
        grades = self.criteria.grades
        for (upper_bound, lower_bound), grade in zip(pair(ranges), grades):
            if self.score >= lower_bound and self.score < upper_bound:
                self._grade = grade
                return
        if self.score == ranges[0]:
            return grades[0]

        raise IndexError("Score not in range.")
