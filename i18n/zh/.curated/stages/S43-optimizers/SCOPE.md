# S43 / 03-06 Optimizers 新译范围

2026-10-02。仅从固定英文 `phases/03-deep-learning-core/06-optimizers/docs/en.md` 独立新译，基线 `1bafaa88bb4668356791150bec3a6d7df38387eb`，source SHA256 `9af59689813d171106b558fca9875f7992c8e834b8d7a69310bbaf7428ff9ad9`。目标为 `i18n/zh/phases/03-deep-learning-core/06-optimizers/docs/zh.md`，逐块记录在 `i18n/zh/.curated/lessons/03-06/translation.json`。

51 项控制与词表依赖按 DEPENDENCIES.json 的固定 Git commit 和 SHA256 逐字节核验。元数据、标识符、数字、公式、路径、代码、Mermaid 与 figure 载荷保护；原无语言围栏仅补 `text`。数量词采用自然中文时记录等值及单位。仅在实际 GFM 观察证明必要后作可逆最小语法修复。

作者完成逐块技术自查和另一次完整中文通读，记录保持 draft；独立技术与中文全文双审由 S45 作者完成。原 strict、33 项控制回归、两个全新工作区目录重放与三项仓库审计分项记录。完整预读源码后只在外置 timeout 下运行有限离线标准库/已装 allowlist 检查；缺包跳过，不安装或访问模型/数据服务。

正文中的动量归一化、二阶矩与方差混用、偏差校正时间尺度、AdamW 更新次序、学习率与更新量混用、收敛/泛化经验性断言及训练指标边界单列源问题，不在译文中修正。作者不写公共 review、共享索引或远端，不读取旧中文、翻译缓存或历史 PR 草稿。
