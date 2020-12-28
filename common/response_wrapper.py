import json


class ResponseWrapper:

    def __init__(self,*args, **kwargs):
        self.success = kwargs.get('success')
        self.data = kwargs.get('data')
        self.error = kwargs.get('error')

    def set_success(self, success):
        self.success = success

    def set_data(self, data):
        self.data = data

    def set_error(self, error):
        self.error = error

    def get_success(self):
        return self.success

    def get_data(self):
        return self.data

    def get_error(self):
        return self.error

    def json(self):
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error
        }

    def __repr__(self):
        response = {
            "success": self.success,
            "data": self.data,
            "error": self.error
        }
        return json.dumps(response)
