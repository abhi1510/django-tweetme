import os
import json
import django
import requests

from web import settings

base_dir = settings.BASE_DIR
base_url = 'https://jsonplaceholder.typicode.com/'
uf_path = os.path.join(base_dir, 'users', 'fixtures')
tf_path = os.path.join(base_dir, 'tweets', 'fixtures')
img_path = os.path.join(base_dir, 'media', 'users')

def fetch_users():
    url = f'{base_url}users'
    res = requests.get(url)
    return res.status_code, res.json()

def fetch_posts():
    url = f'{base_url}posts'
    res = requests.get(url)
    return res.status_code, res.json()

def fetch_photos():
    url = f'{base_url}photos'
    res = requests.get(url)
    return res.status_code, res.json()[:10]
       
def parse_posts_data():
    _data = []
    _status, _json = fetch_posts()
    if _status == 200:
        print('Posts fetched!')
        for post in _json:
            _data.append({
                "model": "tweets.tweet",
                "fields": {
                    'author_id': post.get('userId'),
                    'content': post.get('title')
                }
            })
        return _data
    else:
        raise Exception('Failed to fetch posts')   

def parse_photos_data():
    _data = []
    _counter = 1
    _status, _json = fetch_photos()
    if _status == 200:
        print('Photos fetched!')
        for photo in _json:
            p_url = photo.get('thumbnailUrl')
            fname = p_url.split('/')[-1]
            _data.append({
                "model": "users.profile",
                "pk": _counter,
                "fields": {
                    'user_id': _counter,
                    'avatar': f'/users/{fname}.png'
                }
            })
            _counter += 1
        return _data
    else:
        raise Exception('Failed to fetch photos') 

def create_profile_fixtures(dict_data):
    file_path = os.path.join(uf_path, 'profiles.json')
    f = open(file_path, 'w')
    f.write(json.dumps(dict_data, indent=4, sort_keys=True))
    f.close()
    print('Profiles fixtures created!\n')

def create_tweets_fixtures(dict_data):
    file_path = os.path.join(tf_path, 'tweets.json')
    f = open(file_path, 'w')
    f.write(json.dumps(dict_data, indent=4, sort_keys=True))
    f.close()
    print('Tweets fixtures created!\n')

def download_photos():
    global img_path
    _status, _json = fetch_photos()
    if _status == 200:
        print('Photos fetched!')
        for photo in _json:
            url = photo.get('thumbnailUrl')
            f_name = url.split('/')[-1]
            img = requests.get(url).content
            print(f'\n\tFetched photo on url: {url}!')
            file_path = os.path.join(img_path , f'{f_name}.png')
            with open(file_path, 'wb') as handler:
                handler.write(img)
                print('\tSaved photo!')

def main():
    
    if not os.path.exists(uf_path):
        os.mkdir(uf_path)
    
    if not os.path.exists(tf_path):
        os.mkdir(tf_path)

    if not os.path.exists(img_path):
        os.mkdir(img_path)
    
    parsed_p_data = parse_posts_data()
    create_tweets_fixtures(parsed_p_data)

    # download_photos()

    parsed_p_data = parse_photos_data()
    create_profile_fixtures(parsed_p_data)

        
if __name__ == '__main__':
    main()