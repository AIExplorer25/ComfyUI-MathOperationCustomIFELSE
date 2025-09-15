import math
import numpy as np

# ComfyUI requires the class to be registered in a dict at the bottom of the file
class AutoResizeResolution:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {
                    "default": 640,
                    "min": 1,
                    "max": 8192,
                    "step": 1,
                    "tooltip": "Enter input width"
                }),
                "height": ("INT", {
                    "default": 640,
                    "min": 1,
                    "max": 8192,
                    "step": 1,
                    "tooltip": "Enter input height"
                }),
            },
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("new_width", "new_height",)
    FUNCTION = "resize_resolution"
    CATEGORY = "Utils/Resolution"
    DESCRIPTION = (
        "Adjusts resolution automatically: "
        "If width > height → (832, 480), "
        "If width < height → (480, 832), "
        "If equal → (640, 640)."
    )

    def resize_resolution(self, width, height):
        if width > height:
            return (832, 480)
        elif width < height:
            return (480, 832)
        else:
            return (640, 640)


# Required for ComfyUI to register the node
NODE_CLASS_MAPPINGS = {
    "AutoResizeResolution": AutoResizeResolution
}
