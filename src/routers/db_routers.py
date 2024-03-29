class AuthRouter:
    router_app_labels = {'auth', 'contenttypes', 'admin', 'sessions'}
    
    def db_for_read(self, model, **hints):
        if model.meta.app_label in self.router_app_labels:
            return 'new_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model.meta.app_label in self.router_app_labels:
            return 'new_db'
        return None
    
    # foreign key , many to many, allow
    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1.meta.app_label in self.router_app_labels or
            obj2.meta.app_label in self.router_app_labels 
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == 'new_db'
        return None