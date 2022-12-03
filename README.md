# Yoobit翻译

## 简介
Yoobit翻译是由山西大学贾镇宇开发的基于QyQt5的翻译软件。目前可以进行英译汉与汉译英操作，同时可以记录于个人单词本。并可生成分享图片保存于本地或发送给好友。

## 使用方法
0. 安装依赖库
1. 首先运行sql.py建立单词数据库
2. 运行index.py
3. 在左侧输入框中输入需要翻译的英文（默认英译汉），或在选择框中选择汉译英后输入需要翻译的汉语。
4. 点击翻译按钮，在右侧即可查看翻译结果。
5. 翻译后点击加入单词本按钮即可保存至个人单词本中
6. 点击查看单词本按钮，即可在弹出的单词本窗口中可以查看过去保存的单词
7. 在单词本窗口中选中单词，再点击“记住了”按钮，将删除本单词记录；点击分享按钮即可生成分享图，分享图保存在share/img文件夹下
8. 使用完成后退出软件

## 软件设计
本软件开发目的是为了开发一款纯个人使用的翻译软件，数据库文件保存在本地（userWordBook.db文件），同时将复习、分享等功能集成于软件中，可以更好得起到学习英语的效果。

采用Python开发，使用PyQt5实现GUI，数据库采用sqlite3，并保存于本地。翻译功能使用火山引擎提供文本翻译API接口实现。分享图生成使用PIL库进行图像生成。

依赖库（需提前安装）：
- PyQt5
- PIL
- random
- sqlite3
- os
- json
- volcengine
- sys

## 开发流程

1. 使用Qt Designer绘制UI界面
2. 使用pyuic5将UI文件转化为Python文件。示例代码：`pyuic5 -o mainWindow.py mainWindow.ui`
3. 提前通过pip下载器安装依赖库。示例代码：`pip install PyQt5`
4. 编写核心代码
5. 测试运行
6. 可选项：可使用`PyInstaller`库对文件进行打包成可执行文件。

## 核心功能代码

### 翻译API接口
```python
def translate(self):   #MainWindow类内函数
    self.output_text.setText('')
    data=self.input_text.toPlainText()
    k_access_key = 'YOUR ACCESS KEY'
    k_secret_key = 'YOUR SECRET KEY'
    k_service_info = \
        ServiceInfo('open.volcengineapi.com',
                    {'Content-Type': 'application/json'},
                    Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                    5,
                    5)
    k_query = {
        'Action': 'TranslateText',
        'Version': '2020-06-01'
    }
    k_api_info = {
        'translate': ApiInfo('POST', '/', k_query, {}, {})
    }
    if(self.sel_language.currentText()=='英译汉'):
        TargetLanguage='zh'
    else:
        TargetLanguage='en'
    service = Service(k_service_info, k_api_info)
    TextList=[]
    TextList.append(data)
    body = {
        'TargetLanguage': TargetLanguage,
        'TextList': TextList,
    }
    res = service.json('translate', {}, json.dumps(body))
    res=json.loads(res)
    self.output_text.setText(res['TranslationList'][0]['Translation'])
```

### 生成分享图
```python
def getRandomColor(low,high):   #随机颜色
    return (random.randint(low,high),random.randint(low,high),random.randint(low,high))

def getPicture(string_get):     #生成图片并返回图片地址
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
```

### 数据库生成
```python
conn = sqlite3.connect('userWordBook.db')
cur = conn.cursor()
sql_text_1 = '''CREATE TABLE word
            (uid NUMBER,
            word_info TEXT);'''
cur.execute(sql_text_1)
```

## 软件更新规划

1. 支持更多语言互译功能
2. 将数据库部署于云端服务器，初步计划采用MySQL数据库，python实现使用pymysql进行数据库连接。
3. 采用前后端分离开发，使用Flask开发后端，开放API接口供客户端调用。
4. 支持多用户注册登录，用户数据保存于云端，从而进行单词本云同步，在不同客户端均可得到一致的单词本内容。
5. 设计开发用户背单词排行榜，使用Redis数据库进行开发，从而激励用户背单词。
6. 开发移动端应用，或WEB应用，实现多种设备访问使用。