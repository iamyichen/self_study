# coding=utf8

#迭代器对象
class OwnIteror():
     def __init__(self , arrs ):
          self.index = 0
          self.arrs = arrs
     def  __next__(self):
          if self.index > len( self.arrs ) - 1:
              raise StopIteration
          else:
              self.index +=1
              return self.arrs[ self.index - 1 ]

#可迭代对象
class OwnIterable():
      def __init__(self ,  *arrs ):
          self.arrs = arrs
      def __iter__(self):
          return OwnIteror( self.arrs )
a=OwnIterable(1,2,3,4,4,6)
l=list(a)
for item in a:
      print(item)
print(l)