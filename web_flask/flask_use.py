from flask import Flask  # 首先我们导入了Flask类。该类的实例将会成为我们的WSGI应用

"""
创建一个该类的实例。第一个参数是应用模块或者包的名称。如果你使用 一个单一模块（就像本例），
那么应当使用 __name__ ，因为名称会根据这个 模块是按应用方式使用还是作为一个模块导入而发生
变化（可能是 ‘__main__’ ， 也可能是实际导入的名称）。这个参数是必需的，这样 Flask 才能知
道在哪里可以 找到模板和静态文件等东西。
"""
app = Flask(__name__)


@app.route('/')  # route()装饰器来告诉Flask触发函数的URL
def hello_world():  # 函数名称被用于生成相关联的URL。函数最后返回需要在用户浏览器中显示的信息。
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=20227)
