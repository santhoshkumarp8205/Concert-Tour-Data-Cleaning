#NUMPY:
"""
 *) WHY SHOULD WE LEARN NUMPY?
  first, you should learn numpy. it is the most fundamental module for scientific
  computing with python. numpy provides the support of highly optimized multidimensional
  arrays, which are the most basic data structure of most machine learning algorithms.

  *) WHY DO PEOPLE USE NUMPY?
  numpy is one of the most commonly used packages for scientific computing in python.
  it provides a multidimensional array object, as well as variations such as masks and matrices,
  which can be used for various math operations.

  *) WHY IS NUMPY SO POWERFUL?
  what makes numpy so good? numpy has a syntax which is simultaneously compact,powerful and
  expressive. it allows users to manage data in vectors,matrices and higher dimensional arrays.



Numpy intro:

NumPy is a python library used for working with arrays.
it also has functions for working in domain of linear algebra, fourier transform, and matrices
NumPy was created in 2005 by travis Oliphant. it is an open source project and you can use it freely.
NumPy stands for numerical python



WHY USE NUMPY?
 *) In python we have lists that serve the purpose of arrays, but they are slow to process.
 *) NumPy aims to provide an array object that is up to 50x faster than traditional python lists
 *) the array object in numpy is called ndarray, it provides a lot of support function that makes
    working with ndarray very easy
 *)arrays are very frequently used in data science, where speed and resources are very important


HOW ARRAY IS FASTER THAN LIST:
numpy arrays are stored at continuous place in memory unlike lists, so processes can
access and manipulate them very efficiently.


notes:
a numpy array is a grid of values, all of the same type, and is indexed by a tuple of non_negative
integers. a list is the python equivalent of an array, but is resizeable and can contain of different types.


*) vector:

   --------------------------
   -  1    -  5    -   10   -
   --------------------------

   vector (1D array)
   dimension = 1
   (1 index required)


*) matrices:

   --------------------------
   -  1    -  5    -   10   -
   --------------------------
   -  12   -  50   -   100  -
   --------------------------
   -  25   -  40   -   80   -
   --------------------------

   vector (2D array)
   dimension = 2
   (2 index required)



*) 3D array:


   --------------------------
   -  1    -  5    -   10   -
   --------------------------
   -  12   -  50   -   100  -
   --------------------------
   -  25   -  40   -   80   -
   --------------------------

   vector (3D array)
   dimension = 3
   (3 index required)


*) IN ABOVE 3-DIMENSIONS WILL SAID AS THE ARRAY IS ND-ARRAY.THEN THE VECTOR AND
   DIMENSIONS ARE DEPEND ON THE ARRAY

   vector (ND array)
   dimension = N
   (N index required)



numpy(numerical python) is a linear algebra library in python. it is a very important
library on which almost every data science or machine learning python packages such as
scipy(scientific python), matplotlib(plotting library), scikit-learn, etc depends on to
a reasonable extent.

numpy is very useful for programing mathematical and logical operations on arrays. it
provides an abundance of useful features for operation on n-arrays and matrices in python.


list stored into the separated memory in python but the arrays will stored in contingious memory_space
"""


import numpy as np

scalar
#2

#vector
vec = np.array([1,2,3,4])
print(type(vec))
print(vec.ndim)
print(vec.shape)
"""
#output:
<class 'numpy.ndarray'>
1
(4,)
"""


#Matrices:
matrices = np.array([[1,2,3],[4,6,7],[4,5,6]])
print(type(matrices))
print(matrices.ndim)
print(matrices.shape)
"""
#output:
<class 'numpy.ndarray'>
2
(3, 3)
"""


#tensor
tensor = np.array([[[1,2,3],[4,5,6],[3,4,5]],[[1,2,3],[4,6,7],[4,5,6]]])
print(type(tensor))
print(tensor.ndim)
print(tensor.shape)
"""
#output:
<class 'numpy.ndarray'>
3
(2, 3, 3)
"""



import numpy as np
#sum with - " axis = 0 "
value = [
            [1,  2,   3 ],
            [5,  6,   7 ],
            [10,100,1000]
                            ]

sum_value = np.sum(value,axis=0)
print(sum_value)
"""
#output:
[  16  108 1010]


note:
if the matrix dimension changed as after use the sum function.
let we check
"""

print(sum_value.ndim)
print(sum_value.shape)
"""
#note:
if the dimension will reduced after using sum function.
matrix will reduced as vector

#output:
1
(3,)
"""



#sum with - " axis = 1 "
value = [
            [1,  2,   3 ],
            [5,  6,   7 ],
            [10,100,1000]
                            ]

sum_value = np.sum(value,axis=1)
print(sum_value)
"""
output:
[   6   18 1110]


notes:
note:
if the matrix dimension changed as after use the sum function.
let we check
"""

print(sum_value.ndim)
print(sum_value.shape)
"""
notes:
if the dimension will reduced after using sum function.
matrix will reduced as vector


#output:
1
(3,)
"""



#arange(start,stop,step):
print(np.arange(12))
#[ 0  1  2  3  4  5  6  7  8  9 10 11]

"""
this is not possible in use range to iterate values but that error will
overcome by using numpy arange()

for i in range(0,12,3.14):
    print(i,end=" ")
"""

for i in np.arange(0,12,3.14):
    print(i,end=" ")
#0.0 3.14 6.28 9.42

import numpy as np
#difference between range and np.arange:
print(range(0,12))
#range(0, 12)


print(np.arange(0,12))
"""
note:
this arange method will automatically extended.by the total number of elements
provided is "stop_value" in above equation also there are 12 elements has arrived
into the after loop iteration

#output:
[ 0  1  2  3  4  5  6  7  8  9 10 11]
"""



#np.arange with reshape():
matrices = np.arange(25).reshape(5,5)
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))
"""
#output:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
2
(5, 5)
5
<class 'numpy.ndarray'>
"""




matrices = np.arange(6).reshape(6,1)
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))
"""
#output:
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]]
2
(6, 1)
6
<class 'numpy.ndarray'>
"""




matrices = np.arange(6).reshape(6)
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))
"""
#output:
[0 1 2 3 4 5]
1
(6,)
6
<class 'numpy.ndarray'>
"""



matrices = np.arange(20).reshape([5,2,2])
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))
"""
#output:
[[[ 0  1]
  [ 2  3]]

 [[ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]]

 [[12 13]
  [14 15]]

 [[16 17]
  [18 19]]]
3
(5, 2, 2)
5
<class 'numpy.ndarray'>
"""




"""
matrices = np.arange(25).reshape([5,2,2])
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))


#notes:
if the multiplication of all product in reshape method is equal to arange iterated values.
thats why this will correct otherwise python return error.


#output:
Traceback (most recent call last):
  File "D:\ds\python files\ numpy_py.py", line 311, in <module>
    matrices = np.arange(25).reshape([5,2,2])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: cannot reshape array of size 25 into shape (5,2,2)

"""



matrices = np.arange(40).reshape([5,2,2,2])
print(matrices)
print(np.ndim(matrices))
print(np.shape(matrices))
print(len(matrices))
print(type(matrices))
"""
#notes:
if the arguments are separated by three or four means the dimension also changed.
*) three of you separated the reshape arguments --> 3-dimension to created tensors
*) four of you separated the reshape arguments --> 4-dimension to created tensors
*) five of you separated the reshape arguments --> 5-dimension to created tensors



#output:
[[[[ 0  1]
   [ 2  3]]

  [[ 4  5]
   [ 6  7]]]


 [[[ 8  9]
   [10 11]]

  [[12 13]
   [14 15]]]


 [[[16 17]
   [18 19]]

  [[20 21]
   [22 23]]]


 [[[24 25]
   [26 27]]

  [[28 29]
   [30 31]]]


 [[[32 33]
   [34 35]]

  [[36 37]
   [38 39]]]]
4
(5, 2, 2, 2)
5
<class 'numpy.ndarray'>
"""


#value accessing and slicing
value = [

      [          [ 0,1],[2,3],[4,5]        ],

      [          [6,7],[8,9],[10,11]        ],

      [      [12 , 13],[14 ,15],[16, 17]    ]
                                                 ]

#accessing
"""
notes:
if you accessed the array means that will return the scalar values

"print(value[1][1][1])" --> 1 --> this value is scalar
"""
print(value[1])
print(value[1][1])
print(value[1][1][1])
"""
#output:
[[6, 7], [8, 9], [10, 11]]
[8, 9]
9
"""


print(value[0])
print(value[0][0])
print(value[0][0][1])
"""
#output:
[[0, 1], [2, 3], [4, 5]]
[0, 1]
1
"""


"""
#slicing:

notes:
if we slicing the array means we get into a list or the value been vector
"""
print(value[0:2])
#[[[0, 1], [2, 3], [4, 5]], [[6, 7], [8, 9], [10, 11]]]


# another example for slicing and access different
sampleList = [1,2,3,4,5,6]

#accessing
print(sampleList[2])
print(type(sampleList[2]))
"""
#output:
3
<class 'int'>
"""


#slicing
print(sampleList[2:3])
print(type(sampleList[2:3]))
"""
#output:
[3]
<class 'list'>
"""



#by slicing the array
import numpy as np
matrix = np.arange(18).reshape(2,3,3)
print(matrix)
print(matrix[0][1])
print(matrix[0][1][1])
print(type(matrix[0][1][1]))
"""
#output:
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]]
[3 4 5]
4
<class 'numpy.int64'>
"""



#ndarray():
import numpy as np
array = np.array([1,2,3,4,5])
print(array)
print(type(array))
"""
[1 2 3 4 5]
<class 'numpy.ndarray'>
"""



import numpy as np
array = np.array([1,2,3,4,5],dtype=str,copy=True,subok=True,ndmin=True,order="A")
print(array)
print(type(array))
"""
#output:
['1' '2' '3' '4' '5']
<class 'numpy.ndarray'>
"""



