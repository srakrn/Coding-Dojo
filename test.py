import unittest

import grade


class RecordTest(unittest.TestCase):
    def setUp(self):
        self.record_a = grade.Record(73, name="Computers and Programming")

    def test_class_type(self):
        self.assertIsInstance(self.record_a, grade.Record)

    def test_grade(self):
        self.assertEqual(self.record_a.grade, 3)


if __name__ == "__main__":
    unittest.main()
