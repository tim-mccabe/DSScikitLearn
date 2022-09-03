## Not NULL Rows

The following *df DataFrame* is given:

```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN    NaN   300.0    yes
3  NaN  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```

Extract all rows of the *df* that don't have the value `np.nan` in column *weight*. Using this rows calculate the average value for all numeric columns and print result to the console.

#### Expected result:
```
price     122.333333
weight    415.000000
dtype: float64
```