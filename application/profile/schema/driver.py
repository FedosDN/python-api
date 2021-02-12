from app import ma


class DriverProfileSchema(ma.Schema):
    class Meta:
        fields = ("id", "active")
