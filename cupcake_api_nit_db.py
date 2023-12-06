from fastapi import APIRouter

from datetime import datetime
from Cupcake_api.cupcake_api import edit_cupcakes, delete_cupcakes_db, new_cupcakes, get_exact_cupcakes,get_exact_cupcakes_by_taste

from Cupcake_api.__init__ import CupcakeRegisterValidator,EditeCupcakeValidator

cupcake_router = APIRouter(prefix='/cupcakes', tags='рвбота с кексами')

@cupcake_router.post('/new cupcakes')
async def register_cupcakes(data: CupcakeRegisterValidator):

    new_cupcakes_data = data.model_dump()
    checker = get_exact_cupcakes(data.id)

    if not checker:
        result = new_cupcakes(reg_date = datetime.now(), **new_cupcakes_data)
        return {'message': result}
    else:
        return {'message': 'такой кекс уже есть'}


@cupcake_router.get('/info')
async def get_pancake(pancake_id: int):
    result = get_exact_cupcakes(pancake_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого кекса нету'}

@cupcake_router.delete('/delete-cupcakes')
async def delete_pancakes(pancake_id: int):
    result = delete_cupcakes_db(pancake_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого кекса нету'}

