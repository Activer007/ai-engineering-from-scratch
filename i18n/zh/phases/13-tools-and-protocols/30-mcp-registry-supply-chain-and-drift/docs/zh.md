# MCP Registry 供应链：准入、漂移与回滚

> 注册表（registry）条目告诉你发布者声明了什么。生产环境的准入流程则要证明你获取了什么、观察到了什么、批准了什么，以及能够安全恢复到什么状态。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 13 · 17（网关与注册表）、阶段 13 · 18（生产环境身份验证）
**Time:** ~90 分钟

## 学习目标

- 区分 Registry 发布、包来源信息（provenance）、运行时发现和本地审批。
- 验证 MCP 服务器的命名空间，不信任其自身记录中的名称。
- 固定不可变的发布记录、执行源、来源信息和实时描述符证据。
- 在准入后检测注册表状态变化和运行时漂移。
- 将路由回滚到此前获准的版本，同时不改写历史。
- 维护可检测篡改的准入台账，解释每一项决策。

## 要解决的问题

你在注册表中发现 `com.example/inventory`。描述看起来符合需求，软件包确实存在，服务器也会响应 `server/discover`。

这不是一个事实，而是来自不同权威来源的一串事实：

1. 通过某个命名空间身份验证的发布者提交了一条记录。
2. 包注册表提供了具有特定身份和摘要的产物。
3. 正在运行的端点（endpoint）报告了协议版本、能力、工具以及服务器诊断信息。
4. 你的组织决定允许使用这一确切组合。

如果把这些事实简化为“它在注册表里，所以可以信任”，供应链就会出现盲区。有效的发布记录仍可能被弃用。如果没有固定摘要，包标签可能指向非预期产物。服务器可能在评审后新增具有破坏性的工具。回滚还可能悄悄选中一个从未获准的版本。

解决办法是使用准入控制器（admission controller），在每个边界保留证据。

## Registry 是索引，不是你的审批系统

官方 MCP Registry（MCP 注册表）存储服务器元数据。MCP 是 Model Context Protocol（模型上下文协议）。Registry 的 `server.json` 记录指定服务器版本，并声明一个或多个包或远程端点。发布规则还包括命名空间身份验证、包所有权检查、受限制注册表的规则，以及严格限定的发布者元数据存放位置。

这些控制措施回答的是发布层面的问题。部署层面的问题仍要由你的生产策略回答：

| 边界 | 问题 | 证据责任方 |
|---|---|---|
| 命名空间 | 发布者是否有权使用该名称？ | Registry 身份验证，以及你提供的已验证命名空间输入 |
| 记录 | 发布者为此版本声明了什么？ | 不可变的 `server.json` 摘要 |
| 执行源 | 将执行哪个包，或调用哪个远程端点？ | 声明的源字段、已验证的所有权结果、传输方式和可信摘要 |
| 运行时 | 端点目前暴露了什么？ | `server/discover` 和工具描述符 |
| 准入 | 你的策略是否批准了这一确切组合？ | 本地锁定记录和台账条目 |
| 运维 | 它是否仍然安全，可以用什么替换？ | 漂移检查、状态同步、健康状况和回滚路由 |

Registry 的 schema（结构定义）版本与 MCP 协议版本彼此独立。一条记录可能使用已发布的 `2025-12-11` 服务器 schema，而实际运行的服务器支持 MCP `2026-07-28`。绝不能从其中一个推断另一个。

```figure
mcp-registry-admission
```

## 一次准入决策中的七项控制

### 1. 命名空间验证

官方 Registry 名称使用经过身份验证的命名空间。已验证域名可以映射为反向域名前缀。例如，对 `example.com` 的控制权可以确立 `com.example/*` 命名空间。

不要只做字符串前缀检查：

```python
server_name.startswith("com.example")
```

这种检查也会接受 `com.exampleevil/tool`。应在 `/` 处分割名称，要求名称中斜杠后的部分（slug）非空，并对命名空间部分进行精确比较。更重要的是，应将身份验证结果中的已验证命名空间作为准入输入，不要根据非可信记录建立信任。

基于 GitHub 的命名空间与基于域名的命名空间使用不同的身份验证路径。无论哪条路径，都应统一为同一种准入输入：确切的已验证命名空间字符串。

### 2. 关联来源证据

对于包记录，声明与获取到的产物必须通过明确字段关联：

- 包注册表类型
- 包标识符
- 包版本
- 已验证的所有权结果
- 下载产物的摘要

