def calculate_average_order_value(orders):
    try:
        iterator = iter(orders)
    except TypeError:
        raise TypeError("orders must be an iterable (e.g., list or tuple)")

    total = 0.0
    count = 0
    for order in iterator:
        if not isinstance(order, dict):
            continue
        if order.get("status") == "cancelled":
            continue
        amount = order.get("amount")
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            continue
        total += amt
        count += 1

    if count == 0:
        return None
    return total / count