dayType = 3

weekend = 1
workday = 2
holiday = 3

"""
if dayType == 1:
    print(dayType)
elif dayType == 2:
    print(dayType)
else:
    print(dayType)
"""

# inaczej : wykorzystując pass

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass


# składnia uproszczona

dayDescription = "weekend" if dayType == 1 else "workday" if dayType == 2 else "holiday"
print(dayDescription)
print("weekend") if dayType == 1 else print("workday") if dayType == 2 else print("holiday")