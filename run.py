from orderapp.main import app, db
from orderapp.reference_data_load import *

@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    create_offer_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)