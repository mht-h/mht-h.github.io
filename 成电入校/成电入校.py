# 胡涵的python工厂
# 开发时间：2021/11/16 16:30
from flask import *
import datetime
import sys
sys.path.append(r'..')
from templates.forms import NewPostForm
app=Flask(__name__)
app.config["SECRET_KEY"] = 'c062aa57944c4cddab7b5b1730f94cd6'
name=''
ty=''
@app.route('/login',methods=['GET','POST'])
def login():
    form=NewPostForm()
    if request.method=='POST':
        if form.validate_on_submit():
            print(1)
            if form.rx.data:
                return redirect(url_for('display',name=form.title.data,msg='入校权限有效！'))
            elif form.cx.data:
                return redirect(url_for('display',name=form.title.data,msg='出校登记成功！'))
    return render_template('login.html',form=form)
@app.route('/display?name=<name>,msg=<msg>',methods=['GET','POST'])
def display(name,msg,):
    return render_template('display.html',time=str(datetime.datetime.now()).split('.')[0],name=name,msg=msg)
if __name__=='__main__':
    app.run(host="0.0.0.0",port=80)