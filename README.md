# IDT v1.0
### [English]('https://github.com/baimao-box/satania/blob/main/English.md')

该工具主要的功能是对批量url或者接口进行存活探测，支持浏览器自动打开指定的url，避免手动重复打开网址

## 为什么要使用 IDT？ 
当你收集到许许多多的接口时，如果一个个去访问，却是很浪费时间。但是光是知道状态码和输出url还是不够，还需要手动打开浏览器查看是否存在未授权漏洞。
IDT支持自动使用浏览器打开url，避免了重复手测打开的操作，您只需使用眼睛去观察网页是否存在可疑的密钥或者未授权漏洞即可


## 优势
```
支持筛选url状态码
支持自动化浏览器打开url
支持多线程处理
支持代理模式
```
## 安装

安装模块后即可使用
```
pip install -r requirement.txt
```
![image](https://github.com/cikeroot/IDT/assets/110379183/0b3895a3-f743-4855-be90-a74e97dfe937)


## 选项
```
usage: IDT.py [-h] [-u FILE] [-o OUTPUT] [-sc STATUS_CODE] [-b] [-oss] [-d] [--proxy PROXY]

Open URLs and check for OSS keys.

optional arguments:
  -h, --help            show this help message and exit
  -u FILE, --file FILE  Enumerate files for urls
  -o OUTPUT, --output OUTPUT
                        Specify the output file
  -sc STATUS_CODE, --status_code STATUS_CODE
                        Filter status code
  -b, --browser         Open urls in a web browser
  -oss, --detect_oss    Detect Oss keys
  -d, --default_status_code
                        Default output status code for the current url
  --proxy PROXY         use proxies

```

# 使用例子:

-u 选项指定批量处理的url文件
```
python IDT.py -u url.txt
```
默认输出200返回值状态码的url

![image](https://github.com/cikeroot/IDT/assets/110379183/c6e19b6f-3005-4901-a390-74cfd936aa58)

使用 -b 参数，将会使用浏览器打开输出的url接口进行访问
```
python3 IDT.py -u url.txt -b
```
![image](https://github.com/cikeroot/IDT/assets/110379183/dae43885-c3d3-42bb-b674-c68d1a59184e)

使用 -d 参数可以指定输出所有url的默认状态码
```
python IDT.py -u url.txt -d 
```
![image](https://github.com/cikeroot/IDT/assets/110379183/bb50bcd1-746a-4d15-b515-1abf0f5f5169)

使用 -sc 参数可以进行筛选状态码，然后输出指定的url
```
python IDT.py -u url.txt -sc 301 
```
![image](https://github.com/cikeroot/IDT/assets/110379183/053ce947-b0ef-4f0d-809e-cde5ee5ea989)

添加 -o 参数可以，另存文件
```
python IDT.py -u url.txt -o a.txt
```
添加 --proxy 参数支持代理模式

```
python IDT.py -u url.txt --proxy 127.0.0.1:10809
```
