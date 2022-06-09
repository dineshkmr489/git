weight = int(input())
height = float(input())
BMI_formula = weight/height**2

if BMI_formula <= 18.5:
    print('Underweight')
if BMI_formula >= 18.5 and BMI_formula <= 25:
    print("Normal")
if BMI_formula >= 25 and BMI_formula <= 30:
    print("Overweight")
if BMI_formula >= 30:
    print("Obesity")
