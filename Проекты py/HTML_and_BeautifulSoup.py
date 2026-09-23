from bs4 import BeautifulSoup
with open("itgen.html") as file:
    content = file.read()
суп = BeautifulSoup(content,"html.parser")
print(суп.h1.string)
aat = суп.find_all(name = "a")
print(aat)
