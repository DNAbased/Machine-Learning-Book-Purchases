def main():
    import pandas as pd

    def convert_data(file_in, file_out):
        input_data = pd.read_excel(file_in)
        input_data = input_data[['Pages', 'Language', 'Price', 'Price_per_page', 'Gift']]
        input_data.to_csv(file_out, index=False)


    convert_data('../_book_data/books.xlsx', 'book_data.csv')

if __name__ == '__main__':
    main()
