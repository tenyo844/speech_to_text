from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


user = []


@app.route("/register", method=['POST'])
def register():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')

  if not email or not password:
    return jsonify({'message': 'Email and password are required'}), 400

  # パスワードのハッシュ化
  hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

  # ユーザー情報に設定
  user.append({
    'email': email,
    'password': hashed_password
  })

  # ユーザー情報を保存
  # register_user(user)
  
  