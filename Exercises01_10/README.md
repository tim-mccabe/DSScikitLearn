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

#### Expected result:

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

Using the *scikit-learn* package and the *SimpleImputer* class, fill in the missing data for the column *weight* with the average value. Assign changes to the *df DataFrame*.

In response, print the *df DataFrame* to the console.

**Tip:** More about the *SimpleImputer* class: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

#### Expected result:
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

## Exercise 4

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

## Exercise 5

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

Using the *scikit-learn* package and the *SimpleImputer* class, fill in the missing values for the *size* column with the most frequent value of this column.

Assign changes to the *df DataFrame*. In response, print the *df DataFrame* to the console as shown below.

**Tip:** More about the *SimpleImputer* class: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

#### Expected result:
```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN    NaN   300.0    yes
3    M  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```

## Exercise 6

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

## Exercise 7

The *df DataFrame* is given below:

```
  size  color  gender  price  weight bought
0   XL    red  female  199.0   500.0    yes
1    L  green    male   89.0   450.0     no
2    M   blue     NaN    NaN   300.0    yes
3  NaN  green  female  129.0     NaN     no
4    M    red  female   79.0   410.0    yes
5    M  green    male   89.0     NaN     no
```

Extract columns of *object* type from this *DataFrame*. Then fill in all the missing values for these columns with the value `'empty'`.

Assign the result to the *df_object* variable and print it to the console.

#### Expected result:

```
    size  color  gender bought
0     XL    red  female    yes
1      L  green    male     no
2      M   blue   empty    yes
3  empty  green  female     no
4      M    red  female    yes
5      M  green    male     no
```

## Exercise 8

The *df DataFrame* is given below:
```
df = pd.DataFrame(data={'weight': [75., 78.5, 85., 91., 84.5, 83., 68.]})
```
Discretize the *weight* column. Divide the values of this column into three intervals of equal width. Assign the result to a new column 'weight_cut' as shown below.

In response, print the *df* object to the console.

#### Expected result:

```
   weight        weight_cut
0    75.0  (67.977, 75.667]
1    78.5  (75.667, 83.333]
2    85.0    (83.333, 91.0]
3    91.0    (83.333, 91.0]
4    84.5    (83.333, 91.0]
5    83.0  (75.667, 83.333]
6    68.0  (67.977, 75.667]
```

## Exercise 9

The *df DataFrame* is given below:
```
df = pd.DataFrame(data={'weight': [75., 78.5, 85., 91., 84.5, 83., 68.]})
```

Discretize the column *weight* into three intervals with the given boundaries:

* (60, 75]
* (75, 80]
* (80, 95]

Assign the result to the new column `'weight_cut'` as shown below.

In response, print the `df DataFrame` to the console.

#### Expected result:
```
   weight weight_cut
0    75.0   (60, 75]
1    78.5   (75, 80]
2    85.0   (80, 95]
3    91.0   (80, 95]
4    84.5   (80, 95]
5    83.0   (80, 95]
6    68.0   (60, 75]
```