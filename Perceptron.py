from random import choice
from numpy import array, dot, random

unit_step = lambda x: 1 if x > -0.1 else -1 #function used for evaluation
BD = lambda x: 'Bright' if x > 0 else 'Dark' #helper function for printing

training_data = [
    (array([-1,-1,-1,-1]), -1),
    (array([-1,-1,-1,1]), -1),
    (array([-1,-1,1,-1]), -1),
    (array([-1,-1,1,1]), 1),
    (array([-1,1,-1,-1]), -1),
    (array([-1,1,-1,1]), 1),
    (array([-1,1,1,-1]), 1),
    (array([-1,1,1,1]), 1),
    (array([1,-1,-1,-1]), -1),
    (array([1,-1,-1,1]), 1),
    (array([1,-1,1,-1]), 1),
    (array([1,-1,1,1]), 1),
    (array([1,1,-1,-1]), 1),
    (array([1,1,-1,1]), 1),
    (array([1,1,1,-1]), 1),
    (array([1,1,1,1]), 1),
]

w = random.rand(4)
errors = []
eta = 0.01 #experimented with different values to find best one
n = 300 #setting max number of iterations to 300

for i in range(n): #training
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x
    
correct = 0
print("{} : {} -> {} : {}".format('Input', 'output', "Result", "actual"))
for x, o in training_data:
    result = dot(x, w)
    if (unit_step(result) == o):
        correct += 1
    print("{} : {} -> {} : {}".format(x[:4], result, BD(unit_step(result)), BD(o)))
accuracy = correct/16.0;
print "Accuracy: ", int(accuracy*100), "%"