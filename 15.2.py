Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Animal:
  name=""
  def eat(self):
     print("Ням ням")
  def setName(self, newName):
     self.name = newName
  def getName(self):
     return self.name
  def makeNoise(self):
     print(self.name + " говорит Гррр")
  def __init__(self,newName):
     self.name=newName
     print("Родилось животное " + self.name)

mycat=Animal("Ирис")
mycat.eat()
print(mycat.getName())
mycat.setName("Пушок")
print(mycat.getName())
mycat.makeNoise()