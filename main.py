import os
from dotenv import load_dotenv
import dspy
from langfuse import get_client
from openinference.instrumentation.dspy import DSPyInstrumentor
import time

import evaluation_data
from signatures import PhotoDevelopmentParameterAnalysis

# 環境変数を読み込む
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# LangFuseでのトレースを有効にする
langfuse = get_client()
DSPyInstrumentor().instrument()

def validate_answer(eval_data, pred, trace=None):
    time.sleep(30)
    print("=============================================")
    print("correct parameter and direction is:" , eval_data.parameter, ",", eval_data.direction)
    print("answered parameter and direction is:" , pred.parameter, ",", pred.direction)
    if(eval_data.color or pred.color):
        print("correct color is:" , eval_data.color,)
        print("answered color is:" , pred.color)

    return int(eval_data.parameter == pred.parameter and eval_data.color == pred.color and eval_data.direction == pred.direction)


def main():
    # テスト用データの読み込み
    dataset = [dspy.Example({
        "base_image": dspy.Image(row["base_image"]),
        "developped_image": dspy.Image(row["developped_image"]),
        "parameter": row["parameter"],
        "color": row["color"],
        "direction": row["direction"]
    }).with_inputs("base_image", "developped_image") for row in evaluation_data.evaluation_data]


    with dspy.context(
        lm=dspy.LM(
            #"bedrock/global.anthropic.claude-sonnet-4-5-20250929-v1:0", cache=False, rpm=0.5,
            #"bedrock/global.anthropic.claude-opus-4-5-20251101-v1:0", cache=False, rpm=0.5,
            # "bedrock/us.amazon.nova-2-lite-v1:0", cache=False, rpm=5,
            #"openai/gpt-5.2-2025-12-11", api_key=OPENAI_API_KEY, cache=False, rpm=0.5,
            #"gemini/gemini-3-pro-preview", api_key=GEMINI_API_KEY, cache=False, rpm=0.5,
            "bedrock/global.anthropic.claude-opus-4-6-v1", cache=False, rpm=0.5
        )
    ):
        analyser = dspy.ChainOfThought(PhotoDevelopmentParameterAnalysis)
        evaluate = dspy.Evaluate(devset=dataset, metric=validate_answer, num_thread=1, display_table=True, display_progress=True)
        evaluate(analyser)



if __name__ == "__main__":
    main()
