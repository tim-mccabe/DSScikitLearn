## Simple Imputer Average

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

Missing data for the column *weight* was replaced with the average value of this column using the *SimpleImputer* class.

Print the average value that was replaced with the missing values in the *weight* column.

**Tip:** More about the SimpleImputer class: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

#### Expected result:

```
415.0
```