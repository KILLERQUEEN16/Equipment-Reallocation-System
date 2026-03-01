from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class MoveItemRequest(BaseModel):
    item_id: str = Field(..., min_length=1, description="Identificador único do item")
    from_location_id: str = Field(..., min_length=1, description="Local de origem")
    to_location_id: str = Field(..., min_length=1, description="Local de destino")
    quantity: int = Field(..., gt=0, description="Quantidade a ser movimentada")
    reason: Optional[str] = Field(default=None, max_length=255)
    requested_by: str = Field(..., min_length=1, description="Usuário solicitante")

    @field_validator("to_location_id")
    @classmethod
    def validate_different_locations(cls, value: str, info):
        source = info.data.get("from_location_id")
        if source and source == value:
            raise ValueError("Origem e destino devem ser diferentes")
        return value


class StockRecord(BaseModel):
    item_id: str
    location_id: str
    quantity: int


class MoveItemResponse(BaseModel):
    movement_id: str
    item_id: str
    moved_quantity: int
    from_location_id: str
    to_location_id: str
    from_location_balance: int
    to_location_balance: int
    moved_at: datetime
