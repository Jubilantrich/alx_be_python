

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    convert_to_celsius=fahrenheit-32 * FAHRENHEIT_TO_CELSIUS_FACTOR
    return convert_to_celsius

def convert_to_fahrenheit(celsius):
    convert_to_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return  convert_to_fahrenheit

Celsius_or_Fahrenheit_Value= float(input("Enter the temperature to convert: "))
Celsius_or_Fahrenheit= str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

if Celsius_or_Fahrenheit =="F":
    print(Celsius_or_Fahrenheit_Value,"oF is ",convert_to_celsius(Celsius_or_Fahrenheit_Value),"oC")
elif Celsius_or_Fahrenheit =="C":
     print(Celsius_or_Fahrenheit_Value,"oC is",convert_to_fahrenheit(Celsius_or_Fahrenheit_Value),"oF")
else :
     print("We didnt understand your respond.")


