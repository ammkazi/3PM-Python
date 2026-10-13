def analyse(marks):
    return sum(marks), max(marks), min(marks), sum(marks) / len(marks)

total , max, min , avg = analyse([78,80,40,58,94,33])

print(f"Total {total}, high {max}, low {min}, avg {avg:.2f}")