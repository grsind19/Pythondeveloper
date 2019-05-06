def main():
  # f = open('textfile.txt','w+')

  # for i in  range(10):
  #   f.write("this is line "+str(i) + "\r\n")
  
  g = open('textfile.txt','r')

  if g.mode == 'r':
    contents = g.read()
    print(contents)

if __name__ == "__main__":
    main()