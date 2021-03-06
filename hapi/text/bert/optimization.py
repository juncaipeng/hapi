#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from paddle.fluid.framework import in_dygraph_mode
from hapi.text.bert.dygraph_optimization import DyOptimizer as DyOptimizer
from hapi.text.bert.static_optimization import StOptimizer as StOptimizer


def make_optimizer(warmup_steps,
                   num_train_steps,
                   learning_rate,
                   weight_decay,
                   model,
                   scheduler='linear_warmup_decay',
                   loss_scaling=1.0,
                   parameter_list=None):

    if in_dygraph_mode():
        return DyOptimizer(
            warmup_steps=warmup_steps,
            num_train_steps=num_train_steps,
            learning_rate=learning_rate,
            model_cls=model,
            weight_decay=weight_decay,
            scheduler=scheduler,
            loss_scaling=loss_scaling,
            parameter_list=parameter_list)
    else:
        return StOptimizer(
            warmup_steps=warmup_steps,
            num_train_steps=num_train_steps,
            learning_rate=learning_rate,
            weight_decay=weight_decay,
            scheduler=scheduler)
