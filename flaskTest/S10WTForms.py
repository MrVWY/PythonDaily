#生成html
class InputText(object):

    def __str__(self):
        return '<input type="text" />'

class Inputmail(object):

    def __str__(self):
        return  '<input type="mail" />'


#对数据格式校验
class stringField(object):
    def __init__(self,wg,reg):
        self.wg = wg
        self.reg = reg

    def __str__(self):
        return str(self.wg)

    def vlaid(self,val):
        import re
        return re.match(self.reg,val)


#管理所有字段
class LoginForm(object):
    X = stringField(wg=InputText(),reg='\d+')
    Y = stringField(wg=Inputmail(), reg='\w+')

    def __str__(self,form):
        self.form = '发过来的数据'

    def validate(self):
        field = {'X':self.X,'Y':self.Y}
        for name,field in field.items():
            field.vlaid(self.form[name])

wp = LoginForm()