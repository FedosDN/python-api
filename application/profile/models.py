from app import db


class AdminProfile(db.Model):
    __tablename__ = 'admin_profiles'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    active = db.Column(db.Boolean, nullable=False, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='AdminProfile.user_id == User.id', backref='admin_profiles')


class DriverProfile(db.Model):
    __tablename__ = 'driver_profiles'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    active = db.Column(db.Boolean, nullable=False, index=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='DriverProfile.user_id == User.id', backref='driver_profiles')


class RiderProfile(db.Model):
    __tablename__ = 'rider_profiles'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    active = db.Column(db.Boolean, nullable=False, index=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='RiderProfile.user_id == User.id', backref='rider_profiles')


# class PasswordReset(db.Model):
#     __tablename__ = 'password_resets'
#     __primary_key__ = 'email'
#
#     email = db.Column(db.String(255), nullable=False, index=True)
#     token = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_verified_at = db.Column(db.DateTime)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
