from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    title = 'man Key'
    data = [
        '張三',
        '李四',
        '王大拿'
    ]
    return render_template('index.html', title=title, data=data)


if __name__ == "__main__":
    # debug=True的話之後在run本檔案時修改本檔案會自動重新rerun一般
    app.run(debug=True)
