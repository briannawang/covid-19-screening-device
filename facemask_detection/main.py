import detect_mask
import TemperatureSensor

max_capacity = 2
current_capacity = 0
goodtemp = False
maskon = False

while True:
    maskon = detect_mask.detectmask()
    if maskon == True:
        goodtemp = TemperatureSensor.tempsensor()

    print ("temp good:",goodtemp)
    print ("mask good:", maskon)

    if (maskon and goodtemp and (current_capacity<max_capacity)):
        print ("You are safe to enter")
        current_capacity += 1
        maskon = False
        goodtemp = False
    else:
        print ("You may not enter")
        if current_capacity == max_capacity:
            print("Please wait for someone to leave before entering")
        maskon = False
        goodtemp = False


