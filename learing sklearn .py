import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
modle = LinearRegression()
x  = list(map(int, input("enter year ").split()))
x1 = [[x] for x in x]
y = list(map(int,input("enter number of sale a codining to the year :").split()))
modle.fit(x1,y)
last_year = x[-1]
future_years = [last_year + i for i in range(1, 4)]
future_x = [[i] for i in future_years]
future_sales = modle.predict(future_x)

print(f"modle predict {future_sales}")
all_years = x + future_years
all_sales = y + list(future_sales)

plt.bar(all_years, all_sales)

plt.title("prediced sales")
plt.show()