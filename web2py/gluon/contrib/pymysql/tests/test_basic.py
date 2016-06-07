from pymysql.tests import base
from pymysql import util

import time
import datetime

class TestConversion(base.PyMySQLTestCase):
    def test_datatypes(self):
        """ test every data type """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        try:
            # insert values
            v = (True, -3, 123456789012, 5.7, "hello'\" world", u"Espa\xc3\xb1ol", "binary\x00data".encode(conn.charset), datetime.date(1988,2,2), datetime.datetime.now(), datetime.timedelta(5,6), datetime.time(16,32), time.localtime())
            c.execute
            c.execute
            r = c.fetchone()
            self.assertEqual(util.int2byte(1), r[0])
            self.assertEqual(v[1:8], r[1:8])
            # mysql throws away microseconds so we need to check datetimes
            # specially. additionally times are turned into timedeltas.
            self.assertEqual(datetime.datetime(*v[8].timetuple()[:6]), r[8])
            self.assertEqual(v[9], r[9]) # just timedeltas
            self.assertEqual(datetime.timedelta(0, 60 * (v[10].hour * 60 + v[10].minute)), r[10])
            self.assertEqual(datetime.datetime(*v[-1][:6]), r[-1])

            c.execute

            # check nulls
            c.execute
            c.execute
            r = c.fetchone()
            self.assertEqual(tuple([None] * 12), r)

            c.execute

            # check sequence type
            c.execute
            c.execute
            r = c.fetchall()
            self.assertEqual(((4,),(8,)), r)
        finally:
            c.execute

    def test_dict(self):
        """ test dict escaping """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        try:
            c.execute
            c.execute
            self.assertEqual((1,2,3), c.fetchone())
        finally:
            c.execute

    def test_string(self):
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        test_value = "I am a test string"
        try:
            c.execute
            c.execute
            self.assertEqual((test_value,), c.fetchone())
        finally:
            c.execute

    def test_integer(self):
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        test_value = 12345
        try:
            c.execute
            c.execute
            self.assertEqual((test_value,), c.fetchone())
        finally:
            c.execute

    def test_big_blob(self):
        """ test tons of data """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        try:
            data = "pymysql" * 1024
            c.execute
            c.execute
            self.assertEqual(data.encode(conn.charset), c.fetchone()[0])
        finally:
            c.execute

    def test_untyped(self):
        """ test conversion of null, empty string """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        self.assertEqual((None,u''), c.fetchone())
        c.execute
        self.assertEqual((u'',None), c.fetchone())
    
    def test_datetime(self):
        """ test conversion of null, empty string """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        self.assertEqual((datetime.timedelta(0, 45000),
                          datetime.timedelta(0, 83579),
                          datetime.timedelta(0, 83579, 51000)),
                         c.fetchone())


class TestCursor(base.PyMySQLTestCase):
    # this test case does not work quite right yet, however,
    # we substitute in None for the erroneous field which is
    # compatible with the DB-API 2.0 spec and has not broken
    # any unit tests for anything we've tried.

    #def test_description(self):
    #    """ test description attribute """
    #    # result is from MySQLdb module
    #    r = (('Host', 254, 11, 60, 60, 0, 0),
    #         ('User', 254, 16, 16, 16, 0, 0),
    #         ('Password', 254, 41, 41, 41, 0, 0),
    #         ('Select_priv', 254, 1, 1, 1, 0, 0),
    #         ('Insert_priv', 254, 1, 1, 1, 0, 0),
    #         ('Update_priv', 254, 1, 1, 1, 0, 0),
    #         ('Delete_priv', 254, 1, 1, 1, 0, 0),
    #         ('Create_priv', 254, 1, 1, 1, 0, 0),
    #         ('Drop_priv', 254, 1, 1, 1, 0, 0),
    #         ('Reload_priv', 254, 1, 1, 1, 0, 0),
    #         ('Shutdown_priv', 254, 1, 1, 1, 0, 0),
    #         ('Process_priv', 254, 1, 1, 1, 0, 0),
    #         ('File_priv', 254, 1, 1, 1, 0, 0),
    #         ('Grant_priv', 254, 1, 1, 1, 0, 0),
    #         ('References_priv', 254, 1, 1, 1, 0, 0),
    #         ('Index_priv', 254, 1, 1, 1, 0, 0),
    #         ('Alter_priv', 254, 1, 1, 1, 0, 0),
    #         ('Show_db_priv', 254, 1, 1, 1, 0, 0),
    #         ('Super_priv', 254, 1, 1, 1, 0, 0),
    #         ('Create_tmp_table_priv', 254, 1, 1, 1, 0, 0),
    #         ('Lock_tables_priv', 254, 1, 1, 1, 0, 0),
    #         ('Execute_priv', 254, 1, 1, 1, 0, 0),
    #         ('Repl_slave_priv', 254, 1, 1, 1, 0, 0),
    #         ('Repl_client_priv', 254, 1, 1, 1, 0, 0),
    #         ('Create_view_priv', 254, 1, 1, 1, 0, 0),
    #         ('Show_view_priv', 254, 1, 1, 1, 0, 0),
    #         ('Create_routine_priv', 254, 1, 1, 1, 0, 0),
    #         ('Alter_routine_priv', 254, 1, 1, 1, 0, 0),
    #         ('Create_user_priv', 254, 1, 1, 1, 0, 0),
    #         ('Event_priv', 254, 1, 1, 1, 0, 0),
    #         ('Trigger_priv', 254, 1, 1, 1, 0, 0),
    #         ('ssl_type', 254, 0, 9, 9, 0, 0),
    #         ('ssl_cipher', 252, 0, 65535, 65535, 0, 0),
    #         ('x509_issuer', 252, 0, 65535, 65535, 0, 0),
    #         ('x509_subject', 252, 0, 65535, 65535, 0, 0),
    #         ('max_questions', 3, 1, 11, 11, 0, 0),
    #         ('max_updates', 3, 1, 11, 11, 0, 0),
    #         ('max_connections', 3, 1, 11, 11, 0, 0),
    #         ('max_user_connections', 3, 1, 11, 11, 0, 0))
    #    conn = self.connections[0]
    #    c = conn.cursor()
    #    c.execute("select * from mysql.user")
    #
    #    self.assertEqual(r, c.description)

    def test_fetch_no_result(self):
        """ test a fetchone() with no rows """
        conn = self.connections[0]
        c = conn.cursor()
        c.execute
        try:
            data = "pymysql"
            c.execute
            self.assertEqual(None, c.fetchone())
        finally:
            c.execute

    def test_aggregates(self):
        """ test aggregate functions """
        conn = self.connections[0]
        c = conn.cursor()
        try:
            c.execute
            for i in xrange(0, 10):
                c.execute
            c.execute
            r, = c.fetchone()
            self.assertEqual(sum(range(0,10)), r)
        finally:
            c.execute

    def test_single_tuple(self):
        """ test a single tuple """
        conn = self.connections[0]
        c = conn.cursor()
        try:
            c.execute
            c.execute
            c.execute
            c.execute
            self.assertEqual([(1,)], list(c.fetchall()))
        finally:
            c.execute


__all__ = ["TestConversion","TestCursor"]

if __name__ == "__main__":
    import unittest
    unittest.main()
