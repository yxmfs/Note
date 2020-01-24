#!/usr/bin/env python3
# coding=utf-8
from functools import partial
import itertools
import numpy as np
import pandas as pd
from test import *
from sort import quickSort
from listnode import LinkList
class MyError(Exception):
    def __str__(self,):
        return 'MyError'
def errortest():
    try:
        0/1
        raise MyError()
    except MyError as e:
        print('this is ',e)
    except Exception as e:
        print('that is a error:',e)
    a, *r = [1,2,3,4,5,6]
    print(r)

def part(a,b):
    return a / b

def s(n=10):
    print('start generate!')
    for i in range(n):
        yield i
def path_fr(path):
    with open(path) as f:
        print(f.read().rstrip())

def np_test():
    n = np.arange(16).reshape(4,4)
    print(type(n[[3],[2]])) #numpy.ndarray
    print(type(n[3][2]))    #numpy.int64
    print(n.transpose())   #=.T
    n = np.arange(16).reshape(2,2,4)
    print(n)
    print(n.shape)
    #print(n.swapaxes(1,2))
    #print(n.swapaxes(1,2).shape)
    s = np.sqrt(n) #开根号
    s[0,1,1]=17
    print('max:',np.maximum(n,s))
    s,w = np.modf(s) #取整w和小数部分s
    print('modf',s,w)
    n = np.arange(0,5,1)
    print(n.shape)
    xs,ys = np.meshgrid(n,n)
    print('-'*50)
    print('xs:',xs)
    print('ys:',ys)
    r = np.sqrt(xs**2+ys**2)
    xa = np.arange(0,5)
    ya = np.arange(6,11)
    con = np.array([False,True,False,True,True])
    r = [(x if c else y)for x,y,c in zip(xa,ya,con)]
    print(r)
    r = np.where(con,xa,ya)
    print(r)
    print('mean:{0},sum:{1},cumsum累加:{2},cumprod:{3}'
        .format(r.mean(),r.sum(),r.cumsum(),r.cumprod()))
    print(con.any(),con.all())

def np_fun():
    n = np.array([1,2,3,4,5,6,55,44,4,3])
    np.save('t.npy',n)
    n = np.load('t.npy') #存取数组
    f = {1,2}
    #r = np.in1d(n,f)
    r = np.unique(n)
    print(r,r.shape,type(r),r.sum(),type(f))
def pd_fun():
    df = pd.DataFrame({'a':range(5),'b':range(6,11)})
    df.insert(2,column='c',value=df['b'].apply(lambda x:x*2))
    d = df.copy()
    d.rename(columns={'c':'d'},inplace=True)
    d['a'][0]+=5
    print(df)
    print(d)
    print(d.sub(df,fill_value=10))#d-df
def main():
    '''
    l = ['apple','big','cat','dog']
    #f = lambda x:part(x,2)
    f = partial(part,16,8)
    f_letter = lambda x: x[0]
    print(f())
    gen = s()
    for key in gen:
        print(key,'\t')
    for letter, name in itertools.groupby(l,f_letter):
        print(letter,list(name))
    for x in map(f_letter,l):
        print(x)
    path_fr('test.txt')
    '''
    #np_fun()
    t = test('hello')
    t()
    print(t)
    f = F()
    l = [1,2,45,4,1,3,2,6,77,5]
    print(l)
    quickSort(l,0,len(l)-1)
    linklist_fun()
    pd_fun()
def linklist_fun():
    print('-'*25+'LinkList'+'-'*25)
    ll = LinkList()
    print(len(ll))
    ll.append(1)
    ll.append('2')
    ll.append('33')
    print(len(ll))
    print(ll.index('2'))
    ll.delete(0)
    ll.insert(3,'44')
    print('show all the item')
    for key in range(len(ll)):
        print(key,ll[key])
if __name__ == '__main__':
    main()