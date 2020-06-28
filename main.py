import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

books = pd.read_csv('book_data.csv')
le = preprocessing.LabelEncoder()
books['gift'] = le.fit_transform(books['gift'])
books['language'] = le.fit_transform(books['language'])

books_x = books[['price', 'pages', 'price_per_page']]
books_y = books[['gift']]

books_x_train, books_x_test, books_y_train, books_y_test = train_test_split(books_x, books_y, test_size = 0.20, random_state = 123)

svc_model = LinearSVC(random_state=0)

books_y_train = books_y_train.values.ravel()
books_y_test = books_y_test.values.ravel()

pred = svc_model.fit(books_x_train, books_y_train).predict(books_x_test)

print('LinearSVC accuracy : ', accuracy_score(books_y_test, pred, normalize = True))


gnb = GaussianNB()

pred = gnb.fit(books_x_train, books_y_train).predict(books_x_test)

print('Gaussian Naive Bayes accuracy : ', accuracy_score(books_y_test, pred, normalize = True))


neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(books_x_train, books_y_train)

pred = neigh.predict(books_x_test)

print('k-nearest neighbors accuracy score : ', accuracy_score(books_y_test, pred, normalize = True))


# so far, my decisions have obviously not solely been based on the data, hence perfect prediction is difficult
# try with using pages and price instead of price per page, might get better results when using two dimensions
# analyze effect of the books' language on the decision making process


# https://scikit-learn.org/stable/tutorial/machine_learning_map/
