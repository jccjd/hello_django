import os
from django.core.mail import send_mail

from mysite.mysite import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


def send_email(email, code):
    send_mail(
        '来自 www.jccjd.top 的测试邮件',
        'huanfdfdf',
        'jccjd@sina.com',
        ['jccjd@qq.com'],
    )


def send_email1(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '来自www.jccjd.top的注册确认邮件'
    text_context = '你的邮箱不支持html链接功能'

    html_content = '''
                <p>点击下面链接确定
                <p><a href="http://{}/confirm/?code={}">www.jccjd.top</a>
                <p>链接的有效时间{}!天</p>
                '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_context, 'jccjd@sina.com', [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