array = np.array([1,2,3,4,5],dtype=float,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(type(array))
"""
#output:
[[[1. 2. 3. 4. 5.]]]
<class 'numpy.ndarray'>
"""



array = np.array([1,2,3,4,5],dtype=float,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
notes:
if the "itemsize" describes at size of the item, and then "size" describes at how many elements in array
so the "nbytes" will describes at multiply of both itemsize and size

nbytes = itemsize * size

#output:
[[[1. 2. 3. 4. 5.]]]
8
5
40
"""




array = np.array([1,2,3,4,5],dtype=str,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[['1' '2' '3' '4' '5']]]
4
5
20
"""




array = np.array([[1,2,3],[7,4,5]],dtype=str,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[['1' '2' '3']
  ['7' '4' '5']]]
4
6
24
"""





array = np.array([[1,2,3],[7,4,5]],dtype=bool,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
notes:
if the value is 1, because of the "itemsize" will get 1 at each item has size 1
because of the "size" will get 6

[[[ True  True  True]
  [ True  True  True]]]
1
6
6
"""


array = np.array([[1,2j,2.4],["a",4,0]],dtype=None,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(type(array))
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
notes:
None will provided highest precedence so the datatype make as "string"

#output:
[[['1' '2j' '2.4']
  ['a' '4' '0']]]
<class 'numpy.ndarray'>
256
6
1536
"""



array = np.array([[1,2,0],[7,4,0]],dtype=bool,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[[ True  True False]
  [ True  True False]]]
1
6
6
"""





array = np.array([[1,True,0],[7,4,"a"]],dtype=object,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[[1 True 0]
  [7 4 'a']]]
8
6
48
"""




#if the values will be in mixed dtype we changed as string
array = np.array([[1,True,0],[7,4,"a"]],dtype=str,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[['1' 'True' '0']
  ['7' '4' 'a']]]
16
6
96
"""




array = np.array([[1,2,0],[7,4,0]],dtype=complex,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
#output:
[[[1.+0.j 2.+0.j 0.+0.j]
  [7.+0.j 4.+0.j 0.+0.j]]]
16
6
96
"""





array = np.array([[1,2,False],[7,True,0]],dtype=complex,copy=True,subok=True,ndmin=3,order="f")
print(array)
print(array.itemsize)
print(array.size)
print(array.nbytes)
"""
notes:
if the "True" value will be return 1. then "False" value will be return 0.
to make as complex data type

#output:
[[[1.+0.j 2.+0.j 0.+0.j]
  [7.+0.j 1.+0.j 0.+0.j]]]
16
6
96
"""


import numpy as np

a = np.array([["santhosh","kiran"],["nithish","yuvan"]],dtype=str,ndmin=3)
np.put(a,[3],"praveen")
print(a)
"""
#output:
[[['santhosh' 'kiran']
  ['nithish' 'praveen']]]
"""



a = np.array([["santhosh","kiran"],["nithish","yuvan"]],dtype=str)
np.put(a,[1,2,10],["praveen","kumar","ram"],mode="clip")
print(a)
"""
notes:
if the array did not been extend so the out of index values will replaced as last value

#output:
[['santhosh' 'praveen']
 ['kumar' 'ram']]
"""



#re-assigned
"""
to the below examples "kumar" will replaced in 1st for "yuvan".
and then 2nd "ram" will replaced for "kumar"
"""
a = np.array(["santhosh","kiran","nithish","yuvan"],dtype=str)
np.put(a,[0,7,10],["praveen","kumar","ram"],mode="clip")
print(a)
#['praveen' 'kiran' 'nithish' 'ram']


#by altering bytes to stored values in memory
dt = np.dtype("i1") #or int8
a = np.array([(1,),(2,),(3,),(4,),(127,)],dtype=dt)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[  1]
 [  2]
 [  3]
 [  4]
 [127]]
<class 'numpy.ndarray'>
5
1
5
"""




#int8
a = np.array([(1,),(2,),(3,),(4,),(127,)],dtype=np.int8)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[  1]
 [  2]
 [  3]
 [  4]
 [127]]
<class 'numpy.ndarray'>
5
1
5
"""

#int16 or "i2" --> 2bytes or 16bits
a = np.array([(1,),(2,),(3,),(4,),(129,)],dtype=np.int16)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[  1]
 [  2]
 [  3]
 [  4]
 [129]]
<class 'numpy.ndarray'>
5
2
10
"""



dt = np.dtype("i2")
a = np.array([(1,),(2,),(3,),(4,),(129,)],dtype=dt)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[  1]
 [  2]
 [  3]
 [  4]
 [129]]
<class 'numpy.ndarray'>
5
2
10
"""


#int32 or "i4" --> 4bytes or 32bits
dt = np.dtype("i4")
a = np.array([(1,),(2,),(3,),(4,),(50000,)],dtype=dt)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[    1]
 [    2]
 [    3]
 [    4]
 [50000]]
<class 'numpy.ndarray'>
5
4
20
"""



a = np.array([(1,),(2,),(3,),(4,),(50000,)],dtype=np.int32)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[    1]
 [    2]
 [    3]
 [    4]
 [50000]]
<class 'numpy.ndarray'>
5
4
20
"""



#int64 or "i8" --> 8bytes or 64 bits
dt = np.dtype("i8")
a = np.array([(1,),(2,),(3,),(4,),(50000,)],dtype=dt)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[    1]
 [    2]
 [    3]
 [    4]
 [50000]]
<class 'numpy.ndarray'>
5
8
40
"""



a = np.array([(1,),(2,),(3,),(4,),(50000,)],dtype=np.int64)
print(a)
print(type(a))
print(a.size)
print(a.itemsize)
print(a.nbytes)
"""
#output:
[[    1]
 [    2]
 [    3]
 [    4]
 [50000]]
<class 'numpy.ndarray'>
5
8
40
"""


"""
Numpy - Data Types
1) bool - boolean(True or False) stored as a byte

2)int - default integer type (same as c long: normally either int64 or int32)

3)intc - identical to c int(normally int32 or int64)

4)intp - integer used for indexing(same as C ssize_t: normally either int32 or int64)

5)int8('i1') - byte(-128 to 127)

6)int16('i2') - byte(-32768 to 32768)

7)int32('i4') - bytes(-2147483648 to 2147483647)

8)int64('i8') - bytes(-9223372036854775808 to 9223372036854775807)

9)uint8 - unsigned integer(0 to 255)

10)uint16 - unsigned integer(0 to 65535)

11)uint32 - unsigned integer(0 to 4294967295)

12)uint64 - unsigned integer(0 to 18446744073709551615)

13)float - shorthand for float64

14)float16 - half precision float: sign bit, 5 bits exponent, 10 bits mantissa

15)float32 - single precision float: sign bit, 8 bits exponent, 23 bits mantissa

16)float64 - double precision float: sign bit, 11 bits exponents, 52 bits mantissa

17)complex - shorthand for complex128

18)complex64 - complex number, represented by two 32-bit float(real and imaginary components)

19)complex128 - complex number, represented by teo 64-bit floats(real and imaginary components)

#DataType Objects(dtype)
 a data type object describes interpretation of fixed block of memory corresponding to an array,
 depending on the following aspects:
 *)type of data(integer,float,or python object)
 *)size of data
 *)byte order(order of storing the data)
 *)In case of structured type, the names of fields, data type of each field and part of the memory
   block taken by each field
 *)if data type is a subarray, its shape and data type

  a dtype object is constructed using the following syntax:
  numpy.dtype(object,align,copy)
"""
dt = np.dtype(np.int16,align=False, copy=False)
array = np.array([1,2,3,4,5,6],dtype = dt)
print(array.dtype)
print(array)
"""
#output:
int16
[1 2 3 4 5 6]
"""

"""
#STRUCTURED DATA TYPE:
each build-in data type has a character code that uniquely identifies it.
  *) 'b' - boolean
  *) 'i' - signed integer
  *) 'u' - unsigned integer
  *) 'f' - floating point
  *) 'c' - complex floating point
  *) 'm' - timedelta
  *) 'M' - datetime
  *) 'O' - python_objects
  *) 'S' or 'a' - byte_string
  *) 'U' - unicode string
  *) 'v' - raw data(void)

np.singe --> this is 4bit or half bytes datatype representation
"""

#by arranged as structured (note:float16 by using this examples)
dt = np.dtype([("age",np.int8),("salary",np.float16)])
array_1 = np.array([(50,100),(70,300),(40,500)],dtype=dt)

print(array_1)
print(array_1["age"])
print(array_1["salary"])
"""
#output
[(50, 100.) (70, 300.) (40, 500.)]
[50 70 40]
[100. 300. 500.]
"""


#by arranged as structured (note:float32 by using this examples)
dt = np.dtype([("age","i1"),("salary","f4")])
array_1 = np.array([(50,100000),(70,300000),(40,50000)],dtype=dt)

print(array_1)
print(array_1["age"])
print(array_1["salary"])
"""
#output:
[(50, 100000.) (70, 300000.) (40,  50000.)]
[50 70 40]
[100000. 300000.  50000.]
"""



#by arranged as structured (note:float64 by using this examples)
dt = np.dtype([("age",np.int8),("salary",np.float64)])
array_1 = np.array([(50,1000000),(70,300005000),(40,50003000)],dtype=dt)

print(array_1)
print(array_1["age"])
print(array_1["salary"])
"""
#output:
[(50, 1.00000e+06) (70, 3.00005e+08) (40, 5.00030e+07)]
[50 70 40]
[1.00000e+06 3.00005e+08 5.00030e+07]
"""

#check if its heading type
dt = np.dtype([("Name","S20"),("age","i1"),("marks","i2")])
print(dt)
print(dt["Name"])
print(dt["age"])
print(dt["marks"])
"""
#output:
[('Name', 'S20'), ('age', 'i1'), ('marks', '<i2')]
|S20
int8
int16
"""


#if use "Name" - name used as string data type
dt = np.dtype([("Name","S20"),("age","i1"),("marks","i2")])
data = np.array([("santhosh",21,392),("mukesh",22,471),("ramesh",20,231)],dtype=dt)
print(data)

print(data["Name"])
print(data["age"])
print(data["marks"])
"""
(| -> this symbol denoted as bytes)
this "S" or "a" will declared string data type with bytes

#outut:
[(b'santhosh', 21, 392) (b'mukesh', 22, 471) (b'ramesh', 20, 231)]
[b'santhosh' b'mukesh' b'ramesh']
[21 22 20]
[392 471 231]
"""



#by using "U" -> unicode, as instead of string datatype like "S" or "a"
dt = np.dtype([("Name","U20"),("age","i1"),("marks","i2")])
data = np.array([("santhosh",21,392),("mukesh",22,471),("ramesh",20,231)],dtype=dt)
print(data)

print(data["Name"])
print(data["age"])
print(data["marks"])
"""
#output:
[('santhosh', 21, 392) ('mukesh', 22, 471) ('ramesh', 20, 231)]
['santhosh' 'mukesh' 'ramesh']
[21 22 20]
[392 471 231]
"""

#by using complex float
"""
likely that data type only access at c8 or c16
"""

#c8 or complex64
dt = np.dtype([("Name","S20"),("complex","c8")]) #or ([("Name","S20"),("complex",np.complex64)])
data = np.array([("santhosh",25.3),("kumar",66.3),("jack",43.8)],dtype=dt)
print(data)

print(data["Name"])
print(data["complex"])
"""
#output:
[(b'santhosh', 25.3+0.j) (b'kumar', 66.3+0.j) (b'jack', 43.8+0.j)]
[b'santhosh' b'kumar' b'jack']
[25.3+0.j 66.3+0.j 43.8+0.j]
"""




#c16 or complex128
dt = np.dtype([("Name","S20"),("complex","c16")]) #or ([("Name","S20"),("complex",np.complex128)])
data = np.array([("santhosh",25.3),("kumar",66.3),("jack",43.8)],dtype=dt)
print(data)

print(data["Name"])
print(data["complex"])
"""
#output:
[(b'santhosh', 25.3+0.j) (b'kumar', 66.3+0.j) (b'jack', 43.8+0.j)]
[b'santhosh' b'kumar' b'jack']
[25.3+0.j 66.3+0.j 43.8+0.j]
"""


#object:
dt = np.dtype([("Name","object"),("complex","object")]) #or ([("Name","S20"),("complex",np.complex128)])
data = np.array([("santhosh",25.3),("kumar",66.3),("jack",43.8)],dtype=dt)
print(data)

print(data["Name"])
print(data["complex"])
print(data.size)
print(data.itemsize)
print(data.nbytes)
"""
#output:
[('santhosh', 25.3) ('kumar', 66.3) ('jack', 43.8)]
['santhosh' 'kumar' 'jack']
[25.3 66.3 43.8]
3
16
48
"""




#access the data and modified
dt = np.dtype([("Name","object"),("complex","object")]) #or ([("Name","S20"),("complex",np.complex128)])
data = np.array([("santhosh",25.3),("kumar",66.3),("jack",43.8)],dtype=dt)
print("before it modified:\n",data)
data[0][1] = 30.5
print("after its modified:\n",data)
"""
#output:
before it modified:
 [('santhosh', 25.3) ('kumar', 66.3) ('jack', 43.8)]
after its modified:
 [('santhosh', 30.5) ('kumar', 66.3) ('jack', 43.8)]
"""


#ndarray.shape()
"""
this array attribute returns a tuple consisting of array dimensions. it can also be
used to resize the array.

note:
this method is used for creating an array by the our perspective or
make the array_data shape by our_wise
"""
data = np.array([[1,2,3],[2,5,6],[4,5,6]],ndmin=3,dtype=object)
print(data)
print(data.ndim)
print(data.shape)
"""
#output:
[[[1 2 3]
  [2 5 6]
  [4 5 6]]]
3
(1, 3, 3)
"""



data = np.array([[1,2,3],[1,2,5],[2,5,6],[4,5,6]],ndmin=3,dtype=object)

print("before to reshape the shape by using method - 'shape()' ")
print(data)
print(data.ndim)
print(data.shape)
print("after to reshape the shape by using method - 'shape()' ")

data.shape = (2,6)
print(data)
print(data.ndim)
print(data.shape)
"""
#output:
before to reshape the shape by using method - 'shape()'
[[[1 2 3]
  [1 2 5]
  [2 5 6]
  [4 5 6]]]
3
(1, 4, 3)
after to reshape the shape by using method - 'shape()'
[[1 2 3 1 2 5]
 [2 5 6 4 5 6]]
2
(2, 6)
"""



#problem_2:
data = np.array([[1,2,3],[1,2,5],[2,5,6],[4,5,6]],ndmin=3,dtype=object)

print("before to reshape the shape by using method - 'shape()' ")
print(data)
print(data.ndim)
print(data.shape)
print("after to reshape the shape by using method - 'shape()' ")

data.shape = (2,3,2)
print(data)
print(data.ndim)
print(data.shape)
"""
#output:
before to reshape the shape by using method - 'shape()'
[[[1 2 3]
  [1 2 5]
  [2 5 6]
  [4 5 6]]]
3
(1, 4, 3)
after to reshape the shape by using method - 'shape()'
[[1 2 3 1 2 5]
 [2 5 6 4 5 6]]
2
(2, 6)
before to reshape the shape by using method - 'shape()'
[[[1 2 3]
  [1 2 5]
  [2 5 6]
  [4 5 6]]]
3
(1, 4, 3)
after to reshape the shape by using method - 'shape()'
[[[1 2]
  [3 1]
  [2 5]]

 [[2 5]
  [6 4]
  [5 6]]]
3
(2, 3, 2)
"""




#ndarray.reshape():
"""
this array attribute returns a tuple consisting of array dimensions. it can also be
used to resize the array.

note:
this method is used for modified to the created array by the our perspective or
make the array_data shape by our_wise
"""
data = np.array([[1,2,3],[1,2,5],[2,5,6],[4,5,6]],ndmin=3,dtype=object)
print("before it modified:\n",data)
print("after it modified:\n",data.reshape(2,3,2))
"""
#output:
before it modified:
 [[[1 2 3]
  [1 2 5]
  [2 5 6]
  [4 5 6]]]
after it modified:
 [[[1 2]
  [3 1]
  [2 5]]

 [[2 5]
  [6 4]
  [5 6]]]
"""


#problem_2:
data = np.array([[1,2,3],[1,2,5],[2,5,6],[4,5,6]],ndmin=3,dtype=object)
print("before it modified:\n",data)
print("after it modified:\n",data.reshape(3,2,2))
"""
#output:
before it modified:
 [[[1 2 3]
  [1 2 5]
  [2 5 6]
  [4 5 6]]]
after it modified:
 [[[1 2]
  [3 1]]

 [[2 5]
  [2 5]]

 [[6 4]
  [5 6]]]
"""


"""
*) shape is creating the array by it our purpose of data dimension

*) reshape is for modified the shaped array of data
"""



import numpy as np
from numpy.ma.core import arange

# #np.put()
# data = np.array([1,2,3,4],dtype = object)
# data.put([1,3],["aa","bb"])
# print(data)
# #[1 'aa' 3 'bb']


#by the real time data scenario to use numpy
dt = np.dtype([("name","S20"),("age","i1"),("native","O")])
data = np.array([("ram",25,"madurai"),("selva",32,"karaikudi"),("mani",36,"sivakasi"),("boopathi",26,"dindugal")
                 ,("kasavan",27,"madurai")],ndmin=1) #if the dimension is above we initialize means working

print(data.ndim)#2
print(data.shape)#(5, 3)

print(data.size)#15
print(data.itemsize)#84

#size * itemsize = nbytes
print(data.nbytes)#1260

"""
if the index will calculated as sequence of information like ram is 1
and then selva become 4 and then last value will be index 14 --> (n-1)
"""
data.put([6],"siva")
print(data)
"""
#output:
[['ram' '25' 'madurai']
 ['selva' '32' 'karaikudi']
 ['siva' '36' 'sivakasi']
 ['boopathi' '26' 'dindugal']
 ['kasavan' '27' 'madurai']]
"""



data.put([14],"changed")
print(data)
"""
#output:
[['ram' '25' 'madurai']
 ['selva' '32' 'karaikudi']
 ['siva' '36' 'sivakasi']
 ['boopathi' '26' 'dindugal']
 ['kasavan' '27' 'changed']]
"""

data.shape=(3,5)
print(data)
"""
#output:
[['ram' '25' 'madurai' 'selva' '32']
 ['karaikudi' 'siva' '36' 'sivakasi' 'boopathi']
 ['26' 'dindugal' 'kasavan' '27' 'changed']]
"""


print(np.reshape(data,(5,3)))
"""
#output:
[['ram' '25' 'madurai']
 ['selva' '32' 'karaikudi']
 ['siva' '36' 'sivakasi']
 ['boopathi' '26' 'dindugal']
 ['kasavan' '27' 'changed']]
"""


#arange:
sample = np.arange(0,12).reshape(4,3)
print(sample)
"""
#output:
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
"""
sample.put([4,7,11],[0,0,0,0])
print(sample)
"""
#output:
[[ 0  1  2]
 [ 3  0  5]
 [ 6  0  8]
 [ 9 10  0]]
"""


#doubt in flags concept in numpy



#np.empty() --> empty(shape, dtype=float, order='C', *, device=None, like=None)
data = np.empty((3,3),dtype="i1")
print(data)
"""
notes:
if the empty provides the result like not only provides the zero only.
it provides any random values based on your mentioned data_type

#output:
[[1 0 0]
 [0 0 0]
 [0 0 8]]
"""


data = np.empty((3,3),dtype="f4")
print(data)
"""
#output:
[[1.3563128e-19 4.8008185e+30 4.7421254e+16]
 [1.0077282e-08 6.4096894e-10 2.6657396e-09]
 [6.2353261e-10 1.4584911e-19 4.0273673e-11]]
"""


data = np.empty((3,3),dtype="c8")
print(data)
"""
#output:
[[0.0000000e+00+0.0000000e+00j 0.0000000e+00+0.0000000e+00j
  0.0000000e+00+0.0000000e+00j]
 [0.0000000e+00+0.0000000e+00j 0.0000000e+00+0.0000000e+00j
  9.4167257e-43+0.0000000e+00j]
 [0.0000000e+00+1.1727252e-19j 0.0000000e+00+9.8439425e-12j
  9.8439425e-12+1.3555894e-19j]]
"""



data = np.empty((3,3),dtype="b")
print(data)
"""
#output:
[[0 0 0]
 [0 0 0]
 [1 1 1]]
"""




#if we want zero means by using np.zero() method
#np.zeros():
sample = np.zeros((3,3),dtype="int8")
print(sample)
"""
#output:
[[0 0 0]
 [0 0 0]
 [0 0 0]]
"""




sample = np.zeros((3,3),dtype="int8")
np.put(sample,[0,4,8],[1,1,1])
print(sample)
"""
#output:
[[1 0 0]
 [0 1 0]
 [0 0 1]]
"""




#np.ones():
sample = np.ones((3,3),"S")
print(sample)
"""
#output:
[[b'1' b'1' b'1']
 [b'1' b'1' b'1']
 [b'1' b'1' b'1']]
"""


sample = np.ones((3,3),"i1")
print(sample)
"""
#output:
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""



sample = np.ones((3,3),"c16")
print(sample)
"""
#output:
[[1.+0.j 1.+0.j 1.+0.j]
 [1.+0.j 1.+0.j 1.+0.j]
 [1.+0.j 1.+0.j 1.+0.j]]
"""


sample = np.ones((3,3),"S1")
print(sample)
"""
#output
[[b'1' b'1' b'1']
 [b'1' b'1' b'1']
 [b'1' b'1' b'1']]
"""


import numpy as np
#np.frombuffer() --> for only as string, a bytes-like object is required
a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S1") #dtype is compulsary included this method
print(s)
#[b'S' b'A' b'N' b'T' b'H' b'O' b'S' b'H' b' ' b'K' b'U' b'M' b'A' b'R']



a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S2") #dtype is compulsary included this method
print(s)
#[b'SA' b'NT' b'HO' b'SH' b' K' b'UM' b'AR']


"""
a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S4") #dtype is compulsary included this method
print(s)



notes:
if we included the character in that dtype string only the multiple of len in that character

#output:
Traceback (most recent call last):
  File "D:\ds\python files\numpy_py.py", line 1615, in <module>
    s = np.frombuffer(a,dtype="S4") #dtype is compulsary included this method
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: buffer size must be a multiple of element size
"""



a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S2",offset=2) #dtype is compulsary included this method
print(s)
"""
#output
[b'NT' b'HO' b'SH' b' K' b'UM' b'AR']
"""



a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S2",offset=0,count=5) #dtype is compulsary included this method
print(s)
"""
#output:
[b'SA' b'NT' b'HO' b'SH' b' K']
"""


a = b'SANTHOSH KUMAR'
s = np.frombuffer(a,dtype="S2",offset=2,count=5) #dtype is compulsary included this method
print(s)
"""
#output:
[b'NT' b'HO' b'SH' b' K' b'UM']
"""


"""
asarray - doubt for image operation
"""


import numpy as np
a =np.arange(9).reshape(3,3)
print(a)
print(np.asarray(a,dtype="f4"))
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]

[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]
"""


#asarray_chkfinite(object, dtype=None, order=None)
"""
this checks input for nans and infs / convert the input
to an array checking for nans or infs
"""

import numpy as np
a = [1,2,4,np.inf,np.nan]
print("before use asarray_chkfinite: ",a)
#before use asarray_chkfinite:  [1, 2, 4, inf, nan]

b = np.asarray_chkfinite(a)
print(b)
"""
#output:
  File "D:\ds\python files\numpy_py.py", line 1690, in <module>
    b = np.asarray_chkfinite(a)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages\numpy\lib\_function_base_impl.py", line 665, in asarray_chkfinite
    raise ValueError(
        "array must not contain infs or NaNs")
ValueError: array must not contain infs or NaNs
"""
import numpy as np


a = np.array([1,2,3,"a","ec","bbb"],dtype=object)
b = np.asarray_chkfinite(a,dtype="S")
print(b)
"""
#output:
[b'1' b'2' b'3' b'a' b'ec' b'bbb']
"""


a = np.array([1,2,3,"a","ec","bbb"],dtype=object)
b = np.asarray_chkfinite(a,dtype=object)
print(b)
"""
#output:
[1 2 3 'a' 'ec' 'bbb']
"""


a = [1,2,4,np.inf,np.nan]
try:
    np.asarray_chkfinite(a)
except ValueError:
    print("Value_Error")
"""
#output:
Value_Error
"""

import numpy as np
from numpy.ma.core import reshape, resize

#np.fromiter(): --> fromiter(iter, dtype, count=-1, *, like=None)
a = [1,2,4,np.inf,np.nan]
# a = np.array(a)
b = np.fromiter(a,dtype=object,count=3)
print(b)
"""
#output:
[1 2 4]
"""



#np.full(shape,fill_value,dtype,order)
"""
return a new array of given shape and type, filled with "fill_value"
"""
a = np.full((3,3),"pass",)
print(a)
"""
#output:
[['pass' 'pass' 'pass']
 ['pass' 'pass' 'pass']
 ['pass' 'pass' 'pass']]
"""




a = np.full((3,3),np.nan,)
print(a)
"""
#output:
[[nan nan nan]
 [nan nan nan]
 [nan nan nan]]
"""




#np.full_like()
"""
full_like(
    a,
    fill_value,
    dtype=None,
    order='K',
    subok=True,
    shape=None,
    *,
    device=None
)
"""
a = np.arange(12).reshape((3,4))
b = np.full_like(a,"pass",dtype="S4",shape=(4,3))
print(b)
"""
#output:
[[b'pass' b'pass' b'pass']
 [b'pass' b'pass' b'pass']
 [b'pass' b'pass' b'pass']
 [b'pass' b'pass' b'pass']]
"""

b = np.resize(b,(6,2))
print(b)
"""
#output:
[[b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']]
"""

b.put(0,"Fail")
print(b)
"""
#output:
[[b'Fail' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']
 [b'pass' b'pass']]
"""

import numpy as np
dt = ([("Name","S15"),("Age","i1"),("Native_pin","i4")])
data = np.zeros((3,2),dtype=dt)
print(data)
print(data.ndim)
"""
#output:
[[(b'', 0, 0) (b'', 0, 0)]
 [(b'', 0, 0) (b'', 0, 0)]
 [(b'', 0, 0) (b'', 0, 0)]]
2
"""


data[0][0] = ("santhosh",20,624204)

print(data)
"""
#output:
[[(b'santhosh', 20, 624204) (b'',  0,      0)]
 [(b'',  0,      0) (b'',  0,      0)]
 [(b'',  0,      0) (b'',  0,      0)]]
"""

print("---------------------------------------------------")

np.put(data,[1,2,3],[("nithesh",21,409793),("ram",23,408893),("jhon",20,409003)])
print(data)
"""
#output:
[[(b'santhosh', 20, 624204) (b'nithesh', 21, 409793)]
 [(b'ram', 23, 408893) (b'jhon', 20, 409003)]
 [(b'',  0,      0) (b'',  0,      0)]]
"""
print("---------------------------------------------------------")

data[2] = [("jacky",21,400321),("mohan",20,432123)]
print(data)
"""
#output:
[[(b'santhosh', 20, 624204) (b'nithesh', 21, 409793)]
 [(b'ram', 23, 408893) (b'jhon', 20, 409003)]
 [(b'jacky', 21, 400321) (b'mohan', 20, 432123)]]
"""
print("--------------------------------------------------------------------")


#new method:
dt = ([("Name","S15"),("Age","i1"),("Native_pin","i4")])
data = np.array(np.arange(16),dtype=dt)
print(data)
print("dimension: ",data.ndim)
"""
#output:
[(b'0',  0,  0) (b'1',  1,  1) (b'2',  2,  2) (b'3',  3,  3)
 (b'4',  4,  4) (b'5',  5,  5) (b'6',  6,  6) (b'7',  7,  7)
 (b'8',  8,  8) (b'9',  9,  9) (b'10', 10, 10) (b'11', 11, 11)
 (b'12', 12, 12) (b'13', 13, 13) (b'14', 14, 14) (b'15', 15, 15)]
dimension:  1
"""
data.shape = (4,4)
print(data)
print("dimension: ",data.ndim)
"""
#output:
[[(b'0',  0,  0) (b'1',  1,  1) (b'2',  2,  2) (b'3',  3,  3)]
 [(b'4',  4,  4) (b'5',  5,  5) (b'6',  6,  6) (b'7',  7,  7)]
 [(b'8',  8,  8) (b'9',  9,  9) (b'10', 10, 10) (b'11', 11, 11)]
 [(b'12', 12, 12) (b'13', 13, 13) (b'14', 14, 14) (b'15', 15, 15)]]
#dimension:  2
"""

dt = np.dtype([("name","S15"),("age","i1"),("native_pin","i4")])
student = np.array([("shyam",23,432123),("surya",20,654567),("deepak",23,435678),("mahesh",21,432321)],dtype=dt)
print("orginal_data: \n",student)
student.resize(2,2)
print("resized_data: \n",student)
"""
#output:
orginal_data:
 [(b'shyam', 23, 432123) (b'surya', 20, 654567) (b'deepak', 23, 435678)
 (b'mahesh', 21, 432321)]
resized_data:
 [[(b'shyam', 23, 432123) (b'surya', 20, 654567)]
 [(b'deepak', 23, 435678) (b'mahesh', 21, 432321)]]
"""

#to split the tuple value using zip
student = ([("shyam",23,432123),("surya",20,654567),("deepak",23,435678),("mahesh",21,432321)])
a = (zip(*student))
print(a)
#<zip object at 0x0000023D76654280>
# print(list(a))
#[('shyam', 'surya', 'deepak', 'mahesh'), (23, 20, 23, 21), (432123, 654567, 435678, 432321)]

arr = list(a)
print(arr)
#[('shyam', 'surya', 'deepak', 'mahesh'), (23, 20, 23, 21), (432123, 654567, 435678, 432321)]


x = np.asarray(arr)
print(x)
"""
#output:
[['shyam' 'surya' 'deepak' 'mahesh']
 ['23' '20' '23' '21']
 ['432123' '654567' '435678' '432321']]
"""


import numpy as np
"""
#asarray()
if the asarray() --> method is used to the data make as numeric
"""
data = np.asarray([(1,2,3,4),(5,6,7,8)],dtype="f4",order="f")
print(data)
"""
notes:
by the object data is includes as lists, list of lists, lists of tuples, tuples, tuple of tuples,
tuples of lists and ndarrays

#output:
[[1. 2. 3. 4.]
 [5. 6. 7. 8.]]
"""



"""
#why do we modify the list to ndarray using as array.
sol:
if we want to add the elements of the list, is not possible, where as if we convert list to  ndarray(using asarray),
these arithmetic and scientific operations are easy, see the example below.
"""
a = [1,2,3,4,5]
print(a*5)
#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

b = np.array(a)
print(b*5)
#or
b = np.asarray(a)
print(b*5)
#or
b = np.asanyarray(a)
print(b*5)
"""
notes:
if the both of its method will be an same, like to change the list to ndarray

#output
[ 5 10 15 20 25]
[ 5 10 15 20 25]
[ 5 10 15 20 25]
"""



a = np.array([1,2])
print(type(a))
#<class 'numpy.ndarray'>

b = np.asarray(a)
print(type(b))
#<class 'numpy.ndarray'>

print(a is b)
#True



#check if the two type of creating array as same type or not
a = np.array([1,2])
print(type(a))
print(id(a))

b = np.asarray([1,2])
print(type(b))
print(id(b))

c = np.asanyarray([1,2])
print(type(c))
print(id(c))
"""
note:  if we will generate new object to make as both of the ndarray,
so because of generate each time as new_id(changed).

#output:
<class 'numpy.ndarray'>
2903081684112
<class 'numpy.ndarray'>
2903081684016
<class 'numpy.ndarray'>
2903081684208
"""


a = np.array([1,2])
print(type(a))
print(id(a))

b = np.asarray(a)
print(type(b))
print(id(b))

c = np.asanyarray(b)
print(type(c))
print(id(c))
"""
note: if we will generate new object to make as copy of existed array,
the id will not been changed

#output:
<class 'numpy.ndarray'>
2523151781776
<class 'numpy.ndarray'>
2523151781776
<class 'numpy.ndarray'>
2523151781776
"""

import numpy as np
#different between array(), asarray(), asanyarray().
"""
#b = np.array(a)
#open up a new memory space, make a copy, if we do any changes in b, it
wil not affect the original array 'a'


#c = np.asarray(a)
#still us ethe original memory space, if we do any changes in 'c', it
will affect the original array 'a'


#d = np.asanyarray(a)
#still us ethe original memory space, if we do any changes in 'd', it
will affect the original array 'a'
"""
a = np.array([1,2,3])

b = np.array(a)
c = np.asarray(a)
d = np.asanyarray(a)


print("original_data before modified \n",a)
print("id_of original data :",id(a))

d[1] = 100 #np.asanyarray()

print("original_data after modified \n",a)
print("id_of original data :",id(a))
"""
#note:
if the asanyarray() will created as by using the object of "np.array", but it will be changed

#output:
original_data before modified
 [1 2 3]
id_of original data : 2243978515760
original_data after modified
 [  1 100   3]
id_of original data : 2243978515760
"""



print("original_data before modified \n",a)
print("id_of original data :",id(a))

c[1] = 200 #np.asarray()

print("original_data after modified \n",a)
print("id_of original data :",id(a))
"""
#notes:
if the asarray() will created as by using the object of "np.array", but it will be changed

#output:
id_of original data : 2471249237296
original_data before modified
 [  1 100   3]
id_of original data : 2471249237296
original_data after modified
 [  1 200   3]
id_of original data : 2471249237296
"""



print("original_data before modified \n",a)
print("id_of original data :",id(a))

b[1] = 1000 #np.array()

print("original_data after modified \n",a)
print("id_of original data :",id(a))
"""
#notes:
it will also have an same id but, this will not affected the memory_id

#output:
original_data before modified
 [  1 200   3]
id_of original data : 2236960134448
original_data after modified
 [  1 200   3]
id_of original data : 2236960134448
"""



#diff between as array() vs asarray() vs asanyarray()
"""
1) array(): open up a new space, make a copy.
2) asarray(): still use the orginal space and asarray will only return ndarray.
3) asanyarray() : still use the orginal space, asanyarray will return ndarray or a subclass of ndarray.
"""



#if "dtype" to check the id by its changed or not:
a = np.array([1,2,3],dtype="f4")
print(np.asarray(a,dtype="f4") is a)
#True


a = np.array([1,2,3],dtype="f4")
print(np.asarray(a,dtype="i2") is a)
#False


a = np.array([1,2,3],dtype="f4")
print(np.asarray(a,dtype="f8") is a)
#False


#check "issubclass()"
class abc:
    pass
class xyz(abc):
    pass

print(issubclass(abc,xyz))
#False

print(issubclass(xyz,abc))
#True


#conver a list os tuples to ndarray using asarray()
a = np.asarray([(1,2,3,4),(10,20,30,40)])
print(a)
print(type(a))
"""
#output:
[[ 1  2  3  4]
 [10 20 30 40]]
<class 'numpy.ndarray'>
"""



#convert list to ndarray using asarray()
x = [1,2,3,4,5]
print("type: ",type(x)," --> ",x)
a = np.asarray(a)
print("type: ",type(a)," --> ",a)
"""
#output:
type:  <class 'list'>  -->  [1, 2, 3, 4, 5]
type:  <class 'numpy.ndarray'>  -->  [[ 1  2  3  4]
 [10 20 30 40]]
"""


x = [1,2,3,4,5]
print("type: ",type(x)," --> ",x)

a = np.asarray(x,dtype="f4")
print("type: ",type(a))
print(a)
"""
#output:
type:  <class 'list'>  -->  [1, 2, 3, 4, 5]
type:  <class 'numpy.ndarray'>
[1. 2. 3. 4. 5.]
"""


#convert tuple to ndarray using asarray()
x = (1,2,3,4,5,6)
print("type: ",type(x)," --> ",x)
a = np.asarray(x)
print(type(a))
print(a)
"""
#output:
type:  <class 'tuple'>  -->  (1, 2, 3, 4, 5, 6)
<class 'numpy.ndarray'>
[1 2 3 4 5 6]
"""




#convert list of tuples to ndarray using asarray()
x = [(1,2,3),(4,5,6)]
print("type: ",type(x)," --> ",x)
a = np.asarray(x)
print(type(a))
print(a)
"""
#output:
type:  <class 'list'>  -->  [(1, 2, 3), (4, 5, 6)]
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]]
"""



#convert tuple of tuples to ndarray using asarray()
x = ((1,2,3),(4,5,6))
print("type: ",type(x)," --> ",x)
a = np.asarray(x)
print(type(a))
print(a)
"""
#output:
type:  <class 'tuple'>  -->  ((1, 2, 3), (4, 5, 6))
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]]
"""


"""
tuples can accepted heterogeneous data, but once we changed ndarray, using asarray(), it will accept
only homogeneous data and to avoid it, if our tuple has int and string, better change the dtype to string to
object
"""
x = [(1,2,3,"sss"),("aaa",2,3)]
a = np.asarray(x,dtype=object)
print(type(a))
print(a)
"""
#output:
<class 'numpy.ndarray'>
[(1, 2, 3, 'sss') ('aaa', 2, 3)]
"""


x = [(1,2,3,"sss"),("aaa",2,3)]
a = np.asarray(x,dtype="O")
print(type(a))
print(a)
"""
#output:
<class 'numpy.ndarray'>
[(1, 2, 3, 'sss') ('aaa', 2, 3)]
"""


x = [(1,2,3,"sss","aaa",2,3)]
a = np.asarray(x,dtype="S10")
print(type(a))
print(a)
"""
#output:
<class 'numpy.ndarray'>
[[b'1' b'2' b'3' b'sss' b'aaa' b'2' b'3']]
"""


"""
x = [(1,2,3,"sss","aaa",2,3)]
a = np.asarray(x,dtype="i4")
print(type(a))
print(a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\numpy_py.py", line 2305, in <module>
    a = np.asarray(x,dtype="i4")
ValueError: invalid literal for int() with base 10: 'sss'
"""


x = [(1,2,3,2,3)]
a = np.asarray(x,dtype="f4")
print(type(a))
print(a)
"""
#output:
<class 'numpy.ndarray'>
[[1. 2. 3. 2. 3.]]
"""



#numpy.linspace()
"""
the numpy linspace function creates sequencesof evenly spaced values within a defined interval.
essentally, you specify a starting point and an endpoint of an interval, and then specify the 
total number of breakpoints you want within that interval(including the start and end point).
"""

import numpy as np
x = np.linspace(start=0,stop=10,num=10,dtype="i1",endpoint=True,retstep=True)
print(x)
"""
#output:
(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8, 10], dtype=int8), np.float64(1.1111111111111112))
"""



#enpoint = False --> last value is excluded
x = np.linspace(start=0,stop=10,num=10,dtype="i1",endpoint=False,retstep=True)
print(x)
"""
#output:
(array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int8), np.float64(1.0))
"""


#retstep=False --> to make as ndarray not been mentioned the between values
x = np.linspace(start=0,stop=10,num=10,dtype="i1",endpoint=True,retstep=False)
print(x)
#[ 0  1  2  3  4  5  6  7  8 10]



x = np.linspace(start=0,stop=10,num=8,dtype="f4",endpoint=True,retstep=True)
print(x)
"""
#output:
(array([ 0.       ,  1.4285715,  2.857143 ,  4.285714 ,  5.714286 ,
        7.142857 ,  8.571428 , 10.       ], dtype=float32), np.float64(1.4285714285714286))
"""



#num not mentioned means "defualt value": 50
x = np.linspace(start=0,stop=10,dtype="f4",endpoint=True,retstep=True)
print(x)
"""
(array([ 0.        ,  0.20408164,  0.40816328,  0.6122449 ,  0.81632656,
        1.0204082 ,  1.2244898 ,  1.4285715 ,  1.6326531 ,  1.8367347 ,
        2.0408163 ,  2.2448978 ,  2.4489796 ,  2.6530612 ,  2.857143  ,
        3.0612245 ,  3.2653062 ,  3.4693878 ,  3.6734693 ,  3.877551  ,
        4.0816326 ,  4.285714  ,  4.4897957 ,  4.6938777 ,  4.897959  ,
        5.102041  ,  5.3061223 ,  5.5102043 ,  5.714286  ,  5.9183674 ,
        6.122449  ,  6.3265305 ,  6.5306125 ,  6.734694  ,  6.9387755 ,
        7.142857  ,  7.3469386 ,  7.5510206 ,  7.755102  ,  7.9591837 ,
        8.163265  ,  8.367347  ,  8.571428  ,  8.77551   ,  8.979591  ,
        9.183674  ,  9.387755  ,  9.591837  ,  9.795918  , 10.        ],
      dtype=float32), np.float64(0.20408163265306123))
"""



'by default check'
"start:0, stop=10, num=8, dtype='f4', retstep=False,endpoint=False"
x = np.linspace(0,10,8)
print(x)
"""
[ 0.          1.42857143  2.85714286  4.28571429  5.71428571  7.14285714
  8.57142857 10.        ]
"""




x = np.linspace(0,10,8,endpoint=True)
print(x)
"""
#output:
[ 0.          1.42857143  2.85714286  4.28571429  5.71428571  7.14285714
  8.57142857 10.        ]
"""



x = np.linspace(0,200,20,endpoint=True).reshape(5,4)
print(x)
"""
#output:
[[  0.          10.52631579  21.05263158  31.57894737]
 [ 42.10526316  52.63157895  63.15789474  73.68421053]
 [ 84.21052632  94.73684211 105.26315789 115.78947368]
 [126.31578947 136.84210526 147.36842105 157.89473684]
 [168.42105263 178.94736842 189.47368421 200.        ]]
"""



x = (np.linspace(0,200,20,endpoint=True))
b = x.reshape(5,4)
print(b)
"""
#output:
[[  0.          10.52631579  21.05263158  31.57894737]
 [ 42.10526316  52.63157895  63.15789474  73.68421053]
 [ 84.21052632  94.73684211 105.26315789 115.78947368]
 [126.31578947 136.84210526 147.36842105 157.89473684]
 [168.42105263 178.94736842 189.47368421 200.        ]]
"""



#by using the np involve values into the linspace()
x = np.linspace(0,2*np.pi,100,retstep=False,endpoint=True)
print(x)
"""
#output:
[0.         0.06346652 0.12693304 0.19039955 0.25386607 0.31733259
 0.38079911 0.44426563 0.50773215 0.57119866 0.63466518 0.6981317
 0.76159822 0.82506474 0.88853126 0.95199777 1.01546429 1.07893081
 1.14239733 1.20586385 1.26933037 1.33279688 1.3962634  1.45972992
 1.52319644 1.58666296 1.65012947 1.71359599 1.77706251 1.84052903
 1.90399555 1.96746207 2.03092858 2.0943951  2.15786162 2.22132814
 2.28479466 2.34826118 2.41172769 2.47519421 2.53866073 2.60212725
 2.66559377 2.72906028 2.7925268  2.85599332 2.91945984 2.98292636
 3.04639288 3.10985939 3.17332591 3.23679243 3.30025895 3.36372547
 3.42719199 3.4906585  3.55412502 3.61759154 3.68105806 3.74452458
 3.8079911  3.87145761 3.93492413 3.99839065 4.06185717 4.12532369
 4.1887902  4.25225672 4.31572324 4.37918976 4.44265628 4.5061228
 4.56958931 4.63305583 4.69652235 4.75998887 4.82345539 4.88692191
 4.95038842 5.01385494 5.07732146 5.14078798 5.2042545  5.26772102
 5.33118753 5.39465405 5.45812057 5.52158709 5.58505361 5.64852012
 5.71198664 5.77545316 5.83891968 5.9023862  5.96585272 6.02931923
 6.09278575 6.15625227 6.21971879 6.28318531]
"""







x = np.linspace(0,np.pi,50,retstep=True,endpoint=True)
print(x)
"""
#output:
(array([0.        , 0.06411414, 0.12822827, 0.19234241, 0.25645654,
       0.32057068, 0.38468481, 0.44879895, 0.51291309, 0.57702722,
       0.64114136, 0.70525549, 0.76936963, 0.83348377, 0.8975979 ,
       0.96171204, 1.02582617, 1.08994031, 1.15405444, 1.21816858,
       1.28228272, 1.34639685, 1.41051099, 1.47462512, 1.53873926,
       1.60285339, 1.66696753, 1.73108167, 1.7951958 , 1.85930994,
       1.92342407, 1.98753821, 2.05165235, 2.11576648, 2.17988062,
       2.24399475, 2.30810889, 2.37222302, 2.43633716, 2.5004513 ,
       2.56456543, 2.62867957, 2.6927937 , 2.75690784, 2.82102197,
       2.88513611, 2.94925025, 3.01336438, 3.07747852, 3.14159265]), np.float64(0.0641141357875468))
"""

import numpy as np
import pandas as pd
st = pd.Timestamp("2025-02-08")
end = pd.Timestamp("2025-03-08")
t = np.linspace(st.value,end.value,35)
new_t = pd.to_datetime(t)
print(new_t)
"""
#output:
DatetimeIndex([          '2025-02-08 00:00:00',
               '2025-02-08 19:45:52.941176576',
               '2025-02-09 15:31:45.882352896',
               '2025-02-10 11:17:38.823529472',
               '2025-02-11 07:03:31.764705792',
               '2025-02-12 02:49:24.705882368',
               '2025-02-12 22:35:17.647058944',
               '2025-02-13 18:21:10.588235264',
               '2025-02-14 14:07:03.529411840',
               '2025-02-15 09:52:56.470588160',
               '2025-02-16 05:38:49.411764736',
               '2025-02-17 01:24:42.352941056',
               '2025-02-17 21:10:35.294117632',
               '2025-02-18 16:56:28.235294208',
               '2025-02-19 12:42:21.176470528',
               '2025-02-20 08:28:14.117647104',
               '2025-02-21 04:14:07.058823424',
                         '2025-02-22 00:00:00',
               '2025-02-22 19:45:52.941176576',
               '2025-02-23 15:31:45.882352896',
               '2025-02-24 11:17:38.823529472',
               '2025-02-25 07:03:31.764705792',
               '2025-02-26 02:49:24.705882368',
               '2025-02-26 22:35:17.647058944',
               '2025-02-27 18:21:10.588235264',
               '2025-02-28 14:07:03.529411840',
               '2025-03-01 09:52:56.470588160',
               '2025-03-02 05:38:49.411764736',
               '2025-03-03 01:24:42.352941056',
               '2025-03-03 21:10:35.294117632',
               '2025-03-04 16:56:28.235294208',
               '2025-03-05 12:42:21.176470528',
               '2025-03-06 08:28:14.117647104',
               '2025-03-07 04:14:07.058823424',
                         '2025-03-08 00:00:00'],
              dtype='datetime64[ns]', freq=None)
"""


#np.full
passmark = np.full((4,4),40)
print(passmark)
"""
#output:
[[40 40 40 40]
 [40 40 40 40]
 [40 40 40 40]
 [40 40 40 40]]
"""


passmark = np.full((4,4),40,dtype=float)
print(passmark)
"""
#output:
[[40. 40. 40. 40.]
 [40. 40. 40. 40.]
 [40. 40. 40. 40.]
 [40. 40. 40. 40.]]
"""


passmark = np.full((4,4),"present",dtype="O")
print(passmark)
"""
#output:
[['present' 'present' 'present' 'present']
 ['present' 'present' 'present' 'present']
 ['present' 'present' 'present' 'present']
 ['present' 'present' 'present' 'present']]
"""


attendence = np.full((4,4),"present",dtype="O")
print(passmark)
attendence[0][2] = "Fail"
np.put(attendence,[5,9,15],"Fail")
print(attendence)
"""
#output:
[['present' 'present' 'Fail' 'present']
 ['present' 'Fail' 'present' 'present']
 ['present' 'Fail' 'present' 'present']
 ['present' 'present' 'present' 'Fail']]
"""


a = np.full((4,4),"PRESENT",dtype="S3")
print(a)
"""
#output:
[[b'PRE' b'PRE' b'PRE' b'PRE']
 [b'PRE' b'PRE' b'PRE' b'PRE']
 [b'PRE' b'PRE' b'PRE' b'PRE']
 [b'PRE' b'PRE' b'PRE' b'PRE']]
"""


#np.random.rand()
import numpy as np
a = np.random.rand(4,2)
print(a)
"""
#note:
so this inside values will be below the 1.

#output:
[[0.56147975 0.4609032 ]
 [0.83729116 0.04528577]
 [0.0538795  0.50127858]
 [0.04930619 0.61192483]]
"""



a = np.random.rand(2,4,2)
print(a)
"""
#output:
[[[0.47671017 0.81004324]
  [0.22308828 0.43523069]
  [0.78392241 0.30185415]
  [0.78899662 0.72271576]]

 [[0.98919665 0.01271232]
  [0.87720032 0.59401787]
  [0.96935625 0.41521871]
  [0.7060231  0.52114649]]]
"""

#np.randint()
a = np.random.randint(low=12,size=(3,3))
print(a)
"""
#output:
[[ 0 11  5]
 [10  5  5]
 [ 4  9  2]]
"""


a = np.random.randint(low=5,high=12,size=(3,3))
print(a)
"""
#output:
[[ 6  8 10]
 [ 7  5  7]
 [ 9  5 10]]
"""


a = np.random.randint(low=-5,high=12,size=(3,3))
print(a)
"""
#output:
[[-4  9 -2]
 [-5  5 -2]
 [11  1  8]]
"""



#if high is None(the default), then results are from --> [0 , low]
a = np.random.randint(low = 4, high = None,size=(3,3))
print(a)
"""
#output:
[[3 0 0]
 [0 3 3]
 [2 1 1]]
"""


"""
#if both will be an None --> None

a = np.random.randint(low=None,high=None,size=(3,3))
print(a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 335, in <module>
    a = np.random.randint(low=None,high=None,size=(3,3))
  File "numpy/random/mtrand.pyx", line 794, in numpy.random.mtrand.RandomState.randint
  File "numpy/random/_bounded_integers.pyx", line 2865, in numpy.random._bounded_integers._rand_int32
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
"""



"""
a = np.random.randint(low=0,high=None,size=(3,3))
print(a)

#output: --> error
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 351, in <module>
    a = np.random.randint(low=0,high=None,size=(3,3))
  File "numpy/random/mtrand.pyx", line 794, in numpy.random.mtrand.RandomState.randint
  File "numpy/random/_bounded_integers.pyx", line 2885, in numpy.random._bounded_integers._rand_int32
ValueError: high <= 0
"""


#identity or identity matrix
import numpy as np
a = np.identity(3)
print(a)
"""
#output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""



a = np.identity(5,dtype="i1")
print(a)
"""
#output:
[[1 0 0 0 0]
 [0 1 0 0 0]
 [0 0 1 0 0]
 [0 0 0 1 0]
 [0 0 0 0 1]]
"""




a = np.identity(3,dtype="f4")
print(a)
"""
#output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""


a = np.identity(3,dtype="bool")
print(a)
"""
#output:
[[ True False False]
 [False  True False]
 [False False  True]]
"""




a = np.identity(3,dtype=None)
print(a)
"""
#output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""



a = np.identity(3,dtype=complex)
print(a)
"""
#output:
[[1.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 1.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 1.+0.j]]
"""


#np.repeat()
import numpy as np
a = np.repeat([2,3,4],2,axis=0)
print(a)
"""
#output:
[2 2 3 3 4 4]
"""



a = np.repeat([2,3,4],3,axis=0)
print(a)
"""
#output:
[2 2 2 3 3 3 4 4 4]
"""




a = np.repeat([[2,3,4],[5,6,7]],3,axis=0)
print(a)
"""
#output:
[[2 3 4]
 [2 3 4]
 [2 3 4]
 [5 6 7]
 [5 6 7]
 [5 6 7]]
"""



'''
note:
if the 2d array not been used in repeat method
a = np.repeat([2,3,4],2,axis=1)
print(a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 106, in <module>
    a = np.repeat([2,3,4],2,axis=1)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages\numpy\_core\fromnumeric.py", line 506, in repeat
    return _wrapfunc(a, 'repeat', repeats, axis=axis)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages\numpy\_core\fromnumeric.py", line 54, in _wrapfunc
    return _wrapit(obj, method, *args, **kwds)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages\numpy\_core\fromnumeric.py", line 46, in _wrapit
    result = getattr(arr, method)(*args, **kwds)
numpy.exceptions.AxisError: axis 1 is out of bounds for array of dimension 1
'''



import numpy as np
a = np.repeat([[2,3,4],[5,6,7]],3,axis=1)
print(a)
"""
note:note: repeat in rows --> 1

#output:
[[2 2 2 3 3 3 4 4 4]
 [5 5 5 6 6 6 7 7 7]]
"""


a = np.repeat([[2,3,4],[5,6,7]],3,axis=0)
print(a)
"""
note: repeat in coloumn --> 0

#output:
[[2 3 4]
 [2 3 4]
 [2 3 4]
 [5 6 7]
 [5 6 7]
 [5 6 7]]
"""


#default --> not been taken 3d array and get the 2d array of numbers
import numpy as np
a = np.repeat([[2,3,4],[5,6,7]],3)
print(a)
"""
#output:
[2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7]
"""



import numpy as np
a = np.arange(3)
print(a)

print("-----------------------")
b = np.random.randint(5,10,size=(3,))
print(b)

print("-----------------------")
print(a*b)
"""
#output:
[0 1 2]
-----------------------
[9 7 5]
-----------------------
[ 0  7 10]
"""

#or alternative method matmul --> matrix_multiplication
c = np.matmul(a,b)
print(c)
"""
note:by add the row values

#output:
17
"""



"""
#np.mutmul()
each row of array "a" is multipled by each of all coloumn "b"
"""
a = np.arange(1,10).reshape(3,3)
print(a)

print("*"*10)

b = np.random.randint(1,4,size=(3,3))
print(b)

print("*"*10)

c = np.matmul(a,b,dtype=int)
print(c)
"""
note: to multiple to add as each row by its all column

#output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
**********
[[3 2 3]
 [3 1 3]
 [2 2 2]]
**********
[[15 10 15]
 [39 25 39]
 [63 40 63]]
"""


a = np.arange(1,10).reshape(3,3)
print(a)

print("*"*10)

b = np.random.randint(-2,4,size=(3,3))
print(b)

print("*"*10)

c = np.matmul(a,b,dtype=int)
print(c)
"""
#output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
**********
[[ 1  3 -2]
 [ 1 -2  2]
 [ 1  0  0]]
**********
[[ 6 -1  2]
 [15  2  2]
 [24  5  2]]
"""


#to find determinant in linear algebra
x = np.arange(1,5).reshape(2,2)
print(x)
print("*"*10)
print(np.linalg.det(x))
"""
#output:
[[1 2]
 [3 4]]
**********
-2.0000000000000004
"""



x = np.arange(1,10).reshape(3,3)
print(x)
print("-------------------------")

print(np.linalg.det(x))
"""
#output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
-------------------------
0.0
"""


x = np.random.randint(-3,5,size=(3,3))
print(x)

print("--------------------------------")

print(np.linalg.det(x))
"""
#output:
[[ 2  0  0]
 [-1 -3 -2]
 [-1  3 -3]]
--------------------------------
29.99999999999999
"""

"""
to revise these topics:
#Determinant
#Trace
#Singular Vector Decomposition
#Matrix Norm
#Inverse
#etc...
"""


#min and max in numpy
import numpy as np
stats = np.array([[1,2,3],[-3,-6,-1],[4,2,1]])
print(stats)
print("--------------------------------------")

print(np.min(stats))
print(np.max(stats))
"""
#output:
[[ 1  2  3]
 [-3 -6 -1]
 [ 4  2  1]]
--------------------------------------
-6
4
"""


a = np.random.randint(-4,5,size=(3,3))
print(a)

print("------------------------------")

print("axis_1: row_min:",np.min(a,axis=1))
print("axis_1: row_max:",np.max(a,axis=1))
"""
#output:
[[ 3  0 -3]
 [ 0 -3 -4]
 [ 3  2  2]]
------------------------------
axis_1: row_min: [-3 -4  2]
axis_1: row_max: [3 0 3]
"""



a = np.random.randint(-4,5,size=(3,3))
print(a)

print("------------------------------")

print("axis_1: column_min:",np.min(a,axis=0))
print("axis_1: column_max:",np.max(a,axis=0))
"""
#output:
[[-1  0 -1]
 [ 0  3 -4]
 [ 3  1  3]]
------------------------------
axis_1: column_min: [-1  0 -4]
axis_1: column_max: [3 3 3]
"""


import numpy as np
from scipy import stats as sc
student_mark = np.genfromtxt(fname="numeric.txt",delimiter=',',dtype=int)
print(student_mark)
print("-------------------------------------------------------------------------")

print("min value: ",np.min(student_mark))
print("max value: ",np.max(student_mark))
print("mean value: ",np.mean(student_mark))
print("median value: ",np.median(student_mark))
print("mode value: ",sc.mode(student_mark))# note: numpy does not have mode fn
print("standard deviation: ",np.std(student_mark))
"""
#output:
min value:  4
max value:  100
mean value:  54.9
median value:  54.5
mode value:  ModeResult(mode=np.int64(45), count=np.int64(3))
standard deviation:  23.877953569488874
"""


print(len(student_mark))
#30


print(student_mark.size)
#30


a = student_mark.reshape(5,6)
print(a)
"""
#output:
[[ 30  40  33  11  22  54]
 [ 90  88  76  67  45  76]
 [ 80   4  32  56  78  65]
 [ 54  45  34  67  89 100]
 [ 33  45  43  55  65  70]]
"""


print(sc.mode(a)) #defualt--> axis = 0 (row)
#ModeResult(mode=array([30, 45, 32, 67, 22, 54]), count=array([1, 2, 1, 2, 1, 1]))


print(sc.mode(a,axis=0))
#ModeResult(mode=array([30, 45, 32, 67, 22, 54]), count=array([1, 2, 1, 2, 1, 1]))


print(sc.mode(a,axis=1))
#ModeResult(mode=array([11, 76,  4, 34, 33]), count=array([1, 2, 1, 1, 1]))


c = student_mark.astype("i1").reshape(5,6)
print(c)
"""
#output:
[[ 30  40  33  11  22  54]
 [ 90  88  76  67  45  76]
 [ 80   4  32  56  78  65]
 [ 54  45  34  67  89 100]
 [ 33  45  43  55  65  70]]
"""



c = student_mark.astype("f4").reshape(5,6)
print(c)
"""
#output:
[[ 30.  40.  33.  11.  22.  54.]
 [ 90.  88.  76.  67.  45.  76.]
 [ 80.   4.  32.  56.  78.  65.]
 [ 54.  45.  34.  67.  89. 100.]
 [ 33.  45.  43.  55.  65.  70.]]
"""


c = student_mark.astype(str).reshape(5,6)
print(c)
"""
#output:
[['30' '40' '33' '11' '22' '54']
 ['90' '88' '76' '67' '45' '76']
 ['80' '4' '32' '56' '78' '65']
 ['54' '45' '34' '67' '89' '100']
 ['33' '45' '43' '55' '65' '70']]
"""


#boolean masking
import numpy as np
from scipy import stats as sc
student_mark = np.genfromtxt(fname="numeric.txt",delimiter=',',dtype=int)
print(student_mark)
print("------------------------")

print(student_mark > 30)
"""
#output:
[ 30  40  33  11  22  54  90  88  76  67  45  76  80   4  32  56  78  65
  54  45  34  67  89 100  33  45  43  55  65  70]
------------------------
[False  True  True False False  True  True  True  True  True  True  True
  True False  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True]
"""




print(student_mark > 40)
"""
#output:
[False False False False False  True  True  True  True  True  True  True
  True False False  True  True  True  True  True False  True  True  True
 False  True  True  True  True  True]
"""


#instead of boolean value, show the real values is called as boolean indexing:
import numpy as np
from scipy import stats as sc
student_mark = np.genfromtxt(fname="numeric.txt",delimiter=',',dtype=int)
print(student_mark)
print("------------------------------------")
a = student_mark[student_mark>40]
print(a)
"""
#output:
[ 30  40  33  11  22  54  90  88  76  67  45  76  80   4  32  56  78  65
  54  45  34  67  89 100  33  45  43  55  65  70]
------------------------------------
[ 54  90  88  76  67  45  76  80  56  78  65  54  45  67  89 100  45  43
  55  65  70]
"""



import numpy as np
from scipy import stats as sc
student_mark = np.genfromtxt(fname="numeric.txt",delimiter=',',dtype=int)
print(student_mark)
print("------------------------------------")
a = student_mark[student_mark>30]
print(a)
"""
#output:
[ 30  40  33  11  22  54  90  88  76  67  45  76  80   4  32  56  78  65
  54  45  34  67  89 100  33  45  43  55  65  70]
------------------------------------
[ 40  33  54  90  88  76  67  45  76  80  32  56  78  65  54  45  34  67
  89 100  33  45  43  55  65  70]
"""

#by numpy using at indexing
a = np.array([2,3,4,5,6,7,8])
for i in enumerate(a):
    print(i)
print("-----------------------------")
print(a[[1,2,5,4]])
"""
#output:
(0, np.int64(2))
(1, np.int64(3))
(2, np.int64(4))
(3, np.int64(5))
(4, np.int64(6))
(5, np.int64(7))
(6, np.int64(8))
-----------------------------
[3 4 7 6]
"""




import numpy as np
from numpy import genfromtxt
import os
os.chdir(r"D:\sample\sample") # --> for correct my directory


x = genfromtxt("example_dataset.csv",dtype="U",delimiter=",")
a = np.asarray(x)
print(a)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""

print(len(a))#7
print(a.size)#35


print(a[0])
#['name' 'age' 'native' 'marriage_status' 'salary']


print(a[[0,4,6]])
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""



print(a[0:4])
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']]
"""


#we dont use delimiter
x = genfromtxt("example_dataset.csv",dtype="U")
a = np.asarray(x)
x = a[0]
print(x)
#name,age,native,marriage_status,salary

print(type(x))
#<class 'numpy.str_'>

b = x.split(sep=",")
print(b)
#['name', 'age', 'native', 'marriage_status', 'salary']

print(type(b))
#<class 'list'>


x = genfromtxt("example_dataset.csv",dtype="U",delimiter=",")
a = np.asarray(x)
print(a)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""


print(a[0][[0,1,2]])
#['name' 'age' 'native']



x = genfromtxt("example_dataset.csv",dtype=None,delimiter=",")
a = np.asarray(x)
print(a)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""


x = genfromtxt("example_dataset.csv",dtype=str,delimiter=",")
print(x)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""



x = genfromtxt("example_dataset.csv",dtype=int,delimiter=",")
print(x)
"""
#output:
[[   -1    -1    -1    -1    -1]
 [   -1    22    -1    -1 40000]
 [   -1    21    -1    -1 45000]
 [   -1    22    -1    -1 35000]
 [   -1    25    -1    -1 60000]
 [   -1    23    -1    -1 50000]
 [   -1    43    -1    -1 75000]]
"""




x = genfromtxt("example_dataset.csv",dtype=float,delimiter=",")
print(x)
"""
#output:
[[    nan     nan     nan     nan     nan]
 [    nan 2.2e+01     nan     nan 4.0e+04]
 [    nan 2.1e+01     nan     nan 4.5e+04]
 [    nan 2.2e+01     nan     nan 3.5e+04]
 [    nan 2.5e+01     nan     nan 6.0e+04]
 [    nan 2.3e+01     nan     nan 5.0e+04]
 [    nan 4.3e+01     nan     nan 7.5e+04]]
"""


x = genfromtxt("example_dataset.csv",dtype=object,delimiter=",")
print(x)
"""
#output:
[[b'name' b'age' b'native' b'marriage_status' b'salary']
 [b'santhosh' b'22' b'dgl' b'no' b'40000']
 [b'nithish' b'21' b'mdu' b'no' b'45000']
 [b'rahul' b'22' b'tne' b'no' b'35000']
 [b'mukesh' b'25' b'tvli' b'yes' b'60000']
 [b'suresh' b'23' b'kkd' b'no' b'50000']
 [b'manoj' b'43' b'dgl' b'yes' b'75000']]
"""

print(x[-1])
#[b'manoj' b'43' b'dgl' b'yes' b'75000']


print(x[[-5,-2,-1]])
"""
#output:
[[b'nithish' b'21' b'mdu' b'no' b'45000']
 [b'suresh' b'23' b'kkd' b'no' b'50000']
 [b'manoj' b'43' b'dgl' b'yes' b'75000']]
"""



import  numpy as np
import os

os.chdir(r"D:\sample\sample")

x = np.genfromtxt("example_dataset.csv",dtype="U",delimiter=",")
print(x)
print(len(x))
print(x.size)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['manoj' '43' 'dgl' 'yes' '75000']]

