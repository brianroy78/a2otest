import json

from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def solve_paper_league(req: HttpRequest):
    body: dict = json.loads(req.body)
    print(body)
    return HttpResponse(json.dumps({'response': 'gg pe'}))


@require_http_methods(["POST"])
def solve_chess(req: HttpRequest):
    return HttpResponse(json.dumps({'response': 'response to chess'}))


@require_http_methods(["POST"])
def solve_string_value(req: HttpRequest):
    return HttpResponse(json.dumps({'response': 'response to string value'}))
