LLMs_Zero_to_Hero/
├── configs/                  # 配置文件
│   ├── model/                # 模型架构配置
│   │   ├── base.yaml         # 基础模型参数
│   │   └── 7b.yaml           # 7B版本特定配置
│   └── train/                # 训练配置
│       ├── cpu.yaml          # CPU训练配置
│       └── multi_gpu.yaml    # 多GPU配置
│
├── data/                     # 数据管理
│   ├── raw/                  # 原始数据
│   ├── processed/            # 预处理后数据
│   ├── dataloader.py         # 数据加载实现
│   └── tokenizer/            # 分词器
│       ├── vocab.json        # 词表文件
│       └── merges.txt        # BPE合并规则
│
├── docs/                     # 文档
│   ├── ARCHITECTURE.md       # 架构设计文档
│   └── PRETRAIN.md          # 预训练流程说明
│
├── scripts/                  # 实用脚本
│   ├── deploy/               # 部署脚本
│   ├── monitor/              # 训练监控
│   └── data_preprocess.sh    # 数据预处理
│
├── src/                      # 核心代码
│   ├── modeling/             # 模型实现
│   │   ├── attention.py      # 注意力机制
│   │   ├── blocks.py         # Transformer块
│   │   └── __init__.py       # 模型架构入口
│   │
│   ├── training/             # 训练相关
│   │   ├── trainer.py        # 训练主循环
│   │   ├── optim/            # 优化器实现
│   │   └── scheduler.py      # 学习率调度
│   │
│   ├── utils/                # 工具函数
│   │   ├── logging.py        # 日志系统
│   │   └── metrics.py        # 评估指标
│   │
│   └── inference/            # 推理服务
│       ├── api.py            # REST接口
│       └── quantize.py       # 量化工具
│
├── tests/                    # 测试
│   ├── unit/                 # 单元测试
│   └── integration/          # 集成测试
│
├── requirements.txt          # Python依赖
├── LICENSE                   # 开源协议
└── README.md                 # 项目说明