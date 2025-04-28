from pydantic import BaseModel
from typing import List

# setup the schema for receipt
# so pydantic can validate the input

# also just kept the price and total
# as strings, since the calculations already
# convert them to ints/floats

class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    total: str
    items: List[Item]
