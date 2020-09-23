# 使用蓝图实现认证模块
# 引入多个模块需要换行时，可以使用Tuble
from flask import (
    Blueprint,
    render_template,
    request
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


# 添加auth相关路由
# 注册页面
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        return {
            'unm': form['user_nm'],
            'pwd': form['user_pwd']
        }
    return render_template('auth/register.html')
