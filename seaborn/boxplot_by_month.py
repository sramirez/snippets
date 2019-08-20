df['year_month_origin'] = df.trx_origin.dt.strftime('%Y-%m')

plt.figure(figsize=(20,6))
df = df.sort_values('year_month_origin')
plot = sns.boxplot(df.year_month_origin, df.price)
plot.set_xticklabels(plot.get_xticklabels(), rotation=45)
