height = int(input("Input your height in cm: "))
weight = float(input("Input your weight in kg: "))
assert height != int, 'Error'
assert height > 150 and height < 220, 'Error'
assert weight > 40.0 and weight < 150.0, 'Error'
print("Your body mass index is: ", round(weight / ((height * height)*0.0001), 2))
