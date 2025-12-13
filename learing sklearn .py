import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
modle = LinearRegression()
x  = list(map(int, input("enter year ").split()))
x1 = [[x] for x in x]
y = list(map(int,input("enter number of sale a codining to the year :").split()))
modle.fit(x1,y)
ne = int(input("enter which year data you want"))
ae = modle.predict([[ne]])
print(f"modle predict {ae}")
