import numpy as np
import pandas as pd

s= pd.Series([1,3,5, np.nan,6,8])
#print(s)

dates = pd.date_range("20130101", periods=6)
#print(dates)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A":1.0,
        "B":pd.Timestamp("20130102"),
        "C":pd.Series(1,index=list(range(4)),dtype="float32"),
        "D":np.array([3]*4, dtype="int32"),
        "E":pd.Categorical(["test","train","test","train"]),
        "F":"foo",
    }
)
#print(df2)
#print(df2.dtypes)

print(df.head(2))
print(df.tail(2))

print(df.index)
print(df.columns)
print(df.to_numpy())
print(df2.to_numpy())

print(df.describe())






print('''
Alles klar''')
