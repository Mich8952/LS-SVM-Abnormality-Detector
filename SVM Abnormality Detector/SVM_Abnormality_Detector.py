#https://towardsdatascience.com/support-vector-machine-svm-for-anomaly-detection-73a8d676c331

import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from numpy import where

df = pd.read_csv("xyz_data.csv")

num_outliers = []
gamma_val = []
#gamma_val = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 20.0, 30.0, 40.0]
for gamm in range(1,1000000,1000):
    gamma_to_use = gamm*0.0001
    model2 = OneClassSVM(kernel='rbf', gamma = gamma_to_use, nu = 0.03).fit(df)
    y_preds = model2.predict(df)
    outlier_index = where(y_preds==-1)
    outlier_values = df.iloc[outlier_index]
    num_outliers.append(len(outlier_values))
    gamma_val.append(gamma_to_use)

plt.plot(gamma_val,num_outliers)
plt.xlabel("gamma val")
plt.ylabel("num_outlier")
plt.show

min = min(num_outliers)
min_idx = num_outliers.index(min)


#speficy the model
model = OneClassSVM(kernel='rbf', gamma = gamma_val[min_idx], nu = 0.03).fit(df) #was 0.001 and 0.03


#prediction
y_pred = model.predict(df)

outlier_index = where(y_pred==-1)

outlier_values = df.iloc[outlier_index]
for idx in outlier_index:
    df = df.drop(index = idx)

#visualize
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(df["x"], df["y"], df["z"])
#ax.scatter3D(outlier_values["x"], outlier_values["y"], outlier_values["z"], c ="r")
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = df["x"]
y = df["y"]
z = df["z"]
c = df["op"]

x0 = outlier_values["x"]
y0 = outlier_values["y"]
z0 = outlier_values["z"]
c0 = outlier_values["op"]  

img = ax.scatter(x, y, z, c=c, cmap="hsv")
img2 = ax.scatter(x0, y0, z0, c=c0, cmap="hsv", marker = "x") 
fig.colorbar(img)


print("POTENTIAL OUTLIERS")
idx = outlier_values.index
outlier_values["item #"] = idx
outlier_values = outlier_values[['item #','x','y','z','op']].reset_index(drop = True)
print(outlier_values)

plt.show()