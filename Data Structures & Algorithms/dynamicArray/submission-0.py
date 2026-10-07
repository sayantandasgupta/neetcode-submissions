class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.set(self.length, n)
        self.length += 1
        return



    def popback(self) -> int:
        n = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length -= 1
        return n



    def resize(self) -> None:
        self.arr.extend([0]*self.capacity)
        self.capacity = 2*self.capacity
        return

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
