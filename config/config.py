__author__ = 'damons'

import log
import os
import ConfigParser
import sys

class PsycoXNATConfig(object):
    def __init__(self, settings=os.path.join(os.path.expanduser('~'), '.psycoxnat.ini')):
        self.settings_file = settings
        self.config_parser = ConfigParser.ConfigParser(allow_no_value=True)

        # On init set the deepest level of debug. Then change if the user wants it. Otherwise reset to warning
        self.logger = log.setup_debug_logger('psycoxnat', False)

        if not os.path.isfile(self.settings_file):
            self.logger.debug("NO CONFIG FILE FOUND. Please read the docs for instructions. Exiting..")
            sys.exit(1)

        # Read it and see if it's valid
        self.__read__()
        self.__isvalid__()

        # Now update the log level away from debug
        self._update_logger_level()

    def __read__(self):
        """
        Read the configuration file

        :except: ConfigParser.MissingSectionHeaderError if [ or ] is missing
        :return: None. config_parser is read in place

        """
        try:
            self.config_parser.read(self.settings_file)
        except ConfigParser.MissingSectionHeaderError as MSHE:
            self.logger.CRITICAL("INVALID SETTINGS FILE. EXITING")
            sys.exit(1)

    def __isvalid__(self):

        """
        Check the ini file to make sure that it has the 3 required sections
        (postgres, xnat and log)

        :except: ConfigParser.NoSectionError if any of the 3 required sections
         is missing
        :return: None

        """

        # Check that the postgres section exists and all the expected keys are there
        try:
            self.config_parser.options('postgres')
        except ConfigParser.NoSectionError:
            self.logger.critical('MISSING SECTION "postgres" in config file')
            sys.exit(1)

        self._check_section_by_keys('postgres', ['dbuser',
                                                 'dbname',
                                                 'dbpass',
                                                 'dbhost',
                                                 'dbport'])
        self.logger.info('Section "postgres" OK')

        # Check that the xnat section exists and all the expected keys are there
        try:
            self.config_parser.options('xnat')
        except ConfigParser.NoSectionError:
            self.logger.critical('MISSING SECTION "xnat" in config file')
            sys.exit(1)

        self._check_section_by_keys('xnat', ['xnatuser',
                                             'xnathost',
                                             'xnatpass'])
        self.logger.info('Section "xnat" OK')

        # Check that the log section exists and all the expected keys are there
        try:
            self.config_parser.options('log')
        except ConfigParser.NoSectionError:
            self.logger.critical('MISSING SECTION "log" in config file')
            sys.exit(1)

        self._check_section_by_keys('log', ['level'])
        self.logger.info('Section "log" OK')

    def _get(self, header, key):
        """

        :param header:
        :param key:
        :return:

        """
        value = None

        try:
            value = self.config_parser.get(header, key)
        except ConfigParser.NoOptionError as NOE:
            self.logger.critical('No option %s found in header %s. EXITING'
                                 % (key, header))
            sys.exit(1)
        return value

    def _check_section_by_keys(self, header, keys):
        for key in keys:
            self.logger.debug('Checking for key %s in header %s.' % (key, header))
            self._get(header, key)
            self.logger.debug('Key %s in header %s is OK.' % (key, header))

    def _update_logger_level(self):

        log_level = self._get('log', 'level')
        logger_level_list = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', '']
        if log_level not in logger_level_list:
            self.logger.error('Logging level must be in %s' %
                              ', '.join(logger_level_list))
            sys.exit(1)
        if log_level == '':
            self.logger.warning('Logging level will be set to WARNING since it was left empty')
            self.logger = log.setup_warning_logger('psycoxnat', False)

        if log_level == 'DEBUG':
            self.logger = log.setup_debug_logger('psycoxnat', False)
        elif log_level == 'INFO':
            self.logger = log.setup_info_logger('psycoxnat', False)
        elif log_level == 'WARNING':
            self.logger = log.setup_warning_logger('psycoxnat', False)
        elif log_level == 'ERROR':
            self.logger = log.setup_error_logger('psycoxnat', False)
        elif log_level == 'CRITICAL':
            self.logger = log.setup_critical_logger('psycoxnat', False)
