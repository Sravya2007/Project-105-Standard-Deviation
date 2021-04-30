import math
import csv
import statistics

#Opening the csv file and converting it into list
with open("C:/Users/sravy/White Hat Jr/Project 105- Standard Deviation/data.csv", newline = '') as f:
    read_data = csv.reader(f)
    file_data = list(read_data)

data = file_data[0]

#Finding the mean of the given data
def get_mean(numbers):
    number_of_elements = len(numbers)
    total_value = 0
    
    for i in numbers:
        total_value = total_value + int(i)
    
    mean = total_value / number_of_elements
    return mean

#Subtracting the mean from all the values and squaring them
squares = []
for number in data:
    x = int(number) - get_mean(data)
    x = x ** 2
    squares.append(x)

#Getting the sum of all the elements from the squared list
sum_of_numbers = 0
for element in squares:
    sum_of_numbers = sum_of_numbers + element

#Dividing the sum by the number of values in the dataset
result = sum_of_numbers / (len(data) - 1)

#Getting the square root of the result
standard_deviation = math.sqrt(result)
print("The standard deviation of the data manually:             ", standard_deviation)

#Getting the same result through statistics standard deviation
data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]
print("The standard deviation of the data through a function:   ", statistics.stdev(data))