7
35
"""


#comments = "(what did you want to hide)"
x = np.genfromtxt("example_dataset.csv",dtype="U",delimiter=",",comments="@")
print(x)
print(len(x))
print(x.size)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
5
25
"""



#skip_header = True
x = np.genfromtxt("example_dataset.csv",dtype="U",delimiter=",",comments="@",skip_header=True)
print(x)
"""
#output:
[['santhosh' '22' 'dgl' 'no' '40000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""



x = np.genfromtxt("example_dataset.csv",dtype="U",delimiter=",",comments="@",skip_header=2)
print(x)
"""
#output:
[['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['manoj' '43' 'dgl' 'yes' '75000']]
"""



#skip_footer = 2 or skip_footer = (True or 1)
x = np.genfromtxt("example_dataset.csv",dtype="U",delimiter=",",comments="@",skip_header=False,skip_footer=2)
print(x)
print(len(x))
print(x.size)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['rahul' '22' 'tne' 'no' '35000']]
3
15
"""









#missing values
"""
note:
input file la missing value represent pannura string-a numpy ku solluthu
"""
x = np.genfromtxt("example_dataset.csv",dtype=float,delimiter=",",missing_values=" ",filling_values={0:np.inf})
print(x)
"""
#output:
[[    inf     nan     nan     nan     nan]
 [    inf 2.2e+01     nan     nan 4.0e+04]
 [    inf 2.1e+01     nan     nan 4.5e+04]
 [    inf 2.2e+01     nan     nan 3.5e+04]
 [    inf 2.5e+01     nan     nan 6.0e+04]
 [    inf 2.3e+01     nan     nan 5.0e+04]
 [    inf 4.3e+01     nan     nan 7.5e+04]
 [    inf 3.2e+01     nan     nan     nan]
 [    inf 4.3e+01     nan     nan     nan]]
"""



#by using missing_value and filling_value of numpy parameter to the numpy array filtering
x = np.genfromtxt("example_dataset.csv",dtype=None,delimiter=",")
x[x == ""] = "NA"
print(x)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['@nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['@suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']
 ['mahesh' '32' 'NA' 'no' 'NA']
 ['NA' '43' 'NA' 'yes' 'NA']]
"""



x = np.genfromtxt("example_dataset.csv",dtype=None,delimiter=",")
mask = (x[:,0] == "") #x[:,0] --> to select all data into the file with the column of 0
x[mask,0] = 1
print(x)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['@nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['@suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']
 ['mahesh' '32' '' 'no' '']
 ['1' '43' '' 'yes' '']]
"""

x = np.genfromtxt("example_dataset.csv",dtype=None,delimiter=",")
mask = (x[:,-1] == "") #x[:,0] --> to select all data into the file with the column of 0
x[mask,-1] = 1
print(x)
"""
#output:
[['name' 'age' 'native' 'marriage_status' 'salary']
 ['santhosh' '22' 'dgl' 'no' '40000']
 ['@nithish' '21' 'mdu' 'no' '45000']
 ['rahul' '22' 'tne' 'no' '35000']
 ['mukesh' '25' 'tvli' 'yes' '60000']
 ['@suresh' '23' 'kkd' 'no' '50000']
 ['manoj' '43' 'dgl' 'yes' '75000']
 ['mahesh' '32' '' 'no' '1']
 ['' '43' '' 'yes' '1']]
"""



x = np.genfromtxt("example_dataset.csv",dtype="int",delimiter=",",filling_values={0:999,1:333,2:777,3:987,4:666})
print(x)
"""
#output:
[[  999   333   777   987   666]
 [  999    22   777   987 40000]
 [  999    21   777   987 45000]
 [  999    22   777   987 35000]
 [  999    25   777   987 60000]
 [  999    23   777   987 50000]
 [  999    43   777   987 75000]
 [  999    32   777   987   666]
 [  999    43   777   987   666]]
"""


#how to write np array to csv file
x = np.genfromtxt("example_dataset.csv",dtype = "U")
x.tofile("sample_as_to_file.csv",sep="\n",format="%s")#this will have to given as str as each row
x.tofile("0sample_as_to_file.csv",sep="\n")#this will not an str as each row

import numpy as np
import random
import os

from pyarrow import arange

os.chdir(r"D:\sample\sample")

# Numpy - Indexing & Slicing
"""
Contents of ndarray object can be accessed and modified by indexing or slicing, just like python's in-build
container objects.

As mentioned earlier, items in ndarray object follows zero-based index. three types of indexing methods are
available:
  1) field access,
  2) basic slicing,
  3) advanced indexing.

basic slicing is an extension of python's basic concept of slicing to n dimensions. A python slice object is
constructed by giving start, stop, and step parameters to the build-in slice function. this slice object is 
passed to the array to extract a part of array.
"""
a = np.arange(10)
print(a)
s = slice(4)
print(a[s])
print(type(a[s]))
"""
#output:
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3]
<class 'numpy.ndarray'>
"""

a = np.arange(13)
print(a)
s = slice(0, 13, 6)
print(a[s])
print(type(a[s]))
"""
#output:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12]
[ 0  6 12]
<class 'numpy.ndarray'>
"""

print(a[0:13:6])
# [ 0  6 12]


a = np.random.randint(5, 20, size=(25))
print(a)
s = slice(0, 10, 2)  # start=0,end=10,step=2
print(a[s])
print(type(a[s]))
"""
#output:
[12 14 16  9 10 18 10 11 14  6 16 13 10 12 14 10 14 14 15 12 14  8 17 12
 12]
[12 16 10 10 14]
<class 'numpy.ndarray'>
"""

# difference between using slice and giving index directly to ndarray object.
"""
note:
slice gives for zero to (n-1).// "n" is the stop parameter and it is exclusive(the last item of
ndarray object will not be accessed)

Ndarray[4] gives only one index/field value
"""
a = np.arange(10)
print(a)
s = slice(4)
print(a[s])
print(a[4])
"""
#output:
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3] --> slice
4  --> indexing
"""

# slice items starting from given index on ndarray object as seen list
a = np.arange(10)
print(a)
print(a[2:])  # from second index to end
"""
#output:
[0 1 2 3 4 5 6 7 8 9]
[2 3 4 5 6 7 8 9]
"""

# copy vs slice_copy
b = a

c = a[:]

# the above description applies to multiple-dimensional ndarray
a = np.arange(9).reshape(3, 3)
print(a)
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""
print(a.size)  # 9
print(len(a))  # 3

print(a[0])
# [0 1 2]


print(a[1])
# [3 4 5]


print(a[2])
# [6 7 8]


"""
print(a[3])

#output:

IndexError: index 3 is out of bounds for axis 0 with size 3
"""

print(a[1:])  # from index 1 to end
"""
#output:
[[3 4 5]
 [6 7 8]]
"""

print(a[2:])  # from index 2 to end
# [[6 7 8]]


print(a[0:2])
"""
#output:
[[0 1 2]
 [3 4 5]]
"""

print(a[0:1000])
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""

a = np.array(np.arange(10, 100, 10).reshape(3, 3))
print(a)
print(len(a))
print(a.size)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
3
9
"""

# slicing can also include ellipsis(...) --> used for slicing multidimensional numpy arrays
"""
slicing can also include ellipsis(...) to make a selection tuple of the same length as the 
dimension of an array. if ellipsis is used at the row position, it will return an ndarray
comprising of items in rows.

ellipsis is used for slicing multidimensional numpy arrays.
the ellipsis syntax may be used to indicate selecting in full any remaining unspecified dimensions.

template:
array object[<rows>,<cols>]
"""
a = np.array(np.arange(10, 100, 10).reshape(3, 3))
print(a)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
"""
print(a[..., 0])
# [10 40 70] --> 1st column


print(a[..., 1])
# [20 50 80]  --> 2nd column


print(a[..., 2])
# [30 60 90]  --> 3rd column


print(a[0, ...])
# [10 20 30] --> 1st row


print(a[1, ...])
# [40 50 60] --> 2nd row


print(a[2, ...])
# [70 80 90] --> 3rd row

"""
print(a[3 , ...])
#output:
IndexError: index 3 is out of bounds for axis 0 with size 3
"""

print(a[1, 1, ...])
# 50 --> 1st row 1st value to get


print(a[-1, -1, ...])
# 90 --> last row last value to get


a = np.array(np.arange(0, 18).reshape(3, 3, 2))
print(a)
"""
#output:
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]

 [[12 13]
  [14 15]
  [16 17]]]
"""

print(a[1, ...])
"""
#output:
[[ 6  7]
 [ 8  9]
 [10 11]]
"""

print(a[1, 1, ...])
# [8 9]


print(a[2, 1, ...])
# [14 15]


print(a[..., 2:])
# [] --> only they have two colum so the index is out of range


print(a[..., 1:])
"""
#output:
[[[ 1]
  [ 3]
  [ 5]]

 [[ 7]
  [ 9]
  [11]]

 [[13]
  [15]
  [17]]]
"""

print(a[..., 1, 1:])
"""
note:
they give every 1 st column 1st value will be given as output

#output:
[[ 3]
 [ 9]
 [15]]
"""

print(a[..., :])
"""
#output:
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]

 [[12 13]
  [14 15]
  [16 17]]]
"""


import  numpy as np
import os


os.chdir(r"D:\sample\sample")


data = np.genfromtxt("example_dataset.csv",dtype=None,comments="@",delimiter=",")
print(data[... , 0])
#['name' 'santhosh' 'rahul' 'mukesh' 'manoj' 'mahesh' '']

print(data[... , 2])
#['native' 'dgl' 'tne' 'tvli' 'dgl' '' '']





data = np.genfromtxt("example_dataset.csv",dtype=None,comments="@",delimiter=",")
t_amount = data[... , -1]
t_amount[t_amount == "salary"] = 0
t_amount[t_amount == ""] = 0
total = 0
for i in t_amount:
    total = total + (int(i))
print("total amount of salary will {}".format(total))
#total amount of salary will 210000




data = np.genfromtxt("example_dataset.csv",dtype="int",comments="@",delimiter=",",skip_header=1)
salary = data[... , -1]
salary[salary == -1] = 0
print(sum(salary))
#210000



data = np.genfromtxt("example_dataset.csv",dtype="int",comments="@",delimiter=",",skip_header=1)
salary = data[... , -1].astype("int")
salary = salary[salary  > 1]
print(sum(salary))
#210000



#view and copy method
#view
x = np.arange(9).reshape(3,3)
print("original data before it modified\n",x)
print("id of before original_data_id\n",id(x))

view1 = x.view()
print("\nview data before modified\n",view1)
print("id of before view_data_id\n",id(view1))

view1[1][1] = 100


print("\noriginal data after modified\n",x)
print("id of after original_data_id\n",id(x))
"""
#output:
original data before it modified
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id of before original_data_id
 2289882146032

view data before modified
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id of before view_data_id
 2290153114960

original data after modified
 [[  0   1   2]
 [  3 100   5]
 [  6   7   8]]
id of after original_data_id
 2289882146032
"""




#copy
x = np.arange(9).reshape(3,3)
print("original data before it modified\n",x)
print("id of before original_data_id\n",id(x))

copy1 = x.copy()
print("\ncopy data before modified\n",copy1)
print("id of before copy_data_id\n",id(copy1))

copy1[1][1] = 100


print("\noriginal data after modified\n",x)
print("id of after original_data_id\n",id(x))


print("\ncopy data after modified\n",copy1)
print("id of after copy_data_id\n",id(copy1))
"""
#output:
original data before it modified
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id of before original_data_id
 2651049708976

copy data before modified
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id of before copy_data_id
 2650779215088

original data after modified
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id of after original_data_id
 2651049708976

copy data after modified
 [[  0   1   2]
 [  3 100   5]
 [  6   7   8]]
id of after copy_data_id
 2650779215088
"""



"""
note:
view == slice
they will affected by original data as modified the copied data

copy:
they will not affected by after modified the copied array to the original array
"""

import numpy as np
import os

os.chdir(r"D:\sample\sample")
# numpy advanced indexing
"""
it is possible to make a selection from ndarray that is non-tuple
sequence, ndarray object of integer or boolean data type, or a tuple
with least one item being a sequence object.

advanced indexing always returns a copy of data. as against this, the slicing
only presents a view.

there are two types of advanced indexing
   1)integer
   2)boolean
"""

"""
#Integer Indexing
this mechanism helps in selecting any arbitrary item in an array based on its Ndimensional index.
each integer array represents the number of indexes into that dimension. when the index consists of 
as many integer arrays as the dimensions of the target ndarray, it becomes straight forward.
"""

x = np.arange(9).reshape(3, 3)
print(x)
print("-" * 30)

y = x[[0, 1, 2], [0, 1, 0]]
print(y)
"""
#output:

[[0 1 2]
 [3 4 5]
 [6 7 8]]
------------------------------
[0 4 6]
"""

x = np.arange(9).reshape(3, 3)
print(x)
print("-" * 30)

y = x[[0, 1, 2], [2, 1, 0]]
print(y)
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
------------------------------
[2 4 6]
"""

# notes
'''
 [[ 0      1     2     3  ]
   (0,0) (0,1) (0,2) (0,3)

  [  4     5    6     7   ]  
   (1,0) (1,1) (1,2) (1,3)

  [  8     9    10    11  ]
   (2,0) (2,1) (2,2) (2,3)

  [ 12    13    14    15    ]]
  (3,0) (3,1) (3,2) (3,3)
'''

x = np.arange(9).reshape(3, 3)
print(x)
print("-" * 30)

y = x[[1, 0, 0, 2, 2], [1, 0, -1, 0, -1]]
print(y)
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
------------------------------
[4 0 2 6 8]
"""

x = np.arange(9).reshape(3, 3)
print("original array:\n", x)
rows = np.array([[0, 0], [2, 2]])
columns = np.array([[0, 2], [0, 2]])
y = x[rows, columns]
print("after slicing: \n", y)
"""
#output:
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
after slicing: 
 [[0 2]  --> [(r->0,c->0),(r->0,c->2)]
 [6 8]]  --> [(r->2,c->0)(r->2,c->2)]
"""

x = np.arange(16).reshape(4, 4)
print("original array:\n", x)
rows = np.array([[0, 0], [2, 2], [3, 3]])
columns = np.array([[0, 2], [0, 2], [0, 2]])
y = x[rows, columns]
print("after slicing: \n", y)
"""
#output:
original array:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
after slicing: 
 [[ 0  2]
 [ 8 10]
 [12 14]]
"""

"""
advanced and basic indexing can be combined by using one slice(:) or ellipsis(...) with an index array.
the following examples uses slice for row and advanced index for column. the result is the same when slice
is used for both. but advanced index results in copy and may have different memory layout.
"""

x = np.arange(16).reshape(4, 4)
print("original_data: \n", x)

print("_" * 50)
z = x[1:4]
print(z)

z = x[1:4, 1:3]  # slicing with index[1:4,1:3] 1:4 --> row, 1:3 --> columns
print("after slicing row and columns: \n", z)
"""
#output:
original_data: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
__________________________________________________
[[ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
after slicing row and columns: 
 [[ 5  6]
 [ 9 10]
 [13 14]]
"""

x = np.arange(16).reshape(4, 4)
print("original_data: \n", x)

print("_" * 50)
z = x[1:3]
print(z)

z = x[1:4, 2:2]  # slicing with index[1:3,2:2]1:3 --> row, 2:2 --> columns
print("after slicing row and columns: \n", z)
"""
#output;
original_data: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
__________________________________________________
[[ 4  5  6  7]
 [ 8  9 10 11]]
after slicing row and columns: 
 [] --> reason behind as 2:2

"""

# slicing the value
x = np.arange(16).reshape(4, 4)
print("original_data: \n", x)

print("_" * 50)
z = x[1:4]
print(z)

z = x[1:4, [1, 3]]  # slicing with index[1:4,[1,3]] 1:4 --> row, [1,3] --> columns
print("after slicing row and columns: \n", z)
"""
#output:
original_data: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
__________________________________________________
[[ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
after slicing row and columns: 
 [[ 5  7]
 [ 9 11]
 [13 15]]
"""

x = np.arange(16).reshape(4, 4)
print("original_data: \n", x)

print("_" * 50)
z = x[1:3]
print(z)

z = x[[1, 3], 1:3]  # slicing with index[1:4,[1,3]] 1:4 --> row, [1,3] --> columns
print("after slicing row and columns: \n", z)
'''
#output:
original_data: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
__________________________________________________
7
after slicing row and columns: 
 [[ 5  6]
 [13 14]]
'''

x = np.arange(16).reshape(4, 4)
print("original_data: \n", x)

print("_" * 50)
z = x[1:3]
print(z)

z = x[[1, 3], [1, 3]]
print("after slicing row and columns: \n", z)
"""
#output:
original_data: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
__________________________________________________
[[ 4  5  6  7]
 [ 8  9 10 11]]
after slicing row and columns: 
 [ 5 15]
"""





#slicing the particular rows and columns
x = np.arange(16).reshape(4,4)
print(x,"\n")

print(x[[0,3]])
print("*"*45)
print(x[[0,3]][...,[0,2]])
"""
#output:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]] 

[[ 0  1  2  3]
 [12 13 14 15]]
*********************************************
[[ 0  2]
 [12 14]]
"""



#boolean array indexing
"""
this type of advanced indexing is used when the resultant object is meant to be 
the result of boolean operations, such as comparison operators 
"""
x = np.arange(9).reshape(3,3)
print(x,"\n")
print(x>5,"\n")
print(x[x>5],"\n")
"""
#output:
[[0 1 2]
 [3 4 5]
 [6 7 8]] 

[[False False False]
 [False False False]
 [ True  True  True]] 

[6 7 8] 
"""






x = np.arange(0,81,9).reshape(3,3)
print(x,"\n")

y = x[1]

print(y>27,"\n")

print(y[y>27],"\n")
"""
#output:
[[ 0  9 18]
 [27 36 45]
 [54 63 72]] 

[False  True  True] 

[36 45] 
"""


#find Nan/nan/NAN --> not an number
a = np.array([2,3,4,np.nan,3,2,30,np.nan])
print(a[np.isnan(a)])
#[nan nan]

print(a[~np.isnan(a)])
#[ 2.  3.  4.  3.  2. 30.]


print(a)
x = a[~np.isnan(a)]
x = x[x>=4]
print(x)
"""
we remove the np.nan and then slice the particular value in the ndarray

#output:
[ 2.  3.  4. nan  3.  2. 30. nan]
[ 4. 30.]
"""


#iscomplex to check
x = np.array([2,22+2j,3+1j,33,55,3+3j])
print(x)
#[ 2.+0.j 22.+2.j  3.+1.j 33.+0.j 55.+0.j  3.+3.j]

print([np.iscomplex(x)])
#[array([False,  True,  True, False, False,  True])]

print(x[np.iscomplex(x)])
#[22.+2.j  3.+1.j  3.+3.j]

"""
#by check methods in numpy

*) np.nan --> not an number
*) np.inf --> infinite
*) np.isneginf --> that's check the negative infinite or not
*) np.posinf  -->  that's check the positive infinite or not
*) np.isfinite --> if checks the array elements are finite or not
*) np.iscomplex --> check the value is complex or not
*) np.nat --> not an time
*) np.isclose --> ...
*) np.iscomplexobject --> ...
*) np.isscalar(element) --> to check the element is scalar or not
"""




#broadcasting in numpy
a = np.arange(9).reshape(3,3)
print("a value is :\n ",a)
print("shape of a : ",np.shape(a))
print("dimension of a : ",a.ndim)

print("-"*50)

b = np.arange(9,18).reshape(3,3)
print("b value is :\n ",b)
print("shape of b : ",np.shape(b))
print("dimension of b : ",b.ndim)

print("-"*50)

c = a * b

print("multiple of these two array:\n",c)
print("shape of c : ",np.shape(c))
print("dimension of c : ",c.ndim)
"""
#note:
if the two array will be have the same dimensions that's why these will correct

#output:
a value is :
  [[0 1 2]
 [3 4 5]
 [6 7 8]]
shape of a :  (3, 3)
dimension of a :  2
--------------------------------------------------
b value is :
  [[ 9 10 11]
 [12 13 14]
 [15 16 17]]
shape of b :  (3, 3)
dimension of b :  2
--------------------------------------------------
multiple of these two array:
 [[  0  10  22]
 [ 36  52  70]
 [ 90 112 136]]
shape of c :  (3, 3)
dimension of c :  2
"""







"""
#these dimension will not have been same

a = np.arange(12).reshape(3,4)
print("a value is : ",a)
print("shape of a : ",np.shape(a))
print("dimension of a : ",a.ndim)

print("-"*50)

b = np.arange(9,18).reshape(3,3)
print("b value is : ",b)
print("shape of b : ",np.shape(b))
print("dimension of b : ",b.ndim)

print("-"*50)

c = a * b

print("multiple of these two array:",c)
print("shape of c : ",np.shape(c))
print("dimension of c : ",c.ndim)

#output:
ValueError: operands could not be broadcast together with shapes (3,4) (3,3) 
"""


print("&"*60,"\n")


"""
if the value will broadcast will "one size array --> [2]" these will have an high 
memory space so we use instead of scalar unit
"""
a = np.arange(4).reshape(4)
print("a value is : \n",a)
print("size of a: ",a.size)
print("itemsize of a", a.itemsize)
print("bytes of a",a.nbytes)

print("-"*50)

b = 2

c = a * b
print("the c value is :\n",c)
print("size of c : ",np.size(c))
print("itemsize of c : ",c.itemsize)
print("bytes of c : ",c.nbytes)
"""
#output:
a value is : 
 [0 1 2 3]
size of a:  4
itemsize of a 8
bytes of a 32
--------------------------------------------------
the c value is :
 [0 2 4 6]
size of c :  4
itemsize of c :  8
bytes of c :  32
"""

"""
#broadcast for 2d array
(applicable only to 2dim ndarray)

when operating on two arrays, Numpy compares their shapes element-wise. it starts with
the trailing dimensions and works its way forward. Two Dimensions are compatible 
when

 1) they are equal dimension,(their shape are equal),  or
 2) one of them is 1 (shape is 1,) --> [2d]

 ***************************************************************

 Both arrays shape must be equal

 a array shape (4,3)
 b array shape (4,3)

     or

 a array shape (4,3)
 b array shape (1,3)    or    b array shape(4,1)

example for 'b' arrays row must be 1(note: col must be equal to array 'a')

   #triling array is the last value in the shape of the array
   a array shape (4,3) #triling array must be same
   b array shape (1,3) 
"""

# by multiple by row
a = np.arange(9).reshape(3, 3)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(3).reshape(1, 3)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
shape of a :  (3, 3)
dimension of a :  2
--------------------------------------------------
b values is: 
 [[0 1 2]]
shape of b :  (1, 3)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[ 0  1  4]
 [ 0  4 10]
 [ 0  7 16]]
shape of c :  (3, 3)
dimension of c :  2
"""

# by multiple by column
a = np.arange(9).reshape(3, 3)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(3).reshape(3, 1)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
shape of a :  (3, 3)
dimension of a :  2
--------------------------------------------------
b values is: 
 [[0]
 [1]
 [2]]
shape of b :  (3, 1)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[ 0  0  0]
 [ 3  4  5]
 [12 14 16]]
shape of c :  (3, 3)
dimension of c :  2
"""

# General Broadcasting Rules
"""
(applicable more than 2dim array)

The Below Combination Of Shapes Works Well In Broadcasting

Rules To BroadCasting

   array a,b's ndim is equal, column also equal it works 
"""

# Rule_1
"""
A (2D array): 5 x 4
B (1D array): 1 or [1]

result (2d array): 5 x 4
"""
a = np.arange(20).reshape(5, 4)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(1, 2).reshape(1)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
shape of a :  (5, 4)
dimension of a :  2
--------------------------------------------------
b values is: 
 [1]
shape of b :  (1,)
dimension of b :  1
--------------------------------------------------
c values is: 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
shape of c :  (5, 4)
dimension of c :  2
"""

a = np.arange(40).reshape(2, 5, 4)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(3, 4).reshape(1)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]
  [12 13 14 15]
  [16 17 18 19]]

 [[20 21 22 23]
  [24 25 26 27]
  [28 29 30 31]
  [32 33 34 35]
  [36 37 38 39]]]
shape of a :  (2, 5, 4)
dimension of a :  3
--------------------------------------------------
b values is: 
 [3]
shape of b :  (1,)
dimension of b :  1
--------------------------------------------------
c values is: 
 [[[  0   3   6   9]
  [ 12  15  18  21]
  [ 24  27  30  33]
  [ 36  39  42  45]
  [ 48  51  54  57]]

 [[ 60  63  66  69]
  [ 72  75  78  81]
  [ 84  87  90  93]
  [ 96  99 102 105]
  [108 111 114 117]]]
shape of c :  (2, 5, 4)
dimension of c :  3
"""

# Rule_2
"""
A (2D array): 5 x 4
B (1D array): 4     --> ([1,2,3,4]-->(4,))

Result (2D array): 5 x 4
"""
a = np.arange(40).reshape(2, 5, 4)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(0, 4).reshape(4)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#note:
to multiple by the column of "b" with column of "a" at each value

#output:
a values is: 
 [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]
  [12 13 14 15]
  [16 17 18 19]]

 [[20 21 22 23]
  [24 25 26 27]
  [28 29 30 31]
  [32 33 34 35]
  [36 37 38 39]]]
