import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, header in enumerate(header_row):
        if header == 'latitude':
            latitude_index = index
        elif header == 'longitude':
            longitude_index = index
        elif header == 'brightness':
            brightness_index = index
        elif header == 'scan':
            scan_index = index

    latitudes, longitudes, brightnesses, scans = [], [], [], []
    for row in reader:
        latitudes.append(row[latitude_index])
        longitudes.append(row[longitude_index])
        brightnesses.append(float(row[brightness_index]))
        scans.append(row[scan_index])

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': scans,
    'marker': {
        'size': [brg / 30 for brg in brightnesses],
        'color': [brg for brg in brightnesses],
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightnesses'},
    },
}]
my_layout = Layout(title='World fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
