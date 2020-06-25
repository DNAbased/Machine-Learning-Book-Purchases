def main():
    import pandas as pd

    def convert_data(file_in, file_out):
        input_data = pd.read_excel(file_in)
        input_data = input_data[['pages', 'language', 'price', 'price_per_page', 'gift']]
        input_data.to_csv(file_out, index=False)


    convert_data('../book_data/books.xlsx', 'book_data.csv')

if __name__ == '__main__':
    main()
