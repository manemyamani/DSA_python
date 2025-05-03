from threading import *
from time import *
class A(Thread):
    def run(self):
        for i in range(9):
            print("yamini")
            sleep(0.2)

class B(Thread):
    def run(self):
        for i in range(9):
            print("anand")
            sleep(0.2)
t1=A()
t2=B()
t1.start()
sleep(0.01) #to maintain synchronization between t1,t2
t2.start()
t1.join() #to tell main thread to wait untill the t1,t2 threads completes their work
t2.join()
print("they are pair")
