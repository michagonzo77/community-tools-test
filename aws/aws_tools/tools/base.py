from kubiya_sdk.tools.models import Tool
from .common import COMMON_FILES

class AWSCliTool(Tool):
    def __init__(self, name, description, content, args, long_running=False):
        super().__init__(
            name=name,
            description=description,
            type="docker",
            image="amazon/aws-cli:latest",
            content=content,
            args=args,
            files=COMMON_FILES,
            env=["BLa"],
            long_running=long_running
        )

class AWSSdkTool(Tool):
    def __init__(self, name, description, content, args, long_running=False):
        super().__init__(
            name=name,
            description=description,
            type="python",
            content=content,
            args=args,
            requirements=["boto3"],
            files=COMMON_FILES,
            env=[],
            long_running=long_running
        )
