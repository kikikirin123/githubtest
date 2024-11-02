from flask import Flask , render_template

#アプリケーションをFlaskクラスからインスタンス化
app = Flask(__name__,template_folder="static")

#アノテーションでルーティング設定
@app.route("/")
def TopContents():
    return render_template('index.html')

#ファイル単体で実行する際にはデバッグモードONでプログラム実行
if __name__=="__main__":
    app.run(debug=True)