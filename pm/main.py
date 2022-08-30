from settings.settings import load_settings_from_file
from cli import run

if __name__ == "__main__":
    settings = load_settings_from_file('settings.cfg')

    run.app()

    print("TODO -> need implementation")
