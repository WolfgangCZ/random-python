import os, sys

dirname = os.path.dirname(__file__)
sys.path.append(dirname)

print(f"dir: {dirname}")

class TestClass:
    def __init__(self):
        pass
    
    def do1(self):
        print("im doing 1")
    def do2(self):
        print("im doing 2")

t = TestClass()



a = {"a": t.do1(),
     "b": t.do2()}
def do(name, data):
   return data[name] 
    

do("a", a)
do("b", a)
