import requests
import re

class Spider:
    """
        [Config]:
            require params: (url, method)
            choice params: (optional_config: pattern, params, headers, proxies)
        [Usage]:
            # init
                test = Spider(url = 'http://www.baidu.com', method = 'get', optional_config = {'params': {'key': 'value'}, 'pattern': r'<title>(.+)</title>'})
            # send request
                test.get_info()
    """
    def __init__(self, url, method, optional_config = None):
        self.url = url
        self.method = method
        self.optional_config = optional_config
    def get_info(self):
        url = self.url
        method = self.method
        params = None
        pattern = None
        headers = None
        proxies = None
        response = None
        origin_data = None
        if isinstance(self.optional_config, dict):
            params = self.optional_config.get('params', None)
            pattern = self.optional_config.get('pattern', None)
            headers = self.optional_config.get('headers', None)
            proxies = self.optional_config.get('proxies', None)
        try:
            if method == 'get':
                print(url, method, params, headers, proxies)
                response = requests.get(url = url, params = params, headers = headers, proxies = proxies)
            elif method == 'post':
                response = requests.post(url = url, params = params, headers = headers, proxies = proxies)
            if response:
                origin_data = response.text
            if pattern and origin_data:
                r = re.findall(pattern, origin_data)
                return r
            else:
                return origin_data
        except:
            print('Error!!')
            return 'null'
        finally:
            print('************finish***********')
# test code
if __name__ == '__main__':
    test = Spider(url = 'http://www.bilibili.com', method = 'get', optional_config = {'pattern': r'<title>(.+)</title>'})
    print(test.get_info())