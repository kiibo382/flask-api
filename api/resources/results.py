from flask_restful import Resource, reqparse, abort
from flask import jsonify

from api.models.results import ResultModel, ResultSchema
from api.database import db


class ResultsListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    self.reqparse.add_argument('state', required=True)
    super(ResultsListAPI, self).__init__()


  def get(self):
    results = ResultModel.query.all()
    jsonData = ResultSchema(many=True).dump(results).data
    return jsonify({'items': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    results = ResultModel(args.name, args.state)
    db.session.add(results)
    db.session.commit()
    res = ResultSchema().dump(results).data
    return res, 201


class ResultsAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    self.reqparse.add_argument('state')
    super(ResultsAPI, self).__init__()


  def get(self, id):
    results = db.session.query(ResultModel).filter_by(id=id).first()
    if results is None:
      abort(404)

    res = ResultSchema().dump(results).data
    return res


  def put(self, id):
    results = db.session.query(ResultModel).filter_by(id=id).first()
    if results is None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(results, name, value)
    db.session.add(results)
    db.session.commit()
    return None, 204


  def delete(self, id):
    results = db.session.query(ResultModel).filter_by(id=id).first()
    if results is not None:
      db.session.delete(results)
      db.session.commit()
    return None, 204