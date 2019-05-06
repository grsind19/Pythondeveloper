from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


print(timedelta(days=365,hours=5,minutes=1))
now = datetime.now()

print("one year from now" + str(now+timedelta(days=3)))

today = date.today()

afd = date(today.year,4,1)

if afd < today:
  print("Afd wend pass by %d days ago" %((today-afd).days))
  afd = afd.replace(year=today.year+1)

time_to_afd = afd- today
print("It is just", time_to_afd.days)



# if __name__ == "__main__":
#     main()