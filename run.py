from orderapp.main import app, db

@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)