# create a numpy array called temps_celsius
import numpy as np
temps_celsius = np.array([22,25,28,24,26])
fahrenheit = (temps_celsius*1.8)+32
avg_fh = np.sum(fahrenheit)/len(temps_celsius)
print(f"Celsius : {temps_celsius}")
print(f"Fahrenheit : {fahrenheit}")
print(avg_fh)
# task 2 array shape and statistics

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(f"Shape: {scores.shape}")
print(f"Total elements : {scores.size}")
print(f"Highest score : {max(scores)}")
print(f"Lowest score : {min(scores)}")
print(f"Range : {max(scores)-min(scores)}")
#  Performance Comparison

import time
numbresArray = np.arange(1,50001)
numbersList = list(range(1,50001))

npStartTime = time.time()
npSum= np.sum(numbresArray)
npEndTime = time.time()
npTimeTaken = npEndTime-npStartTime

start_numpy = time.time()
numpy_sum = np.sum(numbresArray)
end_numpy = time.time()

pyStartTime = time.time()
pySum = sum(numbersList)
pyEndTime = time.time()
pyTimeTaken =pyEndTime-pyStartTime
speedDiff = 0
# speedDiff = pyTimeTaken / npTimeTaken # throwing ZeroDivisionError so commenting
print("NumPy Sum:", npSum)
print("Python Sum:", pySum)
print("Time taken by NumPy:", npTimeTaken)
print("Time taken by Python:", pyTimeTaken)
print("NumPy is", speedDiff, "times faster than Python")