# test_dev.py (发给 Agent 调试用的公开测试集)
from scaffold import vis_MC_Gillespie_Elastic_SLS
import numpy as np

print("--- 开始本地基础调试 ---")
try:
    # 只给一组普普通通的参数，让 AI 看看能不能跑通，有没有报错
    T, vf, Fsub, vfmean, Fadh = vis_MC_Gillespie_Elastic_SLS(neta=1.0, ka=0.5)
    
    print(f"代码运行成功！")
    print(f"输出数据长度: T={len(T)}, vf={len(vf)}")
    print(f"稳态平均速度 vfmean: {vfmean:.2f}")
    
    if np.isnan(vfmean):
        print("警告: 结果出现 NaN，你的差分格式存在发散问题，请重新设计！")
        
except Exception as e:
    print(f"代码运行崩溃，报错信息如下：\n{e}")