from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlPlan
from app.uses_cases.plan.gestionarPlan import postPlan, getPlanCod
from app.api.shared.tokenHandler import token_required
## ESTE OBJETO ES UN HELPER;

plan = urlPlan

@plan.route('')
class PlanHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postPlan(data,currentUser)


@plan.route('/<int:codPlan>')
class PlanHandler(Resource):
    @token_required
    def get(data,currentUser,codPlan):
        return getPlanCod(data,codPlan)