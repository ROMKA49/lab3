Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class StringVar:
    name="1"
    def set(self,newName):
        self.name = newName
    def get(self):
        return self.name
str=StringVar()
print(str.get())
str.set("Changed name")
print(str.get())