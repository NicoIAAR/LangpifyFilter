ALLOWED_ORIGINS = (
    "https://tudominio.com",
    "https://otrodominioseguro.com"
)

def is_origin_allowed(origin: str) -> bool:
    """
    Verifica si el origen está permitido.
    """
    return origin in ALLOWED_ORIGINS

def anti_cors_filter(request_headers: dict) -> bool:
    """
    Filtro anti-CORS: retorna True si la solicitud es segura, False si debe ser bloqueada.
    """
    origin = request_headers.get("Origin")
    if origin is None:
        # Si no hay cabecera Origin, puede ser una petición legítima de backend
        return True
    return is_origin_allowed(origin)
