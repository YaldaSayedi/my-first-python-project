# Write your code below this line 👇
from ctypes import HRESULT
from xml.sax import default_parser_list
print("Welcome to tip counting system!")
bill= int(input("How much is the bill? $"))
tip= int(input("How much is the tip? $"))
people= int(input("How many people? "))
total= bill + (tip / 100 * bill)
per_person= total/people

print("Each person should pay: $", per_person)




