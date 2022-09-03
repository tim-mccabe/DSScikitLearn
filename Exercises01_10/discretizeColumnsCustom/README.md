## Discretize Column Custom Bins

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