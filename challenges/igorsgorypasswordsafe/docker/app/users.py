import pymysql
from db import mysql, mysqlRO
import logging
import bcrypt

logger = logging.getLogger(__name__)

def getAllUsers():
    logger.info("Get users ...")
    conn = mysqlRO.connect()
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        logger.info("Got users: {}".format(rows))
    except:
        conn.close()
    finally:
        conn.close()

    return rows

def getUserByLogin(login):
    logger.info("Get user {}".format(login))
    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user where login = '" + login + "'")
        rows = cursor.fetchall()
        logger.info("Got user: {}".format(rows))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()

    if not rows:
        return
    return rows[0]

def loginUser(login, password):
    logger.info("Get user {} / {}".format(login, password))
    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT password FROM user where login = %s", (login))
        rows = cursor.fetchall()
        logger.info("Got user: {}".format(rows))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()

    if not rows:
        return
    else:
        passwordHash = rows[0]["password"]
        if bcrypt.checkpw(password.encode('utf-8'), passwordHash.encode('utf-8')):
            return getUserByLogin(login)
        else:
            return

def createUserFromForm(form):
    email = form.get('email')
    name = form.get('name')
    login = form.get('login')
    password = form.get('password')
    role = 'user'

    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # This is the safe way, no SQL injection possible
    val = (name, email, login, password, role)
    sql = "INSERT INTO `user`(`name`,`email`,`login`,`password`,`role`) values (%s, %s, %s, %s, %s)" 

    conn = mysql.connect()   
    try:    
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
        logger.info(cursor.rowcount, "record inserted.")
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()
