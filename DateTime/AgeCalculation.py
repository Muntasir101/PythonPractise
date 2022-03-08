import datetime

user = str(input("What's your name? "))
age = int(input("How old are you? "))

print("Hi " +user+ ". You will be 100 years old in " + str(datetime.datetime. today().year - age + 100)+ "!")
