from __future__ import division
import random
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import sys

# how much items from dataset to use as training data
tnumber = int(sys.argv[1])

# shuffle and separate data into training dataset and testing dataset
iris = datasets.load_iris()
data = [(a[0], a[1], a[2], a[3], b) for a, b in zip(iris.data, iris.target)]
random.shuffle(data)
data = np.array(data)
train_data = data[:tnumber]
test_data = data[tnumber:]

# random forest
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(train_data[:, :4], train_data[:, 4])
predictions = [clf.predict(item) for item in test_data[:, :4]]

# how many were correct?
correct = 0
for real, predicted in zip(test_data[:, 4], predictions):
    if real == predicted:
        correct += 1

# report status
print 'Total iris dataset has', str(len(iris.data)), 'items'
print 'Training data:', str(len(train_data)), 'items'
print 'Testing data:', str(len(test_data)), 'items'
print "From", str(len(predictions)), "tests we got", str(correct), 'correct.'
