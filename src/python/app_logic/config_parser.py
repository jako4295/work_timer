import json
import os

class ConfigParser:
    current_env_variables = []
    env_setter_called = False

    def __init__(self, config_path: str):
        """
        Config is saved to environment variables.
        In the config JSON everything should be written without underscores
        as they are used to seperate levels of configs in the environment

        As of now only JSON config of level 1 (meaning 1 level of 
        sub dictionary) is supported.
        """
        print("flatpak config path: ", config_path)
        self.config_path = config_path
    
    def set_env_variables(self):
        # should only be called once cause of of set_values works
        if self.env_setter_called:
            return
        set_values = {}
        config = self._read_config()
        for key, value in config.items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    env_key = f"{key.upper()}_{subkey.upper()}"
                    env_value = subvalue
                    os.environ[env_key] = env_value
                    set_values[env_key] = env_value
            else:
                set_values[key] = value
                env_key = key.upper()
                env_value = value
                os.environ[env_key] = env_value
        
        self.current_env_variables = set_values
        self.env_setter_called = True
    
    def get_env_variables(self):
        return self.current_env_variables

    def _read_config(self) -> dict:
        with open(self.config_path, "r") as f:
            config = json.load(f)
        
        return config
    