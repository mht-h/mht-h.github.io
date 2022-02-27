# 胡涵的python工厂
# 开发时间：2022/2/25 13:17
from wtforms import StringField, SubmitField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    cx = SubmitField(u'出校') # 保存按钮
    rx = SubmitField(u'入校') # 发布按钮