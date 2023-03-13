from classSemaphore import BinarySemaphore
semGlobal = BinarySemaphore(1)
semProdEven = BinarySemaphore(0)
semProdOdd = BinarySemaphore(0)
semConsEven = BinarySemaphore(0)
semConsOdd = BinarySemaphore(0)


class Buffer:
    def __init__ (self):
        self._data = []
        self.numOfProdEvenWaiting = 0
        self.numOfProdOddWaiting = 0
        self.numOfConsEvenWaiting = 0
        self.numOfConsOddWaiting = 0
        self.numOfEven = 0
        self.numOfOdd = 0

    def print_buffer(self):
        print(self._data)        
    
    def canPutEven(self):
        if self.numOfEven < 10:
            return True
        return False

    def canPutOdd(self):
        if self.numOfEven > self.numOfOdd:
            return True
        return False
    
    def canConsEven(self):
        if self._data[0] % 2 == 0:
            if self.numOfEven + self.numOfOdd >= 3:
                return True
        return False
    
    def canConsOdd(self):
        if self._data[0] % 2 != 0:
            if self.numOfOdd + self.numOfEven >= 7:
                return True
        return False

    def putEven(self, element):
        semGlobal.P()
        if self.canPutEven() == False:
            self.numOfProdEvenWaiting += 1
            semGlobal.V()
            semProdEven.P()
            self.numOfProdEvenWaiting -= 1

        self._data.append(element)
        self.numOfEven += 1
        print("dodaliśmy liczbę parzystą: " + str(element))
        self.print_buffer()

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            semProdOdd.V()  
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            semConsEven.V() 
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            semConsOdd.V()
        else:
            semGlobal.V()
        return
            
    
    def putOdd(self, element):
        semGlobal.P()
        if self.canPutOdd() == False:
            self.numOfProdOddWaiting += 1
            semGlobal.V()
            semProdOdd.P()
            self.numOfProdOddWaiting -= 1

        self._data.append(element)
        self.numOfOdd += 1
        print("dodaliśmy liczbę nieparzystą: " + str(element))
        self.print_buffer()

        if self.numOfProdEvenWaiting > 0 and self.canPutEven():
            semProdEven.V()  
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            semConsEven.V()
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            semConsOdd.V() 
        else:
            semGlobal.V()
        return
           

    def consEven(self):
        semGlobal.P()
        if self.canConsEven() == False:
            self.numOfConsEvenWaiting += 1
            semGlobal.V()
            semConsEven.P()
            self.numOfConsEvenWaiting -= 1
        el = self._data.pop(0)
        print("usuneliśmy liczbę parzystą: "+ str(el))
        self.print_buffer()
        self.numOfEven -= 1

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            semProdOdd.V()
        elif self.numOfProdEvenWaiting > 0 and self.canPutEven():
            semProdEven.V()
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            semConsOdd.V()
        else:
            semGlobal.V()
            

    def consOdd(self):
        semGlobal.P()
        if self.canConsOdd() == False:
            self.numOfConsOddWaiting += 1
            semGlobal.V()
            semConsOdd.P()
            self.numOfConsOddWaiting -= 1

        el = self._data.pop(0)
        print("usuneliśmy liczbę nieparzystą: "+ str(el))
        self.print_buffer()
        self.numOfOdd -= 1

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            semProdOdd.V()
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            semConsEven.V()
        elif self.numOfProdEvenWaiting > 0 and self.canPutEven():
            semProdEven.V()
        else:
            semGlobal.V()
            

            
        
    
    


    