
# coding: utf-8

from datascience import *
import numpy as np

avocado = Table.read_table('avocado.csv')

# build a kNN classifier for type of avocado

av = avocado.select('AveragePrice', 'Total Volume', 'Total Bags', 'type')
av = av.sample(with_replacement=False)
av_train = av.take(np.arange(18000))
av_test = av.take(np.arange(18000, 18249))

def dist(t, arr):
    '''Takes in a table where the 1st 3 columns are the numerical data
    and returns the cartesian distance from an array with coincident values'''
    dists = make_array()
    for i in np.arange(t.num_rows):
        dist = np.sqrt((t.column(0).item(i) - arr.item(0)) ** 2 + (t.column(1).item(i) - arr.item(1)) ** 2 + (t.column(2).item(i) - arr.item(2)) ** 2)
        dists = np.append(dists, dist)
    return t.with_column('distances', dists)




dist(av_train, np.array(av_test.drop('type').row(0)))




def find_majority(t, t2, row_index):
    '''Takes in training table (t), test table (t2), and row index of test
    table value (row_index) and computes the cartesian distance then
    returns the training table sorted by incrasing distance'''
    test = np.array(t2.drop('type').row(row_index))
    d = dist(t, test)
    return d.sort('distances')

find_majority(av_train, av_test, 0)




def knn(t, t2, row, k):
    test = np.array(t2.drop('type').row(row))
    sort = find_majority(t, t2, row)
    tbl = sort.take(np.arange(k)).group('type').sort(1, descending=True)
    return tbl.column(0).item(0)

# test accuracy of 7-NN classifier
classed = make_array()
for i in np.arange(av_test.num_rows):
    cl = knn(av_train, av_test, i, 7)
    classed = np.append(classed, cl)
    
av_test.with_column('7-NN Class', classed)




def test_accuracy(train, test, k):
    '''Returns proportion of correct classifications from avocado classifier'''
    classed = make_array()
    for i in np.arange(test.num_rows):
        cl = knn(train, test, i, 7)
        classed = np.append(classed, cl)
    
    classed_test = test.with_column('k-NN Class', classed)
    return np.count_nonzero(classed_test.column('k-NN Class') == classed_test.column('type')) / classed_test.num_rows




test_accuracy(av_train, av_test, 7)

