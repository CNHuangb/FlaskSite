import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


# Form：主要就是用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format error!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Verification code format error!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Username format error!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format error!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="The passwords are inconsistent twice!")])

    # 自定义验证：
    # 1. 邮箱是否已经被注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="This email has already been registered!")

    # 2. 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="Email or verification code error!")
        # else:
        #     # todo：可以删掉captcha_model
        #     db.session.delete(captcha_model)
        #     db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format error!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format error!")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="Title format error!")])
    content = wtforms.StringField(validators=[Length(min=3,message="Content format error!")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="Content format error!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="Question ID must be passed in!")])