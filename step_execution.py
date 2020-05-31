from mlspeclib import MLObject
from pathlib import Path
import sys
import uuid
from random import randrange

sys.path.append(str(Path.cwd().parent))

from utils.utils import setupLogger  # noqa

# Making this a class in case we want sub functions.
class StepExecution:
    input_params = {}  # noqa
    execution_params = {}  # noqa
    ml_object = MLObject()  # noqa
    rootLogger = None  # noqa

    def __init__(self, input_params, execution_params):
        self.input_params = input_params
        self.execution_params = execution_params
        self.rootLogger = setupLogger().get_root_logger()

        # Execute all work in here.

        # Output input params & execution params
        if self.input_params is not None:
            self.rootLogger.debug(f"Input params: {self.input_params}")

        if self.execution_params is not None:
            self.rootLogger.debug(f"Execution params: {self.execution_params}")

    def execute(self, result_object_schema_type, result_object_schema_version):
        # Create Result object
        results_object = MLObject()
        results_object.set_type(
            schema_type=result_object_schema_type,
            schema_version=result_object_schema_version,
        )

        # Mocked up results
        return_dict = {
            "training_execution_id": uuid.uuid4(),
            "accuracy": float(f"{randrange(93000,99999)/100000}"),
            "global_step": int(f"{randrange(50,150) * 100}"),
            "loss": float(f"{randrange(10000,99999)/1000000}")
        }

        results_object.training_execution_id = return_dict["training_execution_id"]
        results_object.accuracy = return_dict["accuracy"]
        results_object.global_step = return_dict["global_step"]
        results_object.loss = return_dict["loss"]

        return results_object
