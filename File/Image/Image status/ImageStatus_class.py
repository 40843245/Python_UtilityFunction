import PIL
from PIL import ImageStat

class ImageStatus():
    
    def __init__(self
                 ,im
                 ,mask
                 ):
        self.im=im
        self.im_stat=PIL.ImageStat(im)
        self.im_stat_class=self.im_stat(image_or_list=self.im,mask=mask)
        
    def __list__(self):
        im=self.im_stat_class
        li=[
            im.sum
            ,im.sum2
            ,im.mean
            ,im.median
            ,im.var
            ,im.stddev
            ,im.rms
            ,im.count
            ,im.extrama
            ]
        return li
