# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 16:43 
# @Author : dujun
# @describe : dev执行环境
# @File : caps.py

def Caps(env=''):
    ##测试环境
    if env == '':
        caps = {
            "name": 'test',
            "audit": 'http://audit.51bm.net.cn',
            "user": 'http://user.51bm.net.cn',
            "prob": 'http://prob.51bm.net.cn',
            "base": 'http://base.51bm.net.cn',
            "pool": 'http://pool.51bm.net.cn',
            "college": 'http://college.51bm.net.cn',
            "school": 'http://school.51bm.net.cn',
            "stu": 'http://stu.51bm.net.cn',
            "guide": 'http://guide.51bm.net.cn',
            "notice": 'http://notice.51bm.net.cn',
            "fillCenter": 'http://fillCenter.51bm.net.cn',
            "fileCenter": 'http://fileCenter.51bm.net.cn',
            "fillCenterOnline": 'https://filecenter.artstudent.cn',
            "pay": 'http://pay.51bm.net.cn',
            "index": 'http://index.51bm.net.cn',
            "hulaquan": 'http://hulaquan.51bm.net.cn',
            "info": 'http://info.51bm.net.cn',
            "public": 'http://public.51bm.net.cn',
            "wish": 'http://wish.51bm.net.cn',
            "crm": 'http://crm.51bm.net.cn',
            "xyk": 'http://xyk.51bm.net.cn',
            "print": 'http://print.51bm.net.cn',
            "eval": 'http://eval.51bm.net.cn',
            "advert": 'http://advert.51bm.net.cn',
            "examVideo": 'http://examvideo.51bm.net.cn',
            "sys": 'http://sys.51bm.net.cn',
            "examlog": 'http://examlog.51bm.net.cn',
            '23000': 'http://192.168.18.202:23000'
        }
        return caps

    ##线上环境
    elif env == 'online':
        caps = {
            'college': 'https://college.artstudent.cn',
            "analysis": 'http://192.168.18.202:7000',
            "index": 'http://192.168.18.202:10000',
            "user": 'http://192.168.18.202:10100',
            "base": 'http://192.168.18.202:10200',
            "aftexam": 'http://192.168.18.202:10400',
            "pay": 'http://192.168.18.202:10500',
            "news": 'http://192.168.18.202:10600',
            "filecenter": 'http://192.168.18.202:10700',
            "notice": 'http://192.168.18.202:10800',
            "monitor": 'http://192.168.18.202:10900',
            "sys": 'http://192.168.18.202:11000',
            "hulaquan": 'http://192.168.18.202:12000',
            "report": 'http://192.168.18.202:13000',
            "advert": 'http://192.168.18.202:15000',
            "xyk": 'http://192.168.18.202:16000',
            "wish": 'http://192.168.18.202:17000',
            "prob": 'http://192.168.18.202:18000',
            "member": 'http://192.168.18.202:20200',
            "public": 'http://192.168.18.202:20300',
            "info": 'http://192.168.18.202:20400',
            "pool": 'http://192.168.18.202:20500',
            "stu": 'http://192.168.18.202:20600',
            "print": 'http://192.168.18.202:20700',
            "school": 'https://school.artstudent.cn',
            "menu": 'http://192.168.18.202:20900',
            "guide": 'http://192.168.18.202:22000',
            "audit": 'http://192.168.18.202:23000',
            "examVideo": 'https://examvideo.artstudent.cn',
            "course": 'http://192.168.18.202:25000',
            "live": 'http://192.168.18.202:26000',
            "eval": 'http://192.168.18.202:27000',
            "examlog": 'http://192.168.18.202:28000',
            "crm": 'http://192.168.18.202:40000'
        }
        return caps


if __name__ == "__main__":
    print(Caps()['user'])
