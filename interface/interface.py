__author__ = 'damons'

import config
import psycopg2
import sys
class Interface(object):
    def __init__(self, dbuser, dbpass, dbhost, dbport, dbname, logger):
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.dbhost = dbhost
        self.dbport = dbport
        self.dbname = dbname
        self.logger = logger
        self._connection = None
        self.cursor = None

        self._get_connection()
        self._get_cursor()

    def _get_connection(self):
        """

        :param dbname:
        :param user:
        :param password:
        :return:
        """
        try:
            connection = psycopg2.connect(dbname=self.dbname,
                                          password=self.dbpass,
                                          user=self.dbuser,
                                          host=self.dbhost)

        except psycopg2.OperationalError:
            self.logger.critical('Failed to connect to database. Please '
                                 'check your credentials. Exiting')
            sys.exit(1)
        self.logger.debug('Established connection to db=%s on host=%s' %
                          (self.dbname, self.dbhost))
        self._connection = connection

    def _get_cursor(self):
        """

        :return:
        """
        self.cursor = self._connection.cursor()

    def select(self, template, values):
        self.cursor.execute(template, values)

    def has_one_entry(self):
        return len(self.cursor.fetchall()) == 1

    def has_multiple_entries(self):
        return len(self.cursor.fetchall()) > 1

    def commit(self):
        self._connection.commit()

    def fetchone(self):
        return self._connection.fetchone()


