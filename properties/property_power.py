# class Cricket:
#     # """
#     # this is a class about cricket modes
#     # """
#     _modes = {"TEST", "ODI", "T20"}
#
#     def __init__(self, mode):
#         self.set_mode(mode)
#
#     def get_mode(self):
#         """
#         getting cricket mode
#         """
#         return self._mode
#
#     def set_mode(self, mode):
#         """
#         setting cricket mode
#         """
#         if mode in self._modes:
#             self._mode = mode
#         else:
#             raise ValueError("")
#
#     def del_mode(self):
#         """
#         deleting cricket mode
#         """
#         del self._mode
#
#     mode = property(fget=get_mode, fset=set_mode, fdel=del_mode)
#
#
# t20 = Cricket("T20")
# print(t20.__dict__)
# t20.__dict__["mode"] = "ODI"
# print(t20.__dict__)
# # even though we have mode attr same as property attr, the property attr got invoked
# t20.mode = "TEST"
# print(t20.__dict__)
# del t20.mode
# print(t20.__dict__)
# # the docstring of property always fetches from the getter function and if we provide doc value in property instance..then that will get prioritized.
# print(Cricket.mode.fget.__doc__)
# print(Cricket.mode.fset.__doc__)
# print(Cricket.mode.fdel.__doc__)
# try:
#     raise ArithmeticError("okok")
# except:
#     print("bwh")
# except ArithmeticError:
#     print("dfnjo")
# x='\''
# print(x)
# import math
#
# print(math.pow(2))
# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))
# try:
#     x=x/x
# except Exception as e:
#     print(len(e.args))
# class A:
#     def __str__(self):
#         return "a"
# class B(A):
#     def __str__(self):
#         return "b"
#
# class C(B):
#     pass
#
# c=C()
# print(c)
import math
# def f(x):
#     try :
#         x=x/x
#     except:
#         print("a")
#     else:
#         print("b")
#     finally:
#         print("c")
# f(1)
# f(1)

# class Ex(Exception):
#     def __init__(self,msg):
#         Exception.__init__(self,msg+msg)
#         self.args=(msg,)
#
# try:
#     raise Ex("ex")
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)
from datetime import datetime
# from io import klass
from time import strftime

# print(date(1992,1,16)- date(1992,1,15))
# d=datetime(2019,11,27,11,27,22)
# print(d.strftime('%y/%B/%d %H:%M:%S'))
# b=bytearray(3)
# print(b)
# import calendar
# print(calendar.weekheader(2))
# def fun(n):
#     s='+'
#     for i in range(n):
#         s+=s
#         yield s
# for x in fun(2):
#     print(x)
# print(len("\\\"))
# from datetime import timedelta
# delta=timedelta(weeks=1,days=7,hours=11)
# print(delta*2)
# print(float("1"))
# d1=datetime(2019,12,27,11,27,22)
# d2=datetime(2019,11,27,0,0,0)
# print(d1-d2)
# print("555"=="55")
# print(list(map(lambda x: x + 5, [int(bytearray(10)[0])])))
# print(float("1,0"))
# print(math.ceil(3.0) + math.floor(4.9) + 3)
# print('20' > '8' or '20' > 8)
# class A:
#     b = 'b'
#
#
#     def __init__(self):
#         self.c = 'c'
#         d = self.c
#
#
# a = A()
# print(a.d)
# txt = 'aga aga aga aga'
# print(txt.rfind('aga', 5))
# window max task
deque = []
ans = []
k = 3
lst = [1,3,1,2,0,5]
deque.append(lst[0])
for i in range(1, k):
    if deque[0] > lst[i]:
        deque.append(lst[i])
    else:
        deque.insert(0, lst[i])
print(deque)
for idx in range(k, len(lst)):
    ele = lst[idx]
    ans.append(deque[0])
    deque.remove(lst[idx-k])
    if deque and ele > deque[0]:
        deque.insert(0, ele)
    else:
        deque.append(ele)
ans.append(deque[0])
print(deque)
print(ans)
