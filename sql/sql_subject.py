__author__ = 'damons'

SUBJECT_ID_QUERY = """SELECT id FROM xnat_subjectdata WHERE project=(%s) AND label=(%S)"""
