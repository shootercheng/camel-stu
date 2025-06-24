from camel.agents import TaskPlannerAgent
from camel.agents import TaskSpecifyAgent
from camel.agents import TaskCreationAgent
from camel.agents import TaskPrioritizationAgent
from camel.logger import set_log_level
from model.gpt_4o_model import model

set_log_level('debug')

# Divide this task into subtasks: \n如何排查JavaWeb生产问题, SSE 占用太多的内存\n. Be concise.
def run_task_planner():
    task_planner_agent = TaskPlannerAgent(model=model, output_language='中文')
    res = task_planner_agent.run(task_prompt="""
    如何排查JavaWeb生产问题, SSE 占用太多的内存
    """)
    print(res)

    """
    ## 排查JavaWeb生产问题 SSE占用内存的子任务
    
    1. **确认问题范围**
       - 确定SSE占用内存的具体表现（例如内存使用量、应用响应时间等）。
       - 收集影响的用户数量和频率。
    
    2. **检查代码实现**
       - 审查SSE相关的代码，检查内存管理和资源释放。
       - 确认是否有内存泄漏（如未关闭的连接）。
    
    3. **分析服务器配置**
       - 检查服务器的JVM参数设置（如堆内存大小）。
       - 确认是否有合理的连接数限制。
    
    4. **监控和分析资源使用**
       - 使用Java监控工具（如JVisualVM、Java Mission Control等）观察内存使用情况。
       - 收集和分析GC日志，观察垃圾回收频率和内存回收效果。
    
    5. **扩展测试**
       - 进行压力测试和负载测试，模拟高并发场景，观察内存变化。
       - 针对特定场景（如长连接、长时间保持的SSE连接）进行测试。
    
    6. **优化建议**
       - 根据分析结果，提出优化建议（如调整连接策略、优化数据推送逻辑等）。
       - 考虑限流或降级策略，以减轻内存占用。
    
    7. **实施和验证**
       - 实施优化措施后，再次监控内存使用情况。
       - 验证优化效果，确保问题有效解决。
    """

def task_specify_agent():
    task_specify_agent = TaskSpecifyAgent(model=model, output_language='中文')
    res = task_specify_agent.run(task_prompt="如何学习Python")
    print(res)

def task_creation_agent():
    task_creation_agent = TaskCreationAgent(model=model, role_name='学生',
                                            objective='好好学习', output_language='中文')
    res = task_creation_agent.run(['学习Python','学习大模型'])
    print(res)


if __name__ == '__main__':
    # run_task_planner()
    # task_specify_agent()
    task_creation_agent()