from time import *
import random 

def mistake(paragraph,usertest):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != usertest[i]:
                error += 1
        except:
            error += 1 #if user not entered anything it will cause out of index range error and program will stop thatswhy we use this
    return error

def speed_time(time_start,time_end,user_input):
    time_delay = time_end - time_start
    time_r = round(time_delay,2)
    speed = len(user_input)/time_r
    return round(speed)

test = ["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea.","My name is Abhishek Singh and I am a software developer.","Welcome to Kanpur UP 78, Hope you like the city and its culture."]

test1 = random.choice(test)
print("         *****Typing Speed******")
print(test1)
print()
print()

time_1 = time()
test_input = input(" Enter: ")
time_2 = time()


print("Spped : ",speed_time(time_1,time_2,test_input)," W/sec")
print("Error: ",mistake(test1,test_input))