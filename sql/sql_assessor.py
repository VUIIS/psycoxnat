__author__ = 'damons'

ASSESSOR_ID_QUERY = """SELECT id FROM xnat_experimentdata WHERE label=(%s) AND project=(%s)"""
