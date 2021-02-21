import  csv
import statistics
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import pi,sin
from Mini_A import load_CSV
def smooth_b(x, n):
    return [statistics.mean(x[max(0,i-n): min(i+n+1, len(x))])
            for i in range(len(x))]
def smooth_a(x, n):
    return [ sum(x[max(0,i-n): min(i+n+1, len(x))] +
                   [x[0]] * max(0, n-i) +
                   [x[-1]] * max(0, i+n+1-len(x)))
        /(2*n+1) for i in range(len(x))]
peopleDict = load_CSV()    
fig, ax = plt.subplots()
time = list(range(1960, 2015))
for i in [('dnk', 'blue'), ('fin', 'orange'), ('isl', 'green'), ('nor', 'red'), ('swe', 'purple')]:
    ax.plot(time, peopleDict[i[0]], linestyle = ':', color = i[1], label = i[0])
    ax.plot(time, smooth_a(peopleDict[i[0]], 5), linestyle = '-', color = i[1])
    ax.plot(time, smooth_b(peopleDict[i[0]], 5), linestyle = '--', color = i[1])
ax.set(xlabel='Year', ylabel='CO2 Emissions (kt)', title='Yearly Emissions of CO2 in the Nordic Countries')
plt.legend()
fig.savefig("Test.png")
plt.show() 
