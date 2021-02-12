# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()






class FailedJob(db.Model):
    __tablename__ = 'failed_jobs'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    uuid = db.Column(db.String(255), nullable=False, unique=True)
    connection = db.Column(db.Text, nullable=False)
    queue = db.Column(db.Text, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    exception = db.Column(db.Text, nullable=False)
    failed_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class Migration(db.Model):
    __tablename__ = 'migrations'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    migration = db.Column(db.String(255), nullable=False)
    batch = db.Column(db.Integer, nullable=False)



class ModelHasPermission(db.Model):
    __tablename__ = 'model_has_permissions'
    __table_args__ = (
        db.Index('model_has_permissions_model_id_model_type_index', 'model_id', 'model_type'),
    )

    permission_id = db.Column(db.ForeignKey('permissions.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    model_type = db.Column(db.String(255), primary_key=True, nullable=False)
    model_id = db.Column(db.BigInteger, primary_key=True, nullable=False)

    permission = db.relationship('Permission', primaryjoin='ModelHasPermission.permission_id == Permission.id', backref='model_has_permissions')



class ModelHasRole(db.Model):
    __tablename__ = 'model_has_roles'
    __table_args__ = (
        db.Index('model_has_roles_model_id_model_type_index', 'model_id', 'model_type'),
    )

    role_id = db.Column(db.ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    model_type = db.Column(db.String(255), primary_key=True, nullable=False)
    model_id = db.Column(db.BigInteger, primary_key=True, nullable=False)

    role = db.relationship('Role', primaryjoin='ModelHasRole.role_id == Role.id', backref='model_has_roles')



class OauthAccessToken(db.Model):
    __tablename__ = 'oauth_access_tokens'

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.BigInteger, index=True)
    client_id = db.Column(db.BigInteger, nullable=False)
    name = db.Column(db.String(255))
    scopes = db.Column(db.Text)
    revoked = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    expires_at = db.Column(db.DateTime)



class OauthAuthCode(db.Model):
    __tablename__ = 'oauth_auth_codes'

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True)
    client_id = db.Column(db.BigInteger, nullable=False)
    scopes = db.Column(db.Text)
    revoked = db.Column(db.Boolean, nullable=False)
    expires_at = db.Column(db.DateTime)



class OauthClient(db.Model):
    __tablename__ = 'oauth_clients'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.BigInteger, index=True)
    name = db.Column(db.String(255), nullable=False)
    secret = db.Column(db.String(100))
    provider = db.Column(db.String(255))
    redirect = db.Column(db.Text, nullable=False)
    personal_access_client = db.Column(db.Boolean, nullable=False)
    password_client = db.Column(db.Boolean, nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



class OauthPersonalAccessClient(db.Model):
    __tablename__ = 'oauth_personal_access_clients'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    client_id = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



class OauthRefreshToken(db.Model):
    __tablename__ = 'oauth_refresh_tokens'

    id = db.Column(db.String(100), primary_key=True)
    access_token_id = db.Column(db.String(100), nullable=False, index=True)
    revoked = db.Column(db.Boolean, nullable=False)
    expires_at = db.Column(db.DateTime)






class Permission(db.Model):
    __tablename__ = 'permissions'
    __table_args__ = (
        db.UniqueConstraint('name', 'guard_name'),
    )

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(255), nullable=False)
    guard_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    roles = db.relationship('Role', secondary='role_has_permissions', backref='permissions')






class RoleHasPermission(db.Model):
    __tablename__ = 'role_has_permissions'

    permission_id = db.Column(db.ForeignKey('permissions.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    role_id = db.Column(db.ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True, nullable=False)

    permission = db.relationship('Permission', primaryjoin='RoleHasPermission.permission_id == Permission.id', backref='role_has_permissions')
    role = db.relationship('Role', primaryjoin='RoleHasPermission.role_id == Role.id', backref='role_has_permissions')



class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = (
        db.UniqueConstraint('name', 'guard_name'),
    )

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(255), nullable=False)
    guard_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)



