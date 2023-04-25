"""Degrees to radians function"""
import math as m


def deg_to_rad(grados):
    """radians"""
    radianes = (grados * m.pi)/180
    print(f"{grados}° are {radianes} radians")

    return radianes
