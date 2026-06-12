# motor_clutch_repro_public_refs_strong_blind_slow

实现位置：`scaffold.py`

公开接口：

```python
vis_MC_Gillespie_Elastic_SLS(neta, ka, kl=0.1, is_plot=False)
```

返回值必须是：

```python
T, vf, Fsub, vfmean, Fadh
```

- `T`: 一维时间数组，单位 s。
- `vf`: 与 `T` 同长度的一维 retrograde flow velocity 数组，单位 nm/s。
- `Fsub`: 与 `T` 同长度的一维 substrate/adhesion force 数组，单位 pN。
- `vfmean`: 基于完整仿真时程的平均速度标量。
- `Fadh`: 基于完整仿真时程的平均黏附/牵引力标量。

## Evaluation Notes

隐藏评测返回二元结果：

- `CORRECT`, `Score: 100/100`
- `NOT_CORRECT`, `Score: 0/100`

隐藏评测不会返回中间分数、隐藏阈值、隐藏参数表。但会反馈部分原始raw trace & 特征。

实现中应保留 Gillespie/KMC 随机事件推进，不要仅根据公开数据点拼接或拟合输出曲线。公开数据点的 seed label 只用于识别公开样例，不代表隐藏评测 seed 或完整数据。
