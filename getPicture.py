from PIL import Image,ImageDraw,ImageFont
import random

def getRandomColor(low,high):
    return (random.randint(low,high),random.randint(low,high),random.randint(low,high))

def getPicture(string_get):
    width,height = 800,270
    image = Image.new('RGB',(width,height),getRandomColor(20,100))
    font = ImageFont.truetype('C:/Windows/fonts/SIMLI.TTF',80)
    font_name = ImageFont.truetype('C:/Windows/fonts/stxinwei.ttf',18)
    draw = ImageDraw.Draw(image)
    string = string_get
    string_list=string.split('---')
    string=string_list[0]+'-'+string_list[1]
    if(string_list[0][0].encode( 'UTF-8' ).isalpha()):
        first_is_english=1
    else:
        first_is_english=0
    enter=0
    count=0
    for i in range(len(string)):
        if(first_is_english==1):   #英译汉
            if(string[i]=='-'):
                enter=1
                continue
            if(enter==0):
                count+=1
                draw.text((40*i+10,20),string[i],font = font,fill=getRandomColor(100,200))
            else:
                draw.text((75*(i-count)+10,160),string[i],font = font,fill=getRandomColor(100,200))
        else:                       #汉译英
            if(string[i]=='-'):
                enter=1
                continue
            if(enter==0):
                count+=1
                draw.text((75*i+10,20),string[i],font = font,fill=getRandomColor(100,200))
            else:
                draw.text((40*(i-count)+10,160),string[i],font = font,fill=getRandomColor(100,200))
    draw.text((680,245),'@SXU-贾镇宇',font = font_name,fill=getRandomColor(100,200))
    image.save('./share/img/%s.jpg' % string)
    return r'.\share\img\%s.jpg' % string