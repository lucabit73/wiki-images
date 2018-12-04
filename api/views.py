from django.http import JsonResponse


def index(request):
    resp = {'data': [{'num': 1}, {'num': 2}]}
    return JsonResponse(resp)
