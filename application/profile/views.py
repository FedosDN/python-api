from app import app
from .models import DriverProfile
from .schema.driver import DriverProfileSchema


driver_schema = DriverProfileSchema()


@app.route('/drivers')
def drivers():
    driver = DriverProfile.query.get(1)
    return driver_schema.dump(driver)
