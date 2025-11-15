from litestar.response import Response


def not_found_handler(_, exc: Exception) -> Response:
    return Response({"error": str(exc)}, status_code=404)
