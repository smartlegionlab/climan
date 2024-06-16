# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------


class Config:
    def __init__(self, params: dict):
        self._init(params)

    def _init(self, params: dict):
        for k, v in params.items():
            setattr(self, k, v)


class ConfigsBuilder:
    @classmethod
    def build_config(cls, data: dict):
        return Config(data)
