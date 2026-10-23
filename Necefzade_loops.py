#Q1
for i in range(10,0,-1):
     print(i)
print("Liftoff!")



#Q2
child=0
adult=0 
for i in range(1,6):
     age_of_visitor=int(input("Enter the age"))
     if age_of_visitor<18:
          child=child+1
     else:
          adult=adult+1
print("Child tickets:", child)
print("Adult tickets:", adult)



#Q3
for i in range(1, 10, 2):
      print(i, end=" ")

#Output: 1 3 5 7 9




#Q4
price=0
for i in range(1, 6):
     item_price=float(input("Enter the price"))
     price=price+item_price
average_price=price/5
print("Total:", price)
print("Average:, average_price")




#Q5

password=input("Enter the password")
while len(password)<8:
     print("Too short, try again")
     password=input("Enter the password")
print("Password accepted")

     
        

#Q6
#70
#40
#10
#20
#Done




#Q7
Total_steps=0
for i in range(1, 8):
      Total_steps=Total_steps+1200
      print(i, "-ci gun:", Total_steps)



#Q8



attempts=0
while attempts<3:
     username=input("Enter the username")
     password=input("Enter the password")
     if username=="admin" and password=="1234":
          print("Welcome!")
          break
     else:
          print("Wrong username or password")
          attempts=attempts+1
if attempts==3:
     print("Account locked")







#Q9

balance=500
while True:
      amount=float(input("Amount: "))
      if amount==0:
            print("Goodbye")
            break
      elif amount<0:
           print("invalid amount")
      elif amount>balance:
           print("Insufficient funds")
      else:
           balance=balance-amount
           print("Balance: ", balance)





#Q10

#Wrong Pin, 2, attemts left
#Wrong Pin, 1, attempts left
#Access granted 
#Attemts used: 3



#Q11

passed=0
failed=0
highest_grade=0
count=0
total=0
while True:
     grade=int(input("Grade: "))
     if grade==-1:
          break
     caunt=caunt+1
     total=total+grade
     if grade>=51:
          passed=passed+1
     else:
          failed=failed+1
     if count==1 or grade>highest_grade:
          highest_grade=grade
average=total/count
print("Passed: ", passed)
print("Failed: ", failed)
print("Average: ", average)
print("Highest: ", highest_grade)




#Q12

spaces=20
while True:
     command=input("Command: ")
     if command=="stop":
          break
     elif command=="in":
         if spaces==0:
              print("Garage full")
         else:
              spaces=spaces-1
              print("Free spaces: ", spaces)  
     elif command=="out":
          if spaces==20:
               print("Garage empty")
          else:
               spaces=spaces+1
               print("Free spaces: ", spaces)
     else:
          print("Unknown command")




#Q13
day=0
for i in range(1,8):
     temperature=int(input("Temperature: "))
     if temperature>30:
          day=day+1
          if i==1 or temperature>highest_temperature:
               highest_temperature=temperature
print("Highest temperature: ", highest_temperature)
print("Hot days: ", day)



#Q14  attempts=0 deyiseni while truenun icerisinde yazildigina gore her sehv cavabdan sonra sifirlanir, neticedeattempts==3 serti hec vaxt odemir ve program sonsuz isleyir

password = "secret" 
attempts = 0 
while True: 
     entered = input("Password: ")    
     if entered == password:       
           print("Welcome")         
           break     
     attempts += 1    
     if attempts == 3:        
           print("Account locked")        
           break 



#Q15

password=input("Password: ")
digit=False
upper=False
lower=False
for i in password:
     if i.isdigit():
          digit=True
     elif i.isupper():
          upper=True
     elif i.islower():
          lower=True
if len(password)>=8 and digit==True and upper==True and lower==True:
      print("Strong password")
else:
     print("Weak password")
     reason=[]
     if len(password)<8:
          reason.append("too short")
     if digit==False:
          reason.append("no digits")
     if upper==False:
          print("no upper letter")
     if lower==False:
          print("no lower letter")   
     print(",", reason)




#Q16

money=1000
saving=0
month=0
monthly_saving=50
while saving<money:
     month=month+1
     saving=saving+monthly_saving
     print("Month ", month,":", saving)
     if saving>=money:
          print("Goal reahed in month: ", month)
          break
     monthly_saving=monthly_saving+10





#Q17

#105 cap edir  100den boyuk ilk 7e qaliqsiz bolunen tek ededi tapir



#Q18

pin=2580
balance=1000
