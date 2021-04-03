import asyncio

import uvicorn
from typer import Typer

from handson_fastapi.db.base import init_models

cli = Typer()


@cli.command()
def reset_db():
    asyncio.run(init_models())
    print("Done.")


@cli.command()
def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    cli()
