import matplotlib.pyplot as plt

# """
# Matplotlib na enna?
# Idhu oru 2D plotting library. Idhu mulama charts, graphs, histogram,
# scatter plots apdinu pala vithamana visualization-ah easy-ah panna mudiyum.
# """
#
#
#
# """
# Yethu epudi select panrathu? (Quick Guide)
# Trend irundha: Line Plot use pannunga.
#
# Comparison irundha: Bar Chart use pannunga.
#
# Correlation/Relationship irundha: Scatter Plot use pannunga.
#
# Distribution/Spread irundha: Histogram or Box Plot use pannunga.
#
# Percentage/Parts of a whole: Pie Chart use pannunga.
# """
#
#
#
#
#
# #line chart --> normally called as plot
# # X axis values
# x = [1, 7, 3, 8, 5]
# # Y axis values
# y = [2, 4, 6, 8, 10]
#
# # Plot create panradhu
# plt.plot(x, y)
#
# # Labels kudukuradhu
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("My First Plot")
#
# # Chart-ah display panna
# plt.show()
#
#
#
#
# import matplotlib.pyplot as plt
#
# # 1. Data
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# sales = [10, 20, 15, 30, 25]
#
# # 2. Plotting
# plt.plot(months, sales, color='blue', marker='o') # Line plot
# plt.fill_between(months, sales, color='skyblue', alpha=0.4) # Area-va fill pannum
#
# # 3. Aesthetics
# plt.title('Monthly Sales Trend')
# plt.xlabel('Months')
# plt.ylabel('Sales')
#
# plt.show()
#
#
#
#
#
#
#
# # bar chart --> vertical bar chart
# fruits = ['Apple', 'Banana', 'Orange', 'Mango']
# count = [20, 35, 15, 27]
#
# # Bar chart creation
# plt.bar(fruits, count, color='green')
#
# # Titles and labels
# plt.title("Fruit Sales Comparison")
# plt.xlabel("Fruit Name")
# plt.ylabel("Quantity")
#
# # Display
# plt.show()
#
#
#
#
# # bar chart --> horizontal bar chart
# fruits = ['Apple', 'Banana', 'Orange', 'Mango']
# count = [20, 35, 15, 27]
#
# # Bar chart creation
# plt.barh(fruits, count, color='green')
#
# # Titles and labels
# plt.title("Fruit Sales Comparison")
# plt.xlabel("Fruit Name")
# plt.ylabel("Quantity")
#
# # Display
# plt.show()
#
#
#
#
#histogram
# import matplotlib.pyplot as plt
#
# # Data: Fall events nadantha hours (24 hours format)
# fall_hours = [1, 2, 2, 3, 8, 9, 10, 10, 10, 14, 15, 15,20,21, 22, 23, 23, 23]
#
# # Plotting
# plt.hist(fall_hours, bins=4, color='skyblue', edgecolor='black')
#
# plt.title('Fall Events Frequency by Hour')
# plt.xlabel('Time (Hours)')
# plt.ylabel('Number of Falls')
#
# plt.show()
#
#
#
#
# #box plot
# import matplotlib.pyplot as plt
#
# # Data: Oru group-oda marks nu vachukalam
# marks = [25, 45, 50, 52, 55, 58, 60, 62, 65, 70, 75, 95]
#
# # Plotting
# plt.boxplot(marks)
#
# plt.title('Student Marks Distribution')
# plt.ylabel('Marks')
#
# plt.show()


