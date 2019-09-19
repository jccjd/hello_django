from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import hashlib

from . import forms
from . import models
from django.utils import timezone


# Create your views here.

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/login/index')

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'chick message'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = 'no the user'
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = 'email not acknowledge'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/login/index')

            else:
                message = ' password fiale'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('login/index')

    if request.method == 'POST':
        register_form = forms.ResgisterForm(request.POST)
        message = 'chick message'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的代码不同'

                return render(request, 'login/register.html', locals())

            else:
                same_name_user = models.User.objects.filter(name=username)

                if same_name_user:
                    message = '用户名已经存在'

                    return render(request, 'login/register.html', locals())

                same_email_user = models.User.objects.filter(email=email)

                if same_email_user:
                    message = '改邮箱已经被注册'
                    return render(request, 'login/register.html', locals())
                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)
                message = '请到邮箱确认'
                return render(request, 'login/confirm.html', locals())
        else:

            return render(request, 'login/register.html', locals())

    register_form = forms.ResgisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    request.session.flush()
    return redirect('/login/')


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''

    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的却仍请求'
        return render(request, 'login/confirm.html', locals())
    c_time = confirm.c_time
    now =timezone.now()
    if now > c_time + timezone.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '你的邮箱过期'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '已经确认 请使用账户登录'
        return render(request, 'login/confirm.html', locals())


def make_confirm_string(user):
    now = timezone.now().strftime('%Y-%m-%d%H:%M:%S')
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user)
    return code

def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '来自www.jccjd.top的注册确认邮件'
    text_context = '你的邮箱不支持html链接功能'

    html_content = '''
                <p>点击下面链接确定
                <p><a href="http://{}/login/confirm/?code={}">www.jccjd.top</a>
                <p>链接的有效时间{}!天</p>
                '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_context, 'jccjd@sina.com', [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
