# setup 
import uuid
from fastapi import FastAPI, HTTPException
from app.func.generate_id import gen_id
from app.func.calc_points import calc_points
from app.func.storage import ReceiptStorage
from app.func.schema import Receipt
from app.func.check_data import check_data

app = FastAPI()

receipts = ReceiptStorage()

@app.post("/receipts/process")
def process(receipt: Receipt):
    """
    process a receipt and calculate points
    """
    try: 
        # validate the receipt
        receipt_dict = receipt.dict() 
        check_data(receipt_dict)
        id = gen_id()
        receipts.add_receipt(id, receipt_dict)
        points = calc_points(receipt_dict)
        receipts.add_points(id, points)
    except: 
        raise HTTPException(status_code=400, detail="The receipt is invalid.")
    
    return {"id": id}


@app.get("/receipts/{id}/points")
def get_points(id):
    """
    get points for a receipt
    """
    try:
        return receipts.get_points(id)
    except:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")