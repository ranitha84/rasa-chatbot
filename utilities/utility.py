

def group_by_budget(row):
    if row['budget_for2people'] < 300:
        return 'lesser than 300'
    elif 300 <= row['budget_for2people'] < 700:
        return 'between 300 to 700'
    else:
        return 'greater than 700'
