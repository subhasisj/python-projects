""" lecture and example code for decision tree unit """

import sys
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from pylib.plot import plot_decision_boundary

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--it's your job to fill this in!
from sklearn import tree
clf = tree.DecisionTreeClassifier( min_samples_split=10  )
clf = clf.fit(features_train ,  labels_train, )

#### grader code, do not modify below this line

print(clf.score( features_test , labels_test ))