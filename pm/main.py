from cli import run
from settings.settings import load_settings_from_file

if __name__ == "__main__":
    settings = load_settings_from_file('settings.cfg')

    run.app()

    print("TODO -> need implementation")
