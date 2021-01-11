from skimage.measure import compare_ssim
import cv2
import numpy as np
from collections import Counter
def splitPicture():
    toValue=lambda rgb:rgb[0]*256*256+rgb[1]*256+rgb[2]
    toList=lambda rgb:[rgb//65536,(rgb//256)%256,rgb%256]
    img=cv2.imread('tmp.png')
    h,w=len(img),len(img[0])//4-1
    for i in range(4):
        pic=img[0:h,i*w:(i+1)*w]
        tmp=[list(i) for i in pic]
        tmp1=[]
        dic={}
        for j in tmp:
            tmp1+=j
        tmp1=[toValue(i)for i in tmp1]
        dic=Counter(tmp1).most_common(2)
        for y in range(h):
            for x in range(w):
                if (toValue(pic[y][x]) ==dic[1][0]):
                    pic[y][x]=[0,0,0]
                else:
                    pic[y][x]=[255,255,255]
        cv2.imwrite('result'+str(i)+'.png',pic)
def identify():
    splitPicture()
    result=''
    for i in range(4):
        img1 = cv2.imread('result'+str(i)+'.png')
        maxSim=0
        bestPic=0
        for j in range(1,10):
            img2 = cv2.imread('numPics/'+str(j)+'.png')
            img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
            ssim =  compare_ssim(img1, img2, multichannel = True)
            if (ssim>maxSim):
                maxSim=ssim
                bestPic=j
        result+=str(bestPic)
    return result
