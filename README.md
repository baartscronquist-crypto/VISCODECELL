# motor_clutch_repro_public_refs_standard_slow

你正在复现一个一维 motor-clutch / SLS viscoelastic substrate 随机仿真 benchmark。

实现位置：`scaffold.py`

公开接口：

```python
vis_MC_Gillespie_Elastic_SLS(neta, ka, kl=0.1, is_plot=False)
```

返回值必须是 5 个对象：

```python
T, vf, Fsub, vfmean, Fadh
```

- `T`: 一维时间数组，单位 s。
- `vf`: 与 `T` 同长度的一维 retrograde flow velocity 数组，单位 nm/s。
- `Fsub`: 与 `T` 同长度的一维 substrate/adhesion force 数组，单位 pN。
- `vfmean`: 基于完整仿真时程的平均速度标量。
- `Fadh`: 基于完整仿真时程的平均黏附/牵引力标量。

## Reproduction Notes

这是 benchmark 复现场景，而不是科研发现者场景。你可以使用公开描述和少量公开参考输出校准实现，但隐藏评测只返回二元结果：

- `CORRECT`, `Score: 100/100`
- `NOT_CORRECT`, `Score: 0/100`

隐藏评测不会返回中间分数、隐藏阈值、隐藏 raw trace、隐藏参数表。

建议实现真实的 Gillespie/KMC 微观状态演化，并与 SLS 粘弹性基底耦合。不要用查表、按参数分支硬编码、正弦曲线、sigmoid、高斯曲线或其它经验公式替代动力学过程。

## Model Summary

每个 clutch 处于 bound/unbound 状态。未结合 clutch 以常数 on-rate 结合，已结合 clutch 以 force-dependent slip-bond off-rate 解绑。每次 Gillespie 事件后，用当前 bound clutch 变形和 SLS substrate 状态更新 substrate displacement、clutch force、substrate force 和 retrograde velocity。

典型行为：

- low adhesion / load-fail 条件下，`vf` 与 `Fsub` 常出现强反相关的 sawtooth-like oscillation。
- strong adhesion / frictional-slippage 条件下，高 `neta` 区域的 `vfmean` 会显著升高并接近无负载速度。
- 低到中等 `ka` 的 `vfmean` 随 `neta` 扫描通常不是单调曲线，会出现 valley，并且 valley 位置随 `ka` 增大向右移动。

## Public Sparse References

这些是公开参考输出。它们是 sparse rounded traces，只用于帮助复现者校准量级和时序形状；它们不是隐藏评分表。

```json
[
  {
    "seed_label": "public_ref_202701",
    "args": {"neta": 1.0, "ka": 0.1, "kl": 0.1},
    "columns": ["T", "vf", "Fsub"],
    "vfmean": 38.569,
    "Fadh": 101.911,
    "rows": [
      [0.0, 120.0, 0.0],
      [143.243, 68.802, 64.697],
      [288.885, 31.418, 110.736],
      [433.808, 23.746, 120.329],
      [574.303, 18.79, 126.597],
      [713.856, 41.627, 98.368],
      [854.796, 11.281, 135.9],
      [1000.038, 40.33, 100.392]
    ]
  },
  {
    "seed_label": "public_ref_202702",
    "args": {"neta": 0.1, "ka": 0.5, "kl": 0.1},
    "columns": ["T", "vf", "Fsub"],
    "vfmean": 32.569,
    "Fadh": 109.286,
    "rows": [
      [0.0, 120.0, 0.0],
      [153.704, 20.356, 124.58],
      [295.65, 43.191, 96.061],
      [440.433, 26.13, 117.362],
      [573.789, 36.732, 104.293],
      [721.473, 33.401, 108.25],
      [860.124, 13.366, 133.317],
      [1000.006, 36.335, 104.612]
    ]
  },
  {
    "seed_label": "public_ref_202703",
    "args": {"neta": 10.0, "ka": 10.0, "kl": 0.1},
    "columns": ["T", "vf", "Fsub"],
    "vfmean": 103.183,
    "Fadh": 21.032,
    "rows": [
      [0.0, 120.0, 0.0],
      [143.121, 93.616, 24.272],
      [286.678, 81.106, 57.037],
      [429.818, 66.841, 65.744],
      [573.246, 100.942, 29.054],
      [715.545, 118.063, 2.958],
      [859.266, 120.0, 5.372],
      [1000.006, 96.884, 36.847]
    ]
  }
]
```

## Public Smoke Test

`test_dev.py` 只检查接口、shape、有限性和基本可运行性。通过公开 smoke test 不代表通过隐藏评测。
