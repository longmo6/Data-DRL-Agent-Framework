"""
agents.drl_optimizer_agent
放置强化学习优化相关的 Reward 计算伪代码与接口
"""
from typing import Dict


def compute_reward(metrics: Dict[str, float], weights: Dict[str, float] = None) -> float:
    """伪代码：基于若干指标计算复合 reward。

    metrics 示例: {"throughput": x, "latency": y, "packet_loss": z}
    weights 示例: 权重映射
    """
    weights = weights or {"throughput": 1.0, "latency": -0.5, "packet_loss": -2.0}
    reward = 0.0
    reward += weights.get("throughput", 0.0) * metrics.get("throughput", 0.0)
    reward += weights.get("latency", 0.0) * metrics.get("latency", 0.0)
    reward += weights.get("packet_loss", 0.0) * metrics.get("packet_loss", 0.0)
    # 加上稳定性奖金
    stability = metrics.get("stability", 1.0)
    reward += 0.1 * stability
    return float(reward)


def shape_reward(raw_reward: float, clip_min: float = -100.0, clip_max: float = 100.0) -> float:
    """伪代码：对 reward 进行裁剪与缩放，适配 RL 算法"""
    r = max(min(raw_reward, clip_max), clip_min)
    # 简单归一化示例
    return r / (abs(clip_max) + 1.0)


__all__ = ["compute_reward", "shape_reward"]
