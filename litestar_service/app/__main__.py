from litestar import Litestar
from app.routes import router
from app.db import init_db
from app.error_handlers import not_found_handler


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[router],
        on_startup=[init_db],
        exception_handlers={404: not_found_handler},
    )


# ---- Точка запуску ----
if __name__ == "__main__":
    print(">>> Starting Litestar...")
    import uvicorn

    uvicorn.run("app.__main__:create_app", factory=True, host="0.0.0.0", port=5000, reload=True)
