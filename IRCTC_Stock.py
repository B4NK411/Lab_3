import pandas as pd


def read(x, sheet_name):
    data = pd.read_excel(x, sheet_name=sheet_name)
    return data


Data = read("Lab_Session1_Data.xlsx", sheet_name="IRCTC Stock Price")
Price=Data[["Price"]].values
print(F"Mean value of Prices is {Price.mean()}")
print(f"Variance of Prices is {Price.var()}")
