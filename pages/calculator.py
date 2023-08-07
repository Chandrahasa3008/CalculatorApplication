# calculator_page.py
from pywinauto.application import Application
from utilities.calculator_constants import CalculatorConstants
import time

class CalculatorPage:

    # Launch the Calculator app
    def __init__(self):
        self.app = Application(backend="uia").start(CalculatorConstants.CALC_EXE).connect(title=CalculatorConstants.WINDOW_TITLE, timeout=CalculatorConstants.TIMEOUT)
        # self.app.window().print_control_identifiers()

    # Close the app
    def close(self):
        self.app.kill()

    # Button click function with highlighter
    def click_button(self, button_text):
        self.app.window().child_window(title=button_text, control_type="Button").wrapper_object().click().draw_outline(colour='green', thickness=5)
        time.sleep(0.5)

    # Get results and returned for verification
    def get_result(self, display_id):
        return self.app.window().child_window(auto_id=display_id, control_type="Text").wrapper_object().window_text()

    # Implement other methods as needed to interact with the calculator app.