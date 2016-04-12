from sklearn import tree
#[weight in grams, texture - 0 = bumby and 1 = smooth]
features = [[140, 1], [130, 1], [150, 0], [170,0]]
#0 = apple and 1 = orange
labels = [0 ,0 ,1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[160 , 0]]) #output should be 1 = orange