shape of a :  (2, 5, 4)
dimension of a :  3
--------------------------------------------------
b values is: 
 [0 1 2 3]
shape of b :  (4,)
dimension of b :  1
--------------------------------------------------
c values is: 
 [[[  0   1   4   9]
  [  0   5  12  21]
  [  0   9  20  33]
  [  0  13  28  45]
  [  0  17  36  57]]

 [[  0  21  44  69]
  [  0  25  52  81]
  [  0  29  60  93]
  [  0  33  68 105]
  [  0  37  76 117]]]
shape of c :  (2, 5, 4)
dimension of c :  3
"""

# Rule_3
"""
ndim is same for both arrays. then column must be same for both
arrays(same like 2D rules)

 A array shape(1,4,3) #triling value must be same
 B array shape(1,1,3)

 both column must be same and shape also must be same 
"""
a = np.arange(40).reshape(2, 5, 4)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(8).reshape(2, 1, 4)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]
  [12 13 14 15]
  [16 17 18 19]]

 [[20 21 22 23]
  [24 25 26 27]
  [28 29 30 31]
  [32 33 34 35]
  [36 37 38 39]]]
shape of a :  (2, 5, 4)
dimension of a :  3
--------------------------------------------------
b values is: 
 [[[0 1 2 3]]

 [[4 5 6 7]]]
shape of b :  (2, 1, 4)
dimension of b :  3
--------------------------------------------------
c values is: 
 [[[  0   1   4   9]
  [  0   5  12  21]
  [  0   9  20  33]
  [  0  13  28  45]
  [  0  17  36  57]]

 [[ 80 105 132 161]
  [ 96 125 156 189]
  [112 145 180 217]
  [128 165 204 245]
  [144 185 228 273]]]
shape of c :  (2, 5, 4)
dimension of c :  3
"""

