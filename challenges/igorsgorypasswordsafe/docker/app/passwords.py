import pymysql
from db import mysql, mysqlRO
from flask_login import current_user 
import logging
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

logger = logging.getLogger(__name__)

# generated with os.random(32)
KEY = b'\x06\x0b\xda\xa02\xaa\xf8\n\xd4!\x1ag\xabI\x9f\xa7\xa6\x1f\xf9\xa1\x9e\xce\xbb\\n\xbf\xdd\xe7\t\xb9\x19\x06'

def encrypt(pw):
    AESService = AES.new(KEY, AES.MODE_CBC)
    enc = AESService.encrypt(pad(pw.encode("UTF-8"), AES.block_size))
    return b64encode(AESService.iv + enc).decode('utf-8')

def decrypt(pw):
    enc = b64decode(pw)
    iv = enc[:AES.block_size]
    AESService = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(AESService.decrypt(enc[AES.block_size:]), AES.block_size)

def getPasswordsByLoginId():
    logger.info("Get Passwords ...")
    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM safe where user_id = %s ORDER BY id ASC", (current_user.id))
        rows = cursor.fetchall()
        logger.info("Got passwords: {} for user with id {}".format(rows, current_user.id))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()
    for p in rows:
        p["password"] = decrypt(p["password"])
    return rows


def getPWForClipboard(id):
    logger.info("Get password for Clipboard (by ID)")
    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT password FROM safe WHERE id = " + id)
        rows = cursor.fetchall()
        logger.info("Got password: {}".format(rows))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()
    if not rows:
        return
    
    for p in rows:
        p["password"] = decrypt(p["password"])       
    return rows[0]["password"].decode("UTF-8")

def getPasswordById(id):
    logger.info("Get password by ID")
    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM safe WHERE id = %s and user_id = %s", (id, current_user.id))
        rows = cursor.fetchall()
        logger.info("Got password: {}".format(rows))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()
    if not rows:
        return
    
    for p in rows:
        p["password"] = decrypt(p["password"])       
    return rows[0]

def createPassword(form):
    login = current_user.id
    title = form.get('title')
    url = form.get('url')
    username = form.get('username')
    password = encrypt(form.get('password'))
    comment = form.get('comment')

    # This is the safe way, no SQL injection possible
    val = (login, title, url, username, password, comment)
    sql = "INSERT INTO `safe`(`user_id`, `title`, `url`, `username`, `password`, `comment`) values (%s, %s, %s, %s, %s, %s)" 

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

    
def searchPasswordsByLoginId(searchparameter):
    logger.info("Search passwords ...")

    # This is not safe
    # Make SQLI easy ... (avoid brackets)
    searchparameter = "'{}{}{}' and user_id ='{}'".format("%", searchparameter, "%", current_user.id)
    where = "comment like {} or title like {} or url like {} or username like {}".format(searchparameter, searchparameter, searchparameter, searchparameter)
    sql = "SELECT `id`, `user_id`, `title`, `url`, `username`, `comment` FROM safe WHERE {} ORDER BY id ASC".format(where)
    # logger.info("SQL: {}".format(sql))

    conn = mysqlRO.connect()    
    rows = []
    try:    
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        rows = cursor.fetchall()
        logger.info("Found passwords: {}".format(rows))
    except:
        conn.close()
        raise ValueError("SQL invalid")
    finally:
        conn.close()

    return rows

def updatePassword(form):
    title = form.get('title')
    url = form.get('url')
    username = form.get('username')
    password = encrypt(form.get('password'))
    comment = form.get('comment')
    id = form.get('id')

    # This is the safe way, no SQL injection possible
    val = (title, url, username, password, comment, id)
    sql = "UPDATE `safe` SET title = %s, url = %s, username = %s, password = %s, comment = %s WHERE id = %s"

    dbPassword = getPasswordById(id)
    # double secure not to overwrite the flag
    if dbPassword["user_id"] == current_user.id and not id == 7:
        conn = mysql.connect()   
        try:    
            cursor = conn.cursor()
            cursor.execute(sql, val)
            conn.commit()
            logger.info(cursor.rowcount, "password with id {} updated".format(id))
        except:
            conn.close()
            raise ValueError("SQL invalid")
        finally:
            conn.close()

def deletePassword(id):
    val = (id)
    sql = "DELETE FROM `safe` WHERE id = %s"

    dbPassword = getPasswordById(id)
    # double secure not to overwrite the flag
    if dbPassword["user_id"] == current_user.id and not id == 7:
        conn = mysql.connect()   
        try:    
            cursor = conn.cursor()
            cursor.execute(sql, val)
            conn.commit()
            logger.info(cursor.rowcount, "Password with id {} deleted".format(id))
        except:
            conn.close()
            raise ValueError("SQL invalid")
        finally:
            conn.close()