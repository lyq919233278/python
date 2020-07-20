from django.http import HttpResponse
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