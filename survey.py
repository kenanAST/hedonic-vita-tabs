import random

f = open("cleandb.txt", "r")

names = f.read()
names = names.split(",")

sleep = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sleepDistribution = [0, 0.008, 0.00825, 0.025, 0.09, 0.18, 0.2, 0.14, 0.09, 0.05, 0.01, 0.005]

work = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
workDistribution = [0, 0.008, 0.00825, 0.025, 0.09, 0.18, 0.2, 0.14, 0.09, 0.05, 0.01, 0.005]

age = [13,14,15,16,17,18,19,20,21,22,23,24]
ageDistribution = [0.0025, 0.008, 0.0085, 0.05, 0.17, 0.16, 0.12, 0.12, 0.09, 0.05, 0.01, 0.005]

buy = [0, 1]
buyDistribution = [0.92, 0.08]

# print(names[random.randint(0,999)])


for i in range(100):
    print( str(i + 1) + ". " + names[random.randint(0,999)] + "\tSleep: " + str(random.choices(sleep, sleepDistribution)[0]) + "\tWork: " + str(random.choices(work, workDistribution)[0]) + "\tAge: " + str(random.choices(age, ageDistribution)[0]) )

