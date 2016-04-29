__author__ = 'damons'

import sql_project
import sql_subject
import sql_experiment
import sql_assessor
import log
import sys

LOGGER = log.setup_debug_logger('psycoxnat', False)

class EObject(object):
    def __init__(self, uri, interface, hierarchy):
        self._uri = uri
        self._interface = interface
        self._hierarchy = hierarchy

    def exists(self):
        sql_statement, values = self._uri_to_sql()
        self._interface.select(sql_statement, values)
        return self._interface.has_one_entry()

    def _uri_to_sql(self):
        """
        Break down the uri to check the search values and return the relevant
         SQL statement

        :return: String template of the query
        :return: Tuple of values to insert into the template
        """
        if self._hierarchy =='project':
            return sql_project.PROJECT_ID_QUERY, self._get_project_id_from_uri
        elif self._hierarchy =='subject':
            return sql_subject.SUBJECT_ID_QUERY, self._uri.split('/')[:-1]
        elif self._hierarchy =='experiment':
            return sql_experiment.EXPERIMENT_ID_QUERY, self._uri.split('/')[:-1]
        elif self._hierarchy =='assessor':
            return sql_assessor.ASSESSOR_ID_QUERY, self._uri.split('/')[:-1]

    def _get_project_id_from_uri(self):
        try:
            project_index = self._uri.split('/').index('projects')
            return self._uri.split('/')[project_index+1]
        except ValueError:
            LOGGER.debug('Caught value error searching for "projects" in uri. Trying "project"')
        try:
            project_index = self._uri.split('/').index('project')
            return self._uri.split('/')[project_index+1]
        except ValueError:
            LOGGER.debug('Caught value error searching for "project" in uri. This uri is malformed. Exiting')
            sys.exit(1)

    def _get_subject_label_from_uri(self):

    def _get_experiment_label_from_uri(self):

    def _get_assessor_label_from_uri(self):


    def id(self):
        pass

    def label(self):
        pass

    def datatype(self):
        pass

    def create(self):
        pass

    def delete(self):
        raise NotImplementedError

class Project(EObject):
    def __init__(self, uri, interface, hierarchy='project'):
        EObject.__init__(self, uri, interface, hierarchy)

    def prearchive_code(self):
        pass

    def set_prearchive_code(self, code):
        pass

    def quarantine_code(self):
        pass

    def set_quarantine_code(self, code):
        pass

    def current_arc(self):
        pass

    def set_subfolder_in_current_arc(self, subfolder):
        pass

    def accessibility(self):
        pass

    def set_accessibility(self, accessibility='protected'):
        pass

    def users(self):
        pass

    def owners(self):
        pass

    def members(self):
        pass

    def collaborators(self):
        pass

    def user_role(self, login):
        pass

    def add_user(self, login, role='member'):
        pass

    def remove_user(self, login):
        pass

    def datatype(self):
        return 'xnat:projectData'

    def experiments(self, id_filter='*'):
        pass

    def experiment(self, id):

    pass
    def last_modified(self):
        pass

    def add_custom_variables(self, custom_variables, allow_data_deletion=False):
        raise NotImplementedError

    def get_custom_variables(self):
        raise NotImplementedError

