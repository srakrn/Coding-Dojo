import grade

score = float(input("Input score: "))
record = grade.Record(score)
print("Grade: {}".format(record.grade))
