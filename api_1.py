
from flask import Flask,jsonify,request

#
app = Flask(__name__)

users=[{'id':1,'name':'Alice'},{'id':2,'name':'Tom'},{'id':3,'name':'Bob'}]

@app.route('/users',methods=['GET'])
def get_users():
    return  jsonify(users)
@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    try:
        for user in users:
            if user['id']==user_id:
                return jsonify(user['id'])
    except:
        return jsonify({'error': '用户不存在'}), 404



if __name__=='__main__':
    app.run(debug=True)





















# @app.route('/')
# def hello_world():
#     return 'Hello,World!'
# if __name__=='__main__':
#     app.run(debug=True)

# @app.route('/register',methods=['POST'])
# def register_user():
#     try:
#         data=request.get_json()
#         username=data.get('username')
#         email =data.get('email')
#         return jsonify({
#             'message':f'用户{username}注册成功',
#             'user_info':{
#                 'username':username,
#                 'email':email
#             }
#         })
#     except Exception as e:
#         return jsonify({'error':str(e)}),500
if __name__=='__main__':
    app.run(debug=True)