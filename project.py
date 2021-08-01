# pop mean = 6.134
# sampling mean 6.111

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv
import statistics

# df = pd.read_csv("medium_data.csv")
# data = df["reading_time"].tolist()

# population_mean = statistics.mean(data)   

# def randomSetOfMean(counter):
#     dataSet = []
#     for i in range(0, counter):
#         random_index = random.randint(0, len(data)-1)
#         value = data[random_index]
#         dataSet.append(value)
#     mean = statistics.mean(dataSet)    
#     return mean

# def showFig(meanList):
#     fig = ff.create_distplot(
#         [meanList],
#         ["average"],
#         show_hist=False
#     )
    
#     mean = statistics.mean(meanList)
    
#     fig.add_trace(
#         go.Scatter(
#             x = [mean, mean],
#             y = [0, 1],
#             mode = 'lines',
#             name = "Mean"
#         )
#     )
#     print(mean)
    
#     fig.show()

# def setUp():
#     meanList = []
#     for i in range(0, 100):
#         setOfMeans = randomSetOfMean(30)
#         meanList.append(setOfMeans)
#     sd = statistics.stdev(meanList)
#     print(sd)
#     print("---------")
#     print(population_mean)
#     showFig(meanList)
    
# setUp()

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()


##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


# Function to get the mean of 100 data sets
mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)



## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("medium_data2.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.2], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 1.2], mode="lines", name="MEAN OF INTERVENTION"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1.2], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1.2], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1.2], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

#finding the z score using the formula
z_score = (mean - mean_of_sample1)/std_deviation
print("The z score is = ", z_score)
