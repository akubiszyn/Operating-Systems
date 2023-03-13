from monitor import Monitor, Condition
class MyMonitor (Monitor):
    def __init__(self):
        super().__init__()
        self._buffer = []
        self.numOfProdEvenWaiting = 0
        self.numOfProdOddWaiting = 0
        self.numOfConsEvenWaiting = 0
        self.numOfConsOddWaiting = 0
        self.prodEven = Condition()
        self.prodOdd = Condition()
        self.consEven = Condition()
        self.consOdd = Condition()
        self.numOfEven = 0
        self.numOfOdd = 0

    def print_buffer(self):
        print(self._buffer)

    def canPutEven(self):
        if self.numOfEven < 10:
            return True
        return False

    def canPutOdd(self):
        if self.numOfEven > self.numOfOdd:
            return True
        return False
    
    def canConsEven(self):
        if len(self._buffer) != 0 and self._buffer[0] % 2 == 0:
            if self.numOfEven + self.numOfOdd >= 3:
                return True
        return False
    
    def canConsOdd(self):
        if len(self._buffer) != 0 and self._buffer[0] % 2 != 0:
            if self.numOfOdd + self.numOfEven >= 7:
                return True
        return False

    def putEven(self, element):
        self.enter()
        if self.canPutEven() == False:
            self.numOfProdEvenWaiting += 1
            self.wait(self.prodEven)
            self.numOfProdEvenWaiting -= 1

        self._buffer.append(element)
        self.numOfEven += 1
        print("dodaliśmy liczbę parzystą: " + str(element))
        self.print_buffer()

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            self.signal(self.prodOdd)
            self.leave() 
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            self.signal(self.consEven)
            self.leave() 
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            self.signal(self.consOdd)
            self.leave() 
        else:
            self.leave()
        return
            
    
    def putOdd(self, element):
        self.enter()
        if self.canPutOdd() == False:
            self.numOfProdOddWaiting += 1
            self.wait(self.prodOdd)
            self.numOfProdOddWaiting -= 1

        self._buffer.append(element)
        self.numOfOdd += 1
        print("dodaliśmy liczbę nieparzystą: " + str(element))
        self.print_buffer()

        if self.numOfProdEvenWaiting > 0 and self.canPutEven():
            self.signal(self.prodEven)
            self.leave()  
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            self.signal(self.consEven)
            self.leave() 
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            self.signal(self.consOdd)
            self.leave() 
        else:
            self.leave()
        return
           

    def removeEven(self):
        self.enter()
        if self.canConsEven() == False:
            self.numOfConsEvenWaiting += 1
            self.wait(self.consEven)
            self.numOfConsEvenWaiting -= 1
        el = self._buffer.pop(0)
        print("usuneliśmy liczbę parzystą: "+ str(el))
        self.print_buffer()
        self.numOfEven -= 1

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            self.signal(self.prodOdd)
            self.leave()
        elif self.numOfProdEvenWaiting > 0 and self.canPutEven():
            self.signal(self.prodEven)
            self.leave()
        elif self.numOfConsOddWaiting > 0 and self.canConsOdd():
            self.signal(self.consOdd)
            self.leave()
        else:
            self.leave()
            

    def removeOdd(self):
        self.enter()
        if self.canConsOdd() == False:
            self.numOfConsOddWaiting += 1
            self.wait(self.consOdd)
            self.numOfConsOddWaiting -= 1

        el = self._buffer.pop(0)
        print("usuneliśmy liczbę nieparzystą: "+ str(el))
        self.print_buffer()
        self.numOfOdd -= 1

        if self.numOfProdOddWaiting > 0 and self.canPutOdd():
            self.signal(self.prodOdd)
            self.leave()
        elif self.numOfConsEvenWaiting > 0 and self.canConsEven():
            self.signal(self.consEven)
            self.leave()
        elif self.numOfProdEvenWaiting > 0 and self.canPutEven():
            self.signal(self.prodEven)
            self.leave()
        else:
            self.leave()

    
