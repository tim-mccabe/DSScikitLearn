## Split Strings

The *df DataFrame* is given below:
```
              hashtags
0          #good#vibes
1  #hot#summer#holiday
2         #street#food
3             #workout
```
Split *hashtags* by the `'#'` sign using `pd.Series.str.split()` with argument `expand = True`. You will get four columns. For example, for the second row:
```
'#hot#summer#holiday'
```
it returns the following list:
```
['', 'hot', 'summer', 'holiday']
```

Remove the first column from the result (the first column contains only empty strings `''`). Then assign the names of the remaining columns as follows:

* `'hashtag1'`
* `'hashtag2'`
* `'hashtag3'`

In response, print result to the console.

#### Expected result:
```
  hashtag1 hashtag2 hashtag3
0     good    vibes     None
1      hot   summer  holiday
2   street     food     None
3  workout     None     None
```