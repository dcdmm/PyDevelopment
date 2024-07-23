import asyncio
import requests  # 同步,不支持异步

async def download_image(url):
    print("开始下载", url)

    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, requests.get, url)
    response = await fut
    print("下载完成")
    file_name = "aaa.txt"
    with open(file_name, mode='wb') as obj:
        obj.write(response.content)

if __name__ == '__main__':
    url_list = ['https://www.baidu.com', 'https://www.baidu.com', 'https://www.baidu.com', 'https://www.baidu.com']

    task = [download_image(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task))