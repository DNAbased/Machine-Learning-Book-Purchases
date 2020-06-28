# Machine Learning Book Purchases

Contains a data set of nearly all books I have read so far (title and author removed). I wanted to explore the differences in price/length/language of the books depending on the method of acquisition (purchased myself or obtained as a gift).

This might allow me to automate my decision making process (i.e. do I want to purchase this book myself?).

Basic first approaches (support vector machine; k-nearest neighbors; gaussian naive bayes; no standardization yet, convergence warning for SVM) yielded accuracies of up to 88 %. See main.py. 

![Pages](img/boxplot_pages.png)

![Price](img/boxplot_price.png)

![Price_per_page](img/boxplot_price_per_page.png)

![Price_pages](img/scatterplot_price_pages.png)

Book data last updated: 20200627
