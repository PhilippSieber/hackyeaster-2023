from flask_login import UserMixin

# user class to be used for session managment in flask_login
class User(UserMixin):
    def __init__(self, name, id, role, active=True):
        self.name = name
        self.role = role
        self.id = id
        self.active = active

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True