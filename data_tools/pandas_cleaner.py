import pandas as pd

def clean_and_merge_data():
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6],
        'B': [10, 20, 30, 40, 50, 60],
        'C': ['x', 'y', 'z', 'a', 'b', 'c']
    })

    df2 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'D': [100, 200, 300, 400, 500]
    })

    df = pd.merge(df1, df2, on='A', how='left')
    df = df.dropna()

    return df.to_dict(orient="records")
