XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "'><script>alert(1)</script>"
]

WEAK_PASSWORDS = [
    "123456",
    "password",
    "admin",
    "admin123"
]