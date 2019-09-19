=====
登录和注册系统
=====

### 这是一个用户登录和注册教学项目
###  这是一个可重用的登录和注册APP



### 简单的使用步骤：

1. 创建虚拟环境
2. 使用pip安装第三方依赖
3. 添加相应的路由
4. 配置settings
5. 运行migrate命令，创建数据库和数据表
6. 链接你的index页面
7. 运行python manage.py runserver启动服务器


### 路由设置：

    from django.contrib import admin
    from django.urls import path, include
    from login import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        path('login/', views.login),
        path('register/', views.register),
        path('logout/', views.logout),
        path('confirm/', views.user_confirm),
        path('captcha/', include('captcha.urls'))
    ]
    


### settings配置：

1. 在INSTALLED_APPS中添加‘login’，'captcha'
2. 默认使用Sqlite数据库
3. LANGUAGE_CODE = 'zh-hans'
4. TIME_ZONE = 'Asia/Shanghai'
5. USE_TZ = False

### 邮件服务设置

6. EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
7. EMAIL_HOST = 'smtp.sina.com'
8. EMAIL_PORT = 25
9. EMAIL_HOST_USER = 'xxxx@sina.com'
10. EMAIL_HOST_PASSWORD = 'xxxxx'

### 注册有效期天数
11. CONFIRM_DAYS = 7