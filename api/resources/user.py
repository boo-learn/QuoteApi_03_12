from api import Resource, reqparse, db
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            users = UserModel.query.all()
            return users_schema.dump(users)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

# ImportError: cannot import name 'db' from partially initialized
# module 'api' (most likely due to a circular import)
# (/Users/timur/Projects/FlaskRESTfulTemplate/api/__init__.py)
