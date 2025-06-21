import binascii
import requests
from camel.agents import EmbodiedAgent
from camel.generators import SystemMessageGenerator
from camel.messages import BaseMessage
from camel.types import RoleType
from model.gpt_4o_model import model

# Create an embodied agent
role_name = "Artist"
meta_dict = dict(role=role_name, task="Drawing")
sys_msg = SystemMessageGenerator().from_dict(
    meta_dict=meta_dict,
    role_tuple=(f"{role_name}'s Embodiment", RoleType.EMBODIMENT),
)
embodied_agent = EmbodiedAgent(
    system_message=sys_msg,
    model=model,
    verbose=True
)
embodied_agent.output_language = '中文'

user_msg = BaseMessage.make_user_message(
    role_name=role_name,
    content="Draw all the Camelidae species.",
)

for i in range(3):
    try:
        response = embodied_agent.step(user_msg)
        print(response.msg)
        print(response.terminated)
        print(response.info)
    except (binascii.Error, requests.exceptions.ConnectionError) as ex:
        print(
            "Warning: caught an exception, ignoring it since "
            f"it is a known issue of Huggingface ({ex!s})"
        )