from datetime import datetime

from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
import uuid

from api.database import db


ma = Marshmallow()


class ResultModel(db.Model):
  __tablename__ = 'result'

  id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.String(255), nullable=False)
  state = db.Column(db.String(255), nullable=False)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __init__(self, name, state):
    self.name = name
    self.state = state


  def __repr__(self):
    return '<ResultModel {}:{}>'.format(self.id, self.name)


class ResultSchema(ma.ModelSchema):
  class Meta:
    model = ResultModel

  createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
  updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')