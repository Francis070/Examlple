# class
# over riding is not possible for python
# class mc:
#
#     """__author__ : Abhijit
#        __data__   : Aug 18 2021
#        __desc__   : Class in OOPS concept"""
#     # def __init__(self, name, post):
#     #     self.name = name
#     #     self.post = post
#
#     def a(self):
#         print("This is a")
#     # def b(self):
#     #     print("He is a ", self.post)
#
# class nc(mc):
#     def __init__(self):
#         print("Second class")
#
#     def b(self):
#         print("He is a ")
#
# # print(mo.__doc__)
# mo = nc()
# mo.a()
# mo.b()
# # mo.__nc.__b()


# class rect:
#     def __init__(self, len, wid):
#         self.len = len
#         self.wid = wid
#
#     def area(self):
#         return self.len * self.wid
#
#     def peri(self):
#         return 2 * self.len + 2 * self.wid
#
# class sqr:
#     def __init__(self, len):
#         self.len = len
#
#     def area(self):
#         return self.len * self.len
#
#     def peri(self):
#         return 4 * self.len


# class A:
#     def __init__(self, len):
#         self.len = len
#
#     def area(self):
#         print(self.len, "A")
#
# class B(A):
#     def __init__(self, wid):
#         self.wid = wid
#         super().__init__(self.wid)
#     def peri(self):
#         print(self.wid, "B")
#
# mo = B(12)
# mo.peri()
# mo.area()

# class A:
#     def de(self):
#         print("A")
# class B(A):
#     # def de(self):
#     #     print("B")
#     pass
# class C(A):
#     # def de(self):
#     #     print("C")
#     pass
# class D(B,C):
#     # def de(self):
#     #     print("D")
#     pass
#
# ob = D();
# ob.de()

# exception handling

# try:
#     c = "a"/0
#     print("Yes")
# except (ZeroDivisionError, TypeError) as ex:
#     print(ex)
# except:
#     print("oops")

# try:
#     c = 10/0
#     print("Yes")
# except Exception as ex:
#     print(ex)
# else:
#     print("no error")
# finally:
#     print("welcome")


# try:
#     c = 10
#     if c > 5:
#         raise IndexError("This is error")
# except IndexError as ex:
#     print(ex)

# class myError(Exception):
#     m = "This is a error"
#
# try:
#     c = 10
#     if c > 5:
#         raise myError
# except myError as er:
#     print(er.m)

# from python_iteration_day2 import *
# fun()

# import sys
# sys.path.append(r"C:\Users\i1422\PycharmProjects")
# print(sys.path)

# from python_iteration_day2 import *
# fun()

import sqlite3

# my_io = {"highjump": 1944, "longjump": 2009, "marathon": 2015}
#
# def myDB(query, db = "dhoni.db"):
#     try:
#         connection = sqlite3.connect(db)
#         execution = connection.execute(query)
#         table_d = execution.fetchall()
#         if len(table_d) != 0:
#             return table_d
#     except Exception as ex:
#         print(ex)
#     finally:
#         connection.commit()
#         connection.close()
#
# # query = """select * from sport"""
# # query = """create table tennis ("name" text, "year" integer)"""
# # query = """insert into sport (name, year) values ("badmintton", 1985) """
#
# for x, y in my_io.items():
#     query = """insert into sport (name, year) values ("{}", {}) """.format(x, y)
#     myDB(query)

# if db_data != None:
#     print(db_data)

import tkinter
from tkinter import filedialog
import os

my_io = {"highjump": 1944, "longjump": 2009, "marathon": 2015}

def myDB(query, db = "dhoni.db"):
    try:
        connection = ""
        root = tkinter.Tk()
        root.withdraw()
        path = filedialog.askdirectory()
        file_path = os.path.join(path, db)
        connection = sqlite3.connect(file_path)
        execution = connection.execute(query)
        table_d = execution.fetchall()
        if len(table_d) != 0:
            return table_d
    except Exception as ex:
        print(ex)
    finally:
        if connection != "":
            connection.commit()
            connection.close()

# query = """select * from sport"""
query = """create table fball ("name" text, "year" integer)"""
# query = """insert into sport (name, year) values ("badmintton", 1985) """
db_data = myDB(query)

if db_data != None:
    print(db_data)



