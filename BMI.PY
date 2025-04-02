def bodyMassIndex():
    while True:
        try:
            height=float(input("ENTER YOUR HEIGHT IN METRES: "))
            weight=float(input("ENTER YOUR WEIGHT IN KILOGRAMS: "))
            #BMI for body mass index
            BMI=weight / height**2
            return BMI
        except ValueError as e:
            print("The values must be numerals!!!")
            print(e)

        except ZeroDivisionError as e:
            print("Height can not be ZERO(0)!!, Enter a non zero!!!")  
            print(e)
        except Exception as e:
            print(e)      
BMI=bodyMassIndex()
print(f"Your body mass Index is: ",BMI)

def comment():
 BMI=bodyMassIndex()
if BMI <= 18:
         print(BMI,f": You are underweight, improve on your diet!!!")
elif 18.1<= BMI <=22:
     print(BMI,f": KEEP IT UP YOU HAVE NORMAL WEIGHT,, KEEP IT UP")
elif 22.1<= BMI <=28:
     print(BMI,f": Unfortunately you have an overweight but your weight is manageable,, Consider taking an exercise for 45 minutes atleast four times a week ")
elif 28.1 <=  BMI <=40:
     print(BMI,f": You are overweight is at extreme level, To work for it; Do exercise for atleast 1 hour daily and reduce your food intake!!! 🥙🥗🍞🫔😋")          
elif    BMI >=40.1:
     print(BMI, f": You should be visiting your physician your overweight extreme is not a joke!!!, Subtitute much fats to you diet for this 👉👉🍌🍋🍏🍎🍑🍋‍🟩🫐🥭🍉🍊🍇🍅")    
else:
         print("Check on the inputs may be they are invalids")
 
       