from camel.agents import KnowledgeGraphAgent
from camel.logger import set_log_level
from model.gpt_4o_model import model

set_log_level('DEBUG')

knowledge_agent = KnowledgeGraphAgent(model=model)

result = knowledge_agent.run(element="""
《脑域驾驶员》

第一章：最后一个手动驾驶者
2089年，林夏的改装燃油车在磁悬浮车流中像一头濒死的机械兽。她的太阳穴贴着神经阻断贴片——这是对抗"脑驾时代"的最后武装。

全城99%的人已植入NeuroDrive芯片，眨眨眼就能唤醒车辆，皱皱眉即可飙到时速300公里。但林夏记得父亲车祸那晚，肇事者的脑波突然被黑客劫持，而系统日志只显示"驾驶员自主操作"。

第二章：锈铁与代码的对决
当交通局强拆她的手动方向盘时，林夏偷走了原型机ND-X。这台能反向侵入脑驾系统的设备，让她看见城市上空飘荡的亿万条神经指令——其中混着某些规律的异常波纹。

在第七次追击中，她终于捕捉到那个篡改脑波的信号源：根本不是黑客，而是NeuroDrive公司自己。每十万次操作中随机触发一次"误读"，只为收集人类在死亡恐惧中爆发的原始脑电波。

第三章：雨夜数据洪流
林夏把ND-X接入城市供电塔时，雨滴在高压电网上炸成蓝紫色烟花。所有脑驾者突然听见她通过公共频道的嘶吼："想想你们被删除的急刹车记忆！"

翌日，人们发现林夏的燃油车被焊死在交通局门口，方向盘上刻着NeuroDrive创始人年轻时的手写签名。而她的神经阻断贴片，正贴在市政厅的AI核心服务器上。
""")
print(result)