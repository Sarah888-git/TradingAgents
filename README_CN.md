# TradingAgents: 多智能体LLM金融交易框架

## 项目概述

TradingAgents是一个多智能体交易框架，模拟真实世界交易公司的运作动态。通过部署专业的大语言模型驱动的智能体：从基本面分析师、情绪专家、技术分析师，到交易员、风险管理团队，平台协同评估市场状况并为交易决策提供信息。此外，这些智能体还参与动态讨论，以确定最优策略。

**注意**：TradingAgents框架专为研究目的而设计。交易表现可能因多种因素而异，包括所选择的主干语言模型、模型温度、交易周期、数据质量和其他非确定性因素。本框架不构成金融、投资或交易建议。

## 框架结构

我们的框架将复杂的交易任务分解为专业化的角色，确保系统实现了稳健、可扩展的市场分析和决策制定方法：

### 分析师团队

- **基本面分析师**：评估公司财务和绩效指标，识别内在价值和潜在风险信号
- **情绪分析师**：使用情绪评分算法分析社交媒体和公众情绪，以衡量短期市场情绪
- **新闻分析师**：监控全球新闻和宏观经济指标，解读事件对市场状况的影响
- **技术分析师**：利用技术指标（如MACD和RSI）检测交易模式并预测价格走势

### 研究团队

包含看多和看空研究员，他们批判性地评估分析师团队提供的洞察。通过结构化辩论，平衡潜在收益与固有风险。

### 交易员智能体

整合分析师和研究员的报告，做出明智的交易决策。基于全面的市场洞察确定交易时机和规模。

### 风险管理和投资组合经理

通过评估市场波动性、流动性和其他风险因素持续评估投资组合风险。风险管理团队评估并调整交易策略，向投资组合经理提供评估报告以做最终决策。投资组合经理批准/拒绝交易提案。如获批准，订单将发送到模拟交易所并执行。

## 安装指南

### 前提条件

- Python 3.10或更高版本
- 必要的API密钥：
  - FinnHub API（用于金融数据）
  - OpenAI API（用于智能体）

### 安装步骤

1. 克隆仓库：
   ```bash
   git clone https://github.com/TauricResearch/TradingAgents.git
   cd TradingAgents
   ```

2. 创建虚拟环境：
   ```bash
   python3 -m venv tradingagents_env
   source tradingagents_env/bin/activate  # 在Windows上使用: tradingagents_env\Scripts\activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 设置API密钥：
   ```bash
   export FINNHUB_API_KEY=your_finnhub_api_key
   export OPENAI_API_KEY=your_openai_api_key
   ```
   或者创建一个.env文件并添加这些变量。

## 使用方法

### 命令行界面

你可以通过运行以下命令直接使用CLI：

```bash
python -m cli.main
```

你将看到一个界面，可以选择你想要的股票代码、日期、LLM模型、研究深度等。

### Python代码中使用

要在你的代码中使用TradingAgents，你可以导入tradingagents模块并初始化一个TradingAgentsGraph()对象。.propagate()函数将返回决策。

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# 前向传播
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

你也可以调整默认配置，设置你自己选择的LLM模型、辩论轮数等：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 创建自定义配置
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4.1-mini"  # 使用不同的模型
config["quick_think_llm"] = "gpt-4.1-mini"  # 使用不同的模型
config["max_debate_rounds"] = 1  # 增加辩论轮数
config["online_tools"] = True  # 使用在线工具

# 使用自定义配置初始化
ta = TradingAgentsGraph(debug=True, config=config)
```

## 示例

我们在项目中提供了一个简单的示例脚本`example.py`，你可以运行它来测试框架：

```bash
python example.py
```

## 注意事项

- 为了节省成本，建议使用较小的模型（如gpt-4.1-mini）进行测试，因为框架会进行大量API调用。
- 确保你的API密钥有足够的配额来运行框架。
- 该框架仅用于研究目的，不应用于实际交易决策。

## 贡献

欢迎贡献！请随时提交问题或拉取请求。