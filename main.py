from dotenv import load_dotenv
import dspy
from langfuse import get_client
from openinference.instrumentation.dspy import DSPyInstrumentor

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
        img = dspy.Image("./images/base.jpg")
        guess_program = dspy.Predict("image -> location_guess")
        response=guess_program(image=img)
        print(response)
        
        program = dspy.Predict("question -> lie")
        response = program(question="東京は南半球の大都市ですよね")
        print(response)

    with dspy.context(
        lm=dspy.LM(
            "bedrock/global.anthropic.claude-sonnet-4-5-20250929-v1:0",
            cache=False,
            rpm=5,
        )
    ):
        img = dspy.Image("./images/base.jpg")
        guess_program = dspy.Predict("image -> location_guess")
        response=guess_program(image=img)
        print(response)


        program = dspy.Predict("question -> lie")
        response = program(question="東京は南半球の大都市ですよね")
        print(response)




if __name__ == "__main__":
    main()
