import requests
import re

class Spider:
    """
        [Config]:
            require params: (url, method)
            choice params: (params, pattern)
        [Usage]:
            # init
                test = Spider('http://www.baidu.com', 'get', {'key': 'value'}, r'<title>(.+)</title>')
            # send request
                test.get_info()
    """
    def __init__(self, url, method, params = None, pattern = None):
        self.url = url
        self.method = method
        self.params = params
        self.pattern = pattern
    def get_info(self):
        def get():
            if self.params:
                r = requests.get(url = self.url, params = self.params)
            else:
                r = requests.get(url = self.url)
            return r
        def post():
            if self.params:
                r = requests.post(url = self.url, data = self.params)
            else:
                r = requests.post(url = self.url)
        switcher = {'get': get(), 'post': post()}
        try:
            response = switcher.get(self.method, 'none')
            p = self.pattern
            origin_data = response.text
            if self.pattern:
                r = re.findall(p, origin_data)
                return r
            else:
                return origin_data
        except:
            print('Error!!')
            return 'null'
        finally:
            print('************finish***********')
