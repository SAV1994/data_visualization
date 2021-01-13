import csv
from datetime import datetime

from matplotlib import pyplot as plt

while True:
    # Выбор пользователем станции
    response = input('Введите:\n\t1 - для просмотра данных о DEATH VALLEY, CA US'
                     '\n\t2 - для просмотра данных о SITKA AIRPORT, AK US\n\tq - для выхода\n>>> ')
    filename1 = 'data/death_valley_2018_simple.csv'
    filename2 = 'data/sitka_weather_2018_simple.csv'
    if response in ('q', 'Q'):
        break
    elif response == '1':
        filename = filename1
    else:
        filename = filename2

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Определение индексов нужных данных
        for index, header in enumerate(header_row):
            if header == 'DATE':
                date_index = index
            elif header == 'TMAX':
                t_max_index = index
            elif header == 'TMIN':
                t_min_index = index
            elif header == 'NAME':
                place_index = index

        # Получение дат, температурных максимумов и минимумов из файла.
        dates, highs, lows = [], [], []
        place = None
        for row in reader:
            if not place:
                place = row[place_index]
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[t_max_index])
                low = int(row[t_min_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    # Нанесение данных на диаграмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    ax.set_ylim(20, 140)

    # Форматирование диграммы.
    plt.title(f'Daily high and low temperatures - 2018\n{place}', fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
