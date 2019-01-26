import base64
import os
from django.http import HttpResponse
import infer


#图片存储/读取  输入：username，图片文件  输出：是否成功，存储路径，分类结果
def photo_classify(account_id, img):
    data = {'success': 0, 'path': '', 'type': 67}
    imgdir = open('./' + img.name, 'wb+')
    for chunk in img.chunks():
        imgdir.write(chunk)
    imgdir.close()
    data['success'] = 1
    data['path'] = imgdir
    data['type'] = test('../static/' + img.name)  # infer函数需修改，输入图片路径，返回分类结果
    return data


def test(dir):
    return("here")

