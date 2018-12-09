import unittest
class BinHeap(object):
    '''
        Class representation of a Binary Heap
    '''
    def __init__(self):
        self._array=[]


    def add(self,item):
        '''
        Adds an item to the Binary Heap
        :param item: value to be added to the heap
        '''

        #seeing if the heap is empty
        if len(self._array)==0:

            #added the item to the empty
            self._array.append(item)

        #else there is items all ready in the heap
        else:

            #add the item to the end of the heap
            self._array.append(item)

            #get the items index
            item_index=len(self._array)-1

            #get the parent of the items index
            parent_index=(item_index-1)//2

            '''
            While loop testing if the item is smaller than its
            parents.
            
            This "bubbles" the item into the correct possition
            '''
            while self._array[parent_index] > item:

                #swapping the item and its parent
                self._array[parent_index],self._array[item_index]=self._array[item_index],self._array[parent_index]

                #updating the items index
                item_index=parent_index

                #Calculate the items new parents index
                parent_index=(item_index)//2

    def remove_min(self):
        '''
        Removes the item at the top of the binary heap
        :return: the smallest item in the heap
        '''

        #Testing if theres only one item in the heap
        if len(self._array)==1:

            #getting the only item in the heap
            min_item = self._array[-1]

            #reseting the heap
            self._array = []

            #returning the item
            return min_item


        else:
            #Swap the last node in the heap with the min node
            self._array[0],self._array[-1]=self._array[-1],self._array[0]

            #remove the end item
            min_item=self._array[-1]
            self._array=self._array[:-1]

            #bubble the node at top of the heap down to the correct possition
            item_index=0
            left_child_index=2*item_index+1
            right_child_index=2*item_index+2

            while True:
                #select the minimum of the two children
                #and swap
                if item_index > len(self._array)-1 or right_child_index>len(self._array)-1 or left_child_index>len(self._array)-1:
                    break

                if self._array[left_child_index] < self._array[right_child_index]:
                    if self._array[left_child_index]<self._array[item_index]:
                        self._array[left_child_index],self._array[item_index]=self._array[item_index],self._array[left_child_index]
                        item_index=left_child_index
                    else:
                        break
                else:
                    if self._array[right_child_index]<self._array[item_index]:
                        self._array[right_child_index],self._array[item_index]=self._array[item_index],self._array[right_child_index]
                        item_index=right_child_index
                    else:
                        break

                left_child_index = 2 * item_index + 1
                right_child_index = 2*item_index+ 2
            return min_item


    def min(self):
        '''
        :return: the smallest item in the heap
        '''
        return self._array[0]

    def length(self):
        '''
        :return: the length of the heap
        '''
        return len(self._array)



    def __str__(self):
        '''
        :return: The string representation of the heap
        '''
        return ' , '.join(map(str,self._array))





class Test(unittest.TestCase):
    def test_add(self):
        heap=BinHeap()
        self.assertEqual(str(heap),'')
        heap.add(2)
        self.assertEqual(str(heap),'2')
        heap.add(3)
        self.assertEqual(str(heap),'2 , 3')
        heap.add(4)
        self.assertEqual(str(heap),'2 , 3 , 4')

        heap.add(1)
        self.assertEqual(str(heap),'1 , 2 , 4 , 3')

    def test_remove_min(self):
        heap=BinHeap()
        heap.add(2)
        self.assertEqual(str(heap),'2')
        self.assertEqual(heap.remove_min(),2)
        self.assertEqual(str(heap),'')
        heap.add(5)
        heap.add(4)
        heap.add(3)
        heap.add(2)
        heap.add(1)
        print(heap)
        self.assertEqual(heap.remove_min(),1)
        print(heap)
        self.assertEqual(heap.remove_min(),2)
        print(heap)
        self.assertEqual(heap.remove_min(),3)
        print(heap)
        self.assertEqual(heap.remove_min(),4)
        print(heap)
        self.assertEqual(heap.remove_min(),5)
        print(heap)








if __name__=='__main__':
    unittest.main()