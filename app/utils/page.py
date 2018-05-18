# -*- coding: utf-8 -*-
from flask_sqlalchemy import Pagination
from werkzeug.exceptions import abort


def paginate(query, page, per_page=20, error_out=True):
    """提供分页的方法"""
    if error_out and page < 1:
        abort(404)
    items = query.limit(per_page).offset((page - 1) * per_page).all()
    if not items and page != 1 and error_out:
        abort(404)
    if page == 1 and len(items) < per_page:
        total = len(items)
    else:
        total = query.order_by(None).count()
    return Pagination(query, page, per_page, total, items)
