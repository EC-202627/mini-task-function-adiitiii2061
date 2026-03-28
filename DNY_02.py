def calculate_fine(days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return fine

data = input().split()


book_title = " ".join(data[:-2])
days = int(data[-2])
rate = float(data[-1])


fine = calculate_fine(days, rate)


print("Book:", book_title, "Days overdue:", days, "Fine: Rs.", fine)

