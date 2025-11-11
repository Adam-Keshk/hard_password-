import random as rnd
import string
# variables for the random generator
l=string.ascii_letters
num=string.digits+string.punctuation


# function to generate random strings
def generate_random(count):
    global div_num, random_num1, random_num2
    if count%2==0:
        div_num= count/2
        random_num1= rnd.choices(num,k=div_num)
        random_num2= rnd.choices(l,k=div_num)
        finl_random=random_num1+random_num2
        rnd.shuffle(finl_random)
    else:
        finl_random= rnd.choices([num,l],k=count).shuffle()
    return finl_random

        
        
