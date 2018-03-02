class it():
    def __init__(self,*args):
        self.__args=args

    def __iter__(self):
        return iit(self)
     
    @property    
    def args(self):
        return self.__args

class iit():
    def __init__(self,obj):
        self.index=0
        self.args=obj.args
        self.lenth=len(obj.args)
        

    def __next__(self):
        if self.index <self.lenth:
            self.index+=1
            return self.args[self.index-1]
        else:
            raise StopIteration
            
a=it(1,2,3,4)
for i in a:
    print(str(i))
for i in a:
    print(str(i))