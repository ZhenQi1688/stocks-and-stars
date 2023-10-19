import baostock as bs
import pandas as pd
import threading
import time
from tqdm import tqdm
# 这是一个可以下载A股数据好接口
def download_data():
    lg = bs.login()
    rs = bs.query_history_k_data_plus("sz.000001",
        "date,time,code,open,high,low,close,volume,amount",
        start_date='1999-07-26', end_date=time.strftime("%Y-%m-%d", time.localtime()),
        frequency="5", adjustflag="3")
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    result.to_csv('pingan.csv', index=False)
    bs.logout()

def show_progress():
    pbar = tqdm(total=100)
    while True:
        if pbar.n >= 100:
            break
        pbar.update(10)
        time.sleep(1)
    pbar.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=download_data)
    t2 = threading.Thread(target=show_progress)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
