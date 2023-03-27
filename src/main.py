from python import ConfigParser, MainWindow, Page
import sys


if __name__ == "__main__":
    # only pass config path as arugment
    config_path = sys.argv[1]
    config_parser = ConfigParser(config_path)
    config_parser.set_env_variables()
    env_variables = config_parser.get_env_variables()

    gui = MainWindow(start_page=Page.ABOUT)
    gui.mainloop()
