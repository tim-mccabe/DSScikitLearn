## Discretize Column with Labels

The *df DataFrame* is given below:
```
df = pd.DataFrame(data={'weight': [75., 78.5, 85., 91., 84.5, 83., 68.]})
```

Discretize the column *weight* into three intervals with the given boundaries:

* (60, 75]
* (75, 80]
* (80, 95]

and bound to them the following labels:

* light
* normal
* heavy

Assign the result to the new column `'weight_cut'` as show below.

In response, print the *df DataFrame* to the console.

#### Expected result:

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