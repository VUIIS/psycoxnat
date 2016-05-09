__author__ = 'damons'

PROJECT_ID_QUERY = """SELECT id FROM xnat_projectdata WHERE id=(%s)"""
PROJECT_PREARCHIVE_QUERY="""SELECT prearchive_code FROM arc_project WHERE id=(%s)"""
PROJECT_SET_PREARCHIVE_CODE="""UPDATE arc_project SET prearchive_code=(%s) WHERE id=(%s)"""
PROJECT_QUARANTINE_QUERY="""SELECT quarantine_code FROM arc_project WHERE id=(%s)"""
PROJECT_SET_QUARANTIE_CODE="""UPDATE arc_project SET quarantine_code=(%s) WHERE id=(%s)"""
PROJECT_CURRENT_ARC="""SELECT current_arc FROM arc_project WHERE id=(%s)"""
