import json, copy
from django.views import View
from django.core import serializers

class BaseView(View):
    @classmethod
    def ParseJsonBody(self, request):
        body_data = json.loads(request.body)
        return body_data

    # This doesn't check the type of each attribute, so make sure request payload have correct type for each key-value pair.
    @classmethod
    def ParseJsonBodyStruct(self, request, obj):
        json_body = json.loads(request.body)

        result = obj()
        original = obj()
        for key in vars(original):
            try:
                setattr(result, key, json_body[key])
            except Exception as e:
                continue
        return result