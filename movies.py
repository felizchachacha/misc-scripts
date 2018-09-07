def fetchData(str, page=1):
    base_url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title={title}&page={page}'

    url = base_url.format(title=str, page=page)
    print(url)
    try:
        resp = urlopen(url)
    except URLError as e:
        print('Fetch data error:', e.reason)
        return []
    return json.loads(resp.read().decode('utf-8'))

def getMovieTitles(substr):
    data = fetchData(substr, 1)
    total = [movie['Title'] for movie in data['data']]
    total_pages = int(data['total_pages'])
    if total_pages > 1:
        for page_num in range(int(total_pages)):
            page_query = page_num + 1
            if page_query == 1:
                continue
            dt = fetchData(substr, page_query)
            total += [movie['Title'] for movie in dt['data']]
    else:
        return sorted(total)
    return sorted(total)
