# import library
import math
import random


# function to generate OTP
def generate_otp():
    # Declare a string variable
    # which stores all string
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    otp = ""
    length = len(string)
    for i in range(6):
        otp += string[math.floor(random.random() * length)]

    return otp
