import yagmail
from datetime import *


def send_email():
    yagmail_server = yagmail.SMTP(user='859893448@qq.com', password='wsrbthmniifobdef', host='smtp.qq.com')
    email_to = ['dujun8368@dingtalk.com']
    email_title = '自动化执行报告'
    email_content = '测试邮件' + str(datetime.now())
    email_attachments = [r'D:\pythonProject\Report\report.html']
    yagmail_server.send(email_to, email_title, email_content, attachments=email_attachments)


