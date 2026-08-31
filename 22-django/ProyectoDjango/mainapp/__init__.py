import pymysql

pymysql.install_as_MySQLdb()

try:
    from django.db.backends.mysql import base
    base.DatabaseWrapper.check_database_version_supported = lambda self: None
except Exception:
    pass