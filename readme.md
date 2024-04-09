# 前言
Hello，我是小恒不会java
最近学习django，写了一个demo,学到了不少东西。
我在GitHub上开源了，提示‘自行查看代码，维护，运行’。
最近有事，先发布代码了，我就随缘维护更新吧

# 介绍
![image](https://github.com/lmliheng/transaction-market/blob/main/readme.png)
定位：小众交易网页
核心功能：登录注册认证，商品管理浏览，搜索逻辑，购物车
目的：熟悉django以及MVT模式，模拟业务

技术选型：python3.12，django5.x，js原生，sqlite（mysql）
部署方案：可后台run，也可使用应用服务器uwsgi等

# 部署
1）shell脚本
2）docker拉取
（我在加油书写中）


# 开发流程：
## 设计：
应用创建：user和transction两个应用。user应用用于使用django内置认证权限模块。transaction用于整个网页非登录页面和页面逻辑实现
ORM创建模型model：django自身模型user，在transaction应用下，创建item和contact模型。建立关系，user和contact一对一关联，user和item一对多关联（onetoonefield以及foreignkey）
view视图逻辑：多数函数返回静态文件，通过django内置的模块渲染成可展示的静态文件运用CVB基于类的视图函数，实现每个商品按钮对应相应商品详情页面使用@login-require等内置方法验证登录状态
template和static文件规范：setting设置django查找template和static的目录，template注意django扫描该目录下文件可能会存在重名报错，应增加路由区别不同template文件（我是放在应用下的）。static我放在根目录下。在html文件内继承父文件，加载static，调用对象数据，注意路由

## 页面：
主页、分类页（继承主页）、个人页面、购物车页面、
登录页面，注册页面、商品细节页面

## 逻辑要点：
1）注册登录基本逻辑，登录保留数据
2）发布判断登录状态否则重定向（django自带的认证权限模块实现）
3）权限管理：发布与删除（用户私有），公开数据（商品展示和细节）
4）数据索引：用户-contact（onetoone）-item（forgniekey）（在model文件修改）
5）路由规范：主要是setting和根目录或应用的urls.py的匹配
