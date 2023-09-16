def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    """
    if weight_kg <= 0 or height_m <= 0:
        return None  
    bmi = weight_kg / (height_m ** 2)
    return bmi
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
if bmi is not None:
    print(f"BMI: {bmi:.2f}")
else:
    print("Invalid input.")
