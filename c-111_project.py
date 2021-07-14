import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import csv
import pandas as pd

df = pd.read_csv('School2.csv')
data = df['Math_score'].tolist()

def randomSetOfMean(counter):

    dataSet = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    dataSetM = statistics.mean(dataSet)
    return dataSetM

meanList = []

for i in range(0, 1000):
    set_means = randomSetOfMean(100)
    meanList.append(set_means)


stDev = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print(f'mean and standard_dev of sampling distribution is {mean} , {stDev}')

firstSDStart, firstSDEnd = mean-stDev, mean+stDev
secondSDStart, secondSDEnd = mean-(2*stDev), mean+(2*stDev)
thirdSDStart, thirdSDEnd = mean-(3*stDev), mean+(3*stDev)

df = pd.read_csv('School_1_Sample.csv')
data = df['Math_score'].tolist()
meanOfSample1 = statistics.mean(data)
print(f'mean of sample 1 is {meanOfSample1}')

def plot_graph():
    fig  = ff.create_distplot([meanList], ['Student marks'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = 'lines', name = 'mean'))
    fig.add_trace(go.Scatter(x = [meanOfSample1, meanOfSample1], y = [0, 0.17], mode = 'lines', name = 'mean'))
    fig.add_trace(go.Scatter(x = [firstSDEnd, firstSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-1'))
    fig.add_trace(go.Scatter(x = [secondSDEnd, secondSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-2'))
    fig.add_trace(go.Scatter(x = [thirdSDEnd, thirdSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-3'))
    fig.show()

plot_graph()

df = pd.read_csv('School_2_Sample.csv')
data = df['Math_score'].tolist()
meanOfSample2 = statistics.mean(data)
print(f'mean of sample 2 is {meanOfSample2}')

def plot_graph_2():
    fig = ff.create_distplot([meanList], ['Student marks'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = 'lines', name = 'mean'))
    fig.add_trace(go.Scatter(x = [meanOfSample2, meanOfSample2], y = [0, 0.17], mode = 'lines', name = 'mean'))
    fig.add_trace(go.Scatter(x = [firstSDEnd, firstSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-1'))
    fig.add_trace(go.Scatter(x = [secondSDEnd, secondSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-2'))
    fig.add_trace(go.Scatter(x = [thirdSDEnd, thirdSDEnd], y = [0, 0.17], mode = 'lines', name = 'standard deviation-3'))
    fig.show() 

plot_graph_2()
#finding the z-score using the formula

z_score = (mean-meanOfSample1)/stDev
print(z_score)