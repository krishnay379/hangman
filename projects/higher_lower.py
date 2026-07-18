import random
print(    )
a = ['1','2','3','4','5','6','7','8','9','10','11','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']

number = random.randint(0,50)
# print(number)

user_input = int(input("Guess a number "))
def guess_no():  
    if user_input == number :
        print("You guess number right")
    elif user_input > number :
        print("Guess number is higher")
    elif user_input < number:
        print("Guess number is smaller ")
while number != user_input:
    guess_no()