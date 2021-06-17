from datetime import datetime, time


class Account:
    #   bank_name="Stanbic Bank"


      def __init__(self,name,phone,loan_limit):
          self.name=name
          self.phone=phone
          self.transation=[]
          self.loan_limit=loan_limit
          self.balance=0
          self.loan=0
          self.intrest=0.5
      def  deposit(self,amount):

          if amount<=0:
              return f"The amount must be greater than 0"
          else:
            self.balance+=amount
            transation={
             "amount":amount,
             "balance":self.balance,
             "time":datetime.now(),
             "narration":"Deposit"

           }
            self.transation.append(transation)
          return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
      def  show_balance(self):
          return self.balance

      def withdraw(self,amount):
         if  amount<0:
               return f"Dear{self.name} with {self.phone}  your balance is {self.balance}"
         elif amount>self.balance:
             return f"Your can't withraw"

         else :
              self.balance-=amount
              return f"Dear {self.name} with {self.phone} Your balance is {self.balance}"

      def borrow(self,amount):
          if amount>=self.loan:
              return f"You can't borrow the money, your expectation is above the limits"
          elif  self.loan>=1:
              return f" Pay your first loan to borrow again"

          else:
             self.loan=0
             self.balance+=amount
             return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"

      def get_statement(self):
          for transation in self.transation:
              narration=transation["narration"]
              amount=transation["amount"]
              balance=transation["balance"]
              time=transation["time"]
              print(f"For the time of Transation {time.strftime('%D')} your statment {narration} the money you have{amount}Balance {balance}")


      def withdraw(self,amount):
          if amount<0:
              return f"Dear{self.name} with {self.phone}  your balance is {self.balance}"
          elif amount>self.balance:
             return f"Your can't withraw"

          else :
              self.balance-=amount
              return f"Dear {self.name} with {self.phone} Your balance is {self.balance}"

      def borrow(self,amount):
          if amount<=self.loan_limit:
              return f"You can't borrow the money, your expectation is above the limits"
          elif  self.loan>=1:
              return f" Pay your first loan to borrow again"

          else:
             self.loan=0
             self.balance+=amount
             return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"

      def repay_loan(self,amount):
          if amount<0:
              return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"

          elif  amount<self.loan:
              self.loan-=amount
              return f"You have paid {amount} and the remaning loan is{self.loan} "
          else:
              deference=amount-self.loan
              self.balance+=deference
              self.loan=0
              return f"Dear user, you have  successfully paid your loan which is {self.loan}, your new balance is{self.balance}"
      def deposit(self,amount):
          try:
               4+amount
          except TypeError:
              return f"The amount must be in figures"


      def transfer(self,amount,account):
          try:
               4+amount
          except TypeError:
             return f"The amount must be in figures"
          if amount>0:
              fee=amount*0.05
          if amount+fee>self.balance:
                return f"Your balance is{self.balance}and you need{amount+fee} is not enough to send the money"
          else:
                self.balance-=amount+fee
                account.deposit(amount)
                return f"You have successfully deposited {amount} your new balance is {self.balance}"

                # Inheritance
class MobileMoneyAccount(Account):
    def __init__(self, name, phone,loan_limit,service_provider):
        Account.__init__(self,name,phone,loan_limit)
        self.service_provider=service_provider
        self.limit=3000000

    def by_airtime(self,amount):
         try:
               4+amount
         except TypeError:
             return f"The amount must be in figures"
         if amount<0:
            return  f"You can't borrow the negative money"
         elif amount>self.balance:
              return"You can borrow only a positive number"
         else:
            self.balance-=amount
            return f"Dear{self.name} you have successfully borrowed{amount} your new balance is {self.balance}"











