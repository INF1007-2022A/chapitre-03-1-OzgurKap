#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    a = a ** 0.5
    return a


def square(a: float) -> float:
    a = a ** 2
    return a


def average(a: float, b: float, c: float) -> float:
    d = (a + b + c) / 3
    return d


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degs = (angle_mins * pi) / 180
    angle_mins = angle_mins/60/180*pi
    angle_secs = angle_secs/60/60/180*pi
    return angle_degs, angle_mins, angle_secs


def to_degrees(angle_rads: float) -> tuple:

    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
