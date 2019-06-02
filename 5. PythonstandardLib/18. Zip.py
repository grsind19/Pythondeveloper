import zipfile

zip = zipfile.ZipFile("Archive.zip",'r')
print(zip.namelist())

for meta in zip.infolist():
  print(meta)

print(zip.read("wish.txt"))

with zip.open("wish.txt") as f:
  print(f.read())

zip.extract("wish.txt")
zip.close()