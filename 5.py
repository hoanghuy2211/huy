
import pandas as pd
dataframe_ex = {"a":[1,4,6,7,8],"b":[23,12,56,8,22],"c":[87,65,43,11,34]}
df = pd.DataFrame(dataframe_ex)
df["total"]=df.sum(axis=1)
print(df)

### BTVN tao them 1 cot moi vao dataframe co ten la 'total' gia tri bang tong cac gia tri cot a,b,c
### Sau do luu dataframe ket qua vao file co ten 'ketqua.csv'

