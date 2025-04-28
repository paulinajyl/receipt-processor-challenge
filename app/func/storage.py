class ReceiptStorage:
    def __init__(self):
        self.receipts = {}
    
    def add_receipt(self, id: str, receipt_data):
        """
        add a receipt ID and receipt data, no points yet
        """
        if id in self.receipts:
            raise ValueError("the ID already exists")
        
        self.receipts[id] = {
            "receipt": receipt_data,
            "points": None
        }
        
    def add_points(self, id: str, points: int):
        """
        add points to a specific receipt ID
        """
        if type(points) != int:
            raise TypeError("points must be an integer")
        
        if id in self.receipts:
            self.receipts[id]["points"] = points
        else:
            raise ValueError("the ID does not exist")
            
    def get_points(self, id: str):
        """
        get points for a specific receipt ID
        """
        if id in self.receipts:
            return {"points": self.receipts[id]["points"]}
        else:
            raise ValueError("the ID does not exist")