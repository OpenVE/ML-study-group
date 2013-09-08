#import matplotlib
#matplotlib.use('wxagg')
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import sys

# INCOMPLETO!

def traindata():
    reader = csv.reader((open('data/train.csv')))
    header = reader.next()
    return np.array([row[1:] for row in reader])

if __name__ == '__main__':
    data = traindata()
    surv_age = np.array([(int(d[0]), float(d[4])) for d in data if d[4] != ''])
    surv0 = [p[1] for p in surv_age if p[0]==0]
    surv1 = [p[1] for p in surv_age if p[0]==1]

    # Histogram: Surviving passengers by age
    fig = plt.figure()
    plt.hist(surv1, bins=40, facecolor='blue')
    plt.title('Surviving passengers by age')
    plt.xlabel('Age in years')
    plt.ylabel('Number of persons')
    plt.yticks(np.arange(0, 40, 5))
    plt.savefig('AgeHistogramSurvived.png')

    # Histogram: Non-surviving passengers by age
    fig = plt.figure()
    plt.hist(surv0, bins=40, facecolor='red')
    plt.title('Non-surviving passengers by age')
    plt.xlabel('Age in years')
    plt.ylabel('Number of persons')
    plt.yticks(np.arange(0, 40, 5))
    plt.savefig('AgeHistogramNonSurvived.png')

    # Plot: Survivers (blue) and non-survivers (red) passengers by sex
    fig = plt.figure()
    surv_sex = np.array([(int(d[0]), (1 if d[3] == 'male' else 2), float(d[4])) for d in data if d[3] != '' and d[4] != ''])
    surv0 = ([p[2] for p in surv_sex if p[0]==0], [p[1] for p in surv_sex if p[0]==0])
    surv1 = ([p[2] for p in surv_sex if p[0]==1], [p[1] for p in surv_sex if p[0]==1])
    plt.plot(surv0[0], surv0[1], 'ro')
    plt.plot(surv1[0], surv1[1], 'bo')
    plt.xlabel('Age in years')
    plt.ylabel('Sex')
    plt.yticks(range(4), ['', 'Male', 'Female', ''])
    plt.xticks(np.arange(0, 90, 10))
    plt.savefig('PlotSurvivedByAgeSex.png')

