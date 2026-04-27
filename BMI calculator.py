def calculate_bmi(weight,height):
    bmi=weight/(height*height)
    return (bmi)

def get_category (bmi):
    if bmi<18.5:
        return("underweight😗⬜")
    elif bmi<24.9:
        return("Normal🟩(Healthy)")
    elif bmi<29.9:
        return("overweight🟨")
    else:
        return("Obese🟥")   

print("WELCOME TO THE BMI CALCULATOR:💪")
weight=float(input("what is your weight:😙"))
height_cm = float(input("what is your height in cm:🗼 "))
height_m = height_cm / 100

bmi=calculate_bmi(weight,height_m)
category=get_category(bmi)

print("your bmi is :", round(bmi, 2))
print("your category is :",category)



    