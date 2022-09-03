## Extract Columns of Type

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