def calculate_fine(days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine

data = input().split()

book_title = "".join(data[:-1])
days = int(data[-1])

fine = calculate_fine(days)

print("Books:",book_title,"Days overdue:", days,"fine:Rs.", fine)

if fine == 150.0:
    print ("you have accumulated the maximum fine of INR: 150.0")
    