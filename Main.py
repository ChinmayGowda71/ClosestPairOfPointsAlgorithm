import sys
import time
from ClosestPairofPointsAlgorithm import ClosestPairofPointsAlgorithm

fp = open("DataPoints.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())

print(points)
# Call the compute function passing in the
# contents of the file
start = time.time()
rm = ClosestPairofPointsAlgorithm()
print(rm.compute(points))
end = time.time()
print("time: "+ str(end-start))
