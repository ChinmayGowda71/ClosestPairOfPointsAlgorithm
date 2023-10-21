import math
class ClosestPairofPointsAlgorithm:
    def __init__(self):
        return
    # @return the distance between the closest points
    def compute(self, file_data):
        x = self.parser(file_data)
        newarr = sorted(x, key = lambda s: s[0])
        return self.recurisonsplitting(newarr)
    def distance(self,num1,num2):
        return math.sqrt((num1[0]-num2[0])* (num1[0]-num2[0]) + (num1[1]-num2[1])*(num1[1]-num2[1]))
    def parser(self, file_data):
        x= []
        for i in file_data:
            s = i.split()
            xcord = float(s[0])
            ycord = float(s[1])
            x.append([xcord,ycord])
        return x
    def divide(self,x):
        less_median = []
        more_median = []
        medianarr = []
        if len(x) % 2 != 0:
            median = float(x[math.floor(len(x)/2)][0])
        else:
            f = int(len(x)/2)
            median = (float(x[f][0]) + float(x[f-1][0]))/2
        for i in range(len(x)):
            if float(x[i][0]) < median:
                less_median.append(x[i])
            elif float(x[i][0]) > median:
                more_median.append(x[i])
        return less_median, more_median, median

    def baseCase(self,arr):
        closestpath = 10292093.0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if self.distance(arr[i],arr[j]) < closestpath:
                    closestpath = self.distance(arr[i],arr[j])
        return closestpath

    def recurisonsplitting(self,arr):
        if len(arr) <= 3:
            return self.baseCase(arr)
        less_median, more_median, median = self.divide(arr)
        left_side = self.recurisonsplitting(less_median)
        right_side = self.recurisonsplitting(more_median)
        D = min(left_side,right_side)
        middle = []
        for i in range(len(arr)):
            if (arr[i][0] - median) < D:
                middle.append(arr[i])
        return min(D, self.middle_ground_test(middle,D))

    def middle_ground_test(self,middle,D):
        min_dist = D
        sorted_y = sorted(middle, key=lambda s: s[1])
        for i in range(len(middle)):
            if i < len(middle)-15:
                for j in range(i+1,i+15):
                    if self.distance(sorted_y[j],sorted_y[i]) < min_dist:
                        min_dist = self.distance(sorted_y[j], sorted_y[i])
            else:
                for j in range(i+1,len(middle)):
                    if self.distance(sorted_y[j],sorted_y[i]) < min_dist:
                        min_dist = self.distance(sorted_y[j], sorted_y[i])
        return min_dist


