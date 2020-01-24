class test(object):
    def __init__(self,s):
        print('__init__',s)
    def __new__(cls,s):
        print('__new__',s)
        return super().__new__(cls)
    def __call__(self,):
        print('__call__')
class A(object):
  def __init__(self):
   print("enter A")
   super(A,self).__init__()
   print("leave A")

class B(object):
  def __init__(self):
   print("enter B")
   super(B,self).__init__()
   print("leave B")

class C(A):
  def __init__(self):
   print("enter C")
   super(C, self).__init__()
   print("leave C")

class D(A):
  def __init__(self):
   print("enter D")
   super(D, self).__init__()
   print("leave D")
class E(B, C):
  def __init__(self):
   print("enter E")
   super(E,self).__init__()
   print("leave E")

class F(E, D):
  def __init__(self):
   print("enter F")
   super(F,self).__init__()
   print("leave F")
'''
F() result
enter F

enter E

enter B

enter C

enter D
enter A
leave A
leave D

leave C

leave B

leave E

leave F

'''