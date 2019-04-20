import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user="18210457552@163.com", password="FZY_629442466wo", host='smtp.163.com')

# 邮箱正文
contents = ['今天是周末,我要学习, 学习使我快乐;', '<a href="https://www.python.org/">python官网的超链接</a>', 'https://upload-images.jianshu.io/upload_images/3203841-93fc777683c7e9d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240']

# 发送邮件
yag.send('18210457552@163.com', '主题:学习使我快乐', contents)