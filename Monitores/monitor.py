from threading import Semaphore    

class BinarySemaphore:
    def __init__(self, count):
        self._sem = Semaphore(count)
    
    def V(self):
        self._sem.release()
    
    def P(self):
        self._sem.acquire()

class Monitor:
    def __init__(self):
        self.s = BinarySemaphore(1)

    def enter(self):
        self.s.P()

    def leave(self):
        self.s.V()

    def wait(self, cond ):
        cond.waitingCount += 1
        self.leave()
        cond.wait()
	

    def signal(self, cond ):
        if( cond.signal()):
            self.enter()


class Condition:
    def __init__(self):
        self.waitingCount = 0
        self.w = BinarySemaphore(0)

    def wait(self):
        self.w.P()

    def signal(self):
        if(self.waitingCount ):
            self.waitingCount -= 1
            self.w.V()
            return True
        else:
            return False
