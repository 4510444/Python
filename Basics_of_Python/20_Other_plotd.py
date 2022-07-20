import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nuqte=sns.load_dataset("dots")
# defining a color pallete
p=sns.color_palette("rocket_r")
#plot lineplot
sns.relplot(data=nuqte,x="time",y="firing_rate",hue="coherence",
            size="choice",col="align",kind="line",size_order=["T1","T2"],
            palette=p,height=5, aspect=.75, facet_kws=dict(sharex=False),)
plt.show()