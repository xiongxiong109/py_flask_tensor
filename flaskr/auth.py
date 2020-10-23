# 使用蓝图实现认证模块
# 引入多个模块需要换行时，可以使用Tuble
import functools
from flask import (
    Blueprint, flash, url_for,
    render_template, redirect,
    request, session, g
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


# 注册一个在视图函数之前运行的中间件
@bp.before_app_request
# 载入已登录的用户信息
def load_logged_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        g.user = db.execute(
            'SELECT * FROM user WHERE id = ?',
            (user_id, )
        ).fetchone()


# 添加auth相关路由
# 注册页面
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        form = request.form
        # 表单数据入库
        error = None
        unm = form['user_nm']
        pwd = form['user_pwd']
        # 表单校验
        if not unm:
            error = 'usernm is required'
        elif not pwd:
            error = 'password is required'
        # 注册内容
        else:
            # 查找一个唯一元素
            has_user = db.execute(
                'SELECT id FROM user WHERE username = ?', (unm,)
            ).fetchone()
            if has_user is not None:
                error = 'usernm has already existed'
            else:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (unm, generate_password_hash(pwd))
                )
                db.commit()
        # 如果有表单校验报错，返回对应报错信息
        error is not None and flash(error)
    return render_template('auth/register.html')


# 登录页面
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # 处理post请求
    if request.method == 'POST':
        db = get_db()
        # 切换成ajax
        form = request.json
        unm = form['user_nm']
        pwd = form['user_pwd']
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (unm, )
        ).fetchone()
        if user is None:
            error = 'user not found'
        # 校验密码
        else:
            is_pwd_correct = check_password_hash(user['password'], pwd)
            if not is_pwd_correct:
                error = 'password error'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('blog.index'))
        # error is not None and flash(error)
        if error is not None:
            return {
                "error": error
            }
        else:
            return {
                "error": ""
            }
    # get, 渲染登录页面
    # print(session.get('user_nm'))
    return render_template('auth/login.html')


# 登出
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


# 登录跳转装饰器(鉴权中间件)
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

