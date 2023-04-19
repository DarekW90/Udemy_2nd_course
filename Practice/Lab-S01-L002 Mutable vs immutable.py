days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays.remove("sat")
workdays.remove("sun")
print("Dni tygodnia:  " ,days)
print("Dni pracujące: ",workdays)
