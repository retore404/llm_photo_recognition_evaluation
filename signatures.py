import dspy
from typing import Literal, Optional


class PhotoDevelopmentParameterAnalysis(dspy.Signature):
    """
    Given a base image and a developped image, identify the Lightroom parameters to adjust on the base image to match the developped image.
    """

    base_image: dspy.Image = dspy.InputField(desc="the base image")
    developped_image: dspy.Image = dspy.InputField(
        desc="the image which is developped by using Lightroom."
    )
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
        "saturation(overall)",
        "color_mixier_hue",
        "color_mixier_saturation",
        "color_mixier_brightness",
    ] = dspy.OutputField(
        desc="the Lightroom parameter which is adjusted on the base image to match the developped image."
    )
    color: Optional[Literal[
        "red", "orange", "yellow", "green", "aqua", "blue", "purple", "magenta"
    ]] = dspy.OutputField(
        desc="(optional) the color which is adjusted by color mixier - this field **must be filled only when the parameter is color_mixier_hue or color_mixer_saturation or color_mixer_brightness**"
    )
    direction: Literal["positive", "negative"] = dspy.OutputField(
        desc="the adjustment direction of selected parameter"
    )
