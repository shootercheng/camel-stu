from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.messages import OpenAIMessage
from camel.logger import get_logger, set_log_file, set_log_level
from dotenv import load_dotenv
import os

# Set log output to a file using an absolute path
log_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'camel.log',
)
print(log_path)
set_log_file(log_path)

# Set the logging level
set_log_level('DEBUG')

load_dotenv(override=True)

base_url = os.getenv("base_url")
api_key = os.getenv("api_key")


model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="DeepSeek-R1",
    url=base_url,
    api_key=api_key
)

# 创建聊天代理
agent = ChatAgent(model=model, output_language='中文')

# 执行对话
response = agent.step("你好,你是谁?")

print(response.msgs[0].content)
