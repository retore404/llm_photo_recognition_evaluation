from dotenv import load_dotenv
import dspy
from langfuse import get_client
from openinference.instrumentation.dspy import DSPyInstrumentor

from signatures import PhotoDevelopmentParameterAnalysis

# 環境変数を読み込む
load_dotenv()

# LangFuseでのトレースを有効にする
langfuse = get_client()
DSPyInstrumentor().instrument()


def main():
    with dspy.context(
        lm=dspy.LM(
            # "bedrock/global.anthropic.claude-sonnet-4-5-20250929-v1:0", cache=False, rpm=5
            "bedrock/us.amazon.nova-2-lite-v1:0",
            cache=False,
            rpm=5,
        )
    ):
        base_image = dspy.Image("./images/00_base.jpg")
        exposure_plus_image = dspy.Image("./images/00_exposure_plus1.jpg")

        analyser = dspy.ChainOfThought(PhotoDevelopmentParameterAnalysis)
        response = analyser(base_image=base_image, developped_image=exposure_plus_image)
        print(response)

        exposure_minus_image = dspy.Image("./images/00_exposure_minus1.jpg")
        response = analyser(base_image=base_image, developped_image=exposure_minus_image)
        print(response)


if __name__ == "__main__":
    main()
