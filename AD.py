from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def testing():
    return "enomarozi"

@app.route('/postdata', methods=['POST'])
def postdata():
    username = request.get_json()['username']
    setPassword = check_password(username)
    return jsonify({"message":setPassword})
    
def check_password(username):
    ps_command = f"Get-ADUser -Identity {username} -Properties PasswordLastSet | Select-Object SamAccountName, PasswordLastSet | ConvertTo-Json"
    result = subprocess.run(
        ["powershell","-Command",ps_command],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        output = result.stdout.strip()
        data = json.loads(output)
        return data['PasswordLastSet']
    else:
        return "User tidak ditemukan"

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    username, password = data["username"].split('@')[0], data["password"]
    setPassword = action_change_password(username,password)
    return jsonify({"message":setPassword})
    
def action_change_password(username,password):
    ps_command = f"Set-ADAccountPassword -Identity '{username}' -NewPassword (ConvertTo-SecureString -AsPlainText '{password}' -Force) -Reset"
    result = subprocess.run(
        ["powershell","-Command",ps_command],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return "Success"
    else:
        return "Error"
    
if __name__ == '__main__':
    app.run(host='10.208.1.14',port=80,debug=True)
