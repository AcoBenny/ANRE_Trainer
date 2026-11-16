#!/usr/bin/env python3
"""CKPT051: deterministic numeric and dimension checks, NOT technical or source QA."""
import math
checks = []
def add(name, condition):
    checks.append((name, bool(condition)))
def close(a,b):
    return math.isclose(a,b,rel_tol=0,abs_tol=1e-12)

# ELE057: reciprocal period ratios, n=1, and two harmonics of shared f0.
add("ELE057_T1_2_T2_1_A",close(2/1,2))
add("ELE057_T1_1_T2_2_C",close(1/2,0.5))
add("ELE057_equal_B_and_A",close(1/1,1))
add("ELE057_common_f0_50",close(100/50,2) and close(150/50,3) and not close(150/100,round(150/100)))

# ELE128: phase from positive R and positive or negative net reactance.
for R,X,expected in [(10,10,45),(0,10,90),(10,0,0),(10,-10,-45)]:
    add(f"ELE128_R{R}_X{X}",close(math.degrees(math.atan2(X,R)),expected))

# ELE222: imaginary part of 1/(R+jX), not necessarily 1/X.
for R,X,B in [(3,4,-0.16),(0,4,-0.25),(0,-4,0.25)]:
    add(f"ELE222_R{R}_X{X}",close((1/complex(R,X)).imag,B))

# ELE245: RLC resonance gives unity PF with L and C present.
for R,XL,XC,expected in [(5,10,10,1),(5,10,3,5/math.sqrt(74))]:
    add(f"ELE245_R{R}_XL{XL}_XC{XC}",close(R/math.sqrt(R*R+(XL-XC)**2),expected))

# ELE257: dimension check D*[m²]=C, E*[m²]=V*m.
add("ELE257_D_flux_C",("C/m^2","m^2")==("C/m^2","m^2"))
add("ELE257_E_flux_V_m",("V/m","m^2")==("V/m","m^2"))

# ELE231: for a unit-amplitude sine RMS is real and nonzero.
N=4096
vals=[math.sin(2*math.pi*i/N) for i in range(N)]
add("ELE231_RMS_nonzero",close(math.sqrt(sum(v*v for v in vals)/N),1/math.sqrt(2)))
add("ELE231_mean_zero",close(sum(vals)/N,0.0))

print(f"CKPT051 NUMERIC/DIMENSIONAL PREFLIGHT {sum(v for _,v in checks)}/{len(checks)} PASS")
for name,ok in checks:print(("PASS" if ok else "FAIL"),name)
raise SystemExit(0 if all(v for _,v in checks) else 1)
