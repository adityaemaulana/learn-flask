from flask import request
from flask_restful import Resource
from api.models import Comment, CommentSchema
from api import db

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()

class CommentController(Resource):
  def get(self):
    comments = Comment.query.all()
    comments = comments_schema.dump(comments).data
    return {'status': 'success', 'data': comments}, 200

  def post(self):
    # Fetch the request
    json_data = request.get_json(force=True)
    if not json_data:
      return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = comment_schema.load(json_data)
    if errors:
        return {"status": "error", "data": errors}, 422
    category_id = Category.query.filter_by(id=data['category_id']).first()
    if not category_id:
        return {'status': 'error', 'message': 'comment category not found'}, 400
    
    # Create the object that will be added
    comment = Comment(
        category_id=data['category_id'], 
        comment=data['comment']
        )

    # Insert the data
    db.session.add(comment)
    db.session.commit()

    result = comment_schema.dump(comment).data

    return {'status': "success", 'data': result}, 201

    result = comment_schema.dump(comment).data

    return {'status': "success", 'data': result}, 201