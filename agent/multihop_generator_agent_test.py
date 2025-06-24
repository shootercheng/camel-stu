from camel.agents.multi_hop_generator_agent import MultiHopGeneratorAgent
from camel.logger import set_log_level
from model.gpt_4o_model import model

set_log_level('debug')

multihop_generator_agent = MultiHopGeneratorAgent(model=model, output_language='中文')

res = multihop_generator_agent.generate_multi_hop_qa(context= """
如何排查JavaWeb生产问题, SSE 占用太多的内存
""")
print(res)
