def login(_id):
    members = ['bughunt', 'hs2207']
    for member in members:
        if member==_id:
            return True
    return False
