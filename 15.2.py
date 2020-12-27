Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> класс  Animal :
  name = ""
  def  eat ( self ):
     print ( "Ням ням" )
  def  setName ( self , newName ):
     я . name  =  newName
  def  getName ( сам ):
     вернуть  себя . имя
  def  makeNoise ( сам ):
     печать ( сам . имя  +  "говорит Гррр" )
  def  __init__ ( self , newName ):
     я . name = newName
     print ( "Родилось животное"  +  сам . имя )

mycat = Животное ( "Ирис" )
mycat . есть ()
печать ( mycat . getName ())
mycat . setName ( "Пушок" )
печать ( mycat . getName ())
mycat . makeNoise ()
