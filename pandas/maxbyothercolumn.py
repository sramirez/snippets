df.iloc[df.groupby('date').revenue.transform(lambda x: x.idxmax())].threshold.reset_index(drop=True)
