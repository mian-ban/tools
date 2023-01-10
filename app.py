#requests 发送请求模块
#lxml 解析数据模块
#flask 提供web服务
import requests
from lxml import etree
from flask import Flask,render_template,request

app =Flask(__name__) # 创键一个可以支持web应用的对象

def get_modile(phone):
    #发送请求地址
    url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
    # 伪装
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    # 发送
    resp = requests.get(url,headers = headers)
    # 设置中文
    resp.encoding = 'utf-8'
    # 解析数据
    e = etree.HTML(resp.text)
    # 编写xpath提取数据
    datas = e.xpath('//tr/td[2]/span/text()')
    # 解析响应
    return datas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_phone') # 建立路由
def search_phone():
    phone = request.args.get('phone')
    data = get_modile(phone)
    return '<br/>'.join(data)

app.run(debug=True)
