import sys


def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


book_title = " ".join(sys.argv[1:-2])
days_overdue = int(sys.argv[-2])
max_fine = float(sys.argv[-1])

fine = calculate_fine(book_title, days_overdue, 5.0, max_fine)

print("Book:", book_title)
print("Days overdue:", days_overdue)
print("Fine: Rs.", float(fine))


