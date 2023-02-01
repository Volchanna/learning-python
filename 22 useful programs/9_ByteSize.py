def ByteSize(string):
    return len(string.encode("utf8"))
print(ByteSize("Python")) #6
print(ByteSize("Data")) #4
string = "hello"
print(string.encode("utf8"))