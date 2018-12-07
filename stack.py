import unittest
class Stack(object):
    '''
        Class Representation of a Stack ADT
    '''

    def __init__(self):
        self._lenght=0
        self._items=[]

    def push(self,item):
        '''
        :param item: value to be added to the top of the stack
        '''
        self._items.append(item)
        self._lenght+=1

    def pop(self):
        '''
        :return: the item at the top of the stack
        '''
        self._lenght-=1
        return self._items.pop(-1)

    def top(self):
        '''
        :return:  the item at the top of the stack
        '''
        return self._items[-1]

    def length(self):
        '''
        :return: the number of the items in the stack
        '''
        return self._lenght




class Test(unittest.TestCase):
    def test_push(self):
        stack=Stack()
        self.assertEqual(stack.length(),0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.length(),4)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.length(),4)
        self.assertEqual(stack.pop(),4)
        self.assertEqual(stack.length(),3)
        self.assertEqual(stack.pop(),3)
        self.assertEqual(stack.length(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.length(), 1)
        self.assertEqual(stack.pop(), 1)

    def test_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top(),1)
        self.assertEqual(stack.top(),1)
        stack.push(2)
        self.assertEqual(stack.top(),2)
        self.assertEqual(stack.top(),2)
        stack.push(3)
        self.assertEqual(stack.top(),3)
        self.assertEqual(stack.top(),3)
        stack.push(4)
        self.assertEqual(stack.top(),4)
        self.assertEqual(stack.top(),4)

    def test_length(self):
        stack = Stack()
        self.assertEqual(stack.length(),0)
        stack.push(1)
        self.assertEqual(stack.length(),1)
        stack.push(2)
        self.assertEqual(stack.length(),2)
        stack.push(3)
        self.assertEqual(stack.length(),3)
        stack.push(4)
        self.assertEqual(stack.length(),4)

if __name__=='__main__':
    unittest()
