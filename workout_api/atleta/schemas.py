#os schemas sao responsaveis por fazerem as validaçoes, determinar os dados q vc quer q apareça na api no json deretorno

from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', exampls='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', example='12345678910', max_length=11)]
    idade: Annotated[str, Field(description='Idade do atleta', example=25)]
    peso: Annotated[str, Field(description='Peso do atleta', exampls=75.5)]
    altura: Annotated[str, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]    