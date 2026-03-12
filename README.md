# pen (Python)

一个面向新人的最小 Python 项目骨架，包含：

- `src/` 源码布局
- `tests/` 单元测试
- `unittest` 测试运行方式（零第三方依赖）
- 新人上手建议

## 目录结构

```text
.
├── README.md
├── pyproject.toml
├── src
│   └── pen
│       ├── __init__.py
│       └── main.py
└── tests
    └── test_main.py
```

## 环境要求

- Python 3.10+

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
python -m unittest discover -s tests -v
python -m pen.main
```

## 新人学习路径（建议）

1. 先跑通测试：`python -m unittest discover -s tests -v`
2. 阅读 `src/pen/main.py`，理解函数与 CLI 入口
3. 在 `tests/test_main.py` 增加一个测试用例（比如边界值）
4. 提交一次小改动并发起 PR，熟悉协作流程

## 后续扩展建议

- 引入 `ruff` 做 lint/format
- 引入 `mypy` 做类型检查
- 引入 GitHub Actions 做 CI
- 当模块变多时，按领域拆分包（`pen/core`, `pen/services` 等）
