# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 12:27
# @Author  : Oscar

from django.http import StreamingHttpResponse, HttpResponse


def file_download(request):
    """
    最简单的文件下载功能
    """

    # do something...

    with open('file_name.txt', 'rb') as f:
        c = f.read()
    return HttpResponse(c)


def big_file_download(request):
    """
    Django 实现文件下载功能
        Django的HttpResponse对象允许将<迭代器>作为传入参数，将上面代码中的传入参数c换成一个迭代器，
        便可以将上述下载功能优化为对大小文件均适合；而Django更进一步，推荐使用 StreamingHttpResponse对象取代HttpResponse对象，
        StreamingHttpResponse对象用于将文件流发送给浏览器，与HttpResponse对象非常相似，对于文件下载功能，
        使用StreamingHttpResponse对象更合理。
    """

    # do something...

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "big_file.csv"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response


