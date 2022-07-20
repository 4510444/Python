import seaborn as sns
import matplotlib.pyplot as plt
phool=sns.load_dataset("iris")
sns.lineplot(x="sepal_length",y="sepal_width",data=phool)
plt.title("Line Plot of Iris Data Set")                   #Adding title
sns.set_style("dark")                                     #set style
sns.set_style(style=None, rc=None)
plt.xlim(4)                                               #Adding Limits
plt.ylim(2)
plt.show()