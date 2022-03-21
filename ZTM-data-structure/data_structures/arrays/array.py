class MyArray:

    def __init__(self):
        # Array have the length and the data
        self.length=0
        self.data={}

    def __str__(self):
        return str(self.__dict__)

    def get(self,index):
        # Return the data in the position index
        return self.data[index]

    def push(self,item):
        # Insert data in the last position
        self.data[self.length]=item

        # Increase the length of the array by one
        self.length +=1

        return self.length

    def pop(self):
        """
            Remove last item from the and return the last item
        """

        #  Save the last item in a variable
        lastitem = self.data[self.length-1]

        # Remove last item from the array
        del self.data[self.length-1]

        # Decrease the length by 1
        self.length -=1

        # Return last item
        return lastitem

    def delete(self,index):
        """
            Will receive an parameter index and delete the item. It's almost the same as before,
            but now we can choose the item
        """
        print("Dentro da delete")
        # Get the item you want to delete
        deleted_item = self.data[index]

        
        # Decrease the data index, lefting the last element suplicated
        for i in range(index,self.length-1):
            print(i,self.data)
            self.data[i] = self.data[i+1]
            print(i,self.data)

        # Delete the last one because it is duplicated
        del self.data[self.length-1]


        # Decrease the length by 1
        self.length -=1

        # Return last item
        return deleted_item



arr = MyArray()
arr.push(3)
arr.push('hi')

# print(arr)
# print(arr.get(1))
# print(arr)
arr.push('3')
# print(arr)
arr.push('!')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
# print(arr)
print(arr.get(6))
arr.delete(2)
print(arr.get(6))
# print(arr.pop())
# print(arr.pop())
print(arr)