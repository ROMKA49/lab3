Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Point:
    x=0
    y=0
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y

point=Point()
point.setx(x=int(input("Введите x")))
point.sety(y=int(input("Введите y")))
print(point.getx())
print(point.gety())
