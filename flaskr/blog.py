# 博客蓝图
from flask import (
    Blueprint, render_template
)

# 博客蓝图没有url_prefix，所以指向/
bp = Blueprint('blog', __name__)


# 博客首页
@bp.route('/', methods=['GET'])
def index():
    return render_template('blog/index.html')
