from flask import Flask, render_template, redirect, request
import pymysql


app = Flask(__name__)
api = Api(app)



@app.route('/')  #route는 URL을 결정해 줌 # ip:port번호(aws에서 8080으로 지정. 지정 안하면 5000번이 default)를 입력하면
                                        # 만들어 놓은 웹에 접근할 수 있음
def index():
    return "url에 /board를 입력하세요^^"

def upload_file_to_bucket(file):
    BUCKET_NAME = 's3-board-files-gencomi'
    S3_KEY = 'images/' + file.filename
    s3 = boto3.client('s3')
    s3.put_object(
            Bucket = BUCKET_NAME
        Body = file,
        Key = S3_KEY,
        ContentType = file.content_type)


@app.route('/board')
def board_list():
    db = pymysql.connect(host=database-1.cvc93xvkumqc.ap-northeast-2.rds.amazonaws.com ,port=3306, db=awsdb ,passwd=qpflqpfl95! ,user='admin' )
    curs = db.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM board ORDER BY id DESC'
    curs.execute(sql)
    results = curs.fetchall()
    curs.close()
    db.close()
    return render_template('board_list.html', results=results)












;


# @app.route('/board/writeform')
# def board_writeform():
#     return render_template('board_writeform.html')
#
# @app.route('/board/write')
# def write():
#     return redirect('/board') #client가 재요청하게하는 함수
#
# @app.route('/board/view')
# def view():
#     return




# def hello():
#     return "<h1>hello Flask~~!!  hahaha<h1>"
#
# @app.route('/test')
# def test():
#     # 수행해야 할 로직이 이 곳으로 들어옴
#     return "test"
#
@app.route('/hello')
def hi():
    name = 'an yoo jin'
    return render_template('hello.html',name=name) #flask 모듈이 render_template 제공
                                                   #render_template 함수는 templates에 저장된 html을 불러오는 기능
# @app.route('/board')
#

if __name__ == '__main__':
    app.run("0.0.0.0",port =8080)

#flask 인식이 안 되어서(?) 웹페이지에