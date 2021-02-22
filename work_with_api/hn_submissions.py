from operator import itemgetter

import requests

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Обработка информации о каждой статье.
submissions_ids = r.json()
submissions_dicts = []
for submissions_id in submissions_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submissions_id}.json'
    r = requests.get(url)
    print(f'id: {submissions_id} status code: {r.status_code}')
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    descendants = response_dict.get('descendants') or 0
    submissions_dict = {
        'title': response_dict['title'],
        'hn_link': f'http://news.ycombinator.com/item?id={submissions_id}',
        'comments': descendants,
    }
    submissions_dicts.append(submissions_dict)

submissions_dict = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)

for submissions_dict in submissions_dicts:
    print(f'\nTitle: {submissions_dict["title"]}')
    print(f'Discussion link: {submissions_dict["hn_link"]}')
    print(f'Comments: {submissions_dict["comments"]}')
