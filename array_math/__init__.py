__all__ = ["linalg"]

from array_math import *

import math

class array():
    def __init__(self, a_list, param_range_limit=(-100000,100000)):
        if len(a_list) > 0:
            if type(a_list[0]) == array and type(a_list) == array:
                self.list = [x.list for x in a_list.list]
            elif type(a_list[0]) == array and type(a_list) == list:
                self.list = [x.list for x in a_list]
            elif type(a_list) == array:
                self.list = a_list.list
            elif type(a_list[0]) == list or type(a_list[0]) == int or type(a_list[0]) == float:
                self.list = a_list
        else:
            self.list = []
    def __len__(self):
        return len(self.list)
    def __str__(self):
        if len(self.list) > 0 and type(self.list[0]) == list:
            final_str = "["
            for ls in self.list:
                final_str += str(ls) + "\n"
            final_str += "]"
            return final_str
        else:
            return str(self.list)

    def __getitem__(self,key):
        if type(key) == int:
            if type(self.list[key]) == list:
                return array(self.list[key])
            else:
                return self.list[key]
        elif type(key) == slice:
            return array(self.list[key.start:key.stop:key.step])
        elif type(key) == tuple:
            return array([x[key[1].start:key[1].stop:key[1].step] for x in self.list[key[0].start:key[0].stop:key[0].step]])


    def min(self,axis):
        if axis == 0 and type(self.list[0]) == list:
            return array([min(x) for x in zip(*self.list)])

    def max(self,axis):
        if axis == 0 and type(self.list[0]) == list:
            return array([max(x) for x in zip(*self.list)])

    def __add__(self, other):
        if len(self.list) > 0 and type(self.list[0]) == list:
            pass
        elif len(self) == len(other):
            if type(other) == list:
                return array([self.list[i] + other[i] for i in range(0, len(self))])    
            else:
                return array([self.list[i] + other.list[i] for i in range(0, len(self))])
   
    def __sub__(self, other):
        if len(self.list) > 0 and type(self.list[0]) == list:
            pass
        elif len(self) == len(other):
            if type(other) == list:
                return array([self.list[i] - other[i] for i in range(0, len(self))])    
            else:
                return array([self.list[i] - other.list[i] for i in range(0, len(self))])
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return array([self.list[i] * other for i in range(0, len(self))])
        elif type(other) == array:
            zip_b = list(zip(*other.list))
            return array([[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
                 for col_b in zip_b] for row_a in self.list])

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return array([self.list[i] * other for i in range(0, len(self))])

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return array([self.list[i] / other for i in range(0, len(self))])
        
           

pi = math.pi
uint8 = (0,255)

def arctan2(x, y):
    return math.arctan2(x,y)

def sin(val):
    return math.sin(val)

def cos(val):
    return math.cos(val)

def dotMat(a,b):
    zip_b = list(zip(*b))
    return array([[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a])

def dot_list(a,b):
    if (type(a[0]) == list or type(a[0]) == tuple) and (type(b[0]) == list or type(b[0]) == tuple):
        return dotMat(a,b)
    else:
        return sum([i*j for (i, j) in zip(a, b)])

def dot(a_array,b_array):
    if type(b_array) == list and type(a_array) == list:
        return dot_list(a_array,b_array)
    elif type(b_array) == list:
        return dot_list(a_array.list,b_array)
    elif type(a_array) == list:
        return dot_list(a_array,b_array.list)
    else:
        return dot_list(a_array.list,b_array.list)

def cross(a_array,b_array):
    return array([a_array.list[1]*b_array.list[2] - a_array.list[2]*b_array.list[1],
         a_array.list[2]*b_array.list[0] - a_array.list[0]*b_array.list[2],
         a_array.list[0]*b_array.list[1] - a_array.list[1]*b_array.list[0]])


def zeros(dimensions):
    return array([[0 for x in range(0,dimensions[1])] for y in range(0,dimensions[0]) ])

def ones(dimensions):
    return array([[1.0 for x in range(0,dimensions[1])] for y in range(0,dimensions[0]) ])

def vstack_list(a,b):
    return a + b

def vstack(pair):
    list1 = pair[0]
    list2 = pair[1]
    if type(pair[0]) != list:
        list1 = list1.list
    if type(pair[1]) != list:
        list2 = list2.list
    return array(vstack_list(list1,list2))

def hstack_list(a,b):
    if type(a[0]) == list and type(b[0]) == list:
        if len(a) == len(b):
            for i in range(0,len(a)):
                a[i].append(b[i][0])
    return a
                
def hstack(pair):
    list1 = pair[0]
    list2 = pair[1]
    if type(pair[0]) != list:
        list1 = list1.list
    if type(pair[1]) != list:
        list2 = list2.list
    return array(hstack_list(list1,list2))
    




