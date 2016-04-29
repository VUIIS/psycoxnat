__author__ = 'damons'

EXPERIMENT_ID_QUERY = """SELECT id FROM xnat_experimentdata WHERE label=(%s) AND project=(%s)"""
