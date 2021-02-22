from operator import itemgetter
from plotly import offline
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

submissions_ids = r.json()
news = []
for submissions_id in submissions_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submissions_id}.json'
    r = requests.get(url)
    print(f'id: {submissions_id} status code: {r.status_code}')
    response_dict = r.json()

    title = response_dict['title']
    link = f'http://news.ycombinator.com/item?id={submissions_id}'
    news_link = f'<a href="{link}">{title}</a>'
    comments_number = response_dict.get('descendants') or 0
    news.append({'link': news_link, 'comments': comments_number})

news = sorted(news, key=itemgetter('comments'), reverse=True)
news_links, comments = [item['link'] for item in news], [item['comments'] for item in news]
# Построение визуализации.
data = [{
    'type': 'bar',
    'x': news_links,
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Commented News on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')