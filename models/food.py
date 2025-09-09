from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import date, datetime

# food model
class FoodBase(BaseModel):
    category: Literal["Fruits", "Vegetables", "Grains", "Protein", "Dairy"] = Field(
        ..., #required
        description="Food category.",
        json_schema_extra={"example": "Fruits"},
    )
    nameID: str = Field(
        ...,
        description="Name of the food item.",
        json_schema_extra={"example": "Apple"},
    )
    calories: Optional[int] = Field(
        None,
        description="Calories per serving.",
        json_schema_extra={"example": 95},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category": "Fruits",
                    "nameID": "Apple",
                    "calories": 95,
                }
            ]
        }
    }

class FoodCreate(FoodBase):
    """Add a new Food."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category": "Fruits",
                    "nameID": "Apple",
                    "calories": 95,
                }
            ]
        }
    }

class FoodUpdate(BaseModel):
    """Partial update for a Food"""
    category: Optional[Literal["Fruits", "Vegetables", "Grains", "Protein", "Dairy"]] = Field(
        None, description="Food category.", json_schema_extra={"example": "Fruits"}
    )
    nameID: Optional[str] = Field(None, description="Name of the food item.", json_schema_extra={"example": "Apple"})
    calories: Optional[int] = Field(None, description="Calories per serving.", json_schema_extra={"example": 95})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"nameID": "Banana", "calories": 105},
                {"category": "Vegetables"},
                {"calories": 200},
            ]
        }
    }

class FoodDelete(BaseModel):
    """Delete a Food by nameID"""
    nameID: str = Field(..., description="Name of the food item to delete.", json_schema_extra={"example": "Apple"})
    category: str = Field(..., description="Category of the food item to be deleted.", json_schema_extra={"example": "Fruits"})
    calories: int = Field(..., description="Calories per serving of the food item to be deleted.", json_schema_extra={"example": 95})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category": "Fruits",
                    "nameID": "Apple",
                    "calories": 95,
                }
            ]
        }
    }

class FoodRead(FoodBase):
    """Server representation returned to clients."""
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
                    "category": "Fruits",
                    "nameID": "Apple",
                    "calories": 95,
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }
