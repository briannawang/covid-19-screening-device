import detect_mask
import TemperatureSensor
from termcolor import colored

max_capacity = 2
current_capacity = 0
goodtemp = False
maskon = False

while True:
    maskon = detect_mask.detectmask()
    if maskon == True:
        goodtemp = TemperatureSensor.tempsensor()

    if (maskon and goodtemp):
        if (current_capacity==max_capacity):
            print (colored("Please wait for someone to leave before entering", 'red'))
        else:
            print (colored("You are safe to enter"), 'green')
            current_capacity += 1
        maskon = False
        goodtemp = False
    else:
        print (colored("You may not enter"), 'red')
        maskon = False
        goodtemp = False

    print("\n\n\n")


