from cProfile import label
from turtle import color
from matplotlib import pyplot as plt 

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

plt.pie(slices, labels =labels,explode = explode,shadow = True,startangle=90,
        autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})

plt.title("my awesome pie chart")
plt.show()
plt.tight_layout()