import matplotlib.pyplot as plt
# X=[1,2,3,4,5]
# Y=[2,3,5,7,11]
# plt.plot(X,Y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Graph')
# plt.show()

# for bar graph
# X=[1,2,3,4,5]
# Y=[2,3,5,7,11]
# plt.bar(X,Y,color='Blue')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Bar Graph')
# plt.show()

# for Histogram
data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# plt.hist(data,bins=5,color='Green',edgecolor="Black")
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

# scores = [65, 70, 72, 68, 85, 90, 78, 82, 88, 75, 92, 70, 68, 84, 79]
# plt.hist(scores, bins=5, color='skyblue', edgecolor='black')
# plt.xlabel('Score Range')
# plt.ylabel('Number of Students')
# plt.title('Exam Score Distribution')
# plt.show()

# hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
# exam_scores = [45, 50, 55, 65, 70, 75, 85, 90]

# plt.scatter(hours_studied, exam_scores, color='blue', marker='o')
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Score')
# plt.title('Relationship Between Study Time and Exam Scores')
# plt.show()

# categories = ['Product A', 'Product B', 'Product C', 'Product D']
# values = [40, 30, 20, 10]
# plt.pie(values, labels=categories, autopct='%1.1f%%',
#         labeldistance=1.2, pctdistance=0.85)
# plt.title('Product Sales Distribution')
# plt.show()

# x = [1, 2, 3, 4, 5, 6]
# y = [10, 15, 20, 25, 30, 35]

# plt.fill_between(x, y, color='skyblue')
# plt.plot(x, y, color='blue', linewidth=2)
# plt.show()

# x = [1, 2, 3, 4, 5]
# y1 = [5, 10, 15, 20, 25]
# y2 = [3, 5, 8, 10, 12]

# plt.stackplot(x, y1, y2, labels=['Series A', 'Series B'])
# plt.legend()
# plt.show()

import seaborn as sns
# tips = sns.load_dataset("tips")
# sns.scatterplot(data=tips, x='total_bill', y='tip')
# plt.title('Total Bill vs Tip')
# plt.show()

# flights = sns.load_dataset("flights")
# yearly_passengers = flights.groupby('year')['passengers'].sum().reset_index()
# sns.lineplot(data=yearly_passengers, x='year', y='passengers')
# plt.title('Yearly Passengers Trend')
# plt.show()

# tips = sns.load_dataset("tips")
# sns.barplot(data=tips, x='day', y='total_bill')
# plt.title('Average Total Bill by Day')
# plt.show()

# titanic = sns.load_dataset("titanic")
# sns.countplot(data=titanic, x='class')
# plt.title('Passenger Count by Class')
# plt.show()

# tips = sns.load_dataset("tips")
# sns.boxplot(data=tips, x='day', y='total_bill')
# plt.title('Total Bill Distribution by Day')
# plt.show()

# penguins = sns.load_dataset("penguins")
# sns.histplot(data=penguins, x='flipper_length_mm')
# plt.title('Penguin Flipper Length Distribution')
# plt.show()

# penguins = sns.load_dataset("penguins")
# sns.kdeplot(data=penguins, x='flipper_length_mm')
# plt.title('Penguin Flipper Length - KDE Plot')
# plt.show()
# import numpy as np
# data = np.random.rand(5, 5)
# sns.heatmap(data)
# plt.title('Simple Heatmap')
# plt.show()

tips = sns.load_dataset("tips")
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs Tip - Linear Regression')
plt.show()