class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p
class LinkList(object):
    def __init__(self):
        self.head = 0
    def __len__(self):
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    def is_empty(self):
        if self.__len__() ==0:
            return True
        else:
            return False
    def clear(self):
        self.head=0
    def append(self,item):
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q
    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.__len__():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p
        elif index == j+1:
            print('call the append function')
            self.append(item)
        else:
            print('index:{0},j:{1}'.format(index,j))


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.__len__():
            print('Linklist is empty.')
            return

        if index ==0:
            item = self[0]
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1
    def getitem(self,index):

        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print('target is not exist!')
    def __getitem__(self,key):
        if self.is_empty():
            print('it is empty')
            return
        elif (key < 0)  or (key > self.__len__()):
            print('the given key is error')
            return

        else:
            return self.getitem(key)

    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key <0  or key > self.__len__():
            print('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)
        