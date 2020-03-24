import unittest

import grade


class GradeRangeTest(unittest.TestCase):
    def setUp(self):
        self.grade_range = grade.GradeRange(
            [100, 80, 75, 70, 65, 60, 55, 50, 0], [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
        )
    def test_print(self):
        print(str(self.grade_range))
        print(self.grade_range.info())


class RecordTest(unittest.TestCase):
    def setUp(self):
        self.record_a = grade.Record(73, name="Computers and Programming")
        self.record_b = grade.Record(100, name="Easy subject")

    def test_class_type(self):
        self.assertIsInstance(self.record_a, grade.Record)

    def test_grade(self):
        self.assertEqual(self.record_a.grade, 3)

    def test_unknown_grade(self):
        try:
            self.record_b = grade.Record(-1, name="Some Erronous Subject")
        except IndexError:
            pass
        else:
            self.fail("IndexError not raised")

    def test_grade_change(self):
        self.record_a.set_score(20)
        self.assertEqual(self.record_a.grade, 0)


if __name__ == "__main__":
    unittest.main()
