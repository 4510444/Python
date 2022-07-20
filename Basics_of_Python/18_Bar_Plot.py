# import libraries
import seaborn as sns
import numpy 
import matplotlib.pyplot as plt
# load dataset
kashti = sns.load_dataset("titanic")
# Draw a Bar plot 
sns.barplot(x="who",y="age",hue="who",data=kashti,order=["man","woman","child"],
            color="blue",ci=None,estimator=numpy.mean,saturation=1) 
plt.show()