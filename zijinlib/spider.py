import urllib
import urllib.request
import http.cookiejar

# get方式请求网页，尝试解码，返回网页源码
def open(url, charset=None):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    if charset:
        print('您已指定编码：' + charset)
    else:
        charset = judge_charset(response)

    content = response.read()
    response = try_decode(content, charset)
    return response

# post方式发送请求，尝试解码，返回网页源码
def post(url, data=None, headers=None, charset=None):
    form_data = urlencode(data)
    request = urllib.request.Request(url, data=form_data, headers=headers)
    response = urllib.request.urlopen(request)

    if charset:
        print('您已指定编码：' + charset)
    else:
        charset = judge_charset(response)

    content = response.read()
    response = try_decode(content, charset)
    return response

# url编码
def urlencode(data):
    form_data = urllib.parse.urlencode(data).encode('utf-8')
    return form_data

# 开启http上网代理
def open_proxy(proxy):
    print('已启用HTTP代理 ' + proxy)
    set_proxy = urllib.request.ProxyHandler({'http': proxy})  # 设置proxy
    opener = urllib.request.build_opener(set_proxy)  # 挂载opener
    urllib.request.install_opener(opener)  # 安装opener
    return

# Cookie类
class Cookie:
    def __init__(self):
        self.cookie_object = self.__open_cookie()

    def __open_cookie(self):
        print('开启cookie')
        cookie_object = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie_object)
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)
        return cookie_object

    def __read(self):
        self.cookies = {}
        for i in self.cookie_object:
            self.cookies[i.name] = i.value
        return self.cookies

    def get(self, key):
        self.cookies = self.__read()
        value = self.cookies.get(key)
        return value

    def __str__(self):
        self.cookies = self.__read()
        return str(self.cookies)

# 判断网页编码
def judge_charset(response):
    charset = response.info().get_param('charset')
    if charset:
        print('您未指定编码，自动检测结果：' + charset)
    else:
        charset = 'utf-8'
        print('您未指定编码，自动检测失败，尝试使用utf-8解码')
    return charset

# 尝试解码
def try_decode(content, charset):
    try:
        response = content.decode(charset)
    except Exception as e:
        response = content
        print('编码解析失败，为您返回源码')
    return response
