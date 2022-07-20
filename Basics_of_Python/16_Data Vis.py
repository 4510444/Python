#steps involved in data visualization
# Step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
#Step-2 Set a theme
sns.set_theme(style="ticks",color_codes=True)
#Step 3 import dataset (you can also import your own data)
kashti = sns.load_dataset("titanic")
# print(kashti)
#Step-4 Plot basic graph with 1 variable (count)
p = sns.countplot(x = "sex", data=kashti)
plt.show()
#Step-5 Plot basic graph with 2 variable (count plot)
p = sns.countplot(x = "sex", data=kashti, hue="class")
plt.show()
# Step-5 Plot basic graph with 2 variable (count plot) with title
p = sns.countplot(x = "who", data=kashti, hue="class")
p.set_title("Baba Ammar Ka Count Plot")
plt.show()