
def tongji(seq):
    tmp=[]
    for item in seq:
        if item not in tmp:
            tmp.append(item)            
    var={n:[v,0] for n,v in enumerate(tmp)}
    for k,v in var.items():
        for item in seq:
            if item ==v[0]:
                var[k][1]+=1        
    l=var.values()
    return sorted(l,key=lambda x:x[1],reverse=True)

def quchong(seq):
    tmp_seq=[]
    tmp_list=tongji(seq)
    for v in [x[0] for x in tmp_list]:
        tmp_seq.append(v)
    return tmp_seq        

def view(seq):
    print("去重前:")
    print(seq)
    print("元素统计如下:")
    tmp_list=tongji(seq)
    print("序号\t元素\t重复次数")
    for i in range(len(tmp_list)):
        print("{}\t{}\t{}".format(i+1,tmp_list[i][0],tmp_list[i][1]))
    print("去重后:")
    tmp=quchong(seq)
    print(tmp)
    print("*"*30)     

a=[11,25,33,11,"tt","test",(1,2),"tt",(1,2),["one","two","three"]]
view(a)
b="The dict type has been reimplemented to use a more compact representation based on a proposal by Raymond Hettinger and similar to the PyPy dict implementation. This resulted in dictionaries using 20% to 25% less memory when compared to Python 3.5."
view(b)
c="无论是同性还是异性，在交往过程中千万不要过于亲密，有一句话是这样说的“凡与人交，不可求一时亲密”就是这样意思。"
view(c)