## Number Of Items In Column

The *df DataFrame* is given below:
```
               currency
0            [PLN, USD]
1  [EUR, USD, PLN, CAD]
2                 [GBP]
3       [JPY, CZK, HUF]
4                    []
```

Assign a new column `'number'` that takes the number of items in the *currency* column.

In response, print *df DataFrame* to the console.

#### Expected result:
```
               currency  number
0            [PLN, USD]       2
1  [EUR, USD, PLN, CAD]       4
2                 [GBP]       1
3       [JPY, CZK, HUF]       3
4                    []       0
```
