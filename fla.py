from flask import Flask,render_template
app=Flask(__name__)

ANNOUNCEMENTS=[
    {
        'announcer':'Siddhesh Shrawne',
        'date':'19-01-24',
        'time':'21:37 pm',
        'text':'We are declaring war against Prussia'
    },
    {
        'announcer':'Otto Von Bismarck',
        'date':'19-01-24',
        'time':'21:40 pm',
        'text':'Ems Dispatch LMAO'
    }
]

@app.route("/")
def hello():
    return render_template('index.html',ANNOUNCEMENTS=ANNOUNCEMENTS)

if __name__=='__main__':
    app.run(debug=True)