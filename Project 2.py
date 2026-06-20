
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 


data = load_iris()
X = data.data  # Features
y = data.target  # Labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) #scaled to have a mean of 0 and a standard deviation of 1
X_test = scaler.transform(X_test)

model = LogisticRegression(random_state=42, max_iter=200)
model.fit(X_train, y_train)
