# -*- coding: utf-8 -*-
import json
import uuid

from sqlalchemy import Column, DateTime, Text  # Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext import mutable
from sqlalchemy.sql import func
from sqlalchemy.types import CHAR, TypeDecorator


class CreatedAtMixin:
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class TimestampMixin(CreatedAtMixin):
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class JsonEncodedDict(TypeDecorator):  # pylint: disable=abstract-method
    """Enables JSON storage by encoding and decoding on the fly."""

    impl = Text

    def process_bind_param(
        self, value, dialect
    ):  # pylint: disable=unused-argument, no-self-use
        if value is None:
            return "{}"
        return json.dumps(value)

    def process_result_value(
        self, value, dialect
    ):  # pylint: disable=unused-argument, no-self-use
        if value is None:
            return {}
        return json.loads(value)


class GUID(TypeDecorator):  # pylint: disable=abstract-method
    """Platform-independent GUID type.

    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """

    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if dialect.name == "postgresql":
            return str(value)
        if not isinstance(value, uuid.UUID):
            return "%.32x" % uuid.UUID(value).int
        # hexstring
        return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value


mutable.MutableDict.associate_with(JsonEncodedDict)
