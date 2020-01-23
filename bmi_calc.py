# Simple program to calculate Body Mass Index (BMI)

height = float(input("Enter Height (m): "))
weight = float(input("Enter Weight (kg): "))

bmi = weight / (height**2)

print("BMI = ", round(bmi,2), "kg/m^2")
