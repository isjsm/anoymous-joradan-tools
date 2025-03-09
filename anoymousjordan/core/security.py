# في core/security.py
def rate_limit():
    now = time.time()
    if now - getattr(rate_limit, 'last_call', 0) < 1.0:
        raise Exception("Rate limit exceeded")
    rate_limit.last_call = now
