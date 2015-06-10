##代码简介:   

本系统采用Django1.4和Bootstrap进行开发，数据库采用SQlite，并架设在<a href="https://www.heroku.com" target="_blank">Heroku</a>云平台上，欢迎访问<a href="https://activitymanager.herokuapp.com" target="_blank">https://activitymanager.herokuapp.com</a>。    
关于Django1.4如何架设在Heroku上可参考<a href="http://www.re-cycledair.com/deploying-django-1-4-to-heroku" target="_blank">这里</a>。

##网站介绍:

本系统是一个公益活动的发布,申请以及管理平台,包含有学生,组织者以及管理员三种具有不同权限的用户。其中：   

* **学生**能够申请参加公益活动，成功参加后可获得相应的公益时；
* **组织者**可以创建公益活动（需要经过管理员审核通过才能发布），管理自己所创建的公益活动的申请表队列；
* **管理员**具有最高权限，可以管理用户（包括查看，修改信息，拉黑，删除用户等），管理公益活动（包括编辑，通过，删除等）以及管理申请表（包括通过，删除等）。

**注册须知：**     
在网站中注册用户时，若注册学生，注册后即可正常登录，而若为注册组织者或者管理员，则需要等待管理员审核通过之后才可以正常登录。    

**管理员测试账密：**   
账号：donald   
密码：123456    
