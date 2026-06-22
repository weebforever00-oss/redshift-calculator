#!/usr/bin/env python3
"""Cosmological redshift and distance."""
import math

C = 299792.458  # km/s

def redshift_to_velocity(z):
    """Relativistic velocity from redshift."""
    return C * ((1+z)**2 - 1) / ((1+z)**2 + 1)

def velocity_to_distance_Mpc(v, H0=70):
    """Hubble law: d = v/H0."""
    return v / H0

def lookback_time_Gyr(z, H0=70, Omega_m=0.3):
    """Approximate lookback time."""
    return (2 / (H0 * 3.24e-20 * 3.15e16)) * (1 - 1/math.sqrt(1+z))  # rough

if __name__ == "__main__":
    objects = [("Nearby galaxy", 0.001), ("Virgo cluster", 0.004), ("Coma cluster", 0.023),
               ("Quasar 3C273", 0.158), ("High-z galaxy", 1.5), ("Most distant", 11.0)]
    print("Redshift Calculator")
    for name, z in objects:
        v = redshift_to_velocity(z)
        d = velocity_to_distance_Mpc(v)
        print(f"  {name:20s}: z={z:.3f}, v={v:,.0f} km/s, d={d:,.0f} Mpc")\n