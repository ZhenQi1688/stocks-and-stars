# 这个程序将gw.csv与PLR结合，产生一份在5分钟行情线上对应行星的位置数据positions.csv。
import csv
import datetime
from tqdm import tqdm
from PLR import SolarSystem


# 从CSV文件中读取日期时间
with open('gw.csv', 'r') as f:
    reader = csv.DictReader(f)
    positions = []
    
    for row in tqdm(reader, desc='Calculating positions'):
        date_str = row['date']
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')

        # 创建 SolarSystem 实例并获取位置信息
        solar_system = SolarSystem(date)
        current_positions = solar_system.get_positions()

        # 将位置信息添加到列表中
        row_data = [date]
        for position in current_positions:
            position_str = str(position)
            ra_str, dec_str = position_str.split(',')
            ra_str = ra_str.split('_')[1].strip().replace("RA:", "")
            dec_str = dec_str.split('_')[1].strip().replace("Dec:", "")
            row_data.extend([ra_str, dec_str])








        positions.append(row_data)

# 打开 CSV 文件进行写入
with open('positions.csv', 'w', newline='') as f:
    # 写入 CSV 文件头部
    writer = csv.writer(f)
    writer.writerow(['date',
                      'Mercury_RA', 'Mercury_Dec',
                      'Venus_RA', 'Venus_Dec',
                      'Mars_RA', 'Mars_Dec',
                      'Jupiter_RA', 'Jupiter_Dec',
                      'Saturn_RA', 'Saturn_Dec',
                      'Uranus_RA', 'Uranus_Dec',
                      'Neptune_RA', 'Neptune_Dec',
                      'Pluto_RA', 'Pluto_Dec',
                      'Earth_RA', 'Earth_Dec',
                      'Moon_RA', 'Moon_Dec',
                      'Io_RA', 'Io_Dec',
                      'Europa_RA', 'Europa_Dec',
                      'Ganymede_RA', 'Ganymede_Dec',
                      'Callisto_RA', 'Callisto_Dec',
                      'Mimas_RA', 'Mimas_Dec',
                      'Enceladus_RA', 'Enceladus_Dec',
                      'Tethys_RA', 'Tethys_Dec',
                      'Dione_RA', 'Dione_Dec',
                      'Titan_RA', 'Titan_Dec',
                      'Rhea_RA', 'Rhea_Dec'])

    # 写入位置信息
    for row_data in tqdm(positions, desc='Writing data to file'):
        writer.writerow(row_data)
