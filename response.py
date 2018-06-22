from django.http import HttpResponse, JsonResponse

class Res():
    def success(self, num, data):
        HttpResponse.status_code = 200
        return JsonResponse({'total': num, 'data': data}, safe=False)

    def error(self, msg, code = 500):
        HttpResponse.status_code = code
        return HttpResponse(msg)

    # Alias with error(self, "Method Not Allowed", 405)
    def method_not_allowed(self):
        HttpResponse.status_code = 405
        return HttpResponse("Method Not Allowed")