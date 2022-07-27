def study_schedule(permanence_period, target_time):
    result = None
    if target_time is not None:
        result = 0
        for period in permanence_period:
            value1 = isinstance(period[0], int)
            value2 = isinstance(period[1], int)
            if not value1 or not value2:
                return None
            if period[0] <= target_time <= period[1]:
                result += 1
    return result
