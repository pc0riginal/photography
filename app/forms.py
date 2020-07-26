from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,IntegerField,DateField,MultipleFileField
from wtforms.validators import DataRequired,Required,NumberRange,Regexp,Length,ValidationError,Optional
from flask_wtf.file import FileRequired,FileAllowed
class Upload(FlaskForm):
    folderName = StringField(label="Folder Name",validators=[DataRequired(),Length(max=25)])
    secretKey = PasswordField(label="Secret Key",validators=[DataRequired(),Length(max=25)])
    files = MultipleFileField('File(s) Upload')
    submit = SubmitField(label="Upload")
    def validate_secretKey(self,field):
        if self.secretKey.data != "parasmoon@1998#1998":
            raise ValidationError("enter the valid key!")
