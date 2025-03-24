from kevinbotlib.logger import Level
from kevinbotlib.robot import BaseRobot


class ExampleRobot(BaseRobot):
    def __init__(self):
        super().__init__(["DeployedRobotOpMode"], log_level=Level.TRACE)

    def opmode_init(self, opmode: str, enabled: bool) -> None:
        super().opmode_init(opmode, enabled)
        print("Example robot started up...")  # noqa: T201

        with open("deploy/example.txt", "r") as f:
            print(f.read())

        with open("assets/example.txt", "r") as f:
            print(f.read())