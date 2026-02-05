height=float(input("Enter height in meters"))
weight=int(input("Enter weight in kgs"))
bmi=float(weight/(height**2))
print("Bmi =",bmi)
if bmi<=18.4:
    print("Underweight")
elif bmi<=24.9:
    print("normal")
else:
    print("overweight")