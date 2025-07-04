
SECRET_KEY = "asdfasdfjasdfjasd;lf"

# 数据库的配置信息
HOSTNAME = 'CNHuangb.mysql.pythonanywhere-services.com'
PORT     = '3306'
DATABASE = 'CNHuangb$zhiliaooa_course'
USERNAME = 'CNHuangb'
PASSWORD = 'bmc.112233'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# # 本地数据库的配置信息
# HOSTNAME = '172.16.2.219'
# PORT     = '3306'
# DATABASE = 'zhiliaooa'
# USERNAME = 'root'
# PASSWORD = 'bmc.123'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# SQLALCHEMY_DATABASE_URI = DB_URI





# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "11680917@qq.com"
MAIL_PASSWORD = "lrxtgxqmfawwbifi"
MAIL_DEFAULT_SENDER = "11680917@qq.com"