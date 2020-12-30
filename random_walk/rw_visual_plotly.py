from plotly import express as px

from random_walk import RandomWalk


# Построение случайного блуждания.
rw = RandomWalk(50000)
rw.fill_walk()

# Выделение первой и последней точек.
rw.x_values.append(rw.x_values.pop(0))
rw.y_values.append(rw.y_values.pop(0))
colors = [color for color in range(25001, 74999)] + [100000] + [0]
sizes = [1 for _ in range(49998)] + [25] + [25]

# Нанесение точек на диаграмму.
fig = px.scatter(x=rw.x_values, y=rw.y_values, color=colors, size=sizes)

fig.show()
