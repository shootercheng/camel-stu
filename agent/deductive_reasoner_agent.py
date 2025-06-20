from camel.agents.deductive_reasoner_agent import DeductiveReasonerAgent
from camel.logger import set_log_level
from model.gpt_4o_model import model
import logging

set_log_level('DEBUG')

starting_state = "贫穷"
target_state = "富有"


deductive_reasoner_agent = DeductiveReasonerAgent(model=model)
deductive_reasoner_agent.output_language = '中文'

for i in range(3):
    try:
        conditions_and_quality = deductive_reasoner_agent.deduce_conditions_and_quality(
                starting_state=starting_state, target_state=target_state
        )
        print(conditions_and_quality)
        break
    except Exception as e:
        logging.exception('run error', )