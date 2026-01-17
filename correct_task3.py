import math

def average_valid_measurements(values):
    try:
        iterator = iter(values)
    except TypeError:
        raise TypeError("values must be an iterable (e.g., list or tuple)")

    total = 0.0
    count = 0
    for v in iterator:
        if v is None:
            continue
        try:
            num = float(v)
        except (TypeError, ValueError):
            continue
        if math.isnan(num):
            continue
        total += num
        count += 1

    if count == 0:
        return None
    return total / count