"""
Created on Mon May 16 21:55:48 2016

@author: Minhyun Yoo
"""
import ctypes as c

# list -> array
def list2cArray(target):
    
    arr = (c.c_double * len(target))(*target)
    
    return arr;

# decalare structure 
class strtest(c.Structure):
    _fields_ = [("x", c.c_double),
                ("y", c.c_double)]

# load dll 1, 2
mydll1 = c.cdll.LoadLibrary("R:\\array_pass.dll")
mydll2 = c.cdll.LoadLibrary("R:\\struc_pass.dll")

# init list
x = [1.0, 2.2, 3.3];

# to pass from python to *.dll, modify data type
ia = list2cArray(x);

func = mydll1.cp;

# result data type
func.restype = c.c_double

result = func(c.byref(ia), len(x));

print("<array test>")
print("list sum :", result)

########################################################
print("--------------------------------------")
print("<struct test>")
# # of elements
num = 3;

# return array
res = (c.c_double * num)();

# array of structure 
s1 = (strtest * num)();

# declare funcs
dllfill = mydll2.fill;
dllsum = mydll2.sum;

# call fill func
dllfill(c.byref(s1), c.c_int(num));

for i in range(num):
    print("s1[{}].x, y : {}, {}". format(i, s1[i].x,  s1[i].y))    
#    print("a", format(i))

# call sum func
dllsum(c.byref(res), c.byref(s1), num);

for i in range(num):
    print("sum[{}] : {}". format(i, res[i]))