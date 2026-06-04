def ammount(total, paid):
    if paid >=  total:
        return 0.0
    else:
        return total - paid
    
print(ammount(100.0, 30.0))
