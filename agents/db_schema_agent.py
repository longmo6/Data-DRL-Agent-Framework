"""
agents.db_schema_agent
包含生成 SQL DDL 的函数定义（示例/伪实现）
"""
from typing import List, Tuple, Dict


def generate_create_table_ddl(table_name: str, columns: List[Tuple[str, str]]) -> str:
    """生成简单的 CREATE TABLE DDL。

    columns: List of (column_name, sql_type)
    """
    cols_sql = []
    for name, typ in columns:
        cols_sql.append(f"    {name} {typ}")
    cols_block = ",\n".join(cols_sql)
    ddl = f"CREATE TABLE {table_name} (\n{cols_block}\n);"
    return ddl


def infer_schema_from_samples(samples: List[Dict]) -> List[Tuple[str, str]]:
    """伪代码：从样本记录推断列名与类型（非常粗略）"""
    if not samples:
        return []
    sample = samples[0]
    inferred = []
    for k, v in sample.items():
        if isinstance(v, int):
            inferred.append((k, "BIGINT"))
        elif isinstance(v, float):
            inferred.append((k, "DOUBLE PRECISION"))
        else:
            inferred.append((k, "TEXT"))
    return inferred


__all__ = ["generate_create_table_ddl", "infer_schema_from_samples"]