还要验证声明的包传输方式。只包含远程端点的记录也是有效的，不能因缺少包而拒绝它。对于远程源，应将声明的 URL 和传输类型，与独立验证的端点所有权、可信连接或部署证据的摘要关联起来。

本课代码支持这两种源，并将选定的源与 Registry 来源、服务器名称、Registry 版本、记录摘要和证据摘要一起计算哈希。得到的来源信息摘要是指向完整证据集的紧凑标识，不能代替证据本身的留存。

绝不能接受仅由待验证产物自身提供的摘要。应在可信的获取边界计算摘要，或从包服务获取摘要，并验证该服务提供的验证结果。

### 3. 锁定决策，而不只是版本

Registry 版本是唯一的发布标识符。已发布的元数据不可变；记录发生变化就必须使用新版本。虽然推荐语义化版本，但 Registry 并不强制使用，也不接受版本范围。

因此，`^1.4` 不是准入锁定记录，“latest”也不是。一份有用的锁定记录应包含：

```json
{
  "server": "com.example/inventory",
  "version": "1.0.0",
  "recordDigest": "...",
  "source": {"kind": "package", "registryType": "pypi"},
  "sourceDigest": "...",
  "toolsetDigest": "...",
  "provenanceDigest": "...",
  "registryStatus": "active"
}
```

同时锁定多个层面，可以识别发生变化的边界。同一 Registry 版本下的记录摘要发生变化，说明 Registry 的完整性出了问题；同一包坐标或远程部署下的源摘要发生变化，说明执行源的完整性出了问题；工具集摘要发生变化，则是运行时漂移。

### 4. 实时漂移检测

准入流程应观察真正接收流量的服务器。调用 `server/discover`，并通过可信路径列出或以其他方式获取暴露的工具描述符，验证以下事项：

- `supportedVersions` 中包含 `2026-07-28`
- 本地要求的所有能力均已具备
- 每个工具描述符均具有必需的身份信息和 schema 字段
- 在后续检查中，规范化后的描述符摘要与获准的锁定记录相符

可选结果 `_meta["io.modelcontextprotocol/serverInfo"]` 的值，是服务器自行报告的显示、日志和调试上下文。应将其记录为诊断证据，但绝不能据此确定命名空间、包所有权、端点所有权、准入资格或作出任何其他安全决策。位于 `_meta` 之外的直接 `serverInfo` 别名并不是契约规定的字段，不应被提升为诊断证据。

只规范化顺序不影响含义的字段。示例在计算哈希前，按稳定名称对工具列表排序，因此无害的列表顺序变化不会造成漂移。它不会丢弃描述符字段。新增工具、schema 变更、描述变更或新增注解，都会改变锁定记录。

示例将格式不合法的描述符以及任何描述符摘要变化都视为漂移：隔离锁定记录，移除其活动路由，并禁止将该版本作为回滚目标。生产策略若要允许文字编辑类变更，也只能在重新评审后放行，因为描述会影响模型的工具选择。看似“表面”的元数据也会改变智能体（agent）行为。

### 5. Registry 状态是实时状态

Registry API（应用程序编程接口）会在每条服务器记录旁附加一个响应级 `_meta` 对象。由 Registry 管理的字段位于 `_meta["io.modelcontextprotocol.registry/official"]` 下。应将响应的 `_meta` 对象传入准入流程，并读取 `_meta["io.modelcontextprotocol.registry/official"].status`。直接使用 `_meta.status` 并不是官方协议消息格式。不要将响应元数据与发布记录自身的 `_meta` 混淆。状态可能是：

- `active`：默认返回，并具备接受本地准入审批的资格
- `deprecated`：仍可被发现，但带有警告，不再适合作为安全的自动选择
- `deleted`：默认隐藏，但历史记录仍可通过已删除记录视图或增量视图获取

准入后仍要同步状态。如果一个活动版本变为已弃用或已删除，应隔离其锁定记录，并停止向它路由新任务。证据必须保留。从默认列表中删除，并不意味着可以抹掉你的审计轨迹。

发布者提供的自定义元数据只能放在发布记录的 `_meta.io.modelcontextprotocol.registry/publisher-provided` 下。Registry 管理的响应元数据与其分开。不能让发布者自行设置官方状态。

### 6. 回滚意味着恢复路由

回滚时不编辑不可变的发布记录，而是选择一个先前已获准、当前仍符合条件的锁定记录，并更改活动路由。

