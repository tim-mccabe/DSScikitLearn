## Train Test Split

The IRIS dataset was loaded into *data* and *target* variables.

Using the *scikit-learn* package and the `train_test_split()` function, split the data into the training set (*data_train*, *target_train*) and the test set (*data_test*, *target_test*). Set the test size to 30% of the samples.

As an answer, print the shapes of the following arrays:

* *data_train*
* *target_train*
* *data_test*
* *target_test*

**Tip:** More about `train_test_split()` function: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

#### Expected result:
```
data_train shape: (105, 4)
target_train shape: (105,)
data_test shape: (45, 4)
target_test shape: (45,)
```