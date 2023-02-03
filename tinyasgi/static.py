DEFAULT_GZIP_PARAMS = {
    "minimum_size": 500,
    "compresslevel": 9
}

DEFAULT_CORS_PARAMS = {
    "allow_origins": (),
    "allow_methods": ("GET",),
    "allow_headers": (),
    "allow_credentials": False,
    "allow_origin_regex": None,
    "expose_headers": (),
    "max_age": 600,
} # noqa