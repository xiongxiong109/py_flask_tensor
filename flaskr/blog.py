# 博客蓝图
from flask import (
    Blueprint, render_template
)
from flaskr.auth import login_required

# 博客蓝图没有url_prefix，所以指向/
bp = Blueprint('blog', __name__)


# 博客首页
@bp.route('/', methods=['GET'])
# 需要鉴权
@login_required
def index():
    return render_template('blog/index.html')
