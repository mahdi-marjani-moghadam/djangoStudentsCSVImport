from ..students.models import post,students,parents

class DBRouterMysql:
    
    route_app_labels = {'students', 'parents'}
    dbName = 'django'

    def db_for_read (self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            # your model name as in settings.py/DATABASES
            return self.dbName
        return None
    
    def db_for_write (self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            # your model name as in settings.py/DATABASES
            return self.dbName
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'django' database.
        """
        if app_label in self.route_app_labels:
            return db == self.dbName
        return None