# example_2
a = np.arange(30).reshape(2, 5, 3)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(6).reshape(2, 1, 3)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]
  [12 13 14]]

 [[15 16 17]
  [18 19 20]
  [21 22 23]
  [24 25 26]
  [27 28 29]]]
shape of a :  (2, 5, 3)
dimension of a :  3
--------------------------------------------------
b values is: 
 [[[0 1 2]]

 [[3 4 5]]]
shape of b :  (2, 1, 3)
dimension of b :  3
--------------------------------------------------
c values is: 
 [[[  0   1   4]
  [  0   4  10]
  [  0   7  16]
  [  0  10  22]
  [  0  13  28]]

 [[ 45  64  85]
  [ 54  76 100]
  [ 63  88 115]
  [ 72 100 130]
  [ 81 112 145]]]
shape of c :  (2, 5, 3)
dimension of c :  3
"""

"""
a = np.arange(30).reshape(2,5,3)
print("a values is: ", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-"*50)

b = np.arange(12).reshape(4,1,3)
print("b values is: ", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: ", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)

#note
the first value is not been same that's why error will be gets an output  

#output:
 c = a * b
        ~~^~~
ValueError: operands could not be broadcast together with shapes (2,5,3) (4,1,3) 
"""

# Rule_4
"""
array a,b's ndim is different , but (column) is equal its works

A array shape (1,4,3) #3 is column
B array shape ( ,2,3) #3 is column
"""
a = np.arange(12).reshape(1, 4, 3)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(3).reshape(1, 3)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]]
shape of a :  (1, 4, 3)
dimension of a :  3
--------------------------------------------------
b values is: 
 [[0 1 2]]
shape of b :  (1, 3)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[[ 0  1  4]
  [ 0  4 10]
  [ 0  7 16]
  [ 0 10 22]]]
shape of c :  (1, 4, 3)
dimension of c :  3
"""

a = np.arange(24).reshape(2, 4, 3)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(12).reshape(4, 3)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]]]
shape of a :  (2, 4, 3)
dimension of a :  3
--------------------------------------------------
b values is: 
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
shape of b :  (4, 3)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[[  0   1   4]
  [  9  16  25]
  [ 36  49  64]
  [ 81 100 121]]

 [[  0  13  28]
  [ 45  64  85]
  [108 133 160]
  [189 220 253]]]
shape of c :  (2, 4, 3)
dimension of c :  3
"""

# Rule_5
"""
(row and col diagonal must be 1)

 A array shape(1,6)
 B array shape(5,1)
"""
a = np.arange(6).reshape(1, 6)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(5, 10).reshape(5, 1)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[0 1 2 3 4 5]]
shape of a :  (1, 6)
dimension of a :  2
--------------------------------------------------
b values is: 
 [[5]
 [6]
 [7]
 [8]
 [9]]
shape of b :  (5, 1)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[ 0  5 10 15 20 25]
 [ 0  6 12 18 24 30]
 [ 0  7 14 21 28 35]
 [ 0  8 16 24 32 40]
 [ 0  9 18 27 36 45]]
shape of c :  (5, 6)
dimension of c :  2
"""

"""
a = np.arange(12).reshape(2,6)
print("a values is: ", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-"*50)

b = np.arange(5,15).reshape(5,2)
print("b values is: ", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: ", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
#only to the diagonal must be "1" or otherwise that's rise an error
Traceback (most recent call last):
  File "D:\ds\python filesaaa.py", line 533, in <module>
    c = a * b
        ~~^~~
ValueError: operands could not be broadcast together with shapes (2,6) (5,2)
"""

# Rule_6
"""
(opposite of row and col diagonal must be 1)

 A array shape(6,1)
 B array shape(1,5)
"""
a = np.arange(6).reshape(6, 1)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(5, 10).reshape(1, 5)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[0]
 [1]
 [2]
 [3]
 [4]
 [5]]
shape of a :  (6, 1)
dimension of a :  2
--------------------------------------------------
b values is: 
 [[5 6 7 8 9]]
shape of b :  (1, 5)
dimension of b :  2
--------------------------------------------------
c values is: 
 [[ 0  0  0  0  0]
 [ 5  6  7  8  9]
 [10 12 14 16 18]
 [15 18 21 24 27]
 [20 24 28 32 36]
 [25 30 35 40 45]]
shape of c :  (6, 5)
dimension of c :  2
"""

a = np.arange(6).reshape(6, 1)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(15).reshape(3, 1, 5)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[0]
 [1]
 [2]
 [3]
 [4]
 [5]]
shape of a :  (6, 1)
dimension of a :  2
--------------------------------------------------
b values is: 
 [[[ 0  1  2  3  4]]

 [[ 5  6  7  8  9]]

 [[10 11 12 13 14]]]
shape of b :  (3, 1, 5)
dimension of b :  3
--------------------------------------------------
c values is: 
 [[[ 0  0  0  0  0]
  [ 0  1  2  3  4]
  [ 0  2  4  6  8]
  [ 0  3  6  9 12]
  [ 0  4  8 12 16]
  [ 0  5 10 15 20]]

 [[ 0  0  0  0  0]
  [ 5  6  7  8  9]
  [10 12 14 16 18]
  [15 18 21 24 27]
  [20 24 28 32 36]
  [25 30 35 40 45]]

 [[ 0  0  0  0  0]
  [10 11 12 13 14]
  [20 22 24 26 28]
  [30 33 36 39 42]
  [40 44 48 52 56]
  [50 55 60 65 70]]]
shape of c :  (3, 6, 5)
dimension of c :  3
"""

# Rule_7
"""
rows must be same + either arrays col is 1

array a and b rows Must equal + Either array "a" or array "b" column must be 1

  A array shape(8,1,6,1)
  B array shape( ,4,6,2)
"""
a = np.arange(12).reshape(2, 1, 6, 1)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(24).reshape(2, 6, 2)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[[ 0]
   [ 1]
   [ 2]
   [ 3]
   [ 4]
   [ 5]]]


 [[[ 6]
   [ 7]
   [ 8]
   [ 9]
   [10]
   [11]]]]
shape of a :  (2, 1, 6, 1)
dimension of a :  4
--------------------------------------------------
b values is: 
 [[[ 0  1]
  [ 2  3]
  [ 4  5]
  [ 6  7]
  [ 8  9]
  [10 11]]

 [[12 13]
  [14 15]
  [16 17]
  [18 19]
  [20 21]
  [22 23]]]
