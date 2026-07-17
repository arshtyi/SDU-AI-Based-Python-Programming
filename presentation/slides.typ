#import "slide.typ": jump, meanwhile, pause, setup, theme
#import "utils.typ": *

#show: setup.with(
    title: "基于人工智能的Python入门编程",
    subtitle: "扩散语言模型",
    author: "彭靖轩",
    term: "2026春",
    date: datetime.today(),
)

= 背景与动机

#align(center, {
    text(size: 28pt, weight: "bold", fill: primary)[从串行解码到迭代式并行生成]
    grid(
        columns: 2,
        column-gutter: .5em,
        card([自回归范式], [按照严格的从左到右顺序逐 token 解码，后续输出依赖已生成前缀。], accent: muted),
        card([扩散生成范式], [通过多轮去噪并行恢复多个位置，并在迭代过程中逐步完善全局结构。]),
    )
    pill([研究目标：评估扩散式生成在 Python 编程教学中的应用潜力])
})

== 自回归局限

#grid(
    columns: 2,
    column-gutter: .5em,
    card(
        [串行解码依赖],
        [
            - `for` #sym.arrow `for x` #sym.arrow `for x in` #sym.arrow ...
            - 每个 token 均依赖既有前缀，生成延迟随输出长度持续累积。
        ],
        accent: muted,
    ),
    card(
        [代码编辑具有非线性],
        [代码补全、跨位置错误修复及语法约束满足，均需要联合建模双向上下文。],
        accent: primary,
    ),
)

#note-box("研究动机")[
    目标是探索同时支持*并行生成、任意位置补全与全局一致性检查*的语言模型。扩散范式具备这些潜在优势，但其实际效率仍受到去噪步数、缓存复用与 token 依赖关系的共同影响。@wu2025fastdllm
]


== 扩散生成机制

#grid(
    columns: 5,
    column-gutter: .2em,
    align: horizon,
    flow-node([$t=T$：完全掩码], [`[MASK] [MASK] [MASK]`], accent: muted),
    sym.arrow,
    flow-node([$t=2$：结构恢复], [`for [MASK] in nums:`], accent: amber),
    sym.arrow,
    flow-node([$t=0$：序列完成], [`for x in nums:`], accent: green),
)

#grid(
    columns: 3,
    column-gutter: .5em,
    card([前向扰动], [训练阶段按噪声调度将部分 token 替换为 `[MASK]`。], accent: muted),
    card([反向去噪], [双向 Transformer 基于完整上下文恢复被掩码 token。]),
    card([置信度调度], [优先固定高置信度位置，并继续优化不确定位置。], accent: green),
)

#align(center, text(
    size: 14pt,
    fill: muted.darken(30%),
)[自然语言属于离散数据，因而通常采用离散掩码扩散，而非直接施加连续高斯噪声。@lou2023sedd @sahoo2024masked])

== 技术演进

#table(
    columns: (1fr, auto, 2fr),
    inset: (x: .4em, y: .4em),
    stroke: .5pt + colors.neutral-soft,
    fill: (_, row) => if row == 0 { colors.primary-soft } else if calc.even(row) { pale } else { white },
    table.header(
        text(fill: white, weight: "bold")[时间],
        text(fill: white, weight: "bold")[代表工作],
        text(fill: white, weight: "bold")[关键进展],
    ),
    [2022], [Diffusion-LM、DiffuSeq@li2022diffusionlm @gong2022diffuseq], [验证可控文本生成与条件序列生成的可行性],
    [2023–24], [SEDD、MDLM@lou2023sedd @sahoo2024masked], [改进离散训练目标并缩小与自回归模型的建模差距],
    [2025], [LLaDA、Dream 7B@nie2025llada @ye2025dream], [扩展至 7B/8B 规模及通用、数学与代码任务],
    [2025–26],
    [Fast-dLLM、DiffusionGemma@wu2025fastdllm @google2026diffusiongemma],
    [推进缓存复用、并行解码与低延迟部署],
)

#note-box(
    "技术判断",
)[研究重点已由生成可行性验证转向规模化训练、推理效率与工程部署。DiffusionGemma 官方报告单张 H100 可达到 1,000 token/s 以上、最高约 4x 加速；该结果依赖具体硬件、任务和输出长度。@google2026diffusiongemma]

= 项目方案

#align(center, {
    text(size: 30pt, weight: "bold", fill: primary)[DiffuTutor]
    parbreak()
    text(size: 21pt)[扩散语言模型驱动的实时 Python 学习助手]
})

#grid(
    columns: 3,
    column-gutter: .5em,
    card([多位置补全], [对函数内部的多个不完整位置进行联合补全。]),
    card([约束式修复], [结合抽象语法树与测试反馈修复关联错误。], accent: green),
    card([分层式反馈], [依据课程知识库提供提示、解释与参考方案。], accent: amber),
)

== 场景与流程

#grid(
    align: horizon,
    columns: 7,
    column-gutter: .2em,
    flow-node([1.任务输入], [题目、代码、异常信息], accent: muted),
    sym.arrow,
    flow-node([2.候选生成], [并行预测多个位置]),
    sym.arrow,
    flow-node([3.程序验证], [AST、单元测试], accent: green),
    sym.arrow,
    flow-node([4.分层反馈], [提示 #sym.arrow 解释 #sym.arrow 方案], accent: amber),
)

#grid(
    columns: 2,
    column-gutter: .5em,
    card([学生端], [在循环、函数与列表等基础任务中获得低延迟、可局部采纳的建议。]),
    card([教师端], [聚合常见错误模式与提示使用情况，默认不长期保留学生原始代码。], accent: green),
)

