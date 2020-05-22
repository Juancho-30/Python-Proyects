class Account:

   def __init__(self, filepath):
      self.path=filepath   #Instance variable
      with open(filepath, 'r') as file: #file is temp variable
         self.balance = int(file.read()) # Save the value on instance value balance self object

   def withdraw(self, amount):
      self.balance=self.balance-amount
      
   def deposit(self, amount):
      self.balance=self.balance + amount

    

   def commit(self):
      with open(self.path, 'w') as file:
         file.write(str(self.balance))

class Checking(Account): #sintax for inheritance
   """This class generates checking account objects""" #Doc strings
   type="checking"   #Class variable, Data member
   def __init__(self, filepath, fee): #Constructor for the checking class inherited
      Account.__init__(self, filepath)
      self.fee=fee #Data member

   def transfer(self, amount):
      self.balance=self.balance - amount - self.fee

jack_checking=Checking("account//jack.txt",1)
jack_checking.transfer(100)
print(jack_checking.balance) #Aceesing attributes (balance)
jack_checking.commit()
print(jack_checking.type)


john_checking=Checking("account//john.txt",1)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

print(john_checking.__doc__)