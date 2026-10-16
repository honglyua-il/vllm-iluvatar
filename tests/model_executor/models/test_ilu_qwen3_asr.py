# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright (c) 2026 Shanghai Iluvatar CoreX Semiconductor Co., Ltd.
"""CPU-only registration tests for the Iluvatar Qwen3-ASR override."""

from __future__ import annotations


def test_oot_registration_points_at_plugin_subclass():
    from vllm import ModelRegistry
    from vllm.model_executor.models.registry import _VLLM_MODELS

    from vllm_iluvatar.ilu_register import apply_oot_registrations

    assert "Qwen3ASRForConditionalGeneration" in _VLLM_MODELS

    apply_oot_registrations()
    entry = ModelRegistry.models["Qwen3ASRForConditionalGeneration"]
    assert entry.module_name == "vllm_iluvatar.model_executor.models.qwen3_asr"
    assert entry.class_name == "Qwen3ASRForConditionalGeneration"


def test_plugin_class_subclasses_community():
    from vllm.model_executor.models.qwen3_asr import (
        Qwen3ASRForConditionalGeneration as _Community,
    )
    from vllm_iluvatar.model_executor.models.qwen3_asr import (
        Qwen3ASRForConditionalGeneration,
    )

    assert issubclass(Qwen3ASRForConditionalGeneration, _Community)
