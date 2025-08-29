from flask import Flask, request, jsonify
from pyad import aduser
import pythoncom

app = Flask(__name__)

@app.route('/enomarozi', methods=['GET'])
def testing():
    return "enomarozi"

@app.route('/postdata', methods=['POST'])
def postdata():
    pythoncom.CoInitialize()
    username = request.get_json()['username']
    user = checkUser(username)
    user_account_control = user.get_attribute("userAccountControl")[0]
    if user_account_control != 512:
        return jsonify({"message": None})
    else:
        return jsonify({"message":"Success"})

@app.route('/change-password', methods=['POST'])
def change_password():
    pythoncom.CoInitialize()
    data = request.get_json()
    username, password = data["username"], data["password"]
    user = checkUser(username)
    user.set_password(password)
    return jsonify({"message":"Success"})

def checkUser(username):
    try:
        user = aduser.ADUser.from_cn(username)
        return user
    except:
        return jsonify({"message":"User tidak ada"})
        
if __name__ == '__main__':
    app.run(host='10.208.1.14',port=80,debug=True)
