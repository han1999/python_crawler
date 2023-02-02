import json

import requests
from plotly.graph_objs import Bar
from plotly import offline

if __name__ == '__main__':
    # url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    url = 'https://api.github.com/search/repositories?q=language:golang&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"status code:{r.status_code}")
    resp_json = r.json()
    print(resp_json.keys())

    # github_json_file='github_python.json'
    # with open(github_json_file, 'w') as f:
    #     json.dump(resp_json, f, indent=4)

    repos = resp_json['items']
    print(f"items: {len(repos)}")

    first_repo = repos[0]
    print(f"keys num: {len(first_repo)}")

    for key in sorted(first_repo.keys()):
        print(key)

    repo_links, stars, labels= [], [], []
    for repo in repos:
        # href 要加 ''
        repo_links.append(f"<a href='{repo['html_url']}'>{repo['name']}</a>")
        stars.append(repo['stargazers_count'])
        owner = repo['owner']['login']
        desc = repo['description']
        label= f"{owner}<br />{desc}"
        labels.append(label)

    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        # 'marker': {
        #     'color': 'rgb(60,100,150)',
        #     'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        # },
        # 'opacity':0.6
        'hovertext':labels
    }]
    mylayout = {
        # 'title': 'Github上最受欢迎的python项目',
        'title': 'Github上最受欢迎的golang项目',
        'xaxis': {'title': '仓库名'},
        'yaxis': {'title': '星数'}
    }
    fig = {'data': data, 'layout': mylayout}
    # offline.plot(fig, filename='python_github_repo.html')
    offline.plot(fig, filename='golang_github_repo.html')
