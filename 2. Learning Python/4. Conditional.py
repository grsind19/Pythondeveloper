def main():
  x,y = 10,100

  if x < y :
    st ="X is less than Y"
  elif (x ==y):
    st ="X is same as the Y"
  else:
    st = "X is greater than y"
  print(st)

  st = "X is less than Y " if x <y else "X is greater than or same as y"

  print(st)

if __name__ == "__main__":
    main()