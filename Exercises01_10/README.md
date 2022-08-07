## Exercise 1

The following dictionary is given:

```
data = {
    'size': ['XL', 'L', 'M', np.nan, 'M', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red', 'green'],
    'gender': ['female', 'male', np.nan, 'female', 'female', 'male'],
    'price': [199.0, 89.0, np.nan, 129.0, 79.0, 89.0],
    'weight': [500, 450, 300, np.nan, 410, np.nan],
    'bought': ['yes', 'no', 'yes', 'no', 'yes', 'no']
}
```

From this dictionary create a *DataFrame* object and assign to the *df* variable.

Then check for the missing values for each column (in percent) and print it to console as shown below. Round the result to two decimal places.

Expected result:

```
size      0.17
color     0.00
gender    0.17
price     0.17
weight    0.33
bought    0.00
dtype: float64
```

## Exercise 2

The following df DataFrame is given:

```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN    NaN   300.0    yes
3  NaN  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```

Using the *scikit-learn* package and the *SimpleImputer* class, fill in the missing data for the column *weight* with the average value. Assign changes to the *df DataFrame*.

In response, print the *df DataFrame* to the console.

**Tip:** More about the *SimpleImputer* class: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

Expected result:
```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN    NaN   300.0    yes
3  NaN  green  female  129.0   415.0     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0   415.0     no
```

## Exercise 3

The following df DataFrame is given:

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

Expected result:

```
415.0
```

## Exercise 04

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

Expected result:

```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN   99.0   300.0    yes
3  NaN  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```