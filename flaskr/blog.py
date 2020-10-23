# 博客蓝图
from flask import (
    Blueprint, render_template
)
from flaskr.db import get_db
from flaskr.auth import login_required

# 博客蓝图没有url_prefix，所以指向/
bp = Blueprint('blog', __name__)


# 博客首页
@bp.route('/', methods=['GET'])
# 需要鉴权
@login_required
def index():
    return render_template('blog/index.html')


# 查询博客列表
@bp.route('/articles', methods=['POST'])
def fetch_article_list():
    db = get_db()
    articles = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return {
        "list": articles
    }
    # return articles or []
