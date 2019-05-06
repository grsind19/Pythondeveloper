from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  print(" Todays date is ",today)
  print("Components:", today.day,
  today.month, today.year)

  today = datetime.now()
  print ("Current date and time is:", today)

if __name__ == "__main__":
    main()