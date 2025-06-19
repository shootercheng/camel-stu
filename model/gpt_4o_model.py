from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, RoleType, OpenAIBackendRole
from dotenv import load_dotenv
import os

load_dotenv(override=True)

base_url = os.getenv("gpt_base_url")
api_key = os.getenv("gpt_api_key")

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="gpt-4o-mini",
    url=base_url,
    api_key=api_key
)


if __name__ == '__main__':
    openai_msg = BaseMessage(
            role_name="user",
            role_type=RoleType.USER,
            meta_dict=dict(),
            content="你好,你是谁",
    ).to_openai_message(OpenAIBackendRole.USER)
    messages = [
        openai_msg
    ]
    res = model.run(messages)
    print(res.choices[0].message.content)
