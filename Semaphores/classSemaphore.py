from threading import Semaphore    

class BinarySemaphore:
    def __init__(self, count):
        self._sem = Semaphore(count)
    
    def V(self):
        self._sem.release()
    
    def P(self):
        self._sem.acquire()
