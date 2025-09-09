from pydantic import BaseModel, Field
from typing import Literal, Optional
from uuid import UUID, uuid4
from datetime import datetime

# pet model where it defines the pet with id as the primary key, and is given attributes
# where you can define their species, name, and age
class PetBase(BaseModel):
    species: Literal["Dog", "Cat", "Bird", "Fish"] = Field(
        ..., description="Species of the pet.", json_schema_extra={"example": "Dog"}
    )
    name: str = Field(..., description="Name of the pet.", json_schema_extra={"example": "Mochi"})
    age: Optional[int] = Field(None, description="Age of pet in years.", json_schema_extra={"example": 3})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "species": "Dog",
                    "name": "Mochi",
                    "age": 3,
                }
            ]
        }
    }

class PetCreate(PetBase):
    """Add a new Pet."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "species": "Dog",
                    "name": "Mochi",
                    "age": 3,
                }
            ]
        }
    }

class PetUpdate(BaseModel):
    """Partial update for a Pet"""
    species: Optional[Literal["Dog", "Cat", "Bird", "Fish"]] = Field(
        None, description="Species of the pet.", json_schema_extra={"example": "Dog"}
    )
    name: Optional[str] = Field(None, description="Name of the pet.", json_schema_extra={"example": "Mochi"})
    age: Optional[int] = Field(None, description="Age of pet in years.", json_schema_extra={"example": 3})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Mochi", "age": 3},
                {"species": "Dog"},
                {"age": 3},
            ]
        }
    }

class PetRead(PetBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Pet ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "99999999-9999-4999-8999-999999999999",
                    "species": "Dog",
                    "name": "Mochi",
                    "age": 3,
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }