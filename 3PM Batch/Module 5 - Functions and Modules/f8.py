def analyse_marks(marks):
    return [sum(marks), max(marks), min(marks), sum(marks) / len(marks)]

marks = [60,78,37,91]
total = analyse_marks(marks)

print(type(total))
# print(f"Total marks: {total}, Highest marks: {highest}, Lowest marks: {lowest}, Average: {avg}")