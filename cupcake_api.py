from datetime import datetime
from database.models import Cupcakes

from database import get_db

def new_cupcakes(cupcake_id, cupcake_amount , cupcake_price , cupcake_taste , cupcake_date):
    db = next(get_db())

    new_cupcake = Cupcakes(cupcake_price = cupcake_price, cupcake_id=cupcake_id, cupcake_amount=cupcake_amount , cupcake_date=datetime.now() , cupcake_taste=cupcake_taste)

    db.add(new_cupcake)
    db.commit()

    return 'новый кекс зарегистрирован'

def get_exact_cupcakes(cupcake_id):
    db = next(get_db())

    exact_cupcakes = db.query(Cupcakes).filter_by(cupcake_id=cupcake_id).first()

    return exact_cupcakes

def get_exact_cupcakes_by_taste(cupcake_taste):
    db = next(get_db())

    checker = db.query(Cupcakes).filterby(cupcake_taste=cupcake_taste).first()

    if checker:
        return checker
    else:
        return 'подобных вкусов нет'
def edit_cupcakes(cupcake_id , exact_cupcakes, new_cupcakes):
    db = next(get_db())

    exact_cupcakes = db.query(Cupcakes).filter_by(cupcake_id=cupcake_id).first()

    if exact_cupcakes:
        if edit_cupcakes =='price':
            exact_cupcakes.cupcake_price = new_cupcakes
        elif edit_cupcakes == 'amount':
            exact_cupcakes.cupcake_amount = new_cupcakes
        db.commit()

        return 'данные изменены'
    else:
        return 'не найдено'

def delete_cupcakes_db(cupcake_id):
    db = next(get_db())

    delete_cupcakes = db.query(Cupcakes).filter_by(cupcake_id=cupcake_id).first()
    if delete_cupcakes:
        db.delete(delete_cupcakes)
        db.commit()
        return 'удаление успешно выполнено'
    else:
        return 'данные не найдены'


