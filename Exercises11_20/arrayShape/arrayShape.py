from sklearn.datasets import load_iris


data_raw = load_iris()

data = data_raw['data']
target = data_raw['target']

print(data.shape)
print(target.shape)