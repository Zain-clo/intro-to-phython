weight = float(input("enter ur weight in kilograms"))
height = float(input("Enter your height in metres" ))
BMI = weight/(height*height)

if BMI<= 18.4:
    print("You are underweight") 

elif BMI<=24.9:
    print("You are healthy!")

elif BMI<=29.9:
    print("you are overweight.")

elif BMI<=34.9:
        print("You are severly overweight")
        
elif BMI<= 39.9:
     print("You are obese")        

else :
     print("You are severly Obese")     
    
    

import datetime
print(datetime.datetime.now())
import calendar
print(calendar.calendar(2025))