import uuid
from sqlalchemy import Column, String

from app.database import Base
from app.models.base import GUID

from .base import TimestampMixin


class Demo(TimestampMixin, Base):
    __tablename__ = "demo"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(20), nullable=False)