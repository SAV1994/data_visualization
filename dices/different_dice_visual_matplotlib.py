from matplotlib import pyplot as plt

from die import Die

# Создание двух кубиков D6 и D10.
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

# Анализ результатов.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Визуализация результатов.
fig, ax = plt.subplots()
x_values = list(range(2, max_result + 1))
ax.bar(x_values, frequencies)

ax.set_title('Results of rolling two D6 and D10 dice 50000 times', fontsize=17)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency of Result', fontsize=14)

plt.show()
