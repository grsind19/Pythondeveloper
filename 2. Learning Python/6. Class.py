class myClass():
  def method1(self):
    print("my method 1")
  def method2(self, something):
    print("my method 2", something)

class anotherClass(myClass):
  def method1(self):
    print("another class method1")
  def method2(self):
    myClass.method1(self)
    print("another class method2")

def main():
  c = myClass()
  c.method1()
  c.method2("I hate yu")

  c = anotherClass()
  c.method2()

if __name__ == "__main__":
    main()