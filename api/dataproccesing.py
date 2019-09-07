import pandas as pd

if __name__ == "__main__":
    file_errors_location = 'dataset.xlsx'
    df = pd.read_excel(file_errors_location)
    print(df)