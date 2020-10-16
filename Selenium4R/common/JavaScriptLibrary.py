import json
import os
from json import JSONDecodeError

import requests
from requests.exceptions import RequestException

# JavaScript库下载地址集合
JS_LIBRARY = {
    "jquery": "https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.5.1.min.js"
}


class JavaScriptLibrary(object):
    """JavaScript库地址集合"""

    def __init__(self, cache_path: str):
        self.cache_path = cache_path

    def get(self, name: str) -> str:
        """获取JavaScript库"""
        if name.lower() in JS_LIBRARY:
            # 读取目标JavaScript库的Url
            library_url = JS_LIBRARY[name.lower()]

            # 在缓存文件夹中创建JavaScript库缓存文件夹
            library_list_path = os.path.join(self.cache_path, "libraries.json")

            # 读取缓存JavaScript库列表
            with open(library_list_path, mode="r+") as f1:
                try:
                    library_list = json.loads(f1.read())
                except JSONDecodeError:
                    library_list = {}

                # 当JavaScript库存在于缓存文件夹时，直接读取缓存中的文件
                if library_url in library_list:
                    print("载入缓存中的JavaScript库:", library_list[library_url])
                    with open(library_list[library_url]) as f2:
                        return f2.read()

                # 当JavaScript库不存在于缓存文件夹时，则下载缓存中的文件并存储到缓存文件夹
                else:
                    try:
                        print("下载JavaScript库:", library_url)
                        library_text = requests.get(library_url).text
                        library_path = os.path.join(self.cache_path, "libraries", library_url[library_url.rfind("/") + 1:])

                        library_list[library_url] = library_path

                        # 清空并重新写入列表文件
                        f1.truncate()
                        f1.write(json.dumps(library_list))

                        with open(library_path, mode="w+") as f2:
                            f2.write(library_text)

                        return library_text

                    except RequestException:
                        print("请求下载JavaScript库失败:", library_url)
