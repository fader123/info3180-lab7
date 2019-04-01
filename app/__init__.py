from flask import Flask
from flask_wtf.csrf import CSRFProtect


UPLOAD_FOLDER = './app/static/uploads'
Allowed_uploads=['png','jpg']


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['Allowed_uploads'] = Allowed_uploads

app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'


app.config.from_object(__name__)
from app import views
