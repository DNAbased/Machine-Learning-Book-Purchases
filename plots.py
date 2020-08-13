import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import seaborn as sns

books = pd.read_csv('book_data.csv')

sns.set()
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.boxplot(data=books, x='Gift', y='Price_per_page')
g.set(xlabel='Gift', ylabel='Price per page [Euro]')
fig.savefig('img/boxplot_price_per_page.png', dpi=600)

sns.set()
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.boxplot(data=books, x='Gift', y='Price')
g.set(xlabel='Gift', ylabel='Price [Euro]')
fig.savefig('img/boxplot_price.png', dpi=600)

sns.set()
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.boxplot(data=books, x='Gift', y='Pages')
g.set(xlabel='Gift', ylabel='Pages')
fig.savefig('img/boxplot_pages.png', dpi=600)

sns.set()
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.scatterplot(data=books, x='Pages', y='Price', hue='Gift')
g.set(xlabel='Pages', ylabel='Price [Euro]')
fig.savefig('img/scatterplot_price_pages.png', dpi=600)

# from scipy import stats
# crosstable = pd.crosstab(books['language'], books['gift'])
# stats.chi2_contingency(crosstable)
# 1: chi2 stat; 2: p value; 3: degrees of freedom; 4: table
