from flask import Blueprint, request, make_response, abort, Response
from app.models.author import Author
from app.models.book import Book
from ..db import db
from .route_utilities import validate_model

bp = Blueprint("authors_bp", __name__, url_prefix="/authors")
# create author
@bp.post("")
def create_author():
    request_body = request.get_json()

    try:
        new_author = Author.from_dict(request_body)
        
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    
    db.session.add(new_author)
    db.session.commit()

    return make_response(new_author.to_dict(), 201)

# get all authors
@bp.get("")
def get_all_authors():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.name.ilike(f"%{name_param}%"))

    authors = db.session.scalars(query.order_by(Author.id))
    authors_response = [author.to_dict() for author in authors]

    return authors_response

# create book with authors
@bp.post("/<author_id>/books")
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)
    
    request_body = request.get_json()
    request_body["author_id"] = author.id

    try:
        new_book = Book.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
        
    db.session.add(new_book)
    db.session.commit()

    return make_response(new_book.to_dict(), 201) 

# get books by author
@bp.get("/<author_id>/books")
def get_books_by_author(author_id):
    author = validate_model(Author, author_id)
    response = [book.to_dict() for book in author.books]
    return response

# get authpr by id
@bp.get("/<author_id>")
def get_one_author(author_id):
    author = validate_model(Author, author_id)
    return author.to_dict()

#update author by id
@bp.put("/<author_id>")
def update_author(author_id):
    author = validate_model(Author, author_id)
    request_body = request.get_json()
    
    author.name = request_body["name"]
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")

# delete author
@bp.delete("/<author_id>")
def delete_author(author_id):
    author = validate_model(Author, author_id)
    db.session.delete(author)
    db.session.commit()
    
    return Response(status=204, mimetype="application/json")
