import requests
import os
import hashlib

def download(url):
    try:
        print('准备下载视频:' + url)
        response = requests.get(url)
        data = response.content
        if data:
            file_path = '{}/{}.{}'.format(os.getcwd(), hashlib.md5(data).hexdigest(), 'mp4')
            print('文件为:' + file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(data)
                    f.close()
                    print('视频下载成功:' + url)
    except Exception:
        print('视频下载失败')


if __name__ == '__main__':
    url = "https://morvanzhou.github.io/static/results/reinforcement-learning/mountaincar%20dqn.mp4"
    download(url)
