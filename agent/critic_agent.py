from camel.agents import CriticAgent
from camel.messages import BaseMessage
from camel.types import RoleType
from model.gpt_4o_model import model
from camel.logger import set_log_level

# Set the logging level
set_log_level('DEBUG')

criticAgent = CriticAgent(
    system_message= BaseMessage(
        "critic",
        RoleType.CRITIC,
        None,
        content=(
            "你是一位资深程序员，比较输入编程语言的优缺点，选择一个你最喜欢的编程语言，并且说明理由，请用中文回答"
        ),
    ),
    model=model,
    verbose=True
)

messages = [
    BaseMessage(
        role_name="user",
        role_type=RoleType.USER,
        meta_dict=dict(),
        content="Python",
    ),
    BaseMessage(
        role_name="user",
        role_type=RoleType.USER,
        meta_dict=dict(),
        content="Java",
    ),
]

flatten_options = criticAgent.flatten_options(messages)
print(flatten_options)
print(criticAgent.options_dict)

input_message = BaseMessage(
    role_name="user",
    role_type=RoleType.USER,
    meta_dict=dict(),
    content=flatten_options,
)
res = criticAgent.get_option(input_message)
print(res)