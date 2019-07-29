### Rotate labels in axis

import matplotlib.pyplot as plt

plt.figure(figsize=(20,6))
stats = df.groupby(['year_month_origin', 'TXNTYPE']).AMOUNT.count().reset_index()
plot = sns.barplot(stats.year_month_origin, stats.AMOUNT, hue=stats.TXNTYPE)
plot.set_xticklabels(plot.get_xticklabels(), rotation=45)