#note-box("目标应用")[
    1. 编程实验课、在线判题平台与 IDE 教学插件；
    2. 第一阶段聚焦 Python 入门任务，以控制项目范围并建立可靠基线。
]

== 系统架构

#grid(
    align: horizon,
    columns: 7,
    column-gutter: .2em,
    flow-node([输入层], [题目 + 学生代码 + 异常信息], accent: muted),
    sym.arrow,
    flow-node([上下文层], [课程 RAG + 隐私脱敏], accent: amber),
    sym.arrow,
    flow-node([生成层], [掩码扩散 Transformer + 解码调度]),
    sym.arrow,
    flow-node([验证层], [AST + 沙箱测试 + 安全规则], accent: green),
)

#grid(
    columns: 2,
    column-gutter: .5em,
    card([约束反馈回路], [语法或测试未通过 #sym.arrow 局部重掩码相关 token #sym.arrow 再次去噪。]),
    card([交互输出], [返回 2 - 3 个局部候选、修改依据与置信度，由学生选择采纳。], accent: green),
)

#align(center, text(size: 14pt, fill: muted.darken(30%))[生成模型提出候选，程序分析与测试提供确定性的验证约束。])

== 解码算法

#grid(
    columns: 2,
    column-gutter: .5em,
    card([置信度感知解掩码], [
        1. 将待补全区域初始化为 `[MASK]` 序列；
        2. 并行预测全部掩码位置的 token 分布；
        3. 固定置信度最高的一组 token；
        4. 对低置信度及验证失败相关位置继续去噪；
        5. 达到终止条件后执行 AST 与测试验证。
    ]),
    [
        #card(
            [速度—质量权衡],
            [
                / 低延迟模式: 较少去噪步数与较高并行度
                / 高可靠模式: 多轮细化与更多验证反馈
                根据任务复杂度动态配置解码预算。
            ],
            accent: green,
        )
        #v(.4em)
        #text(
            size: 13pt,
            fill: muted,
        )[Fast-dLLM 表明，近似 KV Cache 与置信度感知并行解码可以提升吞吐；但过高并行度可能破坏 token 间的条件依赖。@wu2025fastdllm]
    ],
)

== 设计与安全

#grid(
    columns: 2,
    column-gutter: .5em,
    row-gutter: .5em,
    card([1 #sym.bar 学习效果优先], [采用渐进式支持策略：先提供提示，再给出解释与参考方案。]),
    card([2 #sym.bar 人机协同控制], [允许锁定正确代码、限定修改区域，并支持逐项撤销。], accent: green),

    card([3 #sym.bar 结果可验证], [所有候选均经过 AST 检查，并区分测试结果与模型置信度。], accent: amber),
    card([4 #sym.bar 隐私与公平性], [遵循数据最小化原则，并评估不同基础学习者的受益差异。], accent: muted),
)

#note-box("安全边界")[
    1. 沙箱环境限制网络、文件系统访问及高风险系统调用；
    2. 测试通过仅表示满足已覆盖用例，不构成程序完全正确的证明。
]


== MVP 与评估

#grid(
    columns: 3,
    column-gutter: .5em,
    card([第 1 - 4 周], [构建 100 道入门题数据集；接入开源模型；完成 AST 与测试管线。], accent: muted),
    card([第 5 - 8 周], [实现局部解掩码、约束反馈回路与 VS Code/网页原型。]),
    card([第 9 - 12 周], [开展自回归基线对照实验，并完成小规模课堂试用。], accent: green),
)

#table(
    columns: (1fr, 1fr, auto),
    inset: (x: .4em, y: .4em),
    stroke: .5pt + colors.neutral-soft,
    fill: (_, row) => if row == 0 { colors.primary-soft } else { pale },
    table.header(
        text(fill: white, weight: "bold")[维度],
        text(fill: white, weight: "bold")[指标],
        text(fill: white, weight: "bold")[MVP],
    ),
    [学习效果], [首次独立通过率], [相对"只给报错信息"提升 #math.gt.eq 15pp],
    [系统质量], [语法有效率], [建议代码 #math.gt.eq 95% 可解析],
    [交互体验], [P95 延迟], [50 token 内局部建议 #math.lt.eq 2s],
    [经济性], [单个有效建议成本], [比同规模 AR 基线降低 #math.gt.eq 30%],
)

= 价值与落地

#align(center)[
    #text(size: 27pt, weight: "bold", fill: primary)[项目定位：面向垂直场景的技术验证]
    #v(.5em)
    #text(size: 20pt)[聚焦低延迟、可控制、可验证的编程教育辅助系统]
]

#grid(
    columns: 3,
    column-gutter: .5em,
    card([技术假设], [扩散式局部生成能够降低重复计算，并改善多位置代码修复。]),
    card([产品假设], [低延迟、分层式反馈能够提高学习者的持续参与度。], accent: green),
    card([商业假设], [院校对可审计、可私有部署的教学辅助系统存在付费需求。], accent: amber),
)

== 经济与社会价值

#grid(
    columns: 2,
    column-gutter: .5em,
    card([经济价值], [
        - *教学机构*：降低重复答疑成本与高峰期服务压力；
        - *商业模式*：校园授权、私有化部署与判题平台 API；
        - *推理成本*：局部生成并动态配置解码预算。
    ]),
    card(
        [社会影响],
        [
            - 提升大班教学与资源不足地区的反馈可及性；
            - 强化错误原因解释，支持形成性学习过程；
            - 持续评估自动化依赖、提示偏差与隐私风险。
        ],
        accent: green,
    ),
)

#bibliography("ref.yml", title: "参考文献")
