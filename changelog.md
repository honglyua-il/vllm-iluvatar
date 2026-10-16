# Changelog

本文件记录 `vllm-iluvatar` 的版本变更。格式参考
[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)。

**版本号与适配的 vLLM 版本保持一致**：`0.26.0` 适配 vLLM 0.26.0;当 vLLM
更新至 0.27.x 时,插件版本号同步更新。同一 vLLM 版本窗口内不再手工修改插件
版本号,其间的日常构建由 CI 追加 `-<git 日期>.<git 短哈希>-<构建版本>`
后缀加以区分。

本文件自 0.26.0 起开始维护，此前的变更请查阅 git 历史。

## [Unreleased]

### Added (Unreleased)

- 新增 vLLM 与 Iluvatar CoreX 联合标识图片。
- 新增 Apache-2.0 许可证文件及项目许可证声明。

### Removed

- 移除 vLLM、ixformer 私有源码子模块及其开发构建脚本。
- 移除私有依赖提交信息和文档中的内部仓库链接；运行依赖由 CoreX 环境提供。

### Changed

- 简化 README，更新独立插件的安装和开发说明。

- GLM / DeepSeek-V4 MoE 构造改为社区 `FusedMoEFactory`（0.27 去掉 `FusedMoE` 导出）。
- `IluMultiHeadLatentAttentionWrapper.__init__` 增加
  `non_causal_multi_token_decode` 与
  `allow_short_prefill_indexer_scoring_skip`，满足 OOT 前缀签名检查。
- `IluCommunicator` 接受并转发 `use_all2all`，对齐 0.27 `GroupCoordinator`。

## [0.26.0] - 2026-08-27

首个正式标记的版本，适配 vLLM 0.26.0 / CoreX 5.0.0。

### Added

- `IluPlatform`：CUDA 兼容的 CoreX 平台适配层，经 `vllm.platform_plugins`
  入口点注册。
- `IluCommunicator`：基于 `ixformer.distributed` 集合通信的通信后端。
- `vllm_iluvatar._C`：原生扩展，提供 vLLM 兼容的 `_C` 算子（`rms_norm`、
  `weak_ref_tensor`、`get_cuda_view_from_cpu_tensor`）。
- `vllm_iluvatar.kernels`：面向 vLLM V1 的天数 IR 算子 provider。
- 模型与量化适配，以及 worker 启动期所需的运行时补丁，经
  `vllm.general_plugins` 入口点注册。
- `IluNixlConnector` / `IluNixlPullConnector` / `IluNixlPushConnector`：
  用于 PD 分离部署的 KV 传输连接器。

以上全部通过 vLLM 的 out-of-tree plugin 机制加载，不修改 vLLM 主仓源码。
