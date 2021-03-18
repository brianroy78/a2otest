import json

from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from tests.business.paper_league import solve_paper_league


@require_http_methods(["POST"])
def solve_paper_league_controller(req: HttpRequest):
    body: dict = json.loads(req.body)
    return HttpResponse(json.dumps({'response': solve_paper_league(body.get('data'))}))


@require_http_methods(["POST"])
def solve_chess_controller(req: HttpRequest):
    return HttpResponse(json.dumps({'response': 'response to chess'}))


@require_http_methods(["POST"])
def solve_string_value_controller(req: HttpRequest):
    return HttpResponse(json.dumps({'response': 'response to string value'}))
