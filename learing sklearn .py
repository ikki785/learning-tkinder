
from sklearn.linear_model import LinearRegression
modle = LinearRegression()
x = [[1],[2],[3],[4],[5]]
y = [20,30,40,50,60]
modle.fit(x,y)
a = int(input("enter your working hours"))
b = modle.predict([[a]])[0]
print(b)
