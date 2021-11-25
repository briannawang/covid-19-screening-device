import time
from gpiozero import LED

from smbus2 import SMBus
from mlx90614 import MLX90614 



bus = SMBus(1)
yellow = LED(14)
yellow.off()
#Note: Address should be checked using $ sudo i2cdetect -y 1
sensor = MLX90614(bus, address=0x5A)
wristTemp = sensor.get_object_1()
#print (sensor.get_amb_temp()) #Prints environment temperature to the console
#print (sensor.get_object_1()) #Prints object temperature to the console
#Retakes temperature if the temperature is not in a valid human range to a maximum of 100 times
#Note: Less than 31*C and greater than 43*C often results in death
counter = 100
print("Please move your wrist in front of the sensor\n")
print ("Ambient Temperature :", sensor.get_ambient())
while (wristTemp<26 or wristTemp>43) and counter>0:
    wristTemp = sensor.get_object_1()
    counter = counter-1 
    #delay each loop by 3 seconds
    time.sleep(1) 
#After taking a reasonable temperature, checks to see if the person can enter
print("")
t = time.localtime()
timeNow = time.strftime("%H:%M:%S", t)

#notification.message = "Testing: ", timeNow," EST"
if(wristTemp<30):
    yellow.on()
    print("Temperature too low: ", wristTemp, " *C \n")
    print("You may enter, but consider getting that checked out\n")
elif(wristTemp>36):
    print("Your temperature is too high: ", wristTemp, " *C\n")
    print("Please stay where you are until someone comes to assist you\n")
    #Gets current time
    #t = time.localtime()
    #timeNow = time.strftime("%H:%M:%S", t)
    #Alerts manager via phone notifications if the customer has a fever
    #notification.message = "Customer temperature too high, please address immediately ", timeNow," EST"
    #notification.send()
else:
    yellow.on()
    print("Your temperature is: ", wristTemp," *C\n")
    print("Thanks for cooperating with us, you may enter\n")

bus.close()