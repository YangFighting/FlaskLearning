from flask import Flask

app = Flask( __name__ )


@app.route( '/' )
def hello_world():
    return 'Hello World!'


#  变量规则
@app.route( '/user/<username>' )
def show_user_profile(username):
    return 'User %s' % username


@app.route( '/post/<int:post_id>' )
def show_post(post_id):
    return 'Post %d' % post_id


@app.route( '/path/<path:string_path>' )
def show_path(string_path):
    return 'string_path %s' % string_path


# ---唯一 URL / 重定向行为 ----#
@app.route( '/projects/' )
def projects():
    return 'The project page'


@app.route( '/about' )
def about():
    return 'The about page'


# ----------------#

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
