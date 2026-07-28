# -*- coding: utf-8 -*-
"""PACK 2 - Multiple-choice questions, topics 1-6. AS 9702.
add(topic, q, options[list of 4], correct index 0-3, ans, svg='')."""
from engine import mcq as M

MT1 = "1&nbsp;&nbsp;Physical quantities and units"
MT2 = "2&nbsp;&nbsp;Kinematics"
MT3 = "3&nbsp;&nbsp;Dynamics"
MT4 = "4&nbsp;&nbsp;Forces, density and pressure"
MT5 = "5&nbsp;&nbsp;Work, energy and power"
MT6 = "6&nbsp;&nbsp;Deformation of solids"


def add(topic, q, options, correct, ans, svg=""):
    M.append({"topic": topic, "q": q, "options": options, "correct": correct,
              "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 1
# ===========================================================================
add(MT1, "Which of the following is a set of SI base units only?",
 ["kg, N, s, A", "m, kg, s, A", "m, kg, s, J", "m, g, s, A"], 1,
 "The SI base units include metre, kilogram, second and ampere. N and J are derived; g (gram) is not "
 "the base unit of mass (kg is).")

add(MT1, "The unit of the joule expressed in SI base units is:",
 ["kg m s<sup>&minus;2</sup>", "kg m&sup2; s<sup>&minus;2</sup>",
  "kg m&sup2; s<sup>&minus;3</sup>", "kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>"], 1,
 "J = N m = (kg m s<sup>&minus;2</sup>)(m) = kg m&sup2; s<sup>&minus;2</sup>.")

add(MT1, "A frequency of 2.5 GHz is equal to:",
 ["2.5 &times; 10<sup>6</sup> Hz", "2.5 &times; 10<sup>9</sup> Hz",
  "2.5 &times; 10<sup>12</sup> Hz", "2.5 &times; 10<sup>&minus;9</sup> Hz"], 1,
 "The prefix giga (G) = 10<sup>9</sup>, so 2.5 GHz = 2.5 &times; 10<sup>9</sup> Hz.")

add(MT1, "Which quantity is a vector?",
 ["kinetic energy", "temperature", "momentum", "electric charge"], 2,
 "Momentum (mass &times; velocity) has direction. The others are scalars.")

add(MT1, "The diameter of a wire is measured as (0.50 &plusmn; 0.01) mm. The percentage uncertainty in "
 "its cross-sectional area is:",
 ["2%", "4%", "1%", "8%"], 1,
 "Area &prop; d&sup2;, so % uncertainty = 2 &times; (0.01/0.50) = 2 &times; 2% = 4%.")

add(MT1, "Two forces of 3.0 N and 4.0 N act at right angles at a point. The magnitude of their "
 "resultant is:",
 ["1.0 N", "5.0 N", "7.0 N", "12 N"], 1,
 "Perpendicular: R = &radic;(3.0&sup2; + 4.0&sup2;) = &radic;25 = 5.0 N.")

add(MT1, "The base units kg m<sup>&minus;1</sup> s<sup>&minus;2</sup> are the units of:",
 ["force", "energy", "pressure", "power"], 2,
 "Pa = N m<sup>&minus;2</sup> = kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>. This is pressure "
 "(also stress).")

add(MT1, "A physical quantity is estimated. Which is the best estimate of the wavelength of red light?",
 ["7 &times; 10<sup>&minus;9</sup> m", "7 &times; 10<sup>&minus;7</sup> m",
  "7 &times; 10<sup>&minus;5</sup> m", "7 &times; 10<sup>&minus;3</sup> m"], 1,
 "Visible light is 400&ndash;700 nm; red is at the long-wavelength end, ~7 &times; 10<sup>&minus;7</sup> m.")

add(MT1, "A force of 20 N acts at 60&deg; to the horizontal. Its horizontal component is:",
 ["10 N", "17 N", "20 N", "12 N"], 0,
 "Horizontal component = 20 cos60&deg; = 20 &times; 0.50 = 10 N.")

add(MT1, "A micrometer has a zero error of +0.02 mm. A reading of 3.46 mm is taken. The true "
 "measurement is:",
 ["3.48 mm", "3.44 mm", "3.46 mm", "3.42 mm"], 1,
 "A positive zero error means readings are too high by 0.02 mm, so subtract: 3.46 &minus; 0.02 = "
 "3.44 mm.")

add(MT1, "Which of the following pairs contains only scalar quantities?",
 ["speed and energy", "velocity and force", "displacement and mass", "acceleration and power"], 0,
 "Speed and energy are both scalars. The other pairs each contain at least one vector.")

add(MT1, "The percentage uncertainties in P, Q and R are 2%, 3% and 1%. For X = PQ/R, the percentage "
 "uncertainty in X is:",
 ["0%", "2%", "6%", "5%"], 2,
 "For products and quotients, percentage uncertainties add: 2 + 3 + 1 = 6%.")

add(MT1, "A measurement is described as accurate but not precise. This means the results are:",
 ["all very close together but far from the true value",
  "scattered but their average is close to the true value",
  "all identical and correct", "affected by a large zero error"], 1,
 "Accurate = mean close to true value; not precise = large random scatter about that mean.")

add(MT1, "Which equation is homogeneous with respect to units? (s = displacement, u = initial velocity, "
 "a = acceleration, t = time)",
 ["s = ut&sup2; + at", "s = ut + &frac12;at&sup2;", "s = u + &frac12;at&sup2;",
  "s = u&sup2;t + at"], 1,
 "Only s = ut + &frac12;at&sup2; is dimensionally consistent: ut has units m, and &frac12;at&sup2; = "
 "(m s<sup>&minus;2</sup>)(s&sup2;) = m.")

add(MT1, "Two forces each of magnitude 6.0 N act at a point with an angle of 120&deg; between them. "
 "The magnitude of the resultant is:",
 ["0 N", "6.0 N", "10.4 N", "12 N"], 1,
 "R&sup2; = 6&sup2; + 6&sup2; + 2(6)(6)cos120&deg; = 36 + 36 + 72(&minus;0.5) = 36 &rArr; R = 6.0 N.")

# ===========================================================================
# TOPIC 2
# ===========================================================================
add(MT2, "A car travels 30 m north then 40 m east. Its displacement from the start is:",
 ["70 m", "50 m", "10 m", "35 m"], 1,
 "Displacement = &radic;(30&sup2; + 40&sup2;) = &radic;2500 = 50 m (the distance travelled is 70 m).")

add(MT2, "An object falls freely from rest. The distance it falls in the first 2.0 s is "
 "(g = 9.8 m s<sup>&minus;2</sup>):",
 ["9.8 m", "19.6 m", "39.2 m", "4.9 m"], 1,
 "s = &frac12;gt&sup2; = &frac12;(9.8)(2.0)&sup2; = &frac12;(9.8)(4.0) = 19.6 m.")

add(MT2, "The gradient of a displacement&ndash;time graph gives:",
 ["acceleration", "velocity", "distance", "force"], 1,
 "Rate of change of displacement with time = velocity.")

add(MT2, "A ball is thrown vertically up at 20 m s<sup>&minus;1</sup>. The time to reach its highest "
 "point is (g = 10 m s<sup>&minus;2</sup>):",
 ["1.0 s", "2.0 s", "4.0 s", "0.5 s"], 1,
 "At the top v = 0: t = (v &minus; u)/(&minus;g) = (0 &minus; 20)/(&minus;10) = 2.0 s.")

add(MT2, "The area under a velocity&ndash;time graph represents:",
 ["acceleration", "displacement", "speed", "force"], 1,
 "Velocity &times; time = displacement, which equals the area beneath the graph.")

add(MT2, "A projectile is launched at 30&deg; to the horizontal at 40 m s<sup>&minus;1</sup>. Its "
 "initial vertical velocity component is:",
 ["20 m s<sup>&minus;1</sup>", "35 m s<sup>&minus;1</sup>", "40 m s<sup>&minus;1</sup>",
  "12 m s<sup>&minus;1</sup>"], 0,
 "u<sub>y</sub> = 40 sin30&deg; = 40 &times; 0.50 = 20 m s<sup>&minus;1</sup>.")

add(MT2, "A stone dropped from a bridge takes 3.0 s to reach the water. The height of the bridge is "
 "(g = 9.8 m s<sup>&minus;2</sup>):",
 ["29 m", "44 m", "88 m", "15 m"], 1,
 "s = &frac12;gt&sup2; = &frac12;(9.8)(9.0) = 44 m.")

add(MT2, "For a body moving with uniform acceleration, which graph is a straight horizontal line?",
 ["displacement&ndash;time", "velocity&ndash;time", "acceleration&ndash;time",
  "kinetic energy&ndash;time"], 2,
 "Uniform (constant) acceleration gives a horizontal acceleration&ndash;time line; v&ndash;t is "
 "sloped and s&ndash;t is curved.")

add(MT2, "A car accelerates uniformly from 5.0 to 15 m s<sup>&minus;1</sup> in 4.0 s. Its acceleration "
 "is:",
 ["2.5 m s<sup>&minus;2</sup>", "5.0 m s<sup>&minus;2</sup>", "10 m s<sup>&minus;2</sup>",
  "1.25 m s<sup>&minus;2</sup>"], 0,
 "a = (v &minus; u)/t = (15 &minus; 5.0)/4.0 = 2.5 m s<sup>&minus;2</sup>.")

add(MT2, "A ball is projected horizontally. Ignoring air resistance, its horizontal component of "
 "velocity during flight:",
 ["increases uniformly", "decreases uniformly", "remains constant", "first increases then decreases"], 2,
 "There is no horizontal force, so the horizontal velocity stays constant; only the vertical "
 "component changes.")

add(MT2, "A car decelerates from 20 m s<sup>&minus;1</sup> to rest in 50 m. Its deceleration is:",
 ["2.0 m s<sup>&minus;2</sup>", "4.0 m s<sup>&minus;2</sup>", "8.0 m s<sup>&minus;2</sup>",
  "0.4 m s<sup>&minus;2</sup>"], 1,
 "v&sup2; = u&sup2; &minus; 2as &rArr; 0 = 400 &minus; 2a(50) &rArr; a = 400/100 = 4.0 m s<sup>&minus;2</sup>.")

add(MT2, "Two balls are released from the same height, one dropped and one thrown horizontally. "
 "Ignoring air resistance, they reach the ground:",
 ["at the same time", "the dropped one first", "the thrown one first",
  "depends on the horizontal speed"], 0,
 "Vertical motion is identical (same initial vertical velocity of zero and same g), so they land "
 "together.")

add(MT2, "The velocity&ndash;time graph of an object is a straight line with negative gradient that "
 "crosses the time axis. At the crossing point the object:",
 ["is momentarily at rest", "has maximum acceleration", "has maximum displacement",
  "reverses its acceleration"], 0,
 "Where v = 0 the object is instantaneously at rest (e.g. at the top of a throw); acceleration is "
 "constant throughout.")

add(MT2, "A body starts from rest with uniform acceleration and travels 5.0 m in the first second. "
 "In the first two seconds it travels:",
 ["10 m", "15 m", "20 m", "25 m"], 2,
 "s &prop; t&sup2; from rest: s(2 s) = 5.0 &times; (2/1)&sup2; = 5.0 &times; 4 = 20 m.")

# ===========================================================================
# TOPIC 3
# ===========================================================================
add(MT3, "A resultant force of 12 N acts on a mass of 3.0 kg. The acceleration produced is:",
 ["4.0 m s<sup>&minus;2</sup>", "36 m s<sup>&minus;2</sup>", "0.25 m s<sup>&minus;2</sup>",
  "9.0 m s<sup>&minus;2</sup>"], 0,
 "a = F/m = 12/3.0 = 4.0 m s<sup>&minus;2</sup>.")

add(MT3, "The linear momentum of a 0.50 kg ball moving at 8.0 m s<sup>&minus;1</sup> is:",
 ["4.0 kg m s<sup>&minus;1</sup>", "16 kg m s<sup>&minus;1</sup>", "0.0625 kg m s<sup>&minus;1</sup>",
  "8.5 kg m s<sup>&minus;1</sup>"], 0,
 "p = mv = 0.50 &times; 8.0 = 4.0 kg m s<sup>&minus;1</sup>.")

add(MT3, "Force is defined as the rate of change of:",
 ["velocity", "momentum", "kinetic energy", "acceleration"], 1,
 "Newton&#39;s second law: F = &Delta;p/&Delta;t, force is the rate of change of momentum.")

add(MT3, "A 1000 kg car experiences a resultant forward force of 2500 N. Its acceleration is:",
 ["0.4 m s<sup>&minus;2</sup>", "2.5 m s<sup>&minus;2</sup>", "4.0 m s<sup>&minus;2</sup>",
  "25 m s<sup>&minus;2</sup>"], 1,
 "a = F/m = 2500/1000 = 2.5 m s<sup>&minus;2</sup>.")

add(MT3, "An object of mass 2.0 kg moving at 3.0 m s<sup>&minus;1</sup> collides with and sticks to a "
 "stationary 4.0 kg object. Their common velocity is:",
 ["0.5 m s<sup>&minus;1</sup>", "1.0 m s<sup>&minus;1</sup>", "1.5 m s<sup>&minus;1</sup>",
  "2.0 m s<sup>&minus;1</sup>"], 1,
 "Momentum: 2.0&times;3.0 = (2.0+4.0)v &rArr; v = 6.0/6.0 = 1.0 m s<sup>&minus;1</sup>.")

add(MT3, "A ball hits a wall at 6.0 m s<sup>&minus;1</sup> and rebounds at 4.0 m s<sup>&minus;1</sup> "
 "along the same line. If its mass is 0.20 kg, the magnitude of its change in momentum is:",
 ["0.40 kg m s<sup>&minus;1</sup>", "2.0 kg m s<sup>&minus;1</sup>", "1.2 kg m s<sup>&minus;1</sup>",
  "0.80 kg m s<sup>&minus;1</sup>"], 1,
 "&Delta;p = m(v &minus; u) = 0.20(&minus;4.0 &minus; 6.0) = &minus;2.0; magnitude 2.0 kg m "
 "s<sup>&minus;1</sup>.")

add(MT3, "Which is a correct statement of Newton&#39;s third law?",
 ["Every action has a bigger reaction", "Forces always act in pairs on the same object",
  "If A exerts a force on B, B exerts an equal and opposite force on A",
  "The resultant force on a body equals its mass times acceleration"], 2,
 "Newton III: the paired forces are equal, opposite, of the same type, and act on different bodies.")

add(MT3, "A skydiver reaches terminal velocity when:",
 ["the drag force is zero", "the weight is zero",
  "the drag force equals the weight", "the acceleration equals g"], 2,
 "At terminal velocity the resultant force is zero, so drag = weight and velocity is constant.")

add(MT3, "An object explodes into two equal masses that fly apart. Compared with each other, the two "
 "pieces have:",
 ["equal momenta in the same direction", "equal and opposite momenta",
  "equal kinetic energies but unequal speeds", "zero total kinetic energy"], 1,
 "Initial momentum is zero, so the two momenta are equal and opposite (they sum to zero).")

add(MT3, "A constant force of 5.0 N acts on a body for 4.0 s. The impulse delivered is:",
 ["1.25 N s", "9.0 N s", "20 N s", "0.80 N s"], 2,
 "Impulse = F&Delta;t = 5.0 &times; 4.0 = 20 N s (= change in momentum).")

add(MT3, "The weight of an object of mass 5.0 kg on a planet where g = 3.7 m s<sup>&minus;2</sup> is:",
 ["1.4 N", "8.7 N", "18.5 N", "49 N"], 2,
 "W = mg = 5.0 &times; 3.7 = 18.5 N.")

add(MT3, "In an elastic collision, which quantity is NOT necessarily conserved for an individual "
 "object?",
 ["total momentum of the system", "total kinetic energy of the system",
  "the momentum of one object", "total energy of the system"], 2,
 "System momentum and (for elastic) kinetic energy are conserved, but an individual object&#39;s "
 "momentum generally changes in the collision.")

add(MT3, "A trolley of mass m moving at speed v collides elastically head-on with an identical "
 "stationary trolley. After the collision the moving trolley:",
 ["continues at speed v", "stops, and the other moves off at v",
  "rebounds at speed v", "both move off at v/2"], 1,
 "For equal masses in an elastic head-on collision the velocities are exchanged: the first stops, "
 "the second moves off at v.")

add(MT3, "A jet of water of mass flow rate 2.0 kg s<sup>&minus;1</sup> hits a wall at "
 "10 m s<sup>&minus;1</sup> and stops. The force on the wall is:",
 ["5.0 N", "20 N", "0.20 N", "100 N"], 1,
 "F = (mass/s)&times;&Delta;v = 2.0 &times; 10 = 20 N.")

add(MT3, "The area under a force&ndash;time graph gives:",
 ["work done", "power", "impulse", "kinetic energy"], 2,
 "&#8747;F dt = impulse = change of momentum.")

add(MT3, "A body of mass 4.0 kg on a rough surface is pulled by a 20 N force but a 8.0 N friction "
 "force opposes it. Its acceleration is:",
 ["7.0 m s<sup>&minus;2</sup>", "3.0 m s<sup>&minus;2</sup>", "5.0 m s<sup>&minus;2</sup>",
  "2.0 m s<sup>&minus;2</sup>"], 1,
 "Resultant = 20 &minus; 8.0 = 12 N; a = 12/4.0 = 3.0 m s<sup>&minus;2</sup>.")

# ===========================================================================
# TOPIC 4
# ===========================================================================
add(MT4, "The moment of a 15 N force acting at a perpendicular distance of 0.40 m from a pivot is:",
 ["6.0 N m", "37.5 N m", "0.027 N m", "15.4 N m"], 0,
 "Moment = F &times; d = 15 &times; 0.40 = 6.0 N m.")

add(MT4, "A couple consists of:",
 ["a single force through the centre of mass",
  "two equal forces in the same direction",
  "two equal, opposite, parallel forces not in line",
  "two unequal forces at right angles"], 2,
 "A couple is a pair of equal, opposite, parallel forces whose lines of action do not coincide, "
 "producing rotation only.")

add(MT4, "The pressure at a depth of 5.0 m in water (density 1000 kg m<sup>&minus;3</sup>) due to the "
 "water alone is (g = 9.8 m s<sup>&minus;2</sup>):",
 ["4.9 &times; 10<sup>3</sup> Pa", "4.9 &times; 10<sup>4</sup> Pa", "5.0 &times; 10<sup>5</sup> Pa",
  "9.8 &times; 10<sup>3</sup> Pa"], 1,
 "&Delta;p = &rho;gh = 1000 &times; 9.8 &times; 5.0 = 4.9 &times; 10<sup>4</sup> Pa.")

add(MT4, "The density of an object of mass 240 g and volume 30 cm&sup3; is:",
 ["8.0 g cm<sup>&minus;3</sup>", "0.125 g cm<sup>&minus;3</sup>", "7200 kg m<sup>&minus;3</sup>",
  "both A and its SI equivalent 8000 kg m<sup>&minus;3</sup>"], 3,
 "&rho; = m/V = 240/30 = 8.0 g cm<sup>&minus;3</sup> = 8000 kg m<sup>&minus;3</sup>.")

add(MT4, "A uniform beam is in equilibrium. This requires that:",
 ["the resultant force is zero only", "the resultant moment is zero only",
  "both the resultant force and the resultant moment are zero",
  "all forces act through one point"], 2,
 "Equilibrium requires zero resultant force AND zero resultant torque.")

add(MT4, "The upthrust on a body fully immersed in a fluid equals the:",
 ["weight of the body", "weight of fluid displaced", "volume of the body",
  "density of the fluid"], 1,
 "Archimedes&#39; principle: upthrust = weight of fluid displaced (= &rho;gV).")

add(MT4, "A 2.0 m uniform plank of weight 60 N is pivoted at its centre. A 40 N weight hangs 0.30 m "
 "from the pivot. To balance it, a 30 N weight must hang on the other side at a distance of:",
 ["0.20 m", "0.40 m", "0.60 m", "0.90 m"], 1,
 "Moments balance: 40 &times; 0.30 = 30 &times; d &rArr; d = 12/30 = 0.40 m.")

add(MT4, "A hydraulic system has pistons of area 4.0 cm&sup2; and 20 cm&sup2;. A force of 30 N on the "
 "small piston produces a force on the large piston of:",
 ["6.0 N", "30 N", "150 N", "600 N"], 2,
 "Equal pressure: F<sub>2</sub> = F<sub>1</sub>(A<sub>2</sub>/A<sub>1</sub>) = 30 &times; 20/4.0 = "
 "150 N.")

add(MT4, "An object floats with 80% of its volume submerged in water (1000 kg m<sup>&minus;3</sup>). "
 "Its density is:",
 ["200 kg m<sup>&minus;3</sup>", "800 kg m<sup>&minus;3</sup>", "1000 kg m<sup>&minus;3</sup>",
  "1250 kg m<sup>&minus;3</sup>"], 1,
 "Fraction submerged = &rho;<sub>object</sub>/&rho;<sub>fluid</sub> &rArr; &rho; = 0.80 &times; 1000 = "
 "800 kg m<sup>&minus;3</sup>.")

add(MT4, "The centre of gravity of a body is the point where:",
 ["the mass is greatest", "all the weight may be taken to act",
  "the density is uniform", "the body is most stable"], 1,
 "The centre of gravity is the single point at which the entire weight can be considered to act.")

add(MT4, "The torque of a couple made of two 12 N forces acting 0.25 m apart is:",
 ["1.5 N m", "3.0 N m", "6.0 N m", "48 N m"], 1,
 "Torque of a couple = F &times; separation = 12 &times; 0.25 = 3.0 N m.")

add(MT4, "The SI base units of density are:",
 ["kg m<sup>&minus;3</sup>", "kg m<sup>3</sup>", "g cm<sup>&minus;3</sup>",
  "kg m<sup>&minus;2</sup>"], 0,
 "Density = mass/volume = kg m<sup>&minus;3</sup> in SI base units.")

add(MT4, "A manometer shows a height difference of 8.0 cm of mercury (density 1.36 &times; "
 "10<sup>4</sup> kg m<sup>&minus;3</sup>). The pressure difference is about:",
 ["1.1 &times; 10<sup>4</sup> Pa", "1.1 &times; 10<sup>3</sup> Pa", "1.1 &times; 10<sup>5</sup> Pa",
  "8.0 &times; 10<sup>3</sup> Pa"], 0,
 "&Delta;p = &rho;gh = 1.36&times;10<sup>4</sup> &times; 9.81 &times; 0.080 = 1.07&times;10<sup>4</sup> Pa.")

add(MT4, "A ball of weight 6.0 N is held in water by a string; the upthrust is 2.5 N. The tension in "
 "the string is:",
 ["8.5 N", "3.5 N", "6.0 N", "2.5 N"], 1,
 "Equilibrium: tension + upthrust = weight &rArr; T = 6.0 &minus; 2.5 = 3.5 N.")

# ===========================================================================
# TOPIC 5
# ===========================================================================
add(MT5, "A force of 25 N moves an object 4.0 m in the direction of the force. The work done is:",
 ["6.25 J", "29 J", "100 J", "21 J"], 2,
 "W = Fs = 25 &times; 4.0 = 100 J.")

add(MT5, "A 2.0 kg object moves at 6.0 m s<sup>&minus;1</sup>. Its kinetic energy is:",
 ["12 J", "36 J", "72 J", "6.0 J"], 1,
 "E<sub>K</sub> = &frac12;mv&sup2; = &frac12;(2.0)(36) = 36 J.")

add(MT5, "Power is defined as:",
 ["force times distance", "work done per unit time", "energy times time",
  "force per unit area"], 1,
 "Power = work done (or energy transferred) per unit time.")

add(MT5, "A load of mass 3.0 kg is raised 2.0 m. The gain in gravitational PE is (g = 9.8 m "
 "s<sup>&minus;2</sup>):",
 ["6.0 J", "29 J", "59 J", "15 J"], 2,
 "&Delta;E<sub>P</sub> = mg&Delta;h = 3.0 &times; 9.8 &times; 2.0 = 58.8 &asymp; 59 J.")

add(MT5, "A machine has an efficiency of 40%. If the input energy is 500 J, the useful output is:",
 ["125 J", "200 J", "300 J", "1250 J"], 1,
 "Useful output = 0.40 &times; 500 = 200 J.")

add(MT5, "A car engine delivers a driving force of 800 N at a constant speed of 25 m s<sup>&minus;1</sup>. "
 "The output power is:",
 ["32 W", "20 kW", "0.032 kW", "825 W"], 1,
 "P = Fv = 800 &times; 25 = 20 000 W = 20 kW.")

add(MT5, "A ball falls freely from rest. When it has fallen half of its total drop height, its speed "
 "is what fraction of its final speed?",
 ["1/2", "1/&radic;2", "1/4", "&radic;2"], 1,
 "v &prop; &radic;h, so at half the height v = &radic;(1/2) &times; v<sub>final</sub> = "
 "v<sub>final</sub>/&radic;2.")

add(MT5, "A 60 W lamp is left on for 5.0 minutes. The energy transferred is:",
 ["300 J", "1.8 &times; 10<sup>4</sup> J", "12 J", "3.0 &times; 10<sup>2</sup> J"], 1,
 "E = Pt = 60 &times; (5.0 &times; 60) = 60 &times; 300 = 1.8 &times; 10<sup>4</sup> J.")

add(MT5, "A pendulum bob is released from a height of 0.20 m. Ignoring resistance, its speed at the "
 "lowest point is (g = 9.8 m s<sup>&minus;2</sup>):",
 ["1.4 m s<sup>&minus;1</sup>", "2.0 m s<sup>&minus;1</sup>", "3.9 m s<sup>&minus;1</sup>",
  "4.0 m s<sup>&minus;1</sup>"], 1,
 "v = &radic;(2gh) = &radic;(2 &times; 9.8 &times; 0.20) = &radic;3.92 = 1.98 &asymp; 2.0 m "
 "s<sup>&minus;1</sup>.")

add(MT5, "Which statement about a body raised at constant velocity is correct?",
 ["Its kinetic energy increases", "Its potential energy increases",
  "No work is done on it", "Its total energy is constant"], 1,
 "At constant velocity KE is unchanged; the work done against gravity increases the gravitational PE.")

add(MT5, "The efficiency of a system is defined as:",
 ["total energy input / useful output", "useful energy output / total energy input",
  "power output &times; time", "energy output &minus; energy input"], 1,
 "Efficiency = useful energy (or power) output &divide; total energy (or power) input.")

add(MT5, "A crane lifts a 500 kg load at a steady 0.40 m s<sup>&minus;1</sup>. The useful power is "
 "(g = 9.8 m s<sup>&minus;2</sup>):",
 ["200 W", "980 W", "1960 W", "1250 W"], 2,
 "P = Fv = mgv = 500 &times; 9.8 &times; 0.40 = 1960 W.")

add(MT5, "A 0.10 kg ball dropped from 2.0 m rebounds to 1.4 m. The energy lost in the bounce is "
 "(g = 9.8 m s<sup>&minus;2</sup>):",
 ["0.59 J", "1.4 J", "2.0 J", "0.20 J"], 0,
 "Loss = mg&Delta;h = 0.10 &times; 9.8 &times; (2.0 &minus; 1.4) = 0.10 &times; 9.8 &times; 0.6 = "
 "0.59 J.")

add(MT5, "The derivation P = Fv applies to a body moving:",
 ["with increasing acceleration", "at constant velocity with force along the motion",
  "in a circle", "against no force"], 1,
 "P = W/t = Fs/t = Fv when the force acts along the direction of motion (constant v assumed for the "
 "simple derivation).")

add(MT5, "A spring stores 8.0 J of elastic PE when compressed by 0.10 m. Its spring constant is:",
 ["80 N m<sup>&minus;1</sup>", "800 N m<sup>&minus;1</sup>", "1600 N m<sup>&minus;1</sup>",
  "160 N m<sup>&minus;1</sup>"], 2,
 "E = &frac12;kx&sup2; &rArr; k = 2E/x&sup2; = 2(8.0)/(0.10)&sup2; = 16/0.01 = 1600 N m<sup>&minus;1</sup>.")

# ===========================================================================
# TOPIC 6
# ===========================================================================
add(MT6, "Hooke&#39;s law states that, up to the limit of proportionality, the extension of a spring "
 "is:",
 ["inversely proportional to the load", "proportional to the load",
  "proportional to the square of the load", "independent of the load"], 1,
 "F = kx: extension is directly proportional to the applied force up to the limit of proportionality.")

add(MT6, "A spring extends 5.0 cm under a load of 10 N. Its spring constant is:",
 ["2.0 N m<sup>&minus;1</sup>", "50 N m<sup>&minus;1</sup>", "200 N m<sup>&minus;1</sup>",
  "0.50 N m<sup>&minus;1</sup>"], 2,
 "k = F/x = 10/0.050 = 200 N m<sup>&minus;1</sup>.")

add(MT6, "The Young modulus is defined as:",
 ["stress &times; strain", "stress / strain", "strain / stress", "force / extension"], 1,
 "E = stress/strain (the gradient of the linear region of a stress&ndash;strain graph).")

add(MT6, "Strain has:",
 ["the unit pascal", "the unit metre", "no unit", "the unit newton"], 2,
 "Strain = extension/original length, a ratio of two lengths, so it has no unit.")

add(MT6, "A wire of cross-sectional area 2.0 &times; 10<sup>&minus;7</sup> m&sup2; carries a tension of "
 "40 N. The stress is:",
 ["2.0 &times; 10<sup>8</sup> Pa", "8.0 &times; 10<sup>&minus;6</sup> Pa", "20 Pa",
  "2.0 &times; 10<sup>7</sup> Pa"], 0,
 "Stress = F/A = 40/2.0&times;10<sup>&minus;7</sup> = 2.0 &times; 10<sup>8</sup> Pa.")

add(MT6, "The elastic potential energy stored in a spring of constant k extended by x is:",
 ["kx", "&frac12;kx", "&frac12;kx&sup2;", "kx&sup2;"], 2,
 "E<sub>P</sub> = &frac12;kx&sup2; = &frac12;Fx (area under the force&ndash;extension line).")

add(MT6, "Beyond the elastic limit, a material:",
 ["obeys Hooke&#39;s law", "returns fully to its original length when unloaded",
  "does not return to its original length when unloaded", "has zero stress"], 2,
 "Beyond the elastic limit the deformation is plastic (permanent), so the material keeps some "
 "extension after unloading.")

add(MT6, "The area under a force&ndash;extension graph represents:",
 ["the spring constant", "the stress", "the work done in stretching", "the strain"], 2,
 "Area under F&ndash;x = work done (elastic PE stored if within the limit of proportionality).")

add(MT6, "A load of 12 N stretches a wire by 0.60 mm. The energy stored (assuming Hooke&#39;s law) is:",
 ["7.2 &times; 10<sup>&minus;3</sup> J", "3.6 &times; 10<sup>&minus;3</sup> J",
  "7.2 J", "3.6 J"], 1,
 "E = &frac12;Fx = &frac12; &times; 12 &times; 0.60&times;10<sup>&minus;3</sup> = 3.6 &times; "
 "10<sup>&minus;3</sup> J.")

add(MT6, "Two identical springs of constant k are joined end to end (in series). The combined spring "
 "constant is:",
 ["2k", "k", "k/2", "4k"], 2,
 "Series: 1/k<sub>eff</sub> = 1/k + 1/k = 2/k &rArr; k<sub>eff</sub> = k/2 (softer, extends more).")

add(MT6, "The gradient of the linear part of a stress&ndash;strain graph gives the:",
 ["spring constant", "Young modulus", "ultimate tensile stress", "elastic limit"], 1,
 "Stress/strain in the linear region = the Young modulus.")

add(MT6, "A steel wire and a copper wire have the same dimensions and carry the same load. Steel has "
 "the larger Young modulus, so the steel wire has the:",
 ["larger extension", "smaller extension", "same extension", "larger stress"], 1,
 "Same stress (same load and area); extension = (stress/E)L, so the larger E (steel) gives the "
 "smaller extension.")

add(MT6, "A material that undergoes large plastic deformation before breaking is described as:",
 ["brittle", "ductile", "elastic", "stiff"], 1,
 "Ductile materials (e.g. copper) can be drawn out with much plastic deformation before fracture; "
 "brittle ones break with little plastic deformation.")
