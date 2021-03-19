import json

from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from tests.business.chess import solve_chess
from tests.business.chess_utils import parse_data
from tests.business.paper_league import solve_paper_league
from tests.business.string_value import solve_string_value


@require_http_methods(["POST"])
def solve_paper_league_controller(req: HttpRequest):
    body: dict = json.loads(req.body)
    return HttpResponse(json.dumps({'response': solve_paper_league(body.get('data'))}))


@require_http_methods(["POST"])
def solve_chess_controller(req: HttpRequest):
    body: dict = json.loads(req.body)
    return HttpResponse(json.dumps({'response': solve_chess(*parse_data(body.get('data')))}))


@require_http_methods(["POST"])
def solve_string_value_controller(req: HttpRequest):
    body: dict = json.loads(req.body)
    return HttpResponse(json.dumps({'response': solve_string_value(body.get('data'))}))
