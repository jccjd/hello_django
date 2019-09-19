django 踩坑记
----------


> 这里记录一点学习框架在使用中的一点坑

###  mysql的版本问题
django 和 mysql的版本不匹配的问题，也就是在django源码中的问题，django源码
中有对mysql版本的限制，所以一般需要对源码修改，很简单将报错的那句话个注视
掉，但我找到了一篇比较详细的解释，

https://www.cnblogs.com/sheshouxin/p/10920255.html
### 数据库问题

在数据库使用时要在`setting.py`的同级 `__init__.py`中添加如下语句使
mysql自动加载

    import pymysql
    pymysql .install_as_MySQLdb()

### timezone
在项目中使用时间的时候要使用django自带的时间，timezone，如果使用python
的时间和django时间交叉使用是有问题的。

还有个细节就是就算你只是用python的时间，看起来是没有交叉使用的，但
如果在创建数据库的时候通过`models.DateTimeField(auto_now_add=True)`
去创建时间字段的时候它默认的还是django的自带时间仍然和python的时间
相冲突，所以不要自找麻烦在整个项目中只用timezone来操作时间

### django部署问题

在django的部署过程中有有关问题

1. 首先云服务器的问题，阿里的端口开放是需要加安全组的，mysql的3306,和 
nginx的80端口，都是需要手动去添加安全组才能在公网访问的， 
2. 在对用户注册是要给用户的注册邮箱发送邮件的时候，stmp的25端口被阿里云
给封了，所以需要换个端口比如 587, 然后还要将这个端口加入到安全组
 





