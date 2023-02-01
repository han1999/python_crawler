import csv
from matplotlib import pyplot as plt
from datetime import datetime

if __name__ == '__main__':
    # file = 'sitka_weather_07-2018_simple.csv'
    file = 'sitka_weather_2018_simple.csv'
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)
        for index, header in enumerate(header_row):
            print(index, header)
        # reader要先迭代一次
        dates, lows, highs = [], [], []
        for row in reader:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"missing data for {date}")
            else :
                highs.append(high)
                lows.append(low)
                dates.append(date)

        # print(dates)
        # print(highs)

    plt.rcParams["font.sans-serif"] = ['SimHei']  # 不加会乱码
    fig, ax = plt.subplots(figsize=(15,9))
    # ax.scatter(x, highs, c=highs, cmap=plt.cm.Reds)
    ax.plot(dates, highs, c='red', alpha=0.8)
    ax.plot(dates, lows, c='blue', alpha=0.8)
    ax.fill_between(dates, lows, highs, facecolor='green', alpha=0.2)

    ax.set_xlabel('日期', fontsize=22)
    ax.set_ylabel('最高温度(F)', fontsize=22)
    ax.set_title('2018全年最高最低温度', fontsize=22)
    ax.tick_params(labelsize=18)
    fig.autofmt_xdate()

    plt.show()
