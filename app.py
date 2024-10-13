from flask import Flask

app = Flask(__name__)

# static route
@app.route('/wallets')
def get_wallets():
    return 'All the wallets returned'

# dynamic route
@app.route('/wallets/<int:id>')
def get_wallet(id):
    return 'Hi, this is coming from wallet {}'.format(str(id))
    
if __name__ == '__main__':
    app.run()