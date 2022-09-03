## Is NULL Sum

The *df DataFrame* is given below:
```
  hashtag1 hashtag2 hashtag3
0     good    vibes     None
1      hot   summer  holiday
2   street     food     None
3  workout     None     None
```
Create a new column `'missing'` and assign the number of missing hashtags for each row as shown below. For example:

* row one -> 1
* row two -> 0
* row three -> 1, etc.

As an answer, print the df DataFrame to the console.

#### Expected result:
```
  hashtag1 hashtag2 hashtag3  missing
0     good    vibes     None        1
1      hot   summer  holiday        0
2   street     food     None        1
3  workout     None     None        2
```