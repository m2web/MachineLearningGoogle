#used https://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code to configure VS Code to display output in VS Code

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0]
# for i in range(len(iris.target)):
#     print "Example %d: features %s, label %s" % (i, iris.data[i], iris.target[i])
test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
# print train_target
# print train_data

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
# print test_target
# print test_data

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
# print test_target
# print clf.predict(test_data)

# from sklearn.externals.six import StringIO  
# import pydot_ng as pydot 
# dot_data = StringIO() 
# tree.export_graphviz(clf, out_file=dot_data,  
#                          feature_names=iris.feature_names,  
#                          class_names=iris.target_names,  
#                          filled=True, rounded=True,  
#                          special_characters=True) 
# graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
# graph.write_pdf("iris.pdf") 
##the above produced a PDF without labels on both Ubintu 14.04 and 15.04. There was a Warning with the output:
##Warning: Not built with libexpat. Table formatting is not available.
##I did the conda install expat but still no fixing it.
##
##I was able to install pydot_ng via conda install -c https://conda.binstar.org/sstromberg pydot
##and then changed the import of pydot to import pydot_ng as pydot and all worked on Windows 10

print test_data[2], test_target[2]
print iris.feature_names, iris.target_names