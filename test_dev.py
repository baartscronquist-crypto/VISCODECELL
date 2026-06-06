from scaffold import vis_MC_Gillespie_Elastic_SLS
import numpy as np

print("--- local smoke test ---")
try:
    T, vf, Fsub, vfmean, Fadh = vis_MC_Gillespie_Elastic_SLS(neta=1.0, ka=0.5)
    T = np.asarray(T, dtype=float)
    vf = np.asarray(vf, dtype=float)
    Fsub = np.asarray(Fsub, dtype=float)
    print(f"lengths: T={len(T)}, vf={len(vf)}, Fsub={len(Fsub)}")
    print(f"vfmean={float(vfmean):.3f}, Fadh={float(Fadh):.3f}")
    assert T.ndim == vf.ndim == Fsub.ndim == 1
    assert len(T) == len(vf) == len(Fsub)
    assert np.all(np.isfinite(T))
    assert np.all(np.isfinite(vf))
    assert np.all(np.isfinite(Fsub))
    assert np.isfinite(float(vfmean))
    assert np.isfinite(float(Fadh))
except Exception as e:
    print(f"local smoke test failed:\n{e}")
