def weekday_name(day_of_week):
    if day_of_week < 1:
        print("None")
        
    if day_of_week > 7:
        print("None")
    
    if day_of_week == 1:
        print("Sunday")

    if day_of_week == 2:
        print("Monday")

    if day_of_week == 3:
        print("Tuesday")

    if day_of_week == 4:
        print("Wednesday")

    if day_of_week == 5:
        print("Thursday")

    if day_of_week == 6:
        print("Friday")

    if day_of_week == 7:
        print("Saturday")

    
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """