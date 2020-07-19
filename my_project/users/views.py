from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.

# 普通视图
def index(request):

    return HttpResponse("Hello world")

# 方式一：查询字符串方式传参
def get_num(request):
    a = request.GET.getlist('a')
    b = request.GET.get('b')
    print(a)
    print(b)
    return HttpResponse("读取参数成功")

# 方式二：路径方式传参
def weather(request, city, year):
    print(city)
    print(year)
    return HttpResponse(f'读取路径参数成功\n{city}\n{year}')

# 方式三：表单类型参数
def get_body(request):
    a = request.POST.getlist('a')
    b = request.POST.get('b')
    return HttpResponse(f'读取表单数据:{a}，{b}')

# 方式四：非表单方式传参
def get_json(request):
    json_bytes = request.body
    json_str = json_bytes.decode()
    j = json.loads(json_str)
    print(j.get("name"))
    print(j.get("age"))
    return HttpResponse(f'获取非表单数据：{j}')