# Third-party source notices

The project's Apache-2.0 license is in [LICENSE](LICENSE). Third-party source
notices and license conditions are retained for the portions to which they
apply; a company modification notice does not replace an original notice.

## vLLM

This plugin contains code copied or adapted from
[vLLM](https://github.com/vllm-project/vllm), including source snapshots embedded
in runtime-patch modules for upstream fingerprint checks.

The public comparison baseline is vLLM `v0.27.1`, commit
`6e448d0ea9bf3d88d898b65449ca6dc2aec170ac`. Per-file references are listed in
[docs/licensing/UPSTREAM_SOURCES.md](docs/licensing/UPSTREAM_SOURCES.md). These
references identify corresponding public code, not a claim that every file
originated at that particular revision or has only one upstream source.

Applicable vLLM contributor notices are retained in the source. Some upstream
files additionally carry NVIDIA, DeepSeek, Hugging Face, Qwen, or other source
attributions; those notices are preserved with the adapted code. The root
Apache-2.0 license accompanies these portions.

## Flash Linear Attention

Files under `vllm_iluvatar/third_party/flash_linear_attention/` incorporate code
from vLLM's vendored Flash Linear Attention implementation. The upstream files
carry vLLM contributor notices and Songlin Yang / Yu Zhang attribution, with
an explicit statement that the original Flash Linear Attention code used MIT.

The original MIT license is retained at
[the component LICENSE](vllm_iluvatar/third_party/flash_linear_attention/LICENSE)
and [licenses/flash-linear-attention-MIT.txt](licenses/flash-linear-attention-MIT.txt).
The Apache SPDX markers inherited from vLLM do not remove the MIT conditions
on incorporated portions. The modified `ilu_l2norm.py` retains this source chain
as well.

## causal-conv1d

`vllm_iluvatar/model_executor/layers/mamba/ops/ilu_causal_conv1d.py` is adapted
from vLLM's causal-convolution implementation. Its original notice identifies
Tri Dao and the causal-conv1d project, and remains in the file.

The BSD-3-Clause license and referenced authors list are included verbatim:

- [licenses/causal-conv1d-BSD-3-Clause.txt](licenses/causal-conv1d-BSD-3-Clause.txt)
- [licenses/causal-conv1d-AUTHORS.txt](licenses/causal-conv1d-AUTHORS.txt)

These texts were retrieved from the original project's
[v1.4.0 LICENSE](https://github.com/Dao-AILab/causal-conv1d/blob/v1.4.0/LICENSE)
and [AUTHORS](https://github.com/Dao-AILab/causal-conv1d/blob/v1.4.0/AUTHORS).
This is a reference for the retained BSD terms, not confirmation that v1.4.0
was the exact revision used by the intermediate vLLM implementation.

## Distribution scope

This document records identified incorporated source, rather than declaring
every file company-original or enumerating every separately installed runtime
dependency. Where additional upstream sources are identified, retain their
applicable notices and license materials as well.
