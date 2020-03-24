import grade

score = float(input("Input score: "))
record = grade.Record(score, criteria=grade.thai_grade_range_wo_charge)
print("Grade: {}".format(record.grade))
