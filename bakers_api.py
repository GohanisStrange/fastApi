# from datetime import datetime
# from database.models import Bakers
# from database import get_db
#
#
# def new_backers():
#     db = next(get_db(Bakers, baker_id))
#
#     new_backer = Bakers(Bakers=Bakers)
#
#     db.add(new_backer)
#     db.commit()
#     return 'новоя пекарня занесена'
#
# def get_exact_baker(Baker):
#     db = next(get_db())
#
#     exact_baker = db.query(Baker).filter_by(baker_id=baker_id).first()
#
#     return exact_cupcakes
#
#
#
