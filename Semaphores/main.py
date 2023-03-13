from classBuffer import Buffer
import random
from threading import Thread
import time

buffer = Buffer()

def evenProducer():
    while(True):
        element = random.randint(0, 25) * 2
        buffer.putEven(element)
        time.sleep(random.randint(2, 10))

        
def oddProducer():
    while(True):
        element = random.randint(1, 25) * 2 - 1
        buffer.putOdd(element)
        time.sleep(random.randint(2, 10))

def evenConsumer():
    while(True):
        buffer.consEven()
        time.sleep(random.randint(2, 10))

def oddConsumer():
    while(True):
        buffer.consOdd()
        time.sleep(random.randint(2, 10))



def main():
    thread_A1 = Thread(target=evenProducer)
    thread_A2 = Thread(target=oddProducer)
    thread_B1 = Thread(target=evenConsumer)
    thread_B2 = Thread(target=oddConsumer)

    thread_A1.start()
    thread_A2.start()
    thread_B1.start()
    thread_B2.start()



if __name__ == "__main__":
    main()