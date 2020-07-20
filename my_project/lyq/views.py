from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
def demo_response(request):

    str = '{"name": "python"}'
    # 返回一个 HttpResponse 响应对象
    return HttpResponse(
        str,                              # 返回数据
        content_type="application/json",  # 指定返回数据的的 MIME 类型。
        status=400                        # 返回HTTP响应状态码
    )

# 创建一个 response 对象
response = HttpResponse()

# 常规用法:
def demo_view(request):
    return HttpResponse('cast python', status=400)

# 或者想这样使用:
def demo_view2(request):
    # 创建一个 response 对象
    response = HttpResponse('cast python', status=400)
    # 在 response 对象中添加一个新的键值对
    response['cast'] = 'Python'
    # 返回 response
    return response

def demo_json(request):
    # 直接返回 JsonResponse 这个对象,并且里面可以直接传入dict参数
    dict = {
      'city': 'beijing',
      'subject': 'python'
    }
    return JsonResponse(dict)