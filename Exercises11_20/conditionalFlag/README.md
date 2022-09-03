## Conditional Flag

The *df DataFrame* is given below:

```
               currency
0            [PLN, USD]
1  [EUR, USD, PLN, CAD]
2                 [GBP]
3       [JPY, CZK, HUF]
4                    []
```

Assign a new column `'PLN_flag'` which stores 1 when the currency `'PLN'` is in the currency column, otherwise 0 as shown below.

In response, print *df DataFrame* to the console.

#### Expected result:

```
               currency  PLN_flag
0            [PLN, USD]         1
1  [EUR, USD, PLN, CAD]         1
2                 [GBP]         0
3       [JPY, CZK, HUF]         0
4                    []         0
```