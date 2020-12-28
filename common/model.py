from marshmallow import Schema, fields, ValidationError, validates_schema
import re


class EmailSchema(Schema):
    recipient = fields.String(required=True)
    email_body = fields.String(required=True)
    email_subject = fields.String(required=True)

    @validates_schema
    def validate_payload(self, data, **kwargs):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if  data['recipient']:
            email = data['recipient']
            if not re.search(regex, email):
                raise ValidationError('Not a valid email id')
