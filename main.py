users={1010:"Arjun Kadam",1011:"Rohit Khokale",1012:"Gaurav Thombare",1013:"Dhiraj Mate",1014:"Mayur Gund",1015:"Abhishek Shinde"}
pins={1010:3435,1011:2342,1012:6354,1013:2254,1014:3936,1015:3527}
 
users_c={110:"Arjun Kadam",111:"Rohit Khokale",112:"Gaurav Thombare",113:"Dhiraj Mate",114:"Mayur Gund",115:"Abhishek Shinde"}
pins_c={110:3438,111:2942,112:3354,113:5654,114:3936,115:5483}
balance={}
balance_c={}
with open("credentials.txt","r") as file:
    line=file.readlines()
    data=line[0].strip().split(" ")
    for i in data:
        key_value=i.split(':')
        balance[int(key_value[0])]=int(key_value[1])
     
with open("credentials_c.txt","r") as file:
    line=file.read()
    data=line.strip().split(" ")
    for i in data:
        key_value=i.split(':')
        balance_c[int(key_value[0])]=int(key_value[1])

from datetime import datetime

class Account():
    def __init__(self,ac_holder,ac_no,bal):
        self.ac_holder=ac_holder
        self.ac_no=ac_no
        self.bal=bal
    def display(self):
        print(f"Account Holder :- {self.ac_holder}")
        print(f"Account Balance :- {self.bal}")

    def deposit(self,amount,type):
        try:
            if(amount<=0):
                raise ValueError("Enter appropriate amount")
            else:
                self.bal=self.bal+amount
                if(type=="current"):
                    balance_c[self.ac_no]=self.bal
                elif(type=="saving"):
                    balance[self.ac_no]=self.bal
                with open("passbook.txt","a") as file:
                    file.write(f"{self.ac_holder}\n account :- current | \tdeposit :- {amount} | \tcurrent bal :- {self.bal} |  {datetime.now().strftime("%d/%m/%Y, %H : %M : %S")}\n\n")
        except ValueError:
            print("Enter appropriate amount")
        
    def withdraw(self,amount,type):
        try:
            if(amount<=0 or amount>self.bal):
                raise ValueError("Enter appropriate amount")
            else:
                self.bal=self.bal-amount
                if(type=="current"):
                    balance_c[self.ac_no]=self.bal
                elif(type=="saving"):
                    balance[self.ac_no]=self.bal           
                with open("passbook.txt","a") as file:
                    file.write(f"{self.ac_holder}\n account :- current | \twithdrawal :- {amount} | \tcurrent bal :- {self.bal} |  {datetime.now().strftime("%d/%m/%Y, %H : %M : %S")}\n\n")
        except ValueError:
            print("Enter appropriate value")
   
class Current_Ac(Account):
    def __init__(self,ac_holder,ac_no,bal):
        super().__init__(ac_holder,ac_no,bal)
    def dep_check(self):
        amount=int(input("Enter Deposit Amount :- "))
        self.deposit(amount,"current")
    def with_check(self):
        amount=int(input("Enter Withdrawal Amount :- "))
        self.withdraw(amount,"current")
        

class Saving_Ac(Account):
    def __init__(self,ac_holder,ac_no,bal):
        super().__init__(ac_holder,ac_no,bal)
    def dep_check(self):
        amount=int(input("Enter Deposit Amount :- "))
        if(amount>=100000):
            print("Your saving account has limit of 100000, you can deposit upto 99999rs/transaction")
        else:
            self.deposit(amount,"saving")
    def with_check(self):
        amount=int(input("Enter Withdrawal Amount :- "))
        if(amount>=100000):
            print("Your saving account has limit of 100000, you can withdraw upto 99999rs/transaction")
        else:
            self.withdraw(amount,"saving")

    
         

print("\t***** Welcome to the New Bank *****\t")
while True:
    choice1=input("Enter Command (Proceed/Exit) :- ").lower()
    if(choice1=="proceed"):
        
        try:
            ac_type=input("Enter Account type(Current/Saving) :- ").lower()
            if(ac_type=="saving"):
                user=int(input("Enter Account no :- "))
                if user in users:
                    pin=int(input(f"Dear {users[user]}, Enter your PIN :- "))
                    if(pin!=pins[user]):
                        print("Incorrect PIN, plz try again or contact the branch")
                    else:
                        Customer=Saving_Ac(users[user],user,balance[user])
                        while True:
                            choice2=input("Do you want to continue with this Saving account (Proceed/Exit) :- ").lower()
                            if(choice2=="proceed"):
                                choice=input("Enter command (Deposit/Withdraw/Balance):- ").lower()

                                if(choice=="deposit"):
                                    Customer.dep_check()

                                elif(choice=="withdraw"):
                                    Customer.with_check()
                                elif(choice=="balance"):
                                    Customer.display()
                                else:
                                    print("Wrong command, try again")
                            elif(choice2=="exit"):
                                with open("credentials.txt","w") as file:
                                    for key in balance:
                                        file.write(f"{key}:{balance[key]} ")
                                break
                            else:
                                print("Wrong command,try again")
            elif(ac_type=="current"):
                user_c=int(input("Enter Account no :- "))
                if user_c in users_c:
                    pin=int(input(f"Dear {users_c[user_c]}, Enter your PIN :- "))
                    if(pin!=pins_c[user_c]):
                        print("Incorrect PIN, plz try again or contact the branch")
                    else:
                        Customer_c=Current_Ac(users_c[user_c],user_c,balance_c[user_c])
                        while True:
                            choice2=input("Do you want to continue with this current account (Proceed/Exit) :- ").lower()
                            if(choice2=="proceed"):
                                choice=input("Enter command (Deposit/Withdraw/Balance):- ").lower()

                                if(choice=="deposit"):
                                    Customer_c.dep_check()

                                elif(choice=="withdraw"):
                                    Customer_c.with_check()
                                elif(choice=="balance"):
                                    Customer_c.display()
                                else:
                                    print("Wrong command,try again")
                            elif(choice2=="exit"):
                                with open("credentials_c.txt","w") as file:
                                    for key in balance_c:
                                        file.write(f"{key}:{balance_c[key]} ")
                                break
                            else:
                                print("Wrong command,try again")


        except ValueError as e:
            print(f"Error fetched :- {e}")
    elif(choice1=="exit"):
        break
    
    else:
        print("command was invalid")