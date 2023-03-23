import os
from typing import Dict
from enum import Enum


class VariableEnums(Enum):
    TIMER_LOG_DIR = 1


class VariableHandler:
    variables = dict()

    def __init__(self, timer_log_dir: str):
        self.variables[VariableEnums.TIMER_LOG_DIR] = timer_log_dir


    def get_variable(self) -> Dict[VariableEnums, str]:
        return self.variables
    
    def set_variable(self, variable: VariableEnums, value: str):
        if variable in self.variables.keys():
            self.variables[variable] = value
        else:
            raise Exception("Variable not found")
