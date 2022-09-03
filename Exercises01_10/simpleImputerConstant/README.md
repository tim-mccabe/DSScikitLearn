## Simple Imputer Constant

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

Using the *scikit-learn* package and the *SimpleImputer* class, fill in the missing data for the *price* column with a constant value = 99.0.

Assign changes to the *df DataFrame*. In response, print the *df DataFrame* to the console as shown below.

**Tip:** More about the SimpleImputer class: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

#### Expected result:

```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN   99.0   300.0    yes
3  NaN  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```
