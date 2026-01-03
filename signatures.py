import dspy
from typing import Literal


class PhotoDevelopmentParameterAnalysis(dspy.Signature):
    """
    Given a base image and a developped image, identify the Lightroom parameters to adjust on the base image to match the developped image.
    """

    base_image: dspy.Image = dspy.InputField(desc="the base image")
    developped_image: dspy.Image = dspy.InputField(desc="the developped image")
    parameter: Literal[
        "whitebalance",
        "exposure",
        "contrast",
        "highlight",
        "shadow",
        "white_level",
        "black_level",
        "texture",
        "clarity",
        "dehaze",
        "vibrance",
        "saturation",
    ] = dspy.OutputField(
        desc="the Lightroom parameter which is adjusted on the base image to match the developped image."
    )
    direction: Literal["positive", "negative"] = dspy.OutputField(
        desc="the adjustment direction of selected parameter"
    )
