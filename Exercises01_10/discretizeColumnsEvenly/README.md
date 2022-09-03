## Discretize Columns Evenly

The *df DataFrame* is given below:
```
df = pd.DataFrame(data={'weight': [75., 78.5, 85., 91., 84.5, 83., 68.]})
```
Discretize the *weight* column. Divide the values of this column into three intervals of equal width. Assign the result to a new column `'weight_cut'` as shown below.

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