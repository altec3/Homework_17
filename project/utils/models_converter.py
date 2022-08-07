from flask_restx import fields as flask_fields
from marshmallow import fields as marshmallow_fields, Schema

from project.setup.inits.app_init import api

TYPE_MAPPING = {
    marshmallow_fields.Float: flask_fields.Float,
    marshmallow_fields.Integer: flask_fields.Integer,
    marshmallow_fields.Int: flask_fields.Integer,
    marshmallow_fields.String: flask_fields.String,
    marshmallow_fields.Number: flask_fields.Integer,
    marshmallow_fields.DateTime: flask_fields.DateTime,
}


def convert_and_register_model(schema_name: str, schema_data: Schema):

    schema_fields = getattr(schema_data, "_declared_fields")
    converted_schema = {}
    for field in schema_fields:
        converted_schema[field] = TYPE_MAPPING[type(schema_fields[field])]

    api.model(name=schema_name, model=converted_schema)

    return converted_schema
