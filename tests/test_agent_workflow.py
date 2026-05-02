"""基本的单元测试骨架，验证各 agent 接口存在并返回预期类型的值（伪测试）。"""
import pytest


def test_db_schema_generation():
    from agents.db_schema_agent import generate_create_table_ddl, infer_schema_from_samples

    samples = [{"id": 1, "name": "alice", "score": 4.2}]
    inferred = infer_schema_from_samples(samples)
    assert isinstance(inferred, list)
    ddl = generate_create_table_ddl("test_table", inferred)
    assert isinstance(ddl, str)
    assert ddl.strip().upper().startswith("CREATE TABLE")


def test_crawler_agent_schedule_and_router():
    from agents.crawler_agent import CrawlerAgent
    from core.llm_router import LLMRouter

    ca = CrawlerAgent(proxy_pool=["p1", "p2"])
    schedule = ca.schedule_with_proxy_pool(["/a", "/b", "/c"])
    assert isinstance(schedule, list)

    router = LLMRouter()
    prompt = router.build_prompt("crawl", {"url": "https://example.com"})
    assert isinstance(prompt, str)


def test_drl_reward():
    from agents.drl_optimizer_agent import compute_reward, shape_reward

    metrics = {"throughput": 100.0, "latency": 10.0, "packet_loss": 0.01}
    r = compute_reward(metrics)
    assert isinstance(r, float)
    sr = shape_reward(r)
    assert isinstance(sr, float)


if __name__ == "__main__":
    pytest.main(["-q"])
