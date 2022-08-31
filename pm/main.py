from cli import run
from pm.settings.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    print(settings.port)
    run.app()

    # TODO -> need implementation
