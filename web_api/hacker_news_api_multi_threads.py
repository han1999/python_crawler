import json
import threading
import time

import requests
from operator import itemgetter

item_msgs = []
def run_http(resp_json, start_index, end_index):
    for item_id in resp_json[start_index:end_index]:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        r = requests.get(item_url)
        print(f"{item_id}, status code: {r.status_code}")
        item_resp = r.json()
        print(item_resp)
        item_msgs.append({
            'title': item_resp['title'] if 'title' in item_resp else 'None',
            'url': item_resp['url'] if 'url' in item_resp else 'None',  # python3删除了has_key()方法
            'comment': item_resp['descendants'] if 'descendants' in item_resp else 0
        })

if __name__ == '__main__':
    start_time=time.time()
    # url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    resp_json = r.json()
    # file = 'hacker_news_item19155826.json'
    file = 'hacker_news_data.json'
    # with open(file, 'w') as f:
    #     json.dump(resp_json, f, indent=4)

    Threads = []
    for i in range(0, 250):
        t = threading.Thread(target=run_http, args=(resp_json, 2*i, 2*(i+1),))
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
    item_msgs.sort(key=itemgetter('comment'), reverse=True)
    # item_msgs=sorted(item_msgs,key=itemgetter('comment'), reverse=True)

    top_story_file = 'top_story.txt'
    with open(top_story_file, mode='w', encoding='utf-8') as f:
        for item_msg in item_msgs:
            f.write(str(item_msg)+"\n")
            print(item_msg)
    end_time=time.time()
    print('耗时(s): ', end_time-start_time)