shape of b :  (2, 6, 2)
dimension of b :  3
--------------------------------------------------
c values is: 
 [[[[  0   0]
   [  2   3]
   [  8  10]
   [ 18  21]
   [ 32  36]
   [ 50  55]]

  [[  0   0]
   [ 14  15]
   [ 32  34]
   [ 54  57]
   [ 80  84]
   [110 115]]]


 [[[  0   6]
   [ 14  21]
   [ 32  40]
   [ 54  63]
   [ 80  90]
   [110 121]]

  [[ 72  78]
   [ 98 105]
   [128 136]
   [162 171]
   [200 210]
   [242 253]]]]
shape of c :  (2, 2, 6, 2)
dimension of c :  4
"""

a = np.arange(12).reshape(2, 1, 3, 2)
print("a values is: \n", a)
print("shape of a : ", a.shape)
print("dimension of a : ", a.ndim)

print("-" * 50)

b = np.arange(6).reshape(2, 3, 1)
print("b values is: \n", b)
print("shape of b : ", b.shape)
print("dimension of b : ", b.ndim)

print("-" * 50)

c = a * b
print("c values is: \n", c)
print("shape of c : ", c.shape)
print("dimension of c : ", c.ndim)
"""
#output:
a values is: 
 [[[[ 0  1]
   [ 2  3]
   [ 4  5]]]


 [[[ 6  7]
   [ 8  9]
   [10 11]]]]
shape of a :  (2, 1, 3, 2)
dimension of a :  4
--------------------------------------------------
b values is: 
 [[[0]
  [1]
  [2]]

 [[3]
  [4]
  [5]]]
shape of b :  (2, 3, 1)
dimension of b :  3
--------------------------------------------------
c values is: 
 [[[[ 0  0]
   [ 2  3]
   [ 8 10]]

  [[ 0  3]
   [ 8 12]
   [20 25]]]


 [[[ 0  0]
   [ 8  9]
   [20 22]]

  [[18 21]
   [32 36]
   [50 55]]]]
shape of c :  (2, 2, 3, 2)
dimension of c :  4
"""



#if we broadcast to the without have in rules by using np.newaxis method
#np.newaxis
a = np.array([1,2,3])
print("shape of a: ",a.shape)
a1 = (a[:,np.newaxis])
print("shape of a1: ",a1.shape)
print("a1 values: \n",a1)

print("------------------------------------------")

b = np.array([1,2,3,4])
print("shape of b: ",b.shape)
b1 = (b[np.newaxis,:])
print("shape of b1: ",b1.shape)
print("value of b1: \n",b1)

print("------------------------------------------")

print(a1*b1)
"""
#output:
shape of a:  (3,)
shape of a1:  (3, 1)
a1 values: 
 [[1]
 [2]
 [3]]
------------------------------------------
shape of b:  (4,)
shape of b1:  (1, 4)
value of b1: 
 [[1 2 3 4]]
------------------------------------------
[[ 1  2  3  4]
 [ 2  4  6  8]
 [ 3  6  9 12]]
"""





#example_2
a = np.arange(6).reshape(3,2)
print("shape of a: ",a.shape)
a1 = (a[:,np.newaxis])
print("shape of a1: ",a1.shape)
print("a1 values: \n",a1)

print("------------------------------------------")

b = np.arange(3)
print("shape of b: ",b.shape)
b1 = (b[:,np.newaxis])
print("shape of b1: ",b1.shape)
print("value of b1: \n",b1)

print("------------------------------------------")

print(a1*b1)
"""
#output:
shape of a:  (3, 2)
shape of a1:  (3, 1, 2)
a1 values: 
 [[[0 1]]

 [[2 3]]

 [[4 5]]]
------------------------------------------
shape of b:  (3,)
shape of b1:  (3, 1)
value of b1: 
 [[0]
 [1]
 [2]]
------------------------------------------
[[[ 0  0]
  [ 0  1]
  [ 0  2]]

 [[ 0  0]
  [ 2  3]
  [ 4  6]]

 [[ 0  0]
  [ 4  5]
  [ 8 10]]]
"""

# np.nditer()  --> iterating over array
"""
 nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K',
        casting='safe', op_axes=None, itershape=None, buffersize=0)

 #parameter:
  op : ndarray or sequence of array_like
       The array(s) to iterate over.

   flags : sequence of str, optional
         Flags to control the behavior of the iterator.

         1) ``buffered`` enables buffering when required.
         2)``c_index`` causes a C-order index to be tracked.
         3)``f_index`` causes a Fortran-order index to be tracked.
         4)``multi_index`` causes a multi-index, or a tuple of indices
             with one per iteration dimension, to be tracked.
         5)``common_dtype`` causes all the operands to be converted to
             a common data type, with copying or buffering as necessary.
         6)``copy_if_overlap`` causes the iterator to determine if read
             operands have overlap with write operands, and make temporary
             copies as necessary to avoid overlap. False positives (needless
             copying) are possible in some cases.
         7)``delay_bufalloc`` delays allocation of the buffers until
             a reset() call is made. Allows ``allocate`` operands to
             be initialized before their values are copied into the buffers.
         8)``external_loop`` causes the ``values`` given to be
             one-dimensional arrays with multiple values instead of
             zero-dimensional arrays.
         9)``grow_inner`` allows the ``value`` array sizes to be made
             larger than the buffer size when both ``buffered`` and
             ``external_loop`` is used.
         10)``ranged`` allows the iterator to be restricted to a sub-range
              of the iterindex values.
         11)``refs_ok`` enables iteration of reference types, such as
              object arrays.
         12)``reduce_ok`` enables iteration of ``readwrite`` operands
              which are broadcasted, also known as reduction operands.
         13)``zerosize_ok`` allows `itersize` to be zero.

   op_flags : list of list of str, optional
         This is a list of flags for each operand. At minimum, one of
         ``readonly``, ``readwrite``, or ``writeonly`` must be specified.

         1)``readonly`` indicates the operand will only be read from.
         2)``readwrite`` indicates the operand will be read from and written to.
         3)``writeonly`` indicates the operand will only be written to.
         4)``no_broadcast`` prevents the operand from being broadcasted.
         5)``contig`` forces the operand data to be contiguous.
         6)``aligned`` forces the operand data to be aligned.
         7)``nbo`` forces the operand data to be in native byte order.
         8)``copy`` allows a temporary read-only copy if required.
         9)``updateifcopy`` allows a temporary read-write copy if required.
         10)``allocate`` causes the array to be allocated if it is None
              in the ``op`` parameter.
         11)``no_subtype`` prevents an ``allocate`` operand from using a subtype.
         12)``arraymask`` indicates that this operand is the mask to use
              for selecting elements when writing to operands with the
              'writemasked' flag set. The iterator does not enforce this,
              but when writing from a buffer back to the array, it only
              copies those elements indicated by this mask.
         13)``writemasked`` indicates that only elements where the chosen
              ``arraymask`` operand is True will be written to.
         14)``overlap_assume_elementwise`` can be used to mark operands that are
              accessed only in the iterator order, to allow less conservative
              copying when ``copy_if_overlap`` is present.

   op_dtypes : dtype or tuple of dtype(s), optional
       The required data type(s) of the operands. If copying or buffering
       is enabled, the data will be converted to/from their original types.

   order : {'C', 'F', 'A', 'K'}, optional:
       Controls the iteration order. 
       1)'C' means C order, 
       2)'F' means Fortran order, 'A' means 'F' order if all the arrays are Fortran
       contiguous, 'C' order otherwise, and 'K' means as close to the
       order the array elements appear in memory as possible. This also
       affects the element memory order of ``allocate`` operands, as they
       are allocated to be compatible with iteration order.

       Default is 'K'.

   casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
       Controls what kind of data casting may occur when making a copy
       or buffering.  Setting this to 'unsafe' is not recommended,
       as it can adversely affect accumulations.

       * 'no' means the data types should not be cast at all.
       * 'equiv' means only byte-order changes are allowed.
       * 'safe' means only casts which can preserve values are allowed.
       * 'same_kind' means only safe casts or casts within a kind,
         like float64 to float32, are allowed.
       * 'unsafe' means any data conversions may be done.

   op_axes : list of list of ints, optional
       If provided, is a list of ints or None for each operands.
       The list of axes for an operand is a mapping from the dimensions
       of the iterator to the dimensions of the operand. A value of
       -1 can be placed for entries, causing that dimension to be
       treated as `newaxis`.

   itershape : tuple of ints, optional
       The desired shape of the iterator. This allows ``allocate`` operands
       with a dimension mapped by op_axes not corresponding to a dimension
       of a different operand to get a value not equal to 1 for that
       dimension.

   buffersize : int, optional
       When buffering is enabled, controls the size of the temporary
       buffers. Set to 0 for the default value.

"""

# notes:
"""
1) row major(C)
  - this row major follows C type order to iterating the array of values in row by row 

2) column major(F)
  - this column major follows F type order to iterating the array of values in column by column
"""

# iterating the method in numpy --> default(C)
x = np.arange(9).reshape(3, 3)
print("the value of x:\n", x)

for i in np.nditer(x):
    print(i, end=" ")
"""
#output:
the value of x:
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
0 1 2 3 4 5 6 7 8 
"""
print(" ")

print("*" * 50)

x = np.arange(1, 10).reshape(3, 3) * (10)
print("the value of x:\n", x)

for i in np.nditer(x, order="C"):  # mentioned as C TYPE ORDER
    print(i, end=" ")
"""
#output:
the value of x:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
10 20 30 40 50 60 70 80 90 
"""
print(" ")

print("*" * 50)

x = np.arange(1, 10).reshape(3, 3) * (10)
print("the value of x:\n", x)

for i in np.nditer(x, order="F"):  # mentioned as F TYPE ORDER or FORTRAN TYPE
    print(i, end=" ")
"""
#output:
the value of x:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
10 40 70 20 50 80 30 60 90 
"""

print(" ")
print("*" * 50)

# transpose --> in numpy
x = np.arange(1, 10).reshape(3, 3) * 10
print(x)

print("*" * 50)

c = x.T
print(c)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
**************************************************
[[10 40 70]
 [20 50 80]
 [30 60 90]]
"""

x = np.arange(1, 10).reshape(3, 3) * 10
print(x)

print("*" * 50)

c = x.transpose()
print(c)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
**************************************************
[[10 40 70]
 [20 50 80]
 [30 60 90]]
"""

# transposed array how react to the iteration method
x = np.arange(1, 10).reshape(3, 3) * 10
print("after shape this array:\n", x)

print("*" * 50)

c = x.transpose()
print("transposed array value:\n", c)

print("*" * 50)

for i in np.nditer(c, order=None):
    print(i, end="  ")
print(" ")
"""
#output:
after shape this array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
**************************************************
transposed array value:
 [[10 40 70]
 [20 50 80]
 [30 60 90]]
**************************************************
10  20  30  40  50  60  70  80  90  
"""

print(" ")

# use np.iternext() to iterate the array of values
x = np.arange(1, 5)
print(x)

print("*" * 50)

c = np.nditer(x)
print(c.iternext())
print(c.iternext())
print(c.iternext())
print(c.iternext())
"""
#output:
[1 2 3 4]
**************************************************
True
True
True
False
"""

# buffered in numpy iterator method in flag
"""
a = np.arange(0,30,5)
print("original array:",a)
print("*"*40)
print("after reshape:")
a = a.reshape(3,2,order="F")

for i in np.nditer(a,op_dtypes=float):
    print(f"value:{i} --> value_type :{type(i)}")

note: 
if we want to change the op_data_type means we use an "buffered" or "copying"
or otherwise output produced as error


#output:
Traceback (most recent call last):
  File "D:\ds\python files|aaa.py", line 258, in <module>
    for i in np.nditer(a,op_dtypes=float):
             ~~~~~~~~~^^^^^^^^^^^^^^^^^^^
TypeError: Iterator operand required copying or buffering, but neither copying nor buffering was enabled
"""

a = np.arange(0, 30, 5)
print("original array:\n", a)
print("*" * 40)
print("after reshape:\n")
a = a.reshape(3, 2, order="F")
print(a)

for i in np.nditer(a, op_dtypes=float, flags=["buffered"]):
    print(f"value:{i} --> value_type :{type(i)}")
"""
#output:
original array:
 [ 0  5 10 15 20 25]
****************************************
after reshape:
[[ 0 15]
 [ 5 20]
 [10 25]]

value:0.0 --> value_type :<class 'numpy.ndarray'>
value:5.0 --> value_type :<class 'numpy.ndarray'>
value:10.0 --> value_type :<class 'numpy.ndarray'>
value:15.0 --> value_type :<class 'numpy.ndarray'>
value:20.0 --> value_type :<class 'numpy.ndarray'>
value:25.0 --> value_type :<class 'numpy.ndarray'>
"""

a = np.arange(0, 30, 5)
print("original array:\n", a)
print("*" * 40)
print("after reshape:")
a = a.reshape(3, 2, order="F")
print(a)

for i in np.nditer(a, op_dtypes=str, flags=["buffered"]):
    print(f"value:{i} --> type_array :{type(i)} --> value_type :{i.dtype}")
"""
#output:
original array:
 [ 0  5 10 15 20 25]
****************************************
after reshape:
[[ 0 15]
 [ 5 20]
 [10 25]]
value:0 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
value:5 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
value:10 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
value:15 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
value:20 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
value:25 --> type_array :<class 'numpy.ndarray'> --> value_type :<U21
"""

"""
*) Example 1 — Write reflect aagum case
import numpy as np

a = np.arange(6).reshape(2, 3)
it = np.nditer(a, flags=['buffered'], op_flags=['readwrite'], op_dtypes=[np.float32])

for x in it:
    x[...] = x * 10   # buffer la value 10x pannura

print("Original array after loop:")
print(a)

Output:
[[ 0 10 20]
 [30 40 50]]


Ithu naama buffer use pannalum,
iteration mudichitu NumPy buffer → original array copy back panniduchu.


*) Example 2 — Read only (no reflection)
a = np.arange(6).reshape(2, 3)
it = np.nditer(a, flags=['buffered'], op_flags=['readonly'], op_dtypes=[np.float32])

for x in it:
    temp = x * 10  # only read, no write

print("Original array after loop:")
print(a)

Output:
[[0 1 2]
 [3 4 5]]

No change — because read-only mode, so buffer copy back panna NumPy illa.
"""

# if we want to make the existing array as to add the new column for that existing array
# method  1:
x = np.arange(10, 100, 10).reshape(3, 3)
print("original array:\n", x)
print("Len of array: ", len(x))
print("dimension of array: ", x.ndim)
n = np.newaxis
print("*" * 50)
c = x[:, n]
print("after the array adding one dimensional:\n", c)
print("Len of array: ", len(c))
print("dimension of array: ", c.ndim)
"""
#output:
original array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
Len of array:  3
dimension of array:  2
**************************************************
after the array adding one dimensional:
 [[[10 20 30]]

 [[40 50 60]]

 [[70 80 90]]]
Len of array:  3
dimension of array:  3
"""

x = np.arange(10, 100, 10).reshape(3, 3)
print("original array:\n", x)
print("Len of array: ", len(x))
print("dimension of array: ", x.ndim)
n = np.newaxis
print("*" * 50)
c = x[:, n, n, n]  # by optional how many dimension we want to mention into the square brackets
print("after the array adding one dimensional:\n", c)
print("Len of array: ", len(c))
print("dimension of array: ", c.ndim)
"""
#output:
original array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
Len of array:  3
dimension of array:  2
**************************************************
after the array adding one dimensional:
 [[[[[10 20 30]]]]



 [[[[40 50 60]]]]



 [[[[70 80 90]]]]]
Len of array:  3
dimension of array:  5
"""

a = np.array([[0, 5, 10], [15, 20, 25], [30, 35, 40]])
print("original value a : \n", a)
for x in np.nditer(op=a, op_flags=["readwrite"]):
    x[...] = 2 * x
print("-----------------------------------------------")
print("after broadcast of array a:\n", a)
"""
#output:
original value a : 
 [[ 0  5 10]
 [15 20 25]
 [30 35 40]]
-----------------------------------------------
after broadcast of array a:
 [[ 0 10 20]
 [30 40 50]
 [60 70 80]]
"""

"""
a = np.array([[0,5,10],[15,20,25],[30,35,40]])
print("original value a : \n",a)
for x in np.nditer(op=a,op_flags=["readonly"]):
    x[...] = 2 * x
print("-----------------------------------------------")
print("after broadcast of array a:\n",a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 515, in <module>
    x[...] = 2 * x
    ~^^^^^
ValueError: assignment destination is read-only
"""

a = np.array([[0, 5, 10], [15, 20, 25], [30, 35, 40]])
print("original value a : \n", a)
for x in np.nditer(op=a, op_flags=["writeonly"]):
    print(x, end=" ")
    x[...] = 2 * x
print("\n-----------------------------------------------")
print("after broadcast of array a:\n", a)
"""
#output:
original value a : 
 [[ 0  5 10]
 [15 20 25]
 [30 35 40]]
0 5 10 15 20 25 30 35 40 
-----------------------------------------------
after broadcast of array a:
 [[ 0 10 20]
 [30 40 50]
 [60 70 80]]
"""

"""
a = np.array([[0,5,10],[15,20,25],[30,35,40]])
print("original value a : \n",a)
for x in np.nditer(op=a,op_flags=["no_broadcast"]):
    print(x,end=" ")
    x[...] = 2 * x
print("\n-----------------------------------------------")
print("after broadcast of array a:\n",a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 559, in <module>
    for x in np.nditer(op=a,op_flags=["no_broadcast"]):
             ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: None of the iterator flags READWRITE, READONLY, or WRITEONLY were specified for an operand
"""

print("-----------------------------------\n")
# flags = external_loop:
"""
The external_loop flag does the following:

 1) converts the 2D or 3D array to 1D individual arrays
 2) transpose the rows and columns if the order is given as F(COL MAJOR) in nditer()
 3) make 1D array if the order is C (ROW MAJOR)
"""

a = np.arange(0, 60, 5).reshape(3, 4)
print("original array:\n", a)

for i in np.nditer(a, flags=["external_loop"]):
    print(i)
print("dimension of array: ", np.ndim(i))
"""
#output:
original array:
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
[ 0  5 10 15 20 25 30 35 40 45 50 55]
dimension of array:  1
"""

a = np.arange(10, 100, 10).reshape(3, 3)
print("original array:\n", a)
print("dimension of array: ", np.ndim(a))
print("length of the array: ", len(a))

for i in np.nditer(a, flags=["external_loop"]):
    print("after use the external loop:\n", i)
    print("dimension of array: ", np.ndim(i))
    print("length of array: ", len(i))
"""
#output:
original array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
dimension of array:  2
length of the array:  3

after use the external loop:
 [10 20 30 40 50 60 70 80 90]
dimension of array:  1
length of array:  9
"""

a = np.arange(10, 100, 10).reshape(3, 3)
print("original array:\n", a)
print("dimension of array: ", np.ndim(a))
print("length of the array: ", len(a))

for i in np.nditer(a, flags=["external_loop"], order="F"):
    print("\nafter use the external loop:\n", i, "")
    print("dimension of array: ", np.ndim(i))
    print("length of array: ", len(i))

"""
note: 
   we use the "order = F" to that iterator so they get the values as column wise in 
   each column as one array by both of the columns have to stored in one array

#output:
original array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
dimension of array:  2
length of the array:  3

after use the external loop:
 [10 40 70]
dimension of array:  1
length of array:  3

after use the external loop:
 [20 50 80]
dimension of array:  1
length of array:  3

after use the external loop:
 [30 60 90]
dimension of array:  1
length of array:  3
"""

a = np.arange(10, 100, 10).reshape(3, 3)
print("original array:\n", a)
print("dimension of array: ", np.ndim(a))
print("length of the array: ", len(a))
print("shape of array: ", np.shape(a))

for i in np.nditer(a, flags=["external_loop"], order="F"):
    print(i)
print("dimension of array: ", np.ndim(i))
print("length of array: ", len(i))
print("shape of array: ", np.shape(i))
"""
#output:
original array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
dimension of array:  2
length of the array:  3
shape of array:  (3, 3)


[10 40 70]
[20 50 80]
[30 60 90]
dimension of array:  1
length of array:  3
shape of array:  (3,)
"""

# broadcasting with iteration
"to make the numeric operation with the use of iterator"

# to use the row major --> "C"
x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
for i, j in np.nditer([x, y], order="C"):
    print(i, j)
"""
#output:
10 1
20 2
30 3
40 1
50 2
60 3
70 1
80 2
90 3
"""

# we use the column major --> "F"
x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
for i, j in np.nditer([x, y], order="F"):
    print(i, j)
"""
#output:
10 1
40 1
70 1
20 2
50 2
80 2
30 3
60 3
90 3
"""

# to make the operation in that iterator method
x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
for i, j in np.nditer([x, y], order="C"):
    print(f"{i} + {j} = {i + j}")
"""
#output:
10 + 1 = 11
20 + 2 = 22
30 + 3 = 33
40 + 1 = 41
50 + 2 = 52
60 + 3 = 63
70 + 1 = 71
80 + 2 = 82
90 + 3 = 93
"""

x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
for i, j in np.nditer([x, y], order="F"):
    print(f"{i} + {j} = {i + j}")
"""
#output:
10 + 1 = 11
40 + 1 = 41
70 + 1 = 71
20 + 2 = 22
50 + 2 = 52
80 + 2 = 82
30 + 3 = 33
60 + 3 = 63
90 + 3 = 93
"""

# multi - array operands
x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
z = np.arange(5, 8).reshape(3)
for i, j, k in np.nditer([x, y, z], order="C"):
    print(f"{i} + {j} + {k} = {i + j + k}")
"""
#output:
10 + 1 + 5 = 16
20 + 2 + 6 = 28
30 + 3 + 7 = 40
40 + 1 + 5 = 46
50 + 2 + 6 = 58
60 + 3 + 7 = 70
70 + 1 + 5 = 76
80 + 2 + 6 = 88
90 + 3 + 7 = 100
"""

x = np.arange(10, 100, 10).reshape(3, 3)
y = np.arange(1, 4)
z = np.arange(5, 8).reshape(3)
for i, j, k in np.nditer([x, y, z], order="F"):
    print(f"{i} + {j} + {k} = {i + j + k}")
"""
#output:
10 + 1 + 5 = 16
40 + 1 + 5 = 46
70 + 1 + 5 = 76
20 + 2 + 6 = 28
50 + 2 + 6 = 58
80 + 2 + 6 = 88
30 + 3 + 7 = 40
60 + 3 + 7 = 70
90 + 3 + 7 = 100
"""

# NumPy - Array Manipulation
"""
several routines / functions are available in Numpy package for
manipulation of elements in ndarray object. they can be classified into
 the following types

   1) reshape
      give a new shape to an array without changing its data

   2) flat
      A (1 - D) iterator over the array

   3) flatten
      returns a copy of the array collapsed into one dimension

    4) ravel
      returns a contiguous flattened array
