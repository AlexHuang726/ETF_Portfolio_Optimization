# 匯入套件
from FinMind.data import DataLoader
import pandas as pd

# 初始化 FinMind API
api = DataLoader()

# 選擇要抓的 ETF 代號
etf_list = ["0050", "00878", "006208"]

# 抓取資料的起始日期
start_date = "2020-01-01"

# 建立空的 DataFrame 來存所有 ETF 的資料
all_data = pd.DataFrame()

for etf in etf_list:
    print(f"正在抓取 {etf} 資料...")
    data = api.taiwan_stock_daily(
        stock_id=etf,
        start_date=start_date
    )
    # 只保留日期與收盤價
    data = data[["date", "stock_id", "close"]]
    all_data = pd.concat([all_data, data])

# 將資料儲存成 CSV
all_data.to_csv("data/etf_price_raw.csv", index=False, encoding="utf-8-sig")
print("資料抓取完成，已儲存到 data/etf_price_raw.csv")
