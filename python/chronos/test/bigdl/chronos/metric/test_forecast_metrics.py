#
# Copyright 2016 The BigDL Authors.
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
#

import numpy as np
from unittest import TestCase
from numpy.testing import assert_almost_equal
from numpy.testing import assert_array_almost_equal

from bigdl.chronos.metric.forecast_metrics import Evaluator

class TestChronosForecastMetrics(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_forecast_metric(self):
        n_samples = 50
        y_true = np.arange(n_samples) + 1
        y_pred = y_true + 1

        assert_almost_equal(Evaluator.evaluate("mse", y_true, y_pred, aggregate="mean")[0], 1.)
        assert_almost_equal(Evaluator.evaluate("mae", y_true, y_pred, aggregate="mean")[0], 1.)
        assert_almost_equal(Evaluator.evaluate("r2", y_true, y_pred, aggregate="mean")[0], 0.995, 2)
        assert_almost_equal(Evaluator.evaluate("smape", y_true, y_pred, aggregate="mean")[0], 3.89*2/100, 2)

        y_true = np.array([3, -0.5, 2, 7])
        y_pred = np.array([2.5, -0.3, 2, 8])

        assert_almost_equal(Evaluator.evaluate("mape", y_true, y_pred, aggregate="mean")[0], 17.74/100, 2)
        assert_almost_equal(Evaluator.evaluate("RMSE", y_true, y_pred, aggregate="mean")[0], 0.57, 2)

    def test_highdim_array_metrics(self):
        y_true = np.array([[[3, -0.5], [2, 7]], [[3, -0.5], [2, 7]], [[3, -0.5], [2, 7]]])
        y_pred = np.array([[[2.5, -0.3], [2, 8]], [[2.5, -0.3], [2, 8]], [[2.5, -0.3], [2, 8]]])

        assert_almost_equal(Evaluator.evaluate("smape", y_true, y_pred, aggregate=None)[0],
                            [[9.09*2/100, 25*2/100], [0*2/100, 6.67*2/100]], 2)
        assert_almost_equal(Evaluator.evaluate("mape", y_true, y_pred, aggregate=None)[0],
                            [[16.67/100, 40.00/100], [0/100, 14.29/100]], 2)
        assert_almost_equal(Evaluator.evaluate("rmse", y_true, y_pred, aggregate=None)[0],
                            [[0.5, 0.2], [0, 1]], 2)
        assert_almost_equal(Evaluator.evaluate("mse", y_true, y_pred, aggregate=None)[0],
                            [[0.25, 0.04], [0, 1]], 2)
