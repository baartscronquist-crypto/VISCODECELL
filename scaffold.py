import numpy as np
import matplotlib.pyplot as plt
import time

# ==========================================
# 核心函数：完全复刻您提供的最新 MATLAB 源码
# ==========================================
def vis_MC_Gillespie_Elastic_SLS(neta, ka, kl=0.1):
    # definition of basic parameters
    Tfinal = 1000      # unit s running time
    kc = 5             # unit pN/nm  clutch stiffness
    ron0 = 1           # unit s^-1  clutch on rate 
    roff = 0.1         # unit s^-1  clutch off rate  
    Fb = 2             # unit pN  characteristic unbinding force 
    Nc = 75            # unit 1  number of clutches
    Nm = 75            # unit 1  number of motors
    Fm = 2             # unit pN  per motor applied force
    vu = 120           # unit nm/s polymerization speed
    
    # Python 中使用列表动态追加，等效于 MATLAB 中不断扩容的数组
    T = [0.0]
    vf = [vu]   
    Fsub = [0.0]
    xst = [0.0]
    
    # solving governing equations based on Monte Carlo method
    t = 0.0


# ==========================================
# 主执行程序与画图
# ==========================================
if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    vu = 120
    start_time = time.time()
    
    # ----------------------------------------------------
    # 验证要求1: 测试 ka 较小 (Load-fail) 和 ka, ks 较大 (Frictional slippage)
    # ----------------------------------------------------
    print("正在计算要求1: 时间序列 t-vf 图...")
    T1, vf1, _, _, _ = vis_MC_Gillespie_Elastic_SLS(neta=1.0, ka=0.1, kl=0.1)
    T2, vf2, _, _, _ = vis_MC_Gillespie_Elastic_SLS(neta=1.0, ka=10, kl=10)
    
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(T1, vf1, 'b-', linewidth=0.5)
    ax1.set_title("Load-fail 状态 (ka=0.1, kl=0.1)")
    ax1.set_xlabel("时间 (s)"), ax1.set_ylabel("流动速度 vf (nm/s)")
    
    ax2.plot(T2, vf2, 'r-', linewidth=0.5)
    ax2.set_title("Frictional slippage 状态 (ka=10, kl=10)")
    ax2.set_xlabel("时间 (s)"), ax2.set_ylabel("流动速度 vf (nm/s)")
    plt.tight_layout()

    # ----------------------------------------------------
    # 验证要求2 & 3: 复刻您 MATLAB 中最新的参数扫描循环
    # ----------------------------------------------------
    print("正在计算要求2与3: KMCS 扫描不同 ka 与 neta ...")
    
    ka_list = [0.1, 0.5, 1.0, 10]
    
    # 【速度优化提示】:
    # MATLAB 原版使用的是 1000 个线性分布点，会导致巨量计算。
    # neta_values = np.linspace(0.01, 100, 50) 
    
    # 为了双对数作图(loglog)更美观且1-2分钟内出结果，这里改用 100 个对数分布点：
    neta_values = np.logspace(np.log10(0.01), np.log10(100), 100)
    