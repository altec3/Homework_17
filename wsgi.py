from inits.app_init import app_init

app = app_init()

if __name__ == '__main__':
    app.run(debug=True)