from app import app, appRO
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ClWKlFMpGHHmJ3OfSE80'
app.config['MYSQL_DATABASE_DB'] = 'passwordsafe'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

mysqlRO = MySQL()
 
# MySQL configurations
appRO.config['MYSQL_DATABASE_USER'] = 'readonly'
appRO.config['MYSQL_DATABASE_PASSWORD'] = '8ezv7QEiSHLE4wv4emmi'
appRO.config['MYSQL_DATABASE_DB'] = 'passwordsafe'
appRO.config['MYSQL_DATABASE_HOST'] = 'db'
mysqlRO.init_app(appRO)

