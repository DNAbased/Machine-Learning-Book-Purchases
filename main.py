def main():
    import pandas as pd

    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    from joblib import dump, load # not implemented yet
    
    books = pd.read_csv('book_data.csv')
    le = preprocessing.LabelEncoder()
    books['Gift'] = le.fit_transform(books['Gift'])
    books['Language'] = le.fit_transform(books['Language'])
    
    X = books[['Price', 'Pages', 'Price_per_page', 'Language']]
    y = books[['Gift']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 321)
      
    y_train = y_train.values.ravel()
    y_test = y_test.values.ravel()

    # scaler = preprocessing.StandardScaler().fit(X_train) # lowers accuracy?
    # X_train_scaled = scaler.transform(X_train)
    # X_test_scaled = scaler.transform(X_test)
    
    KNN = KNeighborsClassifier(n_neighbors=3)
    
    KNN.fit(X_train, y_train)
    
    prediction = KNN.predict(X_test)
    
    print('KNN accuracy : ', accuracy_score(y_test, prediction, normalize = True))

if __name__ == '__main__':
    main()