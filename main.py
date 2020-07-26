def main():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    from joblib import dump, load
    import argparse

    parser = argparse.ArgumentParser(description='Book ML: gift or not', usage='%(prog)s [options]')
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('-m', '--model', action='store_true')
    parser.add_argument('-p', '--price', type=float)
    parser.add_argument('-q', '--pages', type=int)
    parser.add_argument('-l', '--language', type=str)
    args = parser.parse_args()
    
    if args.test:
        books = pd.read_csv('book_data.csv')
        # le = preprocessing.LabelEncoder()
        # books['Gift'] = le.fit_transform(books['Gift'])
        # books['Language'] = le.fit_transform(books['Language']) # need to do this separately to be able to do it in the predictions later on as well
        gift = {'No': 0, 'Yes': 1}
        language = {'English': 0, 'German': 1}

        books['Gift'] = [gift[item] for item in books['Gift']]
        books['Language'] = [language[item] for item in books['Language']]


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

    elif args.model:
        books = pd.read_csv('book_data.csv') # combine this for both first ifs
        gift = {'No': 0, 'Yes': 1}
        language = {'English': 0, 'German': 1}

        books['Gift'] = [gift[item] for item in books['Gift']]
        books['Language'] = [language[item] for item in books['Language']]

        X = books[['Price', 'Pages', 'Price_per_page', 'Language']]
        y = books[['Gift']]

        y = y.values.ravel()

        KNN = KNeighborsClassifier(n_neighbors=3)
        
        KNN.fit(X, y)

        dump(KNN, 'KNN_book_model.joblib')

    else:
        KNN = load('KNN_book_model.joblib')

        ppp = args.price / args.pages
        if args.language in ['EN', 'en', 'English', 'english', '1']:
            language = 0
        else:
            language = 1
        user_input = pd.DataFrame({'Pages': [args.pages], 'Price': [args.price], 'Price_per_page': [ppp], 'Language': [language]})

        prediction = KNN.predict(user_input)

        if prediction == [0]:
            print('Purchase')
        else:
            print('Gift')

if __name__ == '__main__':
    main()