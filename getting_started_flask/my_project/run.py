# run.py

from app import app

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8080, debug=True) #c9
    