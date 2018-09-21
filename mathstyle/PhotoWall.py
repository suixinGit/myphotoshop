
# coding: utf-8

# In[1]:


'''将图片像素化'''
#输入一幅图片，要求黑底白字
#图像放大至短边
#矩阵化
#填图，纵边同一化
#
import cv2
import numpy as np 
import os
import sys
import ssl
import urllib.request
import json
import string
#文件选择对话框对话框依赖模块
import time
import json
import random
#python生成GUID
import uuid
import copy
import glob as gb


# In[2]:


def Get_File_list(imgFoldName):
    filelist = os.listdir(imgFoldName)
    fileNum = len(filelist)
    return filelist,fileNum


# In[3]:


def Get_Image_list(imgFoldName,format_pic):
    img_path_list = gb.glob(imgFoldName + '/*.' + format_pic) 
    imgNum = len(img_path_list)
    return img_path_list,imgNum


# In[4]:


def GetFiledImage(image_height,image_width,image_nchanels,imglist,pix_height):
    imagex_start = 0
    imagey_start = 0
    field_image = np.zeros((image_height,image_width,image_nchanels), np.uint8)
    image_num = len(imglist)
    isaddable = False
    if(image_height > pix_height and image_width > 0):
        isaddable = True
    while isaddable:
        image_index = random.randint(0,(image_num-1))
        image_file = imglist[image_index]
        image = cv2.imread(image_file)
        height_img = image.shape[0]
        width_img = image.shape[1]
        pix_width = round(width_img*pix_height/height_img)
        pix_img = cv2.resize(image,(pix_width,pix_height),interpolation=cv2.INTER_AREA)
        if((imagex_start+pix_width)<image_width):
            #print(imagex_start,imagey_start)
            field_image[imagey_start:(imagey_start+pix_height),imagex_start:(imagex_start+pix_width)] = copy.deepcopy(pix_img)
            imagex_start = imagex_start+pix_width
        else:
            imagex_start = 0
            if((imagey_start+2*pix_height)< image_height):
                imagey_start = imagey_start+pix_height
            else:
                #print(isaddable)
                isaddable = False
    cv2.imwrite('Image_pic1.jpg',field_image)
    return field_image


# In[5]:


def ImageMerge(img,img_mask):
    height_img_mask = img_mask.shape[0]
    width_img_mask = img_mask.shape[1]
    for i in range(height_img_mask):
        for j in range(width_img_mask):
            if(img_mask[i,j] < 100):
                #print(i,j)
                img[i,j,:] = 0
                #print(img)
                #img[i,j] = 0 # 这里可以处理每个像素点
    cv2.imwrite('result.jpg',img)
    


# In[6]:


if __name__ == '__main__':
    imgFoldName = '/home/zhangjie/mathstyle/pic_backed'
    img_format = 'JPG'
    pix_height = 100
    pix_width = 100
    image_height = 10000
    image_width = 10000
    image_nchanels = 3
    #pix_height = 12
    
    #img = cv2.imread('/home/zhangjie/CarRec/20180706/201807061/201807060850_85b50e90-80b6-11e8-bbe5-000c297a242a.jpg')
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换了灰度化
    #retval, im_at_fixed = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY) 
    #height_mash = im_at_fixed.shape[0]
    #width_mash = im_at_fixed.shape[1]

    #将阈值设置为50，阈值类型为cv2.THRESH_BINARY，则灰度在大于50的像素其值将设置为255，其它像素设置为0
    imglist,imgnum = Get_Image_list(imgFoldName,img_format)
    #print(imglist,imgnum)
    field_image = GetFiledImage(image_height,image_width,3,imglist,pix_height)
    #ImageMerge(field_image,im_at_fixed)
    

