from kevinbotlib.robot import BaseRobot


class ExampleRobot(BaseRobot):
    def __init__(self):
        super().__init__(["DeployedRobotOpMode"])

    def opmode_init(self, opmode: str, enabled: bool) -> None:
        super().opmode_init(opmode, enabled)
        print("Example robot started up...")  # noqa: T201
