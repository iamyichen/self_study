def getVar_byName(name):
    for key in globals().keys():
        if key==name:
            return eval(key)
            
def getName_byVar(var):
    for key,value in globals().items():
        if value==var:
            return key

a=1
b=[1,2,3]

c=getVar_byName("a")
c+=1
d=getVar_byName("b")
d.append(0)

print(getVar_byName("a"),id(a),a)
print(getVar_byName("b"),id(b),b)
print(getVar_byName("c"),id(c),c)
print(getVar_byName("d"),id(d),d)