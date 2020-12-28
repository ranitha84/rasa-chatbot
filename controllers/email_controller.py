import logging
import json
import sys
import settings

from utilities import api
from utilities import create_mail

from flask import Response, request
from flask_restx import Resource, fields as restx_fields
from marshmallow import exceptions
from common.model import EmailSchema
from common.response_wrapper import ResponseWrapper
from flask_mail import Message

ns_email = api.namespace('test email', description = 'Test email delivery')

post_parser = ns_email.parser()
post_parser.add_argument('recipient', type=str, help='Recipient Email id', required=True)
post_parser.add_argument('email_body', type=str, help='Email Body', required=True)
post_parser.add_argument('email_subject', type=str, help='Email Subject', required=True)

post_payload = ns_email.model(
    "Email Payload",
    {
        'recipient': restx_fields.String(description = 'Recipient Email id', required= True),
        'email_body': restx_fields.String(description = 'Email body', required= True),
        'email_subject': restx_fields.String(description = 'Email Subject', required= True)
    }
)

@ns_email.route('/send-email')
class SendEmail(Resource):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    @ns_email.expect(post_payload)
    @ns_email.produces(mimetypes=["application/json"])
    @ns_email.response(code=400, description='Bad Request')
    @ns_email.response(code=401, description='Un Authorized')
    @ns_email.response(code=422, description='UnProcessable Entity')
    @ns_email.response(code=500, description='Internal Server Error')
    @ns_email.response(code=501, description='Not Implemented')
    def post(self):
        email_request = {}

        mail = create_mail()
        try:
            email_request = EmailSchema(many=False).load(request.json)
            print("############ error {} ".format(email_request))
        except exceptions.ValidationError as v_error:
            print("############ error {} ".format(v_error.messages))
            response = ResponseWrapper(success=False, error=v_error.messages)

            return Response(json.dumps(response.json()), status=422, mimetype='application/json')
        try:
            msg = Message(subject=email_request.get('email_subject'),
                          sender=settings.MAIL_USERNAME,
                          recipients=[email_request.get('recipient')])
            msg.body = email_request.get('email_body')
            mail.send(msg)
            # return "Please check you email,Sent"
            response = ResponseWrapper(success=True, data='Mail sent successfully',error='')

            return Response(json.dumps(response.json()), status=200, mimetype='application/json')
        except Exception as e:
            error = str(sys.exc_info()[1])
            print("############ error {} ".format(error))
            response = ResponseWrapper(success=False, error=error, data='')

            return Response(json.dumps(response.json()), status=500, mimetype='application/json')