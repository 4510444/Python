import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
kashti=sns.load_dataset("titanic")
sns.boxplot(x="survived",y="age",showmeans=True,
            meanprops={"marker":"*",
                       "markersize":"12",
                       "markeredgecolor":"red"}, 
            data=kashti)
# show labels
plt.xlabel("How Many survived",size=15,weight="bold"),
plt.ylabel("Age(years)",size=15,weight="bold"),
plt.title("box of kitny dooby or kitne bach gye",size=20,weight="bold")

plt.show()