安全的回滚目标必须满足：

1. 具有完整的准入记录。
2. 按照你的策略，其 Registry 状态仍为活动状态。
3. 未因运行时证据或安全证据而被隔离。
4. 仍能解析到锁定的包和实时描述符集合。
5. 通过当前健康检查。

示例重点实现前三项条件。真实的协调器在激活前还应重新获取包，并再次检查实时端点。

### 7. 追加准入台账

准入数据库记录哪些内容处于活动状态，台账解释为什么。

示例中的每个条目包含序号、时间、事件、服务器、版本、结果、原因、证据、前一条目的哈希和自身哈希。修改较早条目的结果，会使该条目及其后的整条链验证失败。

这能让篡改被检测出来，并不意味着篡改绝无可能。应定期将台账链头锚定到独立的信任域，例如签名发布元数据或一次写入存储。限制谁能追加记录。证据中不得包含授权令牌、包凭据、工具参数或私有端点数据。

## 动手实现

可运行的控制器位于 `code/main.py`，仅使用 Python 标准库。

先运行会自行结束的演示：

```bash
cd phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift
python3 code/main.py
```

演示执行五项操作：

1. 在命名空间、包来源信息、协议、能力和工具均匹配时，准入 `1.0.0`。
2. 准入 `1.1.0` 并将其设为活动版本。
3. 观察运行时出现的非预期删除工具。
4. 观察 Registry 中 `1.1.0` 的状态变为 `deprecated`。
5. 将路由恢复到仍然获准的 `1.0.0` 锁定记录。

预期输出结构：

```json
{
  "admitted": [true, true],
  "driftAllowed": false,
  "rollbackAllowed": true,
  "activeVersion": "1.0.0",
  "ledgerValid": true
}
```

按以下顺序阅读实现：

1. `namespace_for_domain()` 和 `namespace_matches()` 确立对名称的确切使用权限。
2. `digest()` 和 `normalized_tools()` 生成确定性证据。
3. `RegistryAdmissionController.admit()` 关联发布记录、来源信息、运行时和策略。
4. `check_live()` 将新观察结果与锁定记录比较。
5. `observe_registry_status()` 隔离 Registry 状态发生变化的版本。
6. `rollback()` 只激活此前获准且符合条件的目标。
7. `AdmissionLedger.verify()` 检测已记录历史是否被改动。

## 实际使用

将控制器放在发现与路由之间：

```text
Registry sync -> artifact verifier -> live discovery -> admission controller -> route table
                                               |                 |
                                               v                 v
                                          evidence store    admission ledger
```

为这些工作使用不同的身份。Registry 同步任务需要元数据读取权限；产物验证器需要包获取权限；路由协调器需要激活获准锁定记录的权限。它们中的任何一个都不需要掌握所有凭据。

明确区分上线过程中的状态。“已批准”表示证据通过策略检查；“活动”表示当前路由选中了它；“已隔离”表示它不能接收新任务；“已替代”表示另一个获准版本处于活动状态。不要把这四层含义压缩进一个布尔值。

在通过 `tools/list` 暴露服务器之前执行准入检查。否则，客户端可能在发布与策略评估之间的空档发现工具。

## 交互实验

你将逐一观察每个边界失效的情况。

### 实验 A：命名空间碰撞

从代码目录启动 Python 交互环境：

```bash
cd phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift/code
python3 -q
```

然后运行：

```python
from main import namespace_matches
namespace_matches("com.example/inventory", "com.example")
namespace_matches("com.exampleevil/inventory", "com.example")
```

第一个结果为 `True`，第二个为 `False`。在本地把精确比较替换为 `startswith`，观察第二个名称为何越过了边界。继续之前，务必恢复精确比较。

### 实验 B：描述符漂移

```python
from main import *
times = iter(f"2026-08-21T12:00:{n:02d}+00:00" for n in range(10))
c = RegistryAdmissionController(clock=lambda: next(times))
meta = {OFFICIAL_META_KEY: {"status": "active"}}
c.admit(sample_record("1.0.0"), meta, "com.example", evidence_for("1.0.0"), sample_live("1.0.0"))
c.check_live("com.example/inventory", "1.0.0", sample_live("1.0.0", True))
```

检查原因和路由状态。包和 Registry 记录没有变化，但运行时暴露的工具接口发生了变化，因此控制器隔离并停用了锁定记录。这就是安装完成后仍须持续进行供应链控制的原因。

