# S03：GPU与Docker交付记录

2026-10-02。00/03 GPU Setup & Cloud与00/07 Docker for AI已完成独立英文新译、全文技术/中文双审和实际GitHub GFM桌面验收，位于本fork [draft PR #9](https://github.com/Activer007/ai-engineering-from-scratch/pull/9)。累计 **24/523** 课已审新译草稿，余 **499** 课未启动；00阶段覆盖10/12课。README不计入课程数，草稿不代表用户批准、合并或发布。

| 课程 | 翻译提交 | 全部块 / 可译块 | 保护围栏 |
|---|---|---:|---:|
| 00/03 GPU配置与云端使用 | `bcce6ee0fe2133f25be1bd2a41b5ab5af50bc237` | 63 / 25 | 7 |
| 00/07 面向AI的Docker | `4ec534dc3a167281db5c10c6ffdb33c026da6bd3` | 149 / 55 | 20 |

## 翻译质量与复验

- 212个源块、80个可译块全覆盖，不抽样；独立技术对照及另一次完整中文通读完成
- 27个围栏载荷原样，31个标题、3张表、数字/单位、架构、flags、路径、公式及字段均保持；围栏内英文选项/价格/说明卡属于保护表面，没有声称已汉化
- Docker补齐CUDA/cuDNN/MPS首次中文解释；独立审校确认最终稿仅三处释义新增，原义与所有保护内容不变
- 2/2本阶段strict检查；隔离组合所有已有新译后 **24/24** strict、**33** 控制回归与两次全24课字节一致重放通过
- 实际GitHub GFM **2/2桌面通过**：中文锚点、表格、代码、字面价格/倍率/占位符、Mermaid、加粗边界、Apple Silicon限制和Compose字段经过检查
- 基线审计523课0问题；认证67课、12评估、505题0问题；README计数与空白检查通过

## 运行结果必须区分

| 检查 | 实际结果 |
|---|---|
| bash围栏语法 | 14段中13通过；1段因未替换的字面`<container_id>`失败，exit2，源代码未改 |
| Python围栏AST | 5段通过；不等于依赖导入或执行成功 |
| gpu_check.py | AST通过；确认torch不存在后，隔离运行只进入“PyTorch not installed”分支并exit0；GPU与benchmark未执行 |
| Compose YAML | 能解析出ai-dev与qdrant；未做完整Compose schema/启动验证 |
| Dockerfile/镜像 | 未build/pull/run；没有安装、网络下载或GPU访问 |

所有Shell检查使用移除BASH_ENV、禁用profile并启用`-n`的模式，不执行载荷。没有把一个未替换模板的失败改写成“全套通过”。

## 英文源风险

逐课review保留了源块位置及处理说明。GPU课的免费T4、云价格、8小时对10分钟、Tensor Core加速和fp16显存估算均欠条件；最大模型容量不能只当参数权重体积，单次矩阵计时不是训练基准。

Docker源文混淆停止/删除与持久性、卷/绑定挂载，泛化平台兼容与CPU回退，Compose实际上是Jupyter+Qdrant且qdrant_client依赖未声明；相对挂载路径指向phases，不是仓库根；清理和runtime/devel替换也有前提。技术含义、字段和命令保持源样，没有静默修正。

官方核验进一步确认：

- docker组会授予root级权限，见[Docker安装后步骤](https://docs.docker.com/engine/install/linux-postinstall)
- bind mount默认可修改宿主文件，见[绑定挂载](https://docs.docker.com/engine/storage/bind-mounts/)
- 停止容器不自动删除其可写层，`--rm`等自动删除情形另论，见[清理容器](https://docs.docker.com/engine/manage-resources/pruning/)
- 未指定宿主IP的发布端口默认覆盖所有接口，见[端口发布](https://docs.docker.com/engine/network/port-publishing/)
- Colab资源和GPU类型会变，见[官方FAQ](https://research.google.com/colaboratory/faq.html)

这些风险提示不是执行许可。未改驱动/用户组/权限/网络，未安装PyTorch/Docker/Toolkit，未运行容器，未租GPU、开户、付款或输入凭据。

## 尚未通过及记录边界

原站离线解析仍存在中文空锚点；真实网站浏览器、移动端、交互figure、托管CI与用户发布验收未通过。继承Actions保持禁用。GFM通过不能替代网站或可执行环境通过，所有PR保持draft。

[TASKS.json](TASKS.json)、[VALIDATION.json](VALIDATION.json)、[TERMINOLOGY.md](TERMINOLOGY.md)只属于S03；不覆盖历史台账。[DEPENDENCIES.json](DEPENDENCIES.json)固定共享控制和之前术语的提交/hash，可在隔离工作树只读组合，不要求先远端合并，也不把其他课程放进本PR。单独S03检查2课，全24结果来自组合验证树。完整33回归另需P1固定测试夹具，不能把测试夹具提交到本PR。

后续00/09数据管理可以作为独立完整主题继续；00/12调试/性能含basic PyTorch先修，按v1.2路线在对应基础具备后安排，不因同属00阶段强行提前。源技术修正与最终合并部署仍另作决定。
