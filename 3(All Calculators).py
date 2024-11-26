import pickle
class Calculator:
    def __init__(self):
         self.result=0
    def add(self,num):
         self.result+=num
         return self.result
    def sub(self,num):
         self.result-=num
         return self.result
    def mul(self,num):
         self.result*=num
         return self.result
    def div(self,num):
         if num>0:
            self.result/=num
            return self.result
         else:
            print("Fuck")
calculator=Calculator()
print(calculator.add(454))
print(calculator.add(454))
save_location="calc.pkl"
with open(save_location,'wb') as file:
    pickle.dump(calculator,file)
print(f"Calculator object saved to :{save_location}")
