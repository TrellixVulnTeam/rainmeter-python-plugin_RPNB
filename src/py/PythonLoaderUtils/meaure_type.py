from .rm_stub import RainmeterW
class MeasureBase:
    _num_instances: int = 0
    last_rm: RainmeterW
    
    @classmethod
    def get_num_instances(cls) -> int:
        return cls._num_instances

    @classmethod
    def set_num_instances(cls, p_num_instances: int):
        cls._num_instances = p_num_instances

    @classmethod
    def increase_instances(cls):
        cls._num_instances += 1
        
    @classmethod
    def decrease_instances(cls):
        cls._num_instances -= 1
    
    
    def __init__(self):
        self.increase_instances()
        self.last_rm = None

    def Reload(self, rm: RainmeterW, maxValue: float):
        self.last_rm = rm

    def Update(self) -> float:
        return 1.0

    def GetString(self) -> str:
        return ""

    def ExecuteBang(self, args):
        pass

    def Finalize(self):
        self.decrease_instances()
