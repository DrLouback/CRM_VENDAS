from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime,time
from typing import Tuple
from enum import Enum


class ProdutoEnum(str, Enum):
    produto1 = 'ZapFlow com Gemini'
    produto2 = 'ZapFlow com Lhama'
    produto3 = 'ZapFlow com ChatGPT'


class Vendas(BaseModel):
    email: EmailStr
    data: str
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: str

    