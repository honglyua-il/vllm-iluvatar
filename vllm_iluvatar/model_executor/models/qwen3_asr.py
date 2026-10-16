# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright (c) 2026 Shanghai Iluvatar CoreX Semiconductor Co., Ltd.
"""Corresponds to: vllm/model_executor/models/qwen3_asr.py

Iluvatar OOT Qwen3-ASR: the community class builds its text tower by importing
``Qwen3ForCausalLM`` directly, so the plugin registration of that arch is not
used. This subclass applies the existing fused q/k RMSNorm after init.

Target   : vllm.model_executor.models.qwen3_asr.Qwen3ASRForConditionalGeneration
           (arch "Qwen3ASRForConditionalGeneration")
Baseline : vllm 0.27.1
Why      : the nested Qwen3 decoder must use the same fused q/k RMSNorm as
           other Iluvatar Qwen3 models. Audio-tower attention already goes
           through ``IluMMEncoderAttention``.
How      : ModelRegistry.register_model points the arch at the subclass below.
           ``super().__init__()`` keeps the community graph, then
           ``qwen3_attention_fusion`` swaps each decoder ``self_attn``.
Scope    : Qwen3-ASR on the Iluvatar platform.
Remove   : when community Qwen3-ASR constructs the registered Qwen3 class, or
           community Qwen3 attention fuses q/k norm natively.

Registration: ``register_model()`` below is invoked by
``vllm_iluvatar.ilu_register.apply_oot_registrations`` during register_general.
"""

from __future__ import annotations

from vllm.config import VllmConfig
from vllm.model_executor.models.qwen3_asr import (
    Qwen3ASRForConditionalGeneration as _Qwen3ASRForConditionalGeneration,
)

from vllm_iluvatar.model_executor.models.qwen3 import qwen3_attention_fusion


class Qwen3ASRForConditionalGeneration(_Qwen3ASRForConditionalGeneration):
    """Qwen3-ASR with Iluvatar fused q/k RMSNorm in the text decoder."""

    def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__(vllm_config=vllm_config, prefix=prefix)
        qwen3_attention_fusion(self.language_model.model)


def register_model() -> None:
    """Point the Qwen3-ASR arch at the Iluvatar subclass."""
    from vllm import ModelRegistry

    ModelRegistry.register_model(
        "Qwen3ASRForConditionalGeneration",
        "vllm_iluvatar.model_executor.models.qwen3_asr:Qwen3ASRForConditionalGeneration",
    )
