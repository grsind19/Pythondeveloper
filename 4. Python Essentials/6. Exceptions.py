import sys

def main():
  try:
    x = 5/0
  except ValueError:
    print('I caught value error')
  except ZeroDivisionError:
    print(f'dont divide by zero:{sys.exc_info()[1]}')
  else:
    print('good job')


if __name__ == "__main__":
    main()