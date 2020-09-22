# 数据库连接
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


# 连接数据库
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# 关闭数据库
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# 初始化数据库表
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# 定义一个指令，用于初始化数据库表
# 命令也需要在venv环境下才能执行
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
