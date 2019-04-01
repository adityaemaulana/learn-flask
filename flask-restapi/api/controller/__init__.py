from flask import Blueprint
from flask_restful import Api
from .category_controller import CategoryController
from .comment_controller import CommentController

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Defining the route

api.add_resource(CategoryController, '/category')
api.add_resource(CommentController, '/comment')