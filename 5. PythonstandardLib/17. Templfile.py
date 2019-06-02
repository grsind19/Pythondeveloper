import tempfile

tempFile = tempfile.TemporaryFile()

tempFile.write(b"save this for me")
tempFile.seek(0)

print(tempFile.read())