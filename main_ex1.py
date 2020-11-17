import time
from LIS2HH12 import LIS2HH12
import pycom 
from pysense import Pysense
import machine

oy_values = list()
pyIoT = Pysense()
acc_value = LIS2HH12(pyIoT)

for _ in range(60):
    print("Acceleration value is " + str(acc_value.acceleration()))
    oy_values.append(str(acc_value.acceleration()[0]))
    time.sleep(1)

with open("acceleration_values.txt", "w+") as file:
    for entry in oy_values:
        file.write(str(entry + "\n"))
