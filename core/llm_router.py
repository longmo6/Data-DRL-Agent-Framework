"""
core.llm_router
简单的 LLM 提示路由器骨架，用于将任务路由到不同 agent 的核心提示构建。
"""
from typing import Dict, Any


class LLMRouter:
    def __init__(self):
        # 可扩展：注入不同 LLM 客户端、缓存、策略等
        pass

    def build_prompt(self, task_type: str, payload: Dict[str, Any]) -> str:
        """根据任务类型构造不同的 prompt 模板（伪实现）。"""
        if task_type == "crawl":
            return f"Analyze DOM and suggest extraction rules for: {payload.get('url')}"
        if task_type == "ddl":
            return f"Design SQL DDL for sample records: {payload.get('sample_keys')}"
        if task_type == "drl":
            return f"Propose reward shaping for metrics: {payload.get('metrics')}"
        return "General routing prompt"

    def route_to_agent(self, agent_name: str, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """伪代码：将构造好的提示发送到目标 agent（或 LLM 客户端）。"""
        prompt = self.build_prompt(task_payload.get("task_type", ""), task_payload)
        # pseudo: response = llm_client.call(prompt)
        return {"agent": agent_name, "prompt": prompt, "status": "queued"}


__all__ = ["LLMRouter"]
