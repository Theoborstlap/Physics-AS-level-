# -*- coding: utf-8 -*-
"""Additional extreme-difficulty multiple-choice questions, AS 9702.
Appends to engine.mcq. add(topic, q, options[4], correct index 0-3, ans, svg='')."""
from engine import mcq as M
from mcq_all import (MT1, MT2, MT3, MT4, MT5, MT6, MT7, MT8, MT9, MT10, MT11)


def add(topic, q, options, correct, ans, svg=""):
    M.append({"topic": topic, "q": q, "options": options, "correct": correct,
              "ans": ans, "svg": svg})


# TOPIC 1
add(MT1,
 "The kinetic energy of a body is E = &frac12;mv&sup2;. If the mass is measured to &plusmn;2% and the "
 "speed to &plusmn;3%, the percentage uncertainty in E is:",
 ["5%", "6%", "8%", "11%"], 2,
 "v is squared, so it contributes 2 &times; 3% = 6%; m contributes 2%. Total = 2 + 6 = 8%.")

add(MT1,
 "A rectangular plate has sides (50.0 &plusmn; 0.5) mm and (20.0 &plusmn; 0.5) mm. The percentage "
 "uncertainty in its area is closest to:",
 ["1.0%", "2.0%", "3.5%", "5.0%"], 2,
 "%unc in each side: 0.5/50.0 = 1.0% and 0.5/20.0 = 2.5%. Area is a product &rArr; add: 1.0 + 2.5 = "
 "3.5%.")

# TOPIC 2
add(MT2,
 "A ball is projected horizontally at 15 m s<sup>&minus;1</sup> from a height of 20 m. The speed "
 "with which it strikes the ground is about (g = 9.8 m s<sup>&minus;2</sup>):",
 ["15 m s<sup>&minus;1</sup>", "20 m s<sup>&minus;1</sup>", "24 m s<sup>&minus;1</sup>",
  "35 m s<sup>&minus;1</sup>"], 2,
 "v<sub>y</sub> = &radic;(2gh) = &radic;(2&times;9.8&times;20) = 19.8 m s<sup>&minus;1</sup>. "
 "Speed = &radic;(15&sup2; + 19.8&sup2;) = &radic;(225 + 392) = &radic;617 = 24.8 &asymp; 24 m s<sup>&minus;1</sup>.")

add(MT2,
 "The area between a velocity&ndash;time graph and the time axis represents displacement. For a graph "
 "that goes positive then equally negative, the area gives zero. This means:",
 ["the object did not move", "the total distance is zero",
  "the object returned to its start point", "the speed was always zero"], 2,
 "Zero net area means zero displacement &mdash; the object returned to its starting point, though it "
 "did travel (distance is non-zero).")

# TOPIC 3
add(MT3,
 "A 1200 kg car changes velocity from 15 m s<sup>&minus;1</sup> east to 15 m s<sup>&minus;1</sup> "
 "north in 6.0 s. The magnitude of the average resultant force is closest to:",
 ["0 N", "2500 N", "4200 N", "6000 N"], 2,
 "&Delta;v = &radic;(15&sup2; + 15&sup2;) = 21.2 m s<sup>&minus;1</sup>. "
 "F = m&Delta;v/&Delta;t = 1200 &times; 21.2/6.0 = 4240 &asymp; 4200 N.")

add(MT3,
 "Water leaves a hose of area 5.0 &times; 10<sup>&minus;4</sup> m&sup2; at 20 m s<sup>&minus;1</sup> "
 "and hits a wall, stopping. (Density 1000 kg m<sup>&minus;3</sup>.) The force on the wall is:",
 ["50 N", "100 N", "200 N", "400 N"], 2,
 "Mass/s = &rho;Av = 1000 &times; 5.0&times;10<sup>&minus;4</sup> &times; 20 = 10 kg s<sup>&minus;1</sup>. "
 "Force = (mass/s)&Delta;v = 10 &times; 20 = 200 N.")

# TOPIC 4
add(MT4,
 "A uniform beam of weight 60 N and length 2.0 m rests on a single pivot 0.50 m from the left end. "
 "The downward force needed at the left end to balance it is:",
 ["30 N", "60 N", "90 N", "120 N"], 1,
 "Weight acts at centre, 0.50 m right of pivot: moment = 60 &times; 0.50 = 30 N m. Force F at 0.50 m "
 "left of pivot: F &times; 0.50 = 30 &rArr; F = 60 N.")

add(MT4,
 "A cube of side 0.10 m and density 600 kg m<sup>&minus;3</sup> floats in water. The depth of the "
 "cube below the surface is:",
 ["0.04 m", "0.06 m", "0.08 m", "0.10 m"], 1,
 "Fraction submerged = &rho;<sub>cube</sub>/&rho;<sub>water</sub> = 600/1000 = 0.60. "
 "Depth = 0.60 &times; 0.10 = 0.06 m.")

# TOPIC 5
add(MT5,
 "A 500 kg lift is raised at a constant 3.0 m s<sup>&minus;1</sup>. The useful power of the motor "
 "(ignoring friction) is:",
 ["1.5 kW", "4.9 kW", "9.8 kW", "15 kW"], 3,
 "At constant speed the motor force = weight = 500 &times; 9.81 = 4905 N. "
 "P = Fv = 4905 &times; 3.0 = 14.7 kW &asymp; 15 kW.")

add(MT5,
 "A ball of mass 0.20 kg is dropped from 5.0 m and rebounds to 3.2 m. The energy dissipated in the "
 "bounce is:",
 ["1.8 J", "3.5 J", "6.3 J", "9.8 J"], 1,
 "Energy lost = mg&Delta;h = 0.20 &times; 9.81 &times; (5.0 &minus; 3.2) = 0.20 &times; 9.81 &times; "
 "1.8 = 3.5 J.")

