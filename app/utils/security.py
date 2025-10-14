from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(p): return generate_password_hash(p)
def verify_password(p, h): return check_password_hash(h, p)
