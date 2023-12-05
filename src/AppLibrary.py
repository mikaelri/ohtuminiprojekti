from ui.ui import Ui
from repositories.reference_writer import ReferenceWriter
from tests.stub_io import StubIO

class AppLibrary:
    def __init__(self):
        self.writer = ReferenceWriter()
        self.io = StubIO()
        self.app = Ui(self.writer, self.io)

    def input(self, value):
        self.app.io.add_input(value)

    def run_application(self):
        self.app.run()

    def output_should_contain(self, value):
        outputs = self.io.outputs
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )
