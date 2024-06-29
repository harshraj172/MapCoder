from promptings.CoT import CoTStrategy
from promptings.Direct import DirectStrategy
from promptings.Analogical import AnalogicalStrategy
from promptings.SelfPlanning import SelfPlanningStrategy

from promptings.MapCoder import MapCoder as MapCoder
from promptings.MapCoderV2 import MapCoderV2
from promptings.MapCoderV3 import MapCoderV3


class PromptingFactory:
    @staticmethod
    def get_prompting_class(prompting_name):
        if prompting_name == "CoT":
            return CoTStrategy
        elif prompting_name == "MapCoder":
            return MapCoder
        elif prompting_name == "MapCoderV2":
            return MapCoderV2
        elif prompting_name == "MapCoderV3":
            return MapCoderV3
        elif prompting_name == "Direct":
            return DirectStrategy
        elif prompting_name == "Analogical":
            return AnalogicalStrategy
        elif prompting_name == "SelfPlanning":
            return SelfPlanningStrategy
        else:
            raise Exception(f"Unknown prompting name {prompting_name}")
