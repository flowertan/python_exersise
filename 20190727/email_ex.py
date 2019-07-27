# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/27 19:45
# @file    : email_ex.py
# @desc    : 发邮件例子
#

from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 替换为自己的sender, receivers
    sender = 'XXXXX@126.com'
    receivers = ['XXXXX@qq.com', 'XXXXX@hotmail.com']
    message = MIMEText('用python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    # 刚开始的时候使用SMTP没有发送成功，登录126邮箱，看见设置是安全模式，因此换成SMTP_SSL成功发送邮件
    smtper = SMTP_SSL('smtp.126.com')
    smtper.login(sender, 'password')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()
