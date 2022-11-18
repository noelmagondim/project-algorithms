def study_schedule(permanence_period, target_time):
    counter = 0

    for (entry, exit) in permanence_period:
        try:
            if entry <= target_time <= exit:
                counter += 1
        except (TypeError, ValueError, NameError):
            return None

    return counter
