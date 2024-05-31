a = 1

def fnc1():
    b=2
    def fnc2():
        c=3
        print(a) 
        print(b) 
        print(c) 
    fnc2()
fnc1()
#сначала внутри fnc2, потом внутри fnc1, затем в глобальной области видимости