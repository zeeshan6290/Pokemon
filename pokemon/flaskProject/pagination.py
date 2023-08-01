from flask import request, jsonify


def paginate(func):
    def inner(*args, **kwargs):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        items = func(*args, **kwargs)
        start = (page - 1) * per_page
        end = start + per_page
        return jsonify({
            "data": items[start:end],
            "total": len(items),
            "page": page,
            "per_page": per_page,
            "total_pages": round(len(items)/per_page,0)
        })
    return inner