# TOPIC 6
add(MT6,
 "Two identical springs each of stiffness k are connected in parallel and support a load. The "
 "combined stiffness is:",
 ["k/2", "k", "2k", "4k"], 2,
 "In parallel the stiffnesses add: k<sub>total</sub> = k + k = 2k (stiffer, extends less for a given "
 "load).")

add(MT6,
 "A wire stretches 1.5 mm under a load. An identical wire of the same material and diameter but half "
 "the length stretches, under the same load, by:",
 ["0.375 mm", "0.75 mm", "1.5 mm", "3.0 mm"], 1,
 "e = FL/(AE) &prop; L. Half the length &rArr; half the extension: 1.5/2 = 0.75 mm.")

# TOPIC 7
add(MT7,
 "A wave on a string has the equation form of a sine wave with period 0.040 s and wavelength 0.50 m. "
 "Its speed is:",
 ["2.0 m s<sup>&minus;1</sup>", "12.5 m s<sup>&minus;1</sup>", "20 m s<sup>&minus;1</sup>",
  "0.020 m s<sup>&minus;1</sup>"], 1,
 "f = 1/T = 25 Hz. v = f&lambda; = 25 &times; 0.50 = 12.5 m s<sup>&minus;1</sup>.")

add(MT7,
 "Plane-polarised light passes through a polariser. The intensity is reduced to 50% of its incident "
 "value when the angle between the polarisation plane and the axis is:",
 ["30&deg;", "45&deg;", "60&deg;", "90&deg;"], 1,
 "Malus: I/I<sub>0</sub> = cos&sup2;&theta; = 0.50 &rArr; cos&theta; = 0.707 &rArr; &theta; = 45&deg;.")

# TOPIC 8
add(MT8,
 "In a double-slit experiment the fringe spacing is 2.0 mm. If the whole apparatus is immersed in "
 "water (refractive index 1.33), which reduces the wavelength, the fringe spacing becomes about:",
 ["1.5 mm", "2.0 mm", "2.7 mm", "3.3 mm"], 0,
 "&lambda; reduces by a factor 1.33 in water, and x &prop; &lambda;, so x = 2.0/1.33 = 1.5 mm.")

add(MT8,
 "Light of wavelength 500 nm is incident normally on a grating with slit spacing "
 "2.0 &times; 10<sup>&minus;6</sup> m. The angle of the first-order maximum is:",
 ["7.2&deg;", "14.5&deg;", "30&deg;", "45&deg;"], 1,
 "sin&theta; = n&lambda;/d = 500&times;10<sup>&minus;9</sup>/2.0&times;10<sup>&minus;6</sup> = 0.25 "
 "&rArr; &theta; = 14.5&deg;.")

# TOPIC 9
add(MT9,
 "A charge of 4.0 mC flows through a lamp in 2.0 ms. The average current is:",
 ["0.5 A", "2.0 A", "8.0 A", "8.0 mA"], 1,
 "I = Q/t = 4.0&times;10<sup>&minus;3</sup>/2.0&times;10<sup>&minus;3</sup> = 2.0 A.")

add(MT9,
 "Two resistors, 6.0 &Omega; and 3.0 &Omega;, are connected in parallel and a total current of 3.0 A "
 "flows into the combination. The current in the 6.0 &Omega; resistor is:",
 ["0.5 A", "1.0 A", "1.5 A", "2.0 A"], 1,
 "Current divides inversely with resistance. I<sub>6</sub>/I<sub>total</sub> = R<sub>3</sub>/(R<sub>3</sub>+R<sub>6</sub>) "
 "= 3.0/9.0 = 1/3. I<sub>6</sub> = 3.0/3 = 1.0 A.")

# TOPIC 10
add(MT10,
 "A cell of e.m.f. 1.5 V is short-circuited (external resistance &asymp; 0) and the current is 6.0 A. "
 "The internal resistance is:",
 ["0.25 &Omega;", "0.40 &Omega;", "4.0 &Omega;", "9.0 &Omega;"], 0,
 "Short circuit: &epsilon; = Ir &rArr; r = 1.5/6.0 = 0.25 &Omega;.")

add(MT10,
 "In a potential divider with a fixed resistor and an LDR (output across the LDR), moving the setup "
 "into brighter light causes the output voltage to:",
 ["increase", "decrease", "stay the same", "become zero"], 1,
 "Brighter light lowers the LDR resistance, so a smaller share of the supply voltage appears across "
 "the LDR &mdash; the output taken across the LDR decreases.")

# TOPIC 11
add(MT11,
 "A nuclide <sup>A</sup><sub>Z</sub>X emits a &beta;<sup>+</sup> particle. The resulting nuclide is:",
 ["<sup>A</sup><sub>Z+1</sub>Y", "<sup>A</sup><sub>Z&minus;1</sub>Y",
  "<sup>A&minus;4</sup><sub>Z&minus;2</sub>Y", "<sup>A&minus;1</sup><sub>Z</sub>Y"], 1,
 "&beta;<sup>+</sup> decay: a proton becomes a neutron, so Z decreases by 1 while A is unchanged: "
 "<sup>A</sup><sub>Z&minus;1</sub>Y.")

add(MT11,
 "Which combination of quarks could form a baryon of charge +2e (such as the &Delta;<sup>++</sup>)?",
 ["uud", "uuu", "u&#363;", "udd"], 1,
 "Charge of uuu = 3 &times; (+&frac23;e) = +2e; three quarks &rArr; a baryon. "
 "uud = +1e, udd = 0, and u&#363; is a meson.")
