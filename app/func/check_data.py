def check_data(receipt):
    """
    check the data of the receipt
    """
    # check if purchase date is formatted yyy-mm-dd
    split_date = receipt["purchaseDate"].split("-")
    if len(split_date) != 3:
        raise ValueError("the purchase date must be formatted yyyy-mm-dd")
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("the purchase date must be formatted yyyy-mm-dd")
    
    # check if the purchase time is formatted hh:mm
    split_time = receipt["purchaseTime"].split(":")
    if len(split_time) != 2:
        raise ValueError("the purchase time must be formatted hh:mm")
    hour = split_time[0]
    minute = split_time[1]
    if len(hour) != 2 or len(minute) != 2:
        raise ValueError("the purchase time must be formatted hh:mm")

    # check if the items are a list
    if type(receipt["items"]) != list:
        raise TypeError("the items must be a list")
    
    # check if price is a float with 2 decimal places
    for item in receipt["items"]:
        split_price = item["price"].split(".")
        if len(split_price) != 2:
            raise ValueError("the price must have 2 decimal places")
        dollars = split_price[0]
        cents = split_price[1]
        if len(dollars) <=0 or len(cents) != 2:
            raise ValueError("the price must have 2 decimal places")