"""

# reshape()
"""
gives a new shape to an array without changing its data, where resize change
the data based on the dimension input to the constructor.
"""
a = np.arange(12)
print("original array - no reshape\n", a)

print("*" * 50)

b = a.reshape(3, 4)
print("original array - after reshape\n", b)

print("*" * 50)

c = b.reshape(6, 2)
print("original array - after second reshape\n", c)
"""
#output:
original array - no reshape
 [ 0  1  2  3  4  5  6  7  8  9 10 11]

**************************************************
original array - after reshape
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
**************************************************

original array - after second reshape
 [[ 0  1]
 [ 2  3]
 [ 4  5]
 [ 6  7]
 [ 8  9]
 [10 11]]
"""

# flat
"""
numpy.ndarray.flat(this is not a fn)

flat returns an iterator object:
 output: <numpy.flatiter object at 0x0B662328>

def __init__(self, *args:Any, **kwargs:Any) --> None
Flat iterator object to iterate over arrays

A flatiter iterator is returned by X.flat for any array X. it allows iterating 
over the array as if it were a 1-D array, either in a for-loop or by calling its
next() method

Iteration is done i row-major, C-style order(the last index varying the fastest).
the iterator can also be indexed using basic slicing or advanced indexing.

ndarray.flat: return a flat iterator over an array.
ndarray.flatten: returns a flattened copy of an array.

a flatiter iterator can not be constructed directly from 
python code by calling the flatiter constructor.
"""
x = np.arange(10, 100, 10).reshape(3, 3)
print("original_array:\n", x)

f = x.flat
print(f)
print(type(f))
"""
#output:
original_array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
<numpy.flatiter object at 0x000001AA00418C00>
<class 'numpy.flatiter'>
"""

"""
if we are accessing that iterator object by use these kinds of methods:

  1)next
  2)index
  3)for-loop
  4)list
  5)enumerate
  6)slicing cum advanced indexing(both integer and boolean indexing)
"""

# next
print(f.__next__())  # 10
print(f.__next__())  # 20

# index
print(f[0])  # 10
print(f[0:4])  # [10 20 30 40]

# list
print(list(f))
# [np.int64(10), np.int64(20), np.int64(30),
# np.int64(40), np.int64(50), np.int64(60),
# np.int64(70), np.int64(80), np.int64(90)]


# for loop
f = np.arange(10, 100, 10).reshape(3, 3).flat
for i in f:
    print(i, end=" ")
"""
#output:
10 20 30 40 50 60 70 80 90 
"""

# enumerate
f = np.arange(10, 100, 10).reshape(3, 3).flat
for i in enumerate(f):
    print(i)
"""
#output:
(1, np.int64(20))
(2, np.int64(30))
(3, np.int64(40))
(4, np.int64(50))
(5, np.int64(60))
(6, np.int64(70))
(7, np.int64(80))
(8, np.int64(90))
"""

# advance slicing
f = np.arange(10, 100, 10).reshape(3, 3).flat
x = (f[...])
print(x)
print(x[:, np.newaxis])

print("===========================================")

print(x[np.newaxis, :])
"""
#output:
[10 20 30 40 50 60 70 80 90]
[[10]
 [20]
 [30]
 [40]
 [50]
 [60]
 [70]
 [80]
 [90]]
===========================================
[[10 20 30 40 50 60 70 80 90]]
"""

x = np.arange(10, 100, 10).reshape(3, 3)
print("original_array:\n", x)

f = x.flat

f[2] = 1000
print("===========================================")

print(f)

print("===========================================")

print("after modification\n", list(x))
"""
#note:
the original array will be affected

#output:
original_array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
===========================================
<numpy.flatiter object at 0x000002C15F026180>
===========================================
after modification
 [array([  10,   20, 1000]), array([40, 50, 60]), array([70, 80, 90])]
"""

# flatten():
"""
FLATTEN() is a method

return always a copy of the array collapsed into one dimension

ndarray.flatten(order="C")

 *) return a copy of the input array collapsed into one dimension.
 *) A copy of the input array, flattened to one dimension.

parameters:
order{"C","F","A","K"}

return : ndarray 
"""

x = np.arange(10, 100, 10).reshape(3, 3)
print("original_array:\n", x)

f = x.flatten()

f[2] = 1000
print("===========================================")

print(f)

print("===========================================")

print("after modification\n", x)
"""
#output:
original_array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
===========================================
[  10   20 1000   40   50   60   70   80   90]
===========================================
after modification
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
"""

f = x.flatten()
"""
#note:
they produced the result as 1-d array so they will not been give like as flat method by an object 
that's why we dont use the next method 
"""

# index
print(f[0])  # 10
print(f[0:4])  # [10 20 30 40]

# list
print(list(f))
"""
#output:
[np.int64(10), np.int64(20), np.int64(30),
 np.int64(40), np.int64(50), np.int64(60), 
 np.int64(70), np.int64(80), np.int64(90)]
"""

# for loop
f = np.arange(10, 100, 10).reshape(3, 3).flatten()
for i in f:
    print(i, end=" ")
# 10 20 30 40 50 60 70 80 90


print(" ")

# advance slicing
f = np.arange(10, 100, 10).reshape(3, 3).flat
x = (f[...])
print(x)
print(x[:, np.newaxis])

print("===========================================")

print(x[np.newaxis, :])
"""
#output:
[10 20 30 40 50 60 70 80 90]
[[10]
 [20]
 [30]
 [40]
 [50]
 [60]
 [70]
 [80]
 [90]]
===========================================
[[10 20 30 40 50 60 70 80 90]]
"""

# enumerate
f = np.arange(10, 100, 10).reshape(3, 3).flatten()
for i in enumerate(f):
    print(i)
"""
#output:
(0, np.int64(10))
(1, np.int64(20))
(2, np.int64(30))
(3, np.int64(40))
(4, np.int64(50))
(5, np.int64(60))
(6, np.int64(70))
(7, np.int64(80))
(8, np.int64(90))
"""

# numpy.ravel() gives view of an array
"""
the flatten method always returns a copy. if you modify the array 
returned by ravel, it may modify the entries in the original array.

ravel will not been copy. they work with the view method, so original 
array affected after the modification

numpy.ravel(a,order)
"""
x = np.arange(9).reshape([3, 3])
print("before its modification:\n", x)
print("id before modification: ", id(x))

c = x.ravel()
c[4] = 200
print("after use ravel method:\n", c)
print("id of ravel method values: ", id(c))

print("after its modification:\n", x)
print("id after modification", id(x))
"""
#output:
before its modification:
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
id before modification:  2229995524656
after use ravel method:
 [  0   1   2   3 200   5   6   7   8]
id of ravel method values:  2229995524848
after its modification:
 [[  0   1   2]
 [  3 200   5]
 [  6   7   8]]
id after modification 2229995524656
"""

# differnce between these three methods:
"""
flat → Returns an iterator to access/modify elements directly (no copy).

flatten() → Returns a new 1D copy of the array (original not affected).

ravel() → Returns a 1D view if possible, else a copy (modifies original only if view).
"""

# Transpose Operations
"""
 1)transpose
   - permutes the dimensions of an array

 2)ndarray.T
   - same as self.transpose()

 3)rollaxis
   - rolls the specified axis backwards

 4)swapaxis
   - interchanges the two axes of an array
"""

# transpose()
"""
permute: to change the order or arrangement of especially: to arrange in all possible ways.

this functions permutes the dimension of the given array, it returns a view wherever possible.
the function takes the following parameters.

numpy.transpose(arr,axes)
"""

# How to convert vector to 1 or 2 or 3d ndarray.

# use np.atleast_1d()
x = [1, 2, 3]
b = np.atleast_1d(x)
print(b)
print(np.shape(b))
"""
#output:
[1 2 3]
(3,)
"""

# use np.atleast_2d()
x = [1, 2, 3]
b = np.atleast_2d(x)
print(b)
print(np.shape(b))
"""
#output:
[[1 2 3]]
(1, 3)
"""

# use np.atleast_3d()
x = [1, 2, 3]
b = np.atleast_3d(x)
print(b)
print(np.shape(b))
"""
#output:
[[[1]
  [2]
  [3]]]

(1, 3, 1)
"""

"""
note:
using atleast_1d,2d,3d, we can make the higher side not lowerside

Ie, 1d and 2d can become 3d, where as 2d and 3d can not be 1d
conversion between lower dim to higher dim is possible, vice versa is NOT

note:
if we need more than 3d, use np.reshape or np.resize
"""

# using newaxis, 1d ndarray can be converted to 2d array
a = np.array([1, 2, 3])
b = a[:, np.newaxis]
print(b)
print(np.ndim(b))
print(np.shape(b))
"""
#output:
[[1]
 [2]
 [3]]
2
(3, 1)
"""

# transpose
x = np.arange(10, 100, 10).reshape(3, 3)
print(x)
print("*********************************************")
c = x.transpose()
print(c)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
*********************************************
[[10 40 70]
 [20 50 80]
 [30 60 90]]
"""

# ndarray.T
x = np.arange(10, 100, 10).reshape(3, 3)
print(x)
print("*********************************************")
c = x.T
print(c)
"""
#output:
[[10 20 30]
 [40 50 60]
 [70 80 90]]
*********************************************
[[10 40 70]
 [20 50 80]
 [30 60 90]]
"""

x = np.arange(24).reshape(2, 3, 4)
print(x)
print("*********************************************")
y = x.transpose(2, 0, 1)
print(y)
print(np.shape(y))
"""
notes:
# 2  3  4 --> we provided reshape
# 0  1  2 --> we give the number to that values

# 0 --> 2
# 1 --> 3
# 2 --> 4

# if we give the values in transpose as : 2 , 0 , 1
# 2 --> 4
# 0 --> 2
# 1 --> 3

#thats the calculation of changing that axis:
# 4, 2, 3



#output:
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
*********************************************
[[[ 0  4  8]
  [12 16 20]]

 [[ 1  5  9]
  [13 17 21]]

 [[ 2  6 10]
  [14 18 22]]

 [[ 3  7 11]
  [15 19 23]]]

(4, 2, 3)
"""

x = np.arange(24).reshape(1, 2, 4, 3)
print(x)
print("*********************************************")
y = x.transpose(2, 3, 0, 1)  # --> (4,3,1,2)
print(y)
print(np.shape(y))
"""
#output:
[[[[ 0  1  2]
   [ 3  4  5]
   [ 6  7  8]
   [ 9 10 11]]

  [[12 13 14]
   [15 16 17]
   [18 19 20]
   [21 22 23]]]]
*********************************************
[[[[ 0 12]]

  [[ 1 13]]

  [[ 2 14]]]


 [[[ 3 15]]

  [[ 4 16]]

  [[ 5 17]]]


 [[[ 6 18]]

  [[ 7 19]]

  [[ 8 20]]]


 [[[ 9 21]]

  [[10 22]]

  [[11 23]]]]
(4, 3, 1, 2)
"""

# numpy.rollaxis
# becomes moveaxis from version 1.11
"""
moveaxis(a, source, destination)
    Move axes of an array to new positions.

    Other axes remain in their original order.

    Parameters
    ----------
    a : np.ndarray
        The array whose axes should be reordered.

    source : int or sequence of int
        Original positions of the axes to move. These must be unique.

    destination : int or sequence of int
        Destination positions for each of the original axes. These must also be
        unique.
"""
x = np.arange(24).reshape(1, 2, 3, 4)
print(x)
print("*********************************************")
y = np.moveaxis(x, 2, 1)
print(y)
print("before use moveaxis: ", np.shape(x))
print("after use moveaxis: ", np.shape(y))
"""
#output:
[[[[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]]
*********************************************
[[[[ 0  1  2  3]
   [12 13 14 15]]

  [[ 4  5  6  7]
   [16 17 18 19]]

  [[ 8  9 10 11]
   [20 21 22 23]]]]
before use moveaxis:  (1, 2, 3, 4)
after use moveaxis:  (1, 3, 2, 4)
"""

x = np.arange(24).reshape(1, 2, 3, 4)
print(x)
print("*********************************************")
y = np.moveaxis(x, 2, 0)
print(y)
print("before use moveaxis: ", np.shape(x))
print("after use moveaxis: ", np.shape(y))
"""
#output:
)
[[[[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]]
*********************************************
[[[[ 0  1  2  3]
   [12 13 14 15]]]


 [[[ 4  5  6  7]
   [16 17 18 19]]]


 [[[ 8  9 10 11]
   [20 21 22 23]]]]
before use moveaxis:  (1, 2, 3, 4)
after use moveaxis:  (3, 1, 2, 4)
"""

x = np.arange(24).reshape(1, 2, 3, 4)
print(x)
print("*********************************************")
y = np.moveaxis(x, 1, 3)
print(y)
print("before use moveaxis: ", np.shape(x))
print("after use moveaxis: ", np.shape(y))
"""
#output:
[[[[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]]

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]]]]
*********************************************
[[[[ 0 12]
   [ 1 13]
   [ 2 14]
   [ 3 15]]

  [[ 4 16]
   [ 5 17]
   [ 6 18]
   [ 7 19]]

  [[ 8 20]
   [ 9 21]
   [10 22]
   [11 23]]]]
before use moveaxis:  (1, 2, 3, 4)
after use moveaxis:  (1, 3, 4, 2)
"""

"""
x = np.arange(24).reshape(2,3,4)
print(x)
print("*********************************************")
y = np.moveaxis(x,2) #BY DEFAULT 0 --> DESTINATION
print(y)
print("before use moveaxis: ",np.shape(x))
print("after use moveaxis: ",np.shape(y))
#output:
Traceback (most recent call last):
  File "D:\ds\python filesaaa.py", line 378, in <module>
    y = np.moveaxis(x,2) #BY DEFAULT 0 --> DESTINATION
TypeError: moveaxis() missing 1 required positional argument: 'destination'
"""

x = np.arange(24).reshape(2, 3, 4)
print(x)
print("*********************************************")
# BY DEFAULT 0 --> DESTINATION
print(np.rollaxis(x, 2))
print("before use moveaxis: ", np.shape(x))
print("after use moveaxis: ", np.shape(np.rollaxis(x, 2)))
"""
#output:
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
*********************************************
[[[ 0  4  8]
  [12 16 20]]

 [[ 1  5  9]
  [13 17 21]]

 [[ 2  6 10]
  [14 18 22]]

 [[ 3  7 11]
  [15 19 23]]]
before use moveaxis:  (2, 3, 4)
after use moveaxis:  (4, 2, 3)
"""

x = np.arange(24).reshape(2, 3, 4)
print(x)
print("*********************************************")
# BY DEFAULT 0 --> DESTINATION
y = np.rollaxis(x, 1)  # by default 0 is the destination
print("before use moveaxis: ", np.shape(x))
print("after use moveaxis: ", np.shape(y))
"""
#output:
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
*********************************************
before use moveaxis:  (2, 3, 4)
after use moveaxis:  (3, 2, 4)
"""

"""
notes:
both of the rollaxis and moveaxis will be same
but the moveaxis to given the whole parameter. but the rollaxis will be 
taken as 0 as the destination in default.
"""





a = np.arange(1,25).reshape(1,2,3,4)
print(a)
print(a.shape)
print("======================================")

b = np.swapaxes(a,axis1=3,axis2=1)
print(b)
print(b.shape)
"""
#output:
[[[[ 1  2  3  4]
   [ 5  6  7  8]
   [ 9 10 11 12]]

  [[13 14 15 16]
   [17 18 19 20]
   [21 22 23 24]]]]
(1, 2, 3, 4)
======================================
[[[[ 1 13]
   [ 5 17]
   [ 9 21]]

  [[ 2 14]
   [ 6 18]
   [10 22]]

  [[ 3 15]
   [ 7 19]
   [11 23]]

  [[ 4 16]
   [ 8 20]
   [12 24]]]]
(1, 4, 3, 2)
"""



a = np.arange(1,9).reshape(2,2,2)
print(a)
print(a.shape)
print("======================================")

b = np.swapaxes(a,axis1=2,axis2=0)
print(b)
print(b.shape)
"""
#notes:
values will be changed as opposite or transpose

#output:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
(2, 2, 2)
======================================
[[[1 5]
  [3 7]]

 [[2 6]
  [4 8]]]
(2, 2, 2)
"""



a = np.arange(1,25).reshape(2,3,4)
print(a)
print(a.shape)
print("======================================")

b = np.swapaxes(a,axis1=2,axis2=0)
print(b)
print(b.shape)
"""
#output:
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]

 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]
(2, 3, 4)
======================================
[[[ 1 13]
  [ 5 17]
  [ 9 21]]

 [[ 2 14]
  [ 6 18]
  [10 22]]

 [[ 3 15]
  [ 7 19]
  [11 23]]

 [[ 4 16]
  [ 8 20]
  [12 24]]]
(4, 3, 2)
"""


"""
#what are the difference between rollaxis and swapaxis

  swapaxis: to exchange only 2 axis in the array
  rollaxis: any number of axis can be switched places in the array
"""


#numpy.broadcast()
"""
this shows the mapping between elements of the arrays that are
involving in broadcasting process

produces an object that mimics broadcasting

as seen earlier, numpy has in-build support for broadcasting. this function mimics/
impersonate/copy the broadcasting mechanism. it returns an object that encapsulates
the result of broadcasting one array against the other

the function takes two arrays ans input parameters. following example illustrates its use.
"""

