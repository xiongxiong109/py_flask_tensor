# 博客蓝图
from flask import (
    Blueprint, render_template
)

bp = Blueprint('blog', __name__, url_prefix='/blog')


# 博客首页
@bp.route('/index', methods=['GET'])
def index():
    return render_template('blog/index.html')
