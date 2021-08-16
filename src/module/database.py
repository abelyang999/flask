
import pymysql
import sys
import logging



class Database:
    def connect(self):
        return pymysql.connect(host="emp-mysql", user="smart", password="cloud", database="emp", charset='utf8mb4')
        #return pymysql.connect(host="dns02", user="smart", password="cloud", database="emp", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM emp order by id asc")
            else:
                cursor.execute(
                    "SELECT * FROM emp where id = %s order by id asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO emp(username,mobile,title,department) VALUES(%s, %s, %s, %s)", (data['username'], data['mobile'], data['title'],data['department']))
            con.commit()

            return True
        except pymysql.Error as e:
            self.con.rollback()
            logger.getErrorLog("MySQLCommand-insert: %d: %s" % (e.args[0], e.args[1]))
            con.rollback()
            return False
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE emp set username = %s, mobile = %s, title = %s, department = %s where id = %s", (data['username'], data['mobile'], data['title'],data['department'], id))
            con.commit()

            return True
        #except pymysql.Error as e:
        #    logger.getErrorLog("MySQLCommand-insert: %d: %s" % (e.args[0], e.args[1]))
        #    con.rollback()
        #    return False

        except :
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM emp where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
