class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self,name):
        print(f"configurations of {name}:",self.cpu,self.ram)
Hp=Computer('intel','128')
Dell=Computer('intel-i5','256')
Hp.config('Hp')
Dell.config('Dell')