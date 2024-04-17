import pandas as pd
import re

# Đọc dữ liệu từ file CSV
df = pd.read_csv('customer.csv')

# Lọc dữ liệu trùng
df_duplicates = df[df.duplicated()]

# Lọc dữ liệu trống
df_empty = df[df.isnull().any(axis=1)]

# Lọc kí tự đặc biệt ở row tuỳ chỉnh
def contains_special_characters(s):
    if isinstance(s, str):
        return bool(re.search('[^A-Za-z0-9\s]+', s))
    return False

#Name là tên cột trong bảng cần lọc dữ liệu có kí tự đặc biệt
df_special_chars = df[df['Name'].apply(contains_special_characters)]

# In kết quả
print("Dữ liệu trùng:")
print(df_duplicates)

print("\nDữ liệu trống:")
print(df_empty)

print("\nDữ liệu chứa kí tự đặc biệt:")
print(df_special_chars)


# Xóa dữ liệu không mong muốn
df_cleaned = df.drop(df_duplicates.index)
df_cleaned = df_cleaned.drop(df_empty.index)
df_cleaned = df_cleaned.drop(df_special_chars.index)

# Lưu DataFrame vào file CSV mới
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("Đã lưu dữ liệu đã lọc vào file cleaned_data.csv")
