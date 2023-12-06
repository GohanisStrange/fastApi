from pydantic import BaseModel

class CupcakeRegisterValidator(BaseModel):
    name = str
    id = str
    price = str
    taste = str
    date = str

class EditeCupcakeValidator(BaseModel):
    cupcake_id = int
    exact_cupcakes = str
    new_cupcakes = str
    