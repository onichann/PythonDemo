from flask import Flask,url_for
import sys

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():

    return 'Hello World!'


@app.route('/post/<string:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    # return 'Post %d' % post_id
    return 'Post {0}'.format(post_id)

if __name__ == '__main__':
    app.run(debug=True)
