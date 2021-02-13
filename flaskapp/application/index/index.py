from app import app

@app.route('/')

def index():
    return {'status': 0, 'api': [
        { "create_order": "order/create" }
    ]}
   