x = np.array([[1],[2],[3]] ,dtype= "O")
y = np.array([4,5,6],dtype = "O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

#to broadcast x against y
b = np.broadcast(x,y) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

print("adding the two array")
b = np.broadcast(x+y) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

print("multiple the two array")
b = np.broadcast(x*y) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

print("by using to multiple operand inside the broadcast")
b = np.broadcast(x*y+x) #(y,x) also possible
print(b)
print(list(b))


print("------------------------------------------------")

print("by using to multiple operand inside the broadcast")
b = np.broadcast(x*y-10) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
[[1]
 [2]
 [3]]
2
(3, 1)
------------------------------------------------
Y ARRAY
[4 5 6]
1
(3,)
------------------------------------------------
<numpy.broadcast object at 0x00000266A2D54B40>
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
------------------------------------------------
adding the two array
<numpy.broadcast object at 0x00000266A2D55840>
[(5,), (6,), (7,), (6,), (7,), (8,), (7,), (8,), (9,)]
------------------------------------------------
multiple the two array
<numpy.broadcast object at 0x00000266A2D55B80>
[(4,), (5,), (6,), (8,), (10,), (12,), (12,), (15,), (18,)]
------------------------------------------------
by using to multiple operand inside the broadcast
<numpy.broadcast object at 0x00000266A2D56200>
[(5,), (6,), (7,), (10,), (12,), (14,), (15,), (18,), (21,)]
------------------------------------------------
by using to multiple operand inside the broadcast
<numpy.broadcast object at 0x00000266A2D54B40>
[(-6,), (-5,), (-4,), (-2,), (0,), (2,), (2,), (5,), (8,)]
"""



x = np.array([[1],[2],[3]] ,dtype= "O")
y = np.array([4,5,6],dtype = "O")
z = np.array([3,2,1],dtype= "O")
print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

print("Z ARRAY")
print(z)
print(z.ndim)
print(z.shape)

print("------------------------------------------------")

#to broadcast x against y ,z
b = np.broadcast(x,y,z) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

print("adding the two array")
b = np.broadcast(x+y+z) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
[[1]
 [2]
 [3]]
2
(3, 1)
------------------------------------------------
Y ARRAY
[4 5 6]
1
(3,)
------------------------------------------------
Z ARRAY
[3 2 1]
1
(3,)
------------------------------------------------
<numpy.broadcast object at 0x000001B7EE916980>
[(1, 4, 3), (1, 5, 2), (1, 6, 1), (2, 4, 3), (2, 5, 2), (2, 6, 1), (3, 4, 3), (3, 5, 2), (3, 6, 1)]
------------------------------------------------
adding the two array
<numpy.broadcast object at 0x000001B7EE90FB80>
[(8,), (8,), (8,), (9,), (9,), (9,), (10,), (10,), (10,)]
"""



#by using broadcasting into STRING
x = np.array(list("SANTHOSH") ,dtype= "O")
y = np.array(list("santhosh"),dtype = "O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

#to broadcast x against y
b = np.broadcast(x,y) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

#to concatenate
b = np.broadcast(x+y) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

#to multiplication into the broadcasting
b = np.broadcast(x*5) #(y,x) also possible
print(b)
print(list(b))

print("------------------------------------------------")

#to multiplication into the broadcasting
b = np.broadcast(x*5+y) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
['S' 'A' 'N' 'T' 'H' 'O' 'S' 'H']
1
(8,)
------------------------------------------------
Y ARRAY
['s' 'a' 'n' 't' 'h' 'o' 's' 'h']
1
(8,)
------------------------------------------------
<numpy.broadcast object at 0x00000217B77903B0>
[('S', 's'), ('A', 'a'), ('N', 'n'), ('T', 't'), ('H', 'h'), ('O', 'o'), ('S', 's'), ('H', 'h')]
------------------------------------------------
<numpy.broadcast object at 0x00000217B778F6B0>
[('Ss',), ('Aa',), ('Nn',), ('Tt',), ('Hh',), ('Oo',), ('Ss',), ('Hh',)]
------------------------------------------------
<numpy.broadcast object at 0x00000217B778F9F0>
[('SSSSS',), ('AAAAA',), ('NNNNN',), ('TTTTT',), ('HHHHH',), ('OOOOO',), ('SSSSS',), ('HHHHH',)]
------------------------------------------------
<numpy.broadcast object at 0x00000217B778F6B0>
[('SSSSSs',), ('AAAAAa',), ('NNNNNn',), ('TTTTTt',), ('HHHHHh',), ('OOOOOo',), ('SSSSSs',), ('HHHHHh',)]
"""


#if they will not list of values,so it decided as whole value as one
x = np.array("SANTHOSH" ,dtype= "O")
y = np.array("santhosh",dtype = "O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

#to broadcast x against y
b = np.broadcast(x,y) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
SANTHOSH
0
()
------------------------------------------------
Y ARRAY
santhosh
0
()
------------------------------------------------
<numpy.broadcast object at 0x00000221695D4720>
[('SANTHOSH', 'santhosh')]
"""




x = np.array(list([1,2,3,4,5,6,7]) ,dtype= "O")
y = np.array("santhosh",dtype = "O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

#to broadcast x against y
b = np.broadcast(x,y) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
[1 2 3 4 5 6 7]
1
(7,)
------------------------------------------------
Y ARRAY
santhosh
0
()
------------------------------------------------
<numpy.broadcast object at 0x00000154D292CEC0>
[(1, 'santhosh'), (2, 'santhosh'), (3, 'santhosh'), (4, 'santhosh'), (5, 'santhosh'), (6, 'santhosh'), (7, 'santhosh')]
"""




x = np.array(list([1,2,]) ,dtype= float)
y = np.array(list([7,6,]),dtype = float)

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

#to broadcast x against y
b = np.broadcast(np.sin(x),np.cos(y)) #(y,x) also possible
print(b)
print(list(b))
"""
#output:
X ARRAY
[1. 2.]
1
(2,)
------------------------------------------------
Y ARRAY
[7. 6.]
1
(2,)
------------------------------------------------
<numpy.broadcast object at 0x000001DBD94137B0>
[(np.float64(0.8414709848078965), np.float64(0.7539022543433046)), (np.float64(0.9092974268256817), np.float64(0.960170286650366))]
"""



#by using comprehension into the broadcast
x = np.array([1,2,3],dtype="O")
y = np.array([7,6,5],dtype="O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

b = np.broadcast(x,y) #(y,x) also possible

x = (list(b))
c = [(item1+item2) for item1, item2 in x] #(y,x) also possible
print(c)
"""
#output:
X ARRAY
[1 2 3]
1
(3,)
------------------------------------------------
Y ARRAY
[7 6 5]
1
(3,)
------------------------------------------------
[8, 8, 8]
"""








x = np.array([1,2,3],dtype="O")
y = np.array([7,6,5],dtype="O")

print("X ARRAY")
print(x)
print(x.ndim)
print(x.shape)

print("------------------------------------------------")

print("Y ARRAY")
print(y)
print(y.ndim)
print(y.shape)

print("------------------------------------------------")

b = np.broadcast(x,y) #(y,x) also possible
print(b)
print(b.shape)

print("------------------------------------------------------")

print("broadcast object index: ",b.index)
print("broadcast object iter: ",b.iters)
print("broadcast object nd: ",b.nd)
print("broadcast object numiter: ",b.numiter)
print("broadcast object ndim: ",b.ndim)
print("broadcast object size: ",b.size)
"""
#output:
X ARRAY
[1 2 3]
1
(3,)
------------------------------------------------
Y ARRAY
[7 6 5]
1
(3,)
------------------------------------------------
<numpy.broadcast object at 0x00000270AFEFB430>
(3,)
------------------------------------------------------
broadcast object index:  0
broadcast object iter:  (<numpy.flatiter object at 0x00000270AFD54E00>, <numpy.flatiter object at 0x00000270AFD452B0>)
broadcast object nd:  1
broadcast object numiter:  2
broadcast object ndim:  1
broadcast object size:  3
"""




#expand_dims()
"""
if we want to expand the dimension as 1. we use the expend dimension
"""
x = np.arange(18).reshape(3,2,3)
print(x)
print("shape X: ",x.shape)
print("len X: ", len(x))

print("-------------------------------------------")
print("axis0")
y = np.expand_dims(x,axis=0)
print(y)
print("shape Y: ",y.shape)
print("len Y: ", len(y))

print("-------------------------------------------")
print("axis1")
y = np.expand_dims(x,axis=1)
print(y)
print("shape Y: ",y.shape)
print("len Y: ", len(y))


print("-------------------------------------------")
print("axis2")
y = np.expand_dims(x,axis=2)
print(y)
print("shape Y: ",y.shape)
print("len Y: ", len(y))

print("-------------------------------------------")
print("axis3")
y = np.expand_dims(x,axis=3)
print(y)
print("shape Y: ",y.shape)
print("len Y: ", len(y))
"""
#note:
if the axis above the count of shape means they produced as the result as error


#output:
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]]]
shape X:  (3, 2, 3)
len X:  3
-------------------------------------------
axis0
[[[[ 0  1  2]
   [ 3  4  5]]

  [[ 6  7  8]
   [ 9 10 11]]

  [[12 13 14]
   [15 16 17]]]]
shape Y:  (1, 3, 2, 3)
len Y:  1
-------------------------------------------
axis1
[[[[ 0  1  2]
   [ 3  4  5]]]


 [[[ 6  7  8]
   [ 9 10 11]]]


 [[[12 13 14]
   [15 16 17]]]]
shape Y:  (3, 1, 2, 3)
len Y:  3
-------------------------------------------
axis2
[[[[ 0  1  2]]

  [[ 3  4  5]]]


 [[[ 6  7  8]]

  [[ 9 10 11]]]


 [[[12 13 14]]

  [[15 16 17]]]]
shape Y:  (3, 2, 1, 3)
len Y:  3
-------------------------------------------
axis3
[[[[ 0]
   [ 1]
   [ 2]]

  [[ 3]
   [ 4]
   [ 5]]]


 [[[ 6]
   [ 7]
   [ 8]]

  [[ 9]
   [10]
   [11]]]


 [[[12]
   [13]
   [14]]

  [[15]
   [16]
   [17]]]]
shape Y:  (3, 2, 3, 1)
len Y:  3
"""



#np.squeeze()
"""
to remove the 1 into the shape
"""
x = np.arange(18).reshape(1,1,3,1,2,3)
print(x)
print("shape X: ",x.shape)
print("len X: ", len(x))

print("----------------------------------------")
print("after using squeeze method")
y = np.squeeze(x)
print(y)
print("shape X: ",y.shape)
print("len X: ", len(y))
"""
#output:
[[[[[[ 0  1  2]
     [ 3  4  5]]]


   [[[ 6  7  8]
     [ 9 10 11]]]


   [[[12 13 14]
     [15 16 17]]]]]]
shape X:  (1, 1, 3, 1, 2, 3)
len X:  1
----------------------------------------
after using squeeze method
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]]]
shape X:  (3, 2, 3)
len X:  3
"""




#using axis in squeeze
x = np.arange(18).reshape(1,1,3,1,2,3)
print(x)
print("shape X: ",x.shape)
print("len X: ", len(x))

print("----------------------------------------")
print("after using squeeze method")
y = np.squeeze(x,axis=3)
print(y)
print("shape X: ",y.shape)
print("len X: ", len(y))
"""
#note:
if the axis denoted place these is no 1 in that place they will produced as error

#output:
[[[[[[ 0  1  2]
     [ 3  4  5]]]


   [[[ 6  7  8]
     [ 9 10 11]]]


   [[[12 13 14]
     [15 16 17]]]]]]
shape X:  (1, 1, 3, 1, 2, 3)
len X:  1
----------------------------------------
after using squeeze method
[[[[[ 0  1  2]
    [ 3  4  5]]

   [[ 6  7  8]
    [ 9 10 11]]

   [[12 13 14]
    [15 16 17]]]]]
shape X:  (1, 1, 3, 2, 3)
len X:  1
"""



#np.hstack()
x = np.array([   [1,2,3],
                [10,20,30]  ])

y = np.array([   [4,5,6],
                [40,50,60]  ])

z = np.array([    [7,8,9],
                 [70,80,90]  ])
c = np.hstack((x,y,z))
print(c)
"""
#output:
[[ 1  2  3  4  5  6  7  8  9]
 [10 20 30 40 50 60 70 80 90]]
"""



#np.vstack()
x = np.array([   [1,2,3],
                [10,20,30]  ])

y = np.array([   [4,5,6],
                [40,50,60]  ])

z = np.array([    [7,8,9],
                 [70,80,90]  ])
c = np.vstack((x,y,z))
print(c)
"""
#output:
[[ 1  2  3]
 [10 20 30]
 [ 4  5  6]
 [40 50 60]
 [ 7  8  9]
 [70 80 90]]
"""

"""
note:
if we use the both v&h stack in every array have same dimension. that will not
run properly they produced as error
"""


#Numpy - String Functions
"""
these functions are available in numpy.char

the following functions are used to perform vectorized string operation
for arrays od dtype numpy.string or numpy.unicode.

they are based on the standard string functions in python's build-in library.
"""
#numpy.char.add
first_name = np.array(["santhosh","ram","vignesh","raju"],dtype=str)
last_name = np.array(["kumar","manoj","babu","manoj"],dtype=str)
full_name = np.char.add(first_name,last_name)
print(full_name)
#['santhoshkumar' 'rammanoj' 'vigneshbabu' 'rajumanoj']



#np.char.multiply
x = np.array(["santhosh","ram","vignesh","raju"],dtype=str)
z = np.char.multiply(x,3)
print(z)
"""
#output:
['santhoshsanthoshsanthosh' 'ramramram' 'vigneshvigneshvignesh'
 'rajurajuraju']
"""


#numpy.char.center()
b = np.char.center("santhosh",20,fillchar="*")
print(b)
#******santhosh******


b = np.char.center("santhosh",50)
print(b)
"""
note:
default fillchar is spaces

#output:
                     santhosh                     
"""



#np.char.join()
first_name = np.array(["santhosh","ram","vignesh","raju"],dtype=str,ndmin=2)
last_name = np.array(["kumar","manoj","babu","manoj"],dtype=str)
full_name = np.char.add(first_name,last_name)
print(full_name)
print("================================================================================")

x = np.char.join("**",full_name)
print(x)
"""
#output
[['santhoshkumar' 'rammanoj' 'vigneshbabu' 'rajumanoj']]
================================================================================
[['s**a**n**t**h**o**s**h**k**u**m**a**r' 'r**a**m**m**a**n**o**j'
  'v**i**g**n**e**s**h**b**a**b**u' 'r**a**j**u**m**a**n**o**j']]
"""



#np.char.capitalize
x = np.char.capitalize("santhosh kumar")
print(x)
#Santhosh kumar


#np.char.title
x = np.char.title("santhosh kumar")
print(x)
#Santhosh Kumar


#np.char.swapcase
x = np.char.swapcase("santhosh KUMAR")
print(x)
#SANTHOSH kumar




#np.char.split()
b = "santhosh kumar lived in dgl"


print(np.char.split(b,"t"))
#['san', 'hosh kumar lived in dgl']

print(np.char.split(b,"h"))
#['sant', 'os', ' kumar lived in dgl']


print(np.char.split(b," "))
#['santhosh', 'kumar', 'lived', 'in', 'dgl']


print(np.char.split(b)) #by default space
#['santhosh', 'kumar', 'lived', 'in', 'dgl']


print(np.char.split(b,"kumar"))
#['santhosh ', ' lived in dgl']




#np.char.decode() and np.char.encode()
a = np.char.encode("santhosh","cp500")
print(a)

a = np.char.decode(a,"cp500")
print(a)

"""
#output:
np.bytes_(b'\xa2\x81\x95\xa3\x88\x96\xa2\x88')
santhosh
"""


"""
a = np.char.encode("santhosh","cp500")
print(a)

a = np.char.decode(a,"hz")
print(a)

#output:
Traceback (most recent call last):
  File "D:\ds\python files\aaa.py", line 972, in <module>
    a = np.char.decode(a,"hz")
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python313\Lib\site-packages\numpy\_core\strings.py", line 596, in decode
    _vec_string(a, np.object_, 'decode', _clean_args(encoding, errors)),
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'hz' codec can't decode byte 0xa2 in position 0: illegal multibyte sequence
decoding with 'hz' codec failed
"""






#Numpy - Mathematical Functions
"""
quite understandably, Numpy contains a large number of various 
mathematical operations. Numpy provides standard trigonometric
functions, functions for arithmetic operations, handling complex numbers, etc
"""

#np.sin,cos,tan
a = np.array([0,30,40,60,90])
print("sin values of a\n",np.sin(a))

print("--------------------------------------------------------")

print("cos values of a\n",np.cos(a))

print("--------------------------------------------------------")

print("tan values of a\n",np.tan(a))
"""
#output:
sin values of a
 [ 0.         -0.98803162  0.74511316 -0.30481062  0.89399666]
--------------------------------------------------------
cos values of a
 [ 1.          0.15425145 -0.66693806 -0.95241298 -0.44807362]
--------------------------------------------------------
tan values of a
 [ 0.         -6.4053312  -1.11721493  0.32004039 -1.99520041]
"""



#FUNCTIONS FOR ROUNDING
"""
#numpy.around()
 this is a function that returns the value rounded to the desired precision.
the function takes the following parameters

np.around(a,decimals)
"""

a = np.array([0,36.5,40.6,6.60,90.7])
print(np.around(a))
#[ 0. 36. 41.  7. 91.]


a = np.array([1.6,2.2,6.4,7.7])
print(np.around(a))
#[2. 2. 6. 8.]



#by using decimal as
a = np.array([1.6,2.2,6.4,17.7]) #the precision is make decimals
print(np.around(a,decimals=1))
#[ 1.6  2.2  6.4 17.7]



a = np.array([1.6,2.2,6.4,17.7]) #the precision is make 1/10
print(np.around(a,decimals=-1))
#[ 0.  0. 10. 20.]


a = np.array([1.6,2.2,60.4,177.7]) #the precision is make 1/100
print(np.around(a,decimals=-2))
#[  0.   0. 100. 200.]


a = np.array([1.6,52.2,560.4,1777.7]) #the precision is make 1/1000
print(np.around(a,decimals=-3))
#[   0.    0. 1000. 2000.]


a = np.array([1.6,52.2,5560.4,17777.7]) #the precision is make 1/10000
print(np.around(a,decimals=-4))
#[    0.     0. 10000. 20000.]



#np.floor()
"""
this function returns the largest integer not greater than the input parameter.
the floor of the scalar x is the largest integer i, such that i<=x. note that in python,
flooring always is rounded away from 0.
"""

a = np.array([-1.2,-2.7,0.6,3.6,4.4])
print(np.floor(a))
#[-2. -3.  0.  3.  4.]


a = np.array([-1.2,-2.7,-0.6,-3.6,-4.4])
print(np.floor(a))
#[-2. -3. -1. -4. -5.]




#numpy.ceil()
"""
the ceil() function returns the ceiling of an input value, the ceil of the
scalar x is the smallest integer i, such that i>=x
"""
a = np.array([-1.2,-2.7,0.6,3.6,4.4])
print(np.ceil(a))
#[-1. -2.  1.  4.  5.]


a = np.array([-1.2,-2.7,-0.6,-3.6,-4.4])
print(np.ceil(a))
#[-1. -2. -0. -3. -4.]



#Numpy - Arithemetic Operations
"""
Input arrays for performing arithmetic operations such as
add(),subtract(),multiply(), and division()  must be either 
of the same shape or should comform to array broadcasting rules.
"""
a = np.arange(10,100,10).reshape(3,3)
b = np.arange(1,10).reshape(3,3)

print("a value: \n",a)
print("b value: \n",b)
print("------------------------------------------------------------")

print("numpy_add:\n",np.add(a,b))

print("----------------------------------------------------------------")

print("numpy_subtract:\n",np.subtract(a,b))

print("----------------------------------------------------------------")

print("numpy_multiply:\n",np.multiply(a,b))

print("----------------------------------------------------------------")

print("numpy_divide:\n",np.divide(a,b))

print("----------------------------------------------------------------")
"""
#output:
a value: 
 [[10 20 30]
 [40 50 60]
 [70 80 90]]
b value: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
------------------------------------------------------------
numpy_add:
 [[11 22 33]
 [44 55 66]
 [77 88 99]]
----------------------------------------------------------------
numpy_subtract:
 [[ 9 18 27]
 [36 45 54]
 [63 72 81]]
----------------------------------------------------------------
numpy_multiply:
 [[ 10  40  90]
 [160 250 360]
 [490 640 810]]
----------------------------------------------------------------
numpy_divide:
 [[10. 10. 10.]
 [10. 10. 10.]
 [10. 10. 10.]]
----------------------------------------------------------------
"""





#reciprocal
"""
reciprocal is the division value of 1 by given values
"""
a = np.array([1,2,3,4,5,6],dtype=float)
c = np.reciprocal(a)
print(c)
#[1.         0.5        0.33333333   0.25       0.2        0.16666667]



a = np.array([3,4,5,6,7],dtype=float)
c = np.reciprocal(a)
print(c)
#[0.33333333   0.25       0.2        0.16666667    0.14285714]



#numpy.power()
"""
this function treats elements in the first input array as base and returns it raised to the 
power of the corresponding elements in the second input array
"""
a = np.array([1,2,3,4,5,6])

print("our array is: ", a)
print("----------------------------------------------")
print("powered the values after the array")

print(np.power(a,2))
print(np.power(a,3))
print(np.power(a,4))
"""
#output:
our array is:  [1 2 3 4 5 6]
----------------------------------------------
powered the values after the array
[ 1  4  9 16 25 36]
[  1   8  27  64 125 216]
[   1   16   81  256  625 1296]
"""


#to power the value a to b values
a = np.array([1,2,3,4,5,6])
b = np.array([10,20,30,40,50,60])

print(np.power(b,a))
#[         10         400       27000     2560000   312500000 46656000000]



#numpy.mod()
"""
this function returns the remainder of division of the corresponding elements in the input array.
the function numpy.remainder() also produces the same result.
"""
a = np.array([1,2,3,4,5,6])

print("our array is: ", a)
print("----------------------------------------------")
print("mod of the values after the array")

print(np.mod(a,2))
print(np.mod(a,3))
"""
#our array is:  [1 2 3 4 5 6]
----------------------------------------------
mod of the values after the array
[1 0 1 0 1 0]
[1 2 0 1 2 0]
"""



#to mod the value a to b values
a = np.array([1,2,3,4,5,6])
b = np.array([15,24,33,45,20,33])

print(np.mod(b,a))
#[0 0 0 1 0 3]



"""
the following functions are used to perform operations on array with 
complex numbers.

numpy.real() - returns the real part of the complex data type argument.
numpy.imag() - returns the imaginary part of the complex data type argument.
numpy.conj() - returns the complex conjugate, which is obtained by changing the sign of 
               the imaginary part
numpy.angle() - returns the angle of the complex argument. the function has degree parameter.
                if true, the angle in the degree is returned, otherwise the angle is in radians.
"""



#numpy.statistical methods
"""
numpy.amin() and numpy,amax() using axis()
 these functions returns the minimum and the maximum from the element
 in the given array along the specified axis 
"""
a = np.arange(1,10).reshape(3,3)
print("original array: \n",a)

print("-------------------------------------------------------")

#amin()
print(np.amin(a,1))#row = 1
#[1 4 7]

print(np.amin(a,0))#column = 0
#[1 2 3]

print(np.amin(a))
#1



#amax()
print(np.amax(a,1))#row = 1
#[3 6 9]

print(np.amax(a,0))#column = 0
#[7 8 9]

print(np.amax(a))
#9




#find range (peak to peak(max value - min value))
"""
#numpy.ptp()
the numpy.ptp() function returns the range(maximum - minimum) of values
along an axis
"""
a = np.arange(1,10).reshape(3,3)
print("original array: \n",a)

print("-------------------------------------------------------")

print(np.ptp(a,1))#row


print(np.ptp(a,0))#column
"""
original array: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
-------------------------------------------------------
[2 2 2]
[6 6 6]
"""



#numpy.percentile()
a = np.arange(1,10).reshape(3,3)
print(np.percentile(a,50))
#5.0


x = np.array([22,15,3,7,13,19])
print(np.percentile(x,15))
#6.0




#median
x = np.array([22,15,3,7,13,19])
print(np.median(x))
#14.0



a = np.arange(1,10).reshape(3,3)
print("original matrix: \n",a)
print("--------------------------------------------------")

print(np.median(a,1))#row

print(np.median(a,0))#column
"""
#output:
#original matrix: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
--------------------------------------------------
[2. 5. 8.]
[4. 5. 6.]
"""

#or

a = np.arange(1,10).reshape(3,3)
print("original matrix: \n",a)
print("--------------------------------------------------")

print(np.average(a,1))#row

print(np.average(a,0))#column
"""
#output:
original matrix: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
--------------------------------------------------
[2. 5. 8.]
[4. 5. 6.]
"""
-------------------------------------------------------------doubt
#this average should calculated weighted average also
a = np.array([10,10,10,10,10])
print("original matrix: \n",a)

print("--------------------------------------------------")
x = [1,1,1,2,3]
print(x)
print(np.average(a,weights=x))
#
# print(np.average(a,0))#column

# print(help(np.average))




























































































