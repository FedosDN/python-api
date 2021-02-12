from app import app
from ..decorators.jwt import token_required 
#from .models import DriverProfile
#from .schema.driver import DriverProfileSchema


#driver_schema = DriverProfileSchema()


@app.route('/order/create')
@token_required
def order_create():
    return {'message': 'hello', 'status': 0}
    #driver = DriverProfile.query.get(1)
    #return driver_schema.dump(driver)