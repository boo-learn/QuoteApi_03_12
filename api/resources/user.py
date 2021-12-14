from api import Resource, reqparse, db
from api.models.user import UserModel


class UserResource(Resource):
    def get(self, author_id=None):
        pass

    def post(self):
        ...
