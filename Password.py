#this is my first program in python coding language
#To calculate student total marks and grades
print("To calculate stdent total marks and grade")
obt_marks=float(input("enter obtaind marks ="))
total_marks=float(input("enter total marks ="))
percentage=(obt_marks/total_marks)*100
if percentage<35:
    print("fail")
   
elif percentage<45:
        print("Grade C")
elif percentage<60:
            print("Grade B")
elif percentage<75:
                print("Grade A")
else:
                print("Grade A++")

print(percentage)



    
    
    