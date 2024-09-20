from pydantic import BaseModel


class BandeiraCreate(BaseModel):
    nome: str
    tarifa: float


class BandeiraRead(BaseModel):
    id: int
    nome: str
    tarifa: float


class BandeiraUpdate(BaseModel):
    tarifa: float
    nome: str


class BandeiraReadList(BaseModel):
    bandeiras: list[BandeiraRead]