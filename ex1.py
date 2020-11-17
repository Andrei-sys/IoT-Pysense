import time
import datetime
import matplotlib.pyplot as plt


ox = list()
over_time = list()
counter = 0
with open("acceleration_values.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        ox.append(line.strip())
        over_time.append(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)
        counter += 1
        print(f"Seconds : {counter}")


plt.plot(over_time, ox)
plt.xticks(rotation=45, ha='right')
plt.title("Accelerometer data plot for 60 seconds")
plt.xlabel("Time")
plt.ylabel("Acceleration over time")
plt.scatter(over_time, ox)
plt.grid()
plt.show()

