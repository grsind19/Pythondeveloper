from html.parser import HTMLParser 

class HTMLParser(HTMLParser):
  def handle_startendtag(self, tag, atts):
    print("Start tag :",tag)
    for attr in atts:
      print("attr :", attr)
  def handle_endtag(self, tag):
     print("End tag :", tag)
  def handle_comment(self, data):
    print("Comment :",data)
  def handle_data(self,data):
    print("Data :", data)


parser = HTMLParser()

parser.feed("<html><head><title>Coder</title></head><body><h1><!-- hi -->Im a coder </h1><body></html>")
print()