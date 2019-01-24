from sklearn import tree

# [weight[kg], height[cm], gender (0 = male, 1 = female)]
#==============================================
data = [32, 57, 0]
#==============================================

features = [[40, 65, 0], [32, 60, 1], [36, 62, 0], [32, 60, 1]] #features of each breed
labels = [1, 1, 0, 0] #which breed it is (1 = gm, 0 = lr)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

if (clf.predict([data]) == 1): #if statement to check if the output is one or zero
  print("It's a German shepherd")
elif (clf.predict([data]) == 0):
  print("It's a Labrador retriever")