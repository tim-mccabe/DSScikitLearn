## Get Dummies

The df DataFrame is given below:
```
   weight weight_cut
0    75.0      light
1    78.5     normal
2    85.0      heavy
3    91.0      heavy
4    84.5      heavy
5    83.0      heavy
6    68.0      light
```

Using `pd.get_dummies()` function convert *weight_cut* categorical column into dummy variable as shown below.

In response, print result to the console.

**Tip:** More about `pd.get_dummies()`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html

#### Expected result:

```
   weight  weight_cut_light  weight_cut_normal  weight_cut_heavy
0    75.0                 1                  0                 0
1    78.5                 0                  1                 0
2    85.0                 0                  0                 1
3    91.0                 0                  0                 1
4    84.5                 0                  0                 1
5    83.0                 0                  0                 1
6    68.0                 1                  0                 0
```