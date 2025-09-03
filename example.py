from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# API密钥已经在.env文件中设置好了
# FINNHUB_API_KEY=d1s9qnpr01qskg7sdb30d1s9qnpr01qskg7sdb3g
# OPENAI_API_KEY=sk-proj-***（已设置）

# 创建自定义配置
config = DEFAULT_CONFIG.copy()

# 可以根据需要修改配置
# 使用较小的模型以节省成本
# 注意：根据用户要求使用gpt-4o-mini模型，并最小化API调用
config["deep_think_llm"] = "gpt-4o-mini"  # 使用gpt-4o-mini模型
config["quick_think_llm"] = "gpt-4o-mini"  # 使用gpt-4o-mini模型
config["max_debate_rounds"] = 0  # 禁用辩论轮数
config["max_risk_discuss_rounds"] = 0  # 禁用风险讨论轮数
config["online_tools"] = False  # 禁用在线工具以减少API调用

# 初始化TradingAgents图
ta = TradingAgentsGraph(debug=True, config=config)

# 选择股票代码和日期
ticker = "8031"  # 苹果公司
date = "2025-09-03"  # 分析日期

# 运行分析并获取决策
print(f"正在分析 {ticker} 在 {date} 的交易决策...")
try:
    _, decision = ta.propagate(ticker, date)
    
    # 打印决策结果
    print("\n交易决策:")
    print(decision)
except Exception as e:
    print(f"\n运行过程中出现错误: {e}")
    print("\n可能的解决方案:")
    print("1. 检查API密钥是否有效")
    print("2. 确认API账户有足够的配额")
    print("3. 尝试使用更便宜的模型（如gpt-3.5-turbo）")
    print("4. 减少辩论轮数或禁用在线工具以减少API调用")