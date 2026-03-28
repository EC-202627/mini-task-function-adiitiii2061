def calculate_fine(book_title, days_overdue, daily_rate=15.0, max_fine=200):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine 
book_title = input()
days_overdue = int(input())
fine = input()
max_fine = input()

fine = calculate_fine(book_title, days_overdue)
print("Book:", book_title)
print("Days overdue:", days_overdue)
print("Fine: Rs.", float(fine))





