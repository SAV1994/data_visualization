import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename2 = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат, температурных максимумов и минимумов из файла.
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        value = float(row[3])
        dates.append(current_date)
        precipitation.append(value)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, c='blue', alpha=0.5)

# Форматирование диграммы.
plt.title('Daily precipitation - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('precipitation (mm)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
