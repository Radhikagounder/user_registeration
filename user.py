import web
import model
import json
urls = ('/', 'Login',
        '/logout/', 'Logout',
        '/register/', 'Register')



class Register:
    def GET(self):
        return "hello"
    def POST(self):
        """ REST API TO ADD NEW ENTRY  """
        data = web.data()
        _id = model.new_user(json.loads(data)['firstname','lastname','email','phone','username','password'])
        return json.dumps({'id': _id})
class Login:
    def GET(self):
        return "hi"
    def POST(self):
        """resr api to authentication"""
        data=web.data()
        uid=model.log(json.loads(data)['username','password'])
        return json.dumps({'id':uid})
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