### 实验 C：状态与回滚

准入 `1.1.0`，将其标为已弃用，然后尝试两个回滚目标：

```python
c.admit(sample_record("1.1.0"), meta, "com.example", evidence_for("1.1.0"), sample_live("1.1.0"))
c.observe_registry_status("com.example/inventory", "1.1.0", "deprecated")
c.rollback("com.example/inventory", "1.1.0", "unsafe retry")
c.rollback("com.example/inventory", "1.0.0", "restore known release")
c.ledger.verify()
```

已隔离的目标会被拒绝，先前的活动锁定记录会被接受，台账仍然有效。

## 实践实验

为控制器扩展一个双人审批门禁。

要求：

- 将审批保存为指向已签名证据的引用，而不是锁定记录中可修改的姓名。
- 如果工具集包含带有 `destructiveHint: true` 的工具，要求两个不同的评审者身份批准。
- 拒绝重复的评审者身份。
- 审批尚未完成时，在台账中保留原始准入尝试。
- 为零次审批、一次审批、重复审批和两个不同身份的审批添加测试。
- 不要记录签名、凭据或完整的私有工具参数。

只有两个身份都批准了完全相同的记录摘要、包摘要和工具集摘要后，破坏性工具才能成为活动工具；做到这一点才算成功。

## 已交付产物

本课交付 `outputs/skill-mcp-registry-admission.md`。评审新的 Registry 版本或调查漂移时，可将它作为扁平、可复用的操作手册。它规定了输入、拒绝规则、证据包、状态协调和回滚证明，不依赖示例中的类名。

## 验证

运行演示和确定性测试套件：

```bash
cd phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift
python3 code/main.py
python3 -m unittest discover -s code/tests -v
```

验证应证明以下事项：

- 精确的命名空间边界会拒绝相似前缀
- 只有官方命名空间下的 Registry 状态才能使版本获得资格
- 未验证或不匹配的包证据和远程端点证据会被拒绝
- 发布者元数据不能冒充 Registry 管理的元数据
- 对工具顺序进行规范化，同时不掩盖描述符变更
- 包或工具结构格式不合法时，会安全地拒绝
- `serverInfo` 仅用于诊断，绝不提供准入授权依据
- 描述符漂移会触发隔离、停用，并阻止回滚到该锁定记录
- 状态变更会隔离活动锁定记录
- 回滚不能选择已隔离或未知版本
- 台账篡改能够被检测到

## 生产环境故障模式

| 故障 | 原因 | 必须采取的措施 |
|---|---|---|
| 名称看似有效，但命名空间从未经过身份验证 | 策略信任了记录中的文字 | 在可信命名空间验证器提供确切前缀之前，拒绝准入 |
| 相同包坐标返回了不同字节 | 上游内容可变，或分发渠道遭入侵 | 停止激活，保留两个摘要，调查获取边界 |
| “Latest”未经评审就发生变化 | 浮动选择绕过了锁定记录 | 只解析确切的已获准版本及摘要 |
| 审批后出现新工具 | 运行时漂移，或实际是另一套部署 | 隔离路由，并采集新的描述符观察结果 |
| 已弃用版本仍处于活动状态 | 缺少状态同步，或同步有延迟 | 定期协调状态，并在激活前再次协调 |
| 已删除记录从默认同步中消失 | 客户端只请求活动记录 | 使用增量协调或能识别删除的协调机制，并保留本地历史 |
| 回滚目标从未获准 | 路由控制与审批状态脱节 | 拒绝回滚，对目标重新执行准入流程 |
| 攻击者改写全部条目后，台账仍能在本地通过验证 | 哈希链没有外部锚点 | 将已签名的台账链头发布到独立信任域 |
| 证据包含 bearer token（持有者令牌）或工具参数 | 日志复制了完整请求 | 在采集时脱敏，只保存所需的最少证据 |

## 运维准则

发布回答“这个身份能否用这个名称发布？”，准入回答“我们是否执行这个确切产物，并暴露这些确切行为？”。这两项决策必须分开，每个关联关系都要锁定；回滚应依据证据选择目标，而不是凭记忆。

## 延伸阅读

- [官方 Registry 的 server.json 要求](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)
- [官方 Registry 的 OpenAPI 契约](https://registry.modelcontextprotocol.io/openapi.yaml)
- [MCP 2026-07-28 服务器发现](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)
