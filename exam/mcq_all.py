# -*- coding: utf-8 -*-
"""100 extreme-difficulty multiple-choice questions, AS 9702 topics 1-11.
add(topic, q, options[list of 4], correct index 0-3, ans, svg='')."""
from engine import mcq as M

def add(topic, q, options, correct, ans, svg=""):
    M.append({"topic": topic, "q": q, "options": options, "correct": correct,
              "ans": ans, "svg": svg})

MT1  = "1&nbsp;&nbsp;Physical quantities and units"
MT2  = "2&nbsp;&nbsp;Kinematics"
MT3  = "3&nbsp;&nbsp;Dynamics"
MT4  = "4&nbsp;&nbsp;Forces, density and pressure"
MT5  = "5&nbsp;&nbsp;Work, energy and power"
MT6  = "6&nbsp;&nbsp;Deformation of solids"
MT7  = "7&nbsp;&nbsp;Waves"
MT8  = "8&nbsp;&nbsp;Superposition"
MT9  = "9&nbsp;&nbsp;Electricity"
MT10 = "10&nbsp;&nbsp;D.C. circuits"
MT11 = "11&nbsp;&nbsp;Particle physics"

# ===========================================================================
# TOPIC 1  (10)
# ===========================================================================
add(MT1,
 "The power P dissipated in a resistor is P = kI<sup>a</sup>R<sup>b</sup>, where I is current and R "
 "is resistance. For the equation to be homogeneous, a and b are:",
 ["a = 1, b = 1", "a = 2, b = 1", "a = 2, b = 2", "a = 1, b = 2"], 1,
 "Power = kg m&sup2; s<sup>&minus;3</sup>; R has units kg m&sup2; s<sup>&minus;3</sup> A<sup>&minus;2</sup>. "
 "For the amperes to cancel, A<sup>a&minus;2b</sup> = A<sup>0</sup> &rArr; a = 2b; matching gives "
 "b = 1, a = 2. This is P = I&sup2;R.")

add(MT1,
 "A quantity is calculated from Y = p&sup2;q / &radic;r. The percentage uncertainties are p: 2%, "
 "q: 3%, r: 8%. The percentage uncertainty in Y is:",
 ["9%", "11%", "13%", "17%"], 1,
 "Add percentage uncertainties, each &times; its power: p&sup2; &rarr; 2(2%) = 4%; q &rarr; 3%; "
 "&radic;r = r<sup>1/2</sup> &rarr; &frac12;(8%) = 4%. Total = 4 + 3 + 4 = 11%.")

add(MT1,
 "Which of the following is a set of three vector quantities only?",
 ["mass, velocity, force", "displacement, acceleration, momentum",
  "work, power, energy", "velocity, speed, weight"], 1,
 "Vectors have magnitude and direction. Displacement, acceleration and momentum are all vectors. "
 "The others contain scalars (mass, work, power, energy, speed).")

add(MT1,
 "The Young modulus has SI base units:",
 ["kg m s<sup>&minus;2</sup>", "kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>",
  "kg m<sup>2</sup> s<sup>&minus;2</sup>", "kg m<sup>&minus;2</sup> s<sup>&minus;1</sup>"], 1,
 "Young modulus = stress/strain = pressure (strain is dimensionless). Pressure = force/area = "
 "(kg m s<sup>&minus;2</sup>)/m&sup2; = kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>.")

add(MT1,
 "A micrometer has a zero error of &minus;0.03 mm (it reads &minus;0.03 mm when closed). A wire "
 "measured with it gives a reading of 0.42 mm. The true diameter is:",
 ["0.39 mm", "0.42 mm", "0.45 mm", "0.48 mm"], 2,
 "A reading of &minus;0.03 when closed means all readings are 0.03 mm too small, so the correction is "
 "to add 0.03: true = 0.42 + 0.03 = 0.45 mm. (True = reading &minus; zero error = 0.42 &minus; (&minus;0.03).)")

add(MT1,
 "Which estimate is closest to the order of magnitude of the kinetic energy of a 60 kg sprinter "
 "running at 10 m s<sup>&minus;1</sup>?",
 ["3 &times; 10<sup>2</sup> J", "3 &times; 10<sup>3</sup> J",
  "3 &times; 10<sup>4</sup> J", "3 &times; 10<sup>5</sup> J"], 1,
 "E<sub>K</sub> = &frac12;mv&sup2; = &frac12; &times; 60 &times; 100 = 3000 J = 3 &times; 10<sup>3</sup> J.")

add(MT1,
 "Two forces of 7.0 N and 4.0 N act at a point. Which value could NOT be the magnitude of their "
 "resultant?",
 ["3.0 N", "7.0 N", "11.0 N", "2.0 N"], 3,
 "The resultant of two forces lies between |7&minus;4| = 3 N and 7+4 = 11 N inclusive. A value of "
 "2.0 N is below the minimum of 3.0 N, so it is impossible.")

add(MT1,
 "A student states a result as (4.0 &plusmn; 0.2) &times; 10<sup>3</sup> and another quantity as "
 "(2.00 &plusmn; 0.05) &times; 10<sup>2</sup>. The percentage uncertainty in their product is "
 "closest to:",
 ["2.5%", "5.0%", "7.5%", "10%"], 2,
 "First: 0.2/4.0 = 5.0%. Second: 0.05/2.00 = 2.5%. Product &rArr; add: 5.0 + 2.5 = 7.5%.")

add(MT1,
 "Which pair of quantities has the same SI base units?",
 ["energy and power", "pressure and stress", "momentum and force",
  "density and pressure"], 1,
 "Pressure and stress are both force/area (kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>). "
 "The other pairs differ (e.g. momentum kg m s<sup>&minus;1</sup> vs force kg m s<sup>&minus;2</sup>).")

add(MT1,
 "The equation for the speed of a wave on a string is v = &radic;(T/&micro;), where T is tension. "
 "For homogeneity, the base units of &micro; must be:",
 ["kg m<sup>&minus;1</sup>", "kg m", "kg s<sup>&minus;1</sup>", "kg m<sup>&minus;2</sup>"], 0,
 "v&sup2; = T/&micro; &rArr; &micro; = T/v&sup2; = (kg m s<sup>&minus;2</sup>)/(m s<sup>&minus;1</sup>)&sup2; "
 "= (kg m s<sup>&minus;2</sup>)/(m&sup2; s<sup>&minus;2</sup>) = kg m<sup>&minus;1</sup>. "
 "(&micro; is mass per unit length.)")

# ===========================================================================
# TOPIC 2  (10)
# ===========================================================================
add(MT2,
 "A ball is thrown vertically up and returns to the thrower. Taking up as positive, which graph best "
 "describes its acceleration against time during the whole flight (ignoring air resistance)?",
 ["a positive constant then negative constant", "a constant negative value throughout",
  "zero at the top, negative elsewhere", "a straight line decreasing through zero"], 1,
 "Throughout the flight the only force is gravity, so a = &minus;g (constant negative) at all times, "
 "including at the highest point where the velocity (not the acceleration) is zero.")

add(MT2,
 "A car accelerates uniformly from rest. In the first second it travels distance d. The distance it "
 "travels in the third second is:",
 ["3d", "5d", "7d", "9d"], 2,
 "For uniform acceleration from rest, distance in the n-th second &prop; (2n&minus;1). "
 "1st second: 1 unit = d. 3rd second: 2(3)&minus;1 = 5 units = 5d. "
 "(Total in 3 s = 9 units; in 2 s = 4 units; difference = 5.)")

add(MT2,
 "A projectile is launched at 30&deg; to the horizontal with speed u. At the highest point of its "
 "path, its speed is:",
 ["0", "u sin30&deg;", "u cos30&deg;", "u"], 2,
 "At the top the vertical component is zero; only the horizontal component u cos30&deg; remains, so "
 "the speed there is u cos30&deg;.")

add(MT2,
 "The displacement&ndash;time graph of an object is a curve that becomes steeper with time. This "
 "represents:",
 ["constant velocity", "increasing velocity (acceleration)",
  "decreasing velocity", "the object at rest"], 1,
 "The gradient of a displacement&ndash;time graph is the velocity. A curve getting steeper means an "
 "increasing gradient, i.e. increasing velocity &mdash; the object is accelerating.")

add(MT2,
 "Two stones are dropped from a cliff, the second 1.0 s after the first. As they fall (no air "
 "resistance), the vertical distance between them:",
 ["stays constant", "increases", "decreases", "first increases then decreases"], 1,
 "Both accelerate at g, so their velocities differ by a constant g&times;1.0 s = 9.81 m s<sup>&minus;1</sup>. "
 "Since the first is always moving faster, the gap between them increases with time.")

add(MT2,
 "A ball falls from rest and passes a window 1.5 m tall in 0.20 s. Approximately how far above the "
 "top of the window was it released? (g = 9.8 m s<sup>&minus;2</sup>)",
 ["1.5 m", "2.0 m", "2.5 m", "3.0 m"], 2,
 "Average speed past window = 1.5/0.20 = 7.5 m s<sup>&minus;1</sup> = speed at mid-window. "
 "Speed at top &asymp; 7.5 &minus; 9.8&times;0.10 = 6.52 m s<sup>&minus;1</sup>. "
 "Fall distance to top = v&sup2;/2g = 6.52&sup2;/19.6 = 2.17 &asymp; 2.5 m (nearest option).")

add(MT2,
 "An object moves with constant velocity in the x-direction and constant acceleration in the "
 "y-direction (starting with zero y-velocity). Its path is:",
 ["a straight line", "a circle", "a parabola", "a hyperbola"], 2,
 "x &prop; t and y &prop; t&sup2;, so y &prop; x&sup2; &mdash; a parabola. This is projectile-type "
 "motion.")

add(MT2,
 "A car travels 40 m at 20 m s<sup>&minus;1</sup> then 40 m at 40 m s<sup>&minus;1</sup>. Its average "
 "speed over the 80 m is:",
 ["24 m s<sup>&minus;1</sup>", "26.7 m s<sup>&minus;1</sup>", "30 m s<sup>&minus;1</sup>",
  "33.3 m s<sup>&minus;1</sup>"], 1,
 "Times: 40/20 = 2.0 s and 40/40 = 1.0 s; total 3.0 s for 80 m. "
 "Average = 80/3.0 = 26.7 m s<sup>&minus;1</sup> (not the arithmetic mean 30).")

add(MT2,
 "A velocity&ndash;time graph is a straight line from (0 s, 8 m s<sup>&minus;1</sup>) to "
 "(4 s, 0 m s<sup>&minus;1</sup>), then continues as a straight line to (6 s, &minus;6 m s<sup>&minus;1</sup>). "
 "The total distance travelled (not displacement) in 6 s is:",
 ["10 m", "16 m", "22 m", "6 m"], 2,
 "Distance = total area magnitude. 0&ndash;4 s: &frac12;(4)(8) = 16 m forward. 4&ndash;6 s: "
 "&frac12;(2)(6) = 6 m (backward, but distance counts magnitude). Total distance = 16 + 6 = 22 m.")

add(MT2,
 "A stone thrown horizontally from a height h lands a horizontal distance R away. If it were thrown "
 "horizontally at twice the speed from the same height, the horizontal distance would be:",
 ["R", "&radic;2 R", "2R", "4R"], 2,
 "Time to fall depends only on h (same), t = &radic;(2h/g). Horizontal distance = speed &times; t, so "
 "doubling the speed doubles R.")

# ===========================================================================
# TOPIC 3  (12)
# ===========================================================================
add(MT3,
 "A 2.0 kg body moving at 3.0 m s<sup>&minus;1</sup> east experiences a constant force and, 4.0 s "
 "later, moves at 3.0 m s<sup>&minus;1</sup> west. The magnitude of the average force is:",
 ["0 N", "1.5 N", "3.0 N", "6.0 N"], 2,
 "Change in momentum = m&Delta;v = 2.0(&minus;3.0 &minus; 3.0) = &minus;12 kg m s<sup>&minus;1</sup> "
 "(magnitude 12). Force = &Delta;p/&Delta;t = 12/4.0 = 3.0 N.")

add(MT3,
 "A ball of mass m hits the ground vertically at speed v and rebounds at speed v. The magnitude of "
 "the impulse on the ball is:",
 ["0", "mv", "2mv", "mv&sup2;"], 2,
 "Taking up as positive: impulse = &Delta;p = m(v) &minus; m(&minus;v) = 2mv. The momentum reverses, "
 "so the change is twice the initial magnitude.")

add(MT3,
 "Two trolleys, masses m and 2m, moving towards each other at the same speed v, collide and stick "
 "together. Their common velocity has magnitude:",
 ["0", "v/3", "v/2", "2v/3"], 1,
 "Take the 2m direction as positive: total momentum = 2m(v) + m(&minus;v) = mv. "
 "Combined mass 3m: velocity = mv/3m = v/3 (in the direction of the heavier trolley).")

add(MT3,
 "A resultant force&ndash;time graph for an object is a triangle: rising from 0 to F<sub>0</sub> over "
 "time &tau; then falling to 0 over the next &tau;. The change in momentum is:",
 ["F<sub>0</sub>&tau;", "&frac12;F<sub>0</sub>&tau;", "2F<sub>0</sub>&tau;",
  "F<sub>0</sub>&tau;/4"], 0,
 "Impulse = area under F&ndash;t graph = area of triangle = &frac12; &times; base &times; height = "
 "&frac12; &times; (2&tau;) &times; F<sub>0</sub> = F<sub>0</sub>&tau;.")

add(MT3,
 "An object falls through air and reaches terminal velocity. At terminal velocity:",
 ["the drag force is zero", "the weight is zero",
  "the resultant force is zero", "the acceleration equals g"], 2,
 "At terminal velocity the (upward) drag has grown equal to the (downward) weight, so the resultant "
 "force &mdash; and hence the acceleration &mdash; is zero; the object moves at constant velocity.")

add(MT3,
 "A 0.20 kg ball moving at 5.0 m s<sup>&minus;1</sup> is struck and moves off at 5.0 m s<sup>&minus;1</sup> "
 "at 90&deg; to its original direction. The magnitude of the change in momentum is:",
 ["0", "1.0 kg m s<sup>&minus;1</sup>", "1.41 kg m s<sup>&minus;1</sup>",
  "2.0 kg m s<sup>&minus;1</sup>"], 2,
 "Momentum vectors before and after are perpendicular, each of magnitude 0.20&times;5.0 = 1.0. "
 "&Delta;p = &radic;(1.0&sup2; + 1.0&sup2;) = &radic;2 = 1.41 kg m s<sup>&minus;1</sup>.")

add(MT3,
 "In an elastic collision between two equal masses, one initially at rest, the moving mass:",
 ["stops and the other moves off with its velocity",
  "continues with the same velocity", "reverses direction",
  "and the target move off together"], 0,
 "For equal masses in a 1-D elastic collision with one at rest, the velocities are exchanged: the "
 "incoming mass stops and the target moves off with the incoming velocity (as with Newton's cradle).")

add(MT3,
 "A rocket ejects 50 kg of gas per second at 800 m s<sup>&minus;1</sup> relative to the rocket. The "
 "thrust is:",
 ["1.6 &times; 10<sup>1</sup> N", "4.0 &times; 10<sup>4</sup> N",
  "4.0 &times; 10<sup>3</sup> N", "6.4 &times; 10<sup>5</sup> N"], 1,
 "Thrust = rate of change of momentum of exhaust = (dm/dt)v = 50 &times; 800 = 4.0 &times; 10<sup>4</sup> N.")

add(MT3,
 "A body of constant mass has a momentum&ndash;time graph that is a straight line of positive "
 "gradient. This tells us that:",
 ["the velocity is constant", "the resultant force is constant and non-zero",
  "the body is in equilibrium", "the acceleration is zero"], 1,
 "The gradient of a momentum&ndash;time graph is the resultant force (F = dp/dt). A constant positive "
 "gradient means a constant non-zero force, hence constant acceleration.")

add(MT3,
 "A person of weight W stands in a lift accelerating downward at a. The reading on scales beneath "
 "them is:",
 ["W(1 + a/g)", "W(1 &minus; a/g)", "W", "Wa/g"], 1,
 "N = m(g &minus; a) = mg(1 &minus; a/g) = W(1 &minus; a/g). Downward acceleration reduces the "
 "apparent weight.")

add(MT3,
 "Two objects interact. Which statement is always true, whatever the type of collision?",
 ["kinetic energy is conserved", "total momentum is conserved",
  "the objects have equal speeds afterwards", "the total kinetic energy increases"], 1,
 "Momentum is conserved in all collisions (no external resultant force). Kinetic energy is conserved "
 "only in elastic collisions; it is not generally conserved.")

add(MT3,
 "A trolley of mass 1.0 kg moving at 4.0 m s<sup>&minus;1</sup> collides with a stationary 3.0 kg "
 "trolley and they move off together. The fraction of the original kinetic energy that is lost is:",
 ["1/4", "1/2", "3/4", "0"], 2,
 "Common velocity = 1.0(4.0)/4.0 = 1.0 m s<sup>&minus;1</sup>. KE before = &frac12;(1.0)(16) = 8.0 J; "
 "after = &frac12;(4.0)(1.0)&sup2; = 2.0 J. Lost = 6.0 J = 3/4 of 8.0 J.")


# ===========================================================================
# TOPIC 4  (8)
# ===========================================================================
add(MT4,
 "A uniform metre rule is pivoted at its centre. A 2.0 N weight hangs at the 20 cm mark. To balance "
 "it, a 4.0 N weight must hang at the:",
 ["65 cm mark", "70 cm mark", "80 cm mark", "90 cm mark"], 0,
 "The 2.0 N weight is 30 cm from the pivot (50&minus;20): moment = 2.0&times;0.30 = 0.60 N m. "
 "For balance 4.0 &times; d = 0.60 &rArr; d = 0.15 m = 15 cm from centre, i.e. the 65 cm mark.")

add(MT4,
 "The pressure at a depth of 20 m in seawater (density 1030 kg m<sup>&minus;3</sup>) due to the water "
 "alone is approximately:",
 ["2.0 &times; 10<sup>4</sup> Pa", "1.0 &times; 10<sup>5</sup> Pa",
  "2.0 &times; 10<sup>5</sup> Pa", "2.0 &times; 10<sup>6</sup> Pa"], 2,
 "&Delta;p = &rho;g&Delta;h = 1030 &times; 9.81 &times; 20 &asymp; 2.02 &times; 10<sup>5</sup> Pa.")

add(MT4,
 "A couple consists of two forces of 6.0 N separated by 0.25 m. Its torque is:",
 ["0.75 N m", "1.5 N m", "3.0 N m", "0 N m"], 1,
 "Torque of a couple = one force &times; separation = 6.0 &times; 0.25 = 1.5 N m. (The two forces are "
 "equal and opposite, so the resultant force is zero, but the torque is not.)")

add(MT4,
 "A block floats in water with 80% of its volume submerged. Its density is:",
 ["200 kg m<sup>&minus;3</sup>", "800 kg m<sup>&minus;3</sup>",
  "1000 kg m<sup>&minus;3</sup>", "1250 kg m<sup>&minus;3</sup>"], 1,
 "Floating: weight = upthrust &rArr; &rho;<sub>block</sub>Vg = &rho;<sub>water</sub>(0.80V)g &rArr; "
 "&rho;<sub>block</sub> = 0.80 &times; 1000 = 800 kg m<sup>&minus;3</sup>.")

add(MT4,
 "A ladder rests against a smooth wall on rough ground. The frictional force at the ground acts:",
 ["vertically up", "vertically down", "horizontally towards the wall",
  "horizontally away from the wall"], 2,
 "The smooth wall pushes the ladder horizontally away from it; for horizontal equilibrium friction at "
 "the base must act horizontally towards the wall.")

add(MT4,
 "An object of volume V and density &rho;<sub>o</sub> is fully immersed in a fluid of density "
 "&rho;<sub>f</sub> (with &rho;<sub>o</sub> &gt; &rho;<sub>f</sub>). The apparent weight (true weight "
 "minus upthrust) is:",
 ["&rho;<sub>f</sub>Vg", "(&rho;<sub>o</sub> &minus; &rho;<sub>f</sub>)Vg",
  "(&rho;<sub>o</sub> + &rho;<sub>f</sub>)Vg", "&rho;<sub>o</sub>Vg"], 1,
 "True weight = &rho;<sub>o</sub>Vg; upthrust = &rho;<sub>f</sub>Vg. "
 "Apparent weight = (&rho;<sub>o</sub> &minus; &rho;<sub>f</sub>)Vg.")

add(MT4,
 "Three forces act on a body in equilibrium. When drawn head-to-tail they must:",
 ["all be parallel", "form a closed triangle", "form a right angle",
  "have equal magnitudes"], 1,
 "For equilibrium the vector sum is zero, so three forces drawn head-to-tail form a closed triangle.")

add(MT4,
 "A non-uniform beam of weight 200 N rests on two supports 3.0 m apart, one at each end. The left "
 "support reads 120 N and the right support reads 80 N. The distance of the centre of gravity from "
 "the left support is:",
 ["1.0 m", "1.2 m", "1.5 m", "1.8 m"], 1,
 "Taking moments about the left support, the weight (200 N acting at distance d) is balanced by the "
 "right reaction (80 N at 3.0 m): 200 &times; d = 80 &times; 3.0 &rArr; d = 240/200 = 1.2 m. The "
 "centre of gravity lies nearer the more heavily loaded left support, as expected.")

# ===========================================================================
# TOPIC 5  (9)
# ===========================================================================
add(MT5,
 "A 2.0 kg object is raised 5.0 m and also given a speed of 4.0 m s<sup>&minus;1</sup>. The total "
 "energy supplied (no losses) is:",
 ["16 J", "98 J", "114 J", "196 J"], 2,
 "&Delta;PE = mgh = 2.0&times;9.81&times;5.0 = 98.1 J; &Delta;KE = &frac12;(2.0)(4.0)&sup2; = 16 J. "
 "Total = 98.1 + 16 = 114 J.")

add(MT5,
 "A car of power output P travels at constant speed v against a resistive force F. Which is correct?",
 ["P = Fv", "P = F/v", "P = Fv&sup2;", "P = &frac12;Fv"], 0,
 "At constant speed the driving force equals F; power = force &times; velocity = Fv.")

add(MT5,
 "The braking distance of a car on a level road is 20 m at 15 m s<sup>&minus;1</sup>. With the same "
 "braking force, the braking distance at 30 m s<sup>&minus;1</sup> is:",
 ["40 m", "60 m", "80 m", "160 m"], 2,
 "Fd = &frac12;mv&sup2; &rArr; d &prop; v&sup2;. Doubling v quadruples d: 4 &times; 20 = 80 m.")

add(MT5,
 "A pump raises 300 kg of water per minute to a height of 12 m. The minimum power required is "
 "approximately:",
 ["59 W", "590 W", "3500 W", "35 W"], 1,
 "Mass/s = 300/60 = 5.0 kg s<sup>&minus;1</sup>. P = (m/t)gh = 5.0 &times; 9.81 &times; 12 &asymp; "
 "589 W.")

add(MT5,
 "A 60 kg skier descends a 20 m vertical drop and arrives with KE of 9.0 kJ. The energy dissipated "
 "by friction is approximately:",
 ["2.8 kJ", "9.0 kJ", "11.8 kJ", "20.8 kJ"], 0,
 "PE lost = mgh = 60&times;9.81&times;20 = 11.77 kJ. Dissipated = 11.77 &minus; 9.0 = 2.8 kJ.")

add(MT5,
 "An object is projected vertically up with kinetic energy E. At the height where its speed has "
 "halved, its kinetic energy is:",
 ["E/2", "E/4", "3E/4", "E"], 1,
 "KE &prop; v&sup2;. If v halves, KE becomes (&frac12;)&sup2; = &frac14; of the original, i.e. E/4.")

add(MT5,
 "A machine has an efficiency of 40%. To deliver 800 J of useful output, the energy input required "
 "is:",
 ["320 J", "1120 J", "2000 J", "3200 J"], 2,
 "Efficiency = useful/input &rArr; input = useful/efficiency = 800/0.40 = 2000 J.")

add(MT5,
 "A constant force of 20 N pulls a box 5.0 m across a floor; the force acts at 60&deg; to the "
 "horizontal (direction of motion). The work done by the force is:",
 ["50 J", "87 J", "100 J", "173 J"], 0,
 "W = Fs cos&theta; = 20 &times; 5.0 &times; cos60&deg; = 100 &times; 0.5 = 50 J.")

add(MT5,
 "Water flows over a waterfall of height 50 m at 200 kg s<sup>&minus;1</sup>. If all the PE were "
 "converted to electrical energy, the maximum power output would be about:",
 ["9.8 kW", "98 kW", "980 kW", "9.8 MW"], 1,
 "P = (m/t)gh = 200 &times; 9.81 &times; 50 = 9.81 &times; 10<sup>4</sup> W &asymp; 98 kW.")

# ===========================================================================
# TOPIC 6  (7)
# ===========================================================================
add(MT6,
 "A wire extends 2.0 mm under a load. A second wire of the same material and length but twice the "
 "diameter carries the same load. Its extension is:",
 ["0.5 mm", "1.0 mm", "2.0 mm", "4.0 mm"], 0,
 "e = FL/(AE). Twice the diameter &rArr; 4&times; area &rArr; extension &times; 1/4: "
 "2.0/4 = 0.5 mm.")

add(MT6,
 "The area under a force&ndash;extension graph (within the limit of proportionality) represents:",
 ["the spring constant", "the stress", "the elastic potential energy stored",
  "the Young modulus"], 2,
 "Work done stretching = area under F&ndash;x graph = elastic PE stored (&frac12;Fx within the "
 "limit of proportionality).")

add(MT6,
 "Two springs each of stiffness k are joined end-to-end (in series). The combined stiffness is:",
 ["2k", "k", "k/2", "k/4"], 2,
 "In series 1/k<sub>total</sub> = 1/k + 1/k = 2/k &rArr; k<sub>total</sub> = k/2 (softer, extends "
 "more for a given force).")

add(MT6,
 "A material is stretched beyond its elastic limit and then unloaded. On the force&ndash;extension "
 "graph, this shows as:",
 ["the line returning exactly along the loading line",
  "a permanent extension when the force reaches zero",
  "an increased spring constant", "no extension at all"], 1,
 "Beyond the elastic limit deformation is partly plastic, so on unloading a permanent (residual) "
 "extension remains when the force returns to zero.")

add(MT6,
 "A wire of Young modulus E, length L and cross-sectional area A is stretched by force F. The "
 "extension is:",
 ["FL/(AE)", "FA/(LE)", "EAL/F", "FE/(AL)"], 0,
 "E = (F/A)/(e/L) &rArr; e = FL/(AE).")

add(MT6,
 "A steel wire and a copper wire have the same dimensions and carry the same load within their "
 "limits of proportionality. Steel has the larger Young modulus. Compared with the copper wire, the "
 "steel wire has:",
 ["greater stress and greater strain", "the same stress but smaller strain",
  "smaller stress and greater strain", "the same stress and the same strain"], 1,
 "Same load and dimensions &rArr; same stress (F/A). Since E = stress/strain and steel has larger E, "
 "the steel wire has the smaller strain (and hence smaller extension).")

add(MT6,
 "A spring stores 0.80 J of elastic PE at an extension of 40 mm (within its limit of "
 "proportionality). At an extension of 20 mm it stores:",
 ["0.20 J", "0.40 J", "0.60 J", "0.80 J"], 0,
 "E<sub>P</sub> = &frac12;kx&sup2; &prop; x&sup2;. Halving x &rArr; PE &times; 1/4: "
 "0.80/4 = 0.20 J.")

# ===========================================================================
# TOPIC 7  (10)
# ===========================================================================
add(MT7,
 "A wave has speed 340 m s<sup>&minus;1</sup> and frequency 170 Hz. Two points 1.5 m apart along the "
 "direction of travel have a phase difference of:",
 ["90&deg;", "180&deg;", "270&deg;", "360&deg;"], 2,
 "&lambda; = v/f = 340/170 = 2.0 m. Phase difference = (1.5/2.0) &times; 360&deg; = 270&deg;.")

add(MT7,
 "On a CRO the time-base is 5.0 ms/div and one cycle spans 4.0 divisions. The frequency is:",
 ["25 Hz", "50 Hz", "100 Hz", "200 Hz"], 1,
 "Period = 4.0 &times; 5.0 ms = 20 ms = 0.020 s. f = 1/0.020 = 50 Hz.")

add(MT7,
 "The intensity of a wave is quadrupled. Its amplitude changes by a factor of:",
 ["&radic;2", "2", "4", "16"], 1,
 "I &prop; A&sup2; &rArr; A &prop; &radic;I. Quadrupling I multiplies A by &radic;4 = 2.")

add(MT7,
 "A source of sound moves towards a stationary observer at speed v<sub>s</sub>; the speed of sound "
 "is v. The observed frequency is:",
 ["f<sub>s</sub>(v &minus; v<sub>s</sub>)/v", "f<sub>s</sub>v/(v + v<sub>s</sub>)",
  "f<sub>s</sub>v/(v &minus; v<sub>s</sub>)", "f<sub>s</sub>(v + v<sub>s</sub>)/v"], 2,
 "For an approaching source use the minus sign in the denominator: "
 "f<sub>o</sub> = f<sub>s</sub>v/(v &minus; v<sub>s</sub>), giving a higher observed frequency.")

add(MT7,
 "Which electromagnetic radiation has the shortest wavelength in free space?",
 ["microwaves", "infrared", "ultraviolet", "gamma rays"], 3,
 "Gamma rays have the shortest wavelength (&lt; 10<sup>&minus;12</sup> m), shorter than UV, infrared "
 "and microwaves.")

add(MT7,
 "Plane-polarised light of intensity I<sub>0</sub> passes through a polariser whose axis is at "
 "30&deg; to the plane of polarisation. The transmitted intensity is:",
 ["0.25 I<sub>0</sub>", "0.50 I<sub>0</sub>", "0.75 I<sub>0</sub>", "0.87 I<sub>0</sub>"], 2,
 "Malus: I = I<sub>0</sub>cos&sup2;30&deg; = I<sub>0</sub>(0.866)&sup2; = 0.75 I<sub>0</sub>.")

add(MT7,
 "A sound wave passes from air into water, where its speed is greater. Which quantity is unchanged?",
 ["speed", "wavelength", "frequency", "intensity"], 2,
 "Frequency is fixed by the source and is continuous across the boundary. Speed and wavelength both "
 "change (v = f&lambda;).")

add(MT7,
 "Which statement about a longitudinal wave is correct?",
 ["it can be polarised", "particles oscillate perpendicular to travel",
  "it consists of compressions and rarefactions", "it cannot transfer energy"], 2,
 "Longitudinal waves have particle oscillations parallel to the travel direction, forming "
 "compressions and rarefactions; they cannot be polarised but do transfer energy.")

add(MT7,
 "Two points on a transverse progressive wave are exactly half a wavelength apart. Their motions "
 "are:",
 ["in phase", "in antiphase (180&deg; out of phase)", "90&deg; out of phase",
  "always both at maximum displacement"], 1,
 "A separation of &lambda;/2 corresponds to a phase difference of 180&deg; &mdash; the points are in "
 "antiphase (moving in opposite directions).")

add(MT7,
 "Unpolarised light of intensity I<sub>0</sub> passes through one ideal polarising filter. The "
 "transmitted intensity is:",
 ["I<sub>0</sub>", "0.71 I<sub>0</sub>", "0.50 I<sub>0</sub>", "0.25 I<sub>0</sub>"], 2,
 "An ideal polariser transmits half the incident unpolarised intensity: 0.50 I<sub>0</sub> (and the "
 "output is plane-polarised).")


# ===========================================================================
# TOPIC 8  (8)
# ===========================================================================
add(MT8,
 "In a double-slit experiment, the fringe separation is x. If the slit separation is halved and the "
 "screen distance is doubled, the new fringe separation is:",
 ["x", "2x", "4x", "x/4"], 2,
 "x = &lambda;D/a. Halving a multiplies by 2; doubling D multiplies by 2; combined &times;4.")

add(MT8,
 "A diffraction grating of 300 lines per mm is used with light of wavelength 500 nm. The number of "
 "diffracted orders visible on each side of the centre is:",
 ["4", "5", "6", "7"], 2,
 "d = 1/(300&times;10<sup>3</sup>) = 3.33&times;10<sup>&minus;6</sup> m. Max order: n = d/&lambda; = "
 "3.33&times;10<sup>&minus;6</sup>/500&times;10<sup>&minus;9</sup> = 6.67, so n = 6 (six orders each "
 "side).")

add(MT8,
 "Adjacent nodes on a stationary wave are 0.30 m apart. The wavelength of the waves forming it is:",
 ["0.15 m", "0.30 m", "0.60 m", "1.2 m"], 2,
 "Adjacent nodes are &lambda;/2 apart, so &lambda; = 2 &times; 0.30 = 0.60 m.")

add(MT8,
 "For a stable two-source interference pattern, the two sources must be:",
 ["of different frequency", "coherent (constant phase difference)",
  "incoherent", "of perpendicular polarisation"], 1,
 "Observable, stable fringes require coherent sources &mdash; a constant phase difference (hence the "
 "same frequency).")

add(MT8,
 "A stationary wave differs from a progressive wave in that a stationary wave:",
 ["transfers energy along its length", "has all points oscillating with the same amplitude",
  "does not transfer energy along its length", "has no nodes"], 2,
 "A stationary wave stores energy and does not transfer it along the wave; amplitude varies from "
 "zero at nodes to a maximum at antinodes.")

add(MT8,
 "White light passes through a diffraction grating. In the first-order spectrum, the colour "
 "diffracted through the largest angle is:",
 ["violet", "green", "red", "all diffracted equally"], 2,
 "d sin&theta; = n&lambda; &rArr; sin&theta; &prop; &lambda;. Red has the longest wavelength, so it "
 "is diffracted through the largest angle.")

add(MT8,
 "Two coherent sources produce interference. At a point the path difference is 2.5&lambda;. This "
 "point is:",
 ["a bright fringe (constructive)", "a dark fringe (destructive)",
  "of intermediate intensity", "outside the pattern"], 1,
 "A path difference of an odd number of half-wavelengths (2.5&lambda; = 5 &times; &lambda;/2) gives "
 "antiphase arrival &mdash; destructive interference (dark).")

add(MT8,
 "The most pronounced diffraction of a wave through a gap occurs when the gap width is:",
 ["much larger than the wavelength", "approximately equal to the wavelength",
  "much smaller than the wavelength", "independent of the wavelength"], 1,
 "Diffraction is greatest when the gap width is comparable to the wavelength.")

# ===========================================================================
# TOPIC 9  (9)
# ===========================================================================
add(MT9,
 "A current of 5.0 A flows for 4.0 minutes. The number of electrons passing a point is "
 "(e = 1.6 &times; 10<sup>&minus;19</sup> C):",
 ["7.5 &times; 10<sup>21</sup>", "1.9 &times; 10<sup>21</sup>",
  "7.5 &times; 10<sup>19</sup>", "1.2 &times; 10<sup>3</sup>"], 0,
 "Q = It = 5.0 &times; 240 = 1200 C. N = Q/e = 1200/1.6&times;10<sup>&minus;19</sup> = "
 "7.5 &times; 10<sup>21</sup>.")

add(MT9,
 "For a wire carrying current I with n charge carriers per unit volume, each of charge q, and "
 "cross-sectional area A, the drift speed is:",
 ["I/(nAq)", "nAq/I", "InAq", "IA/(nq)"], 0,
 "I = nAvq &rArr; v = I/(nAq).")

add(MT9,
 "A wire is stretched to twice its length (volume constant). Its resistance becomes:",
 ["half", "double", "four times", "unchanged"], 2,
 "Constant volume: doubling L halves A. R = &rho;L/A &rarr; &rho;(2L)/(A/2) = 4&rho;L/A = 4R.")

add(MT9,
 "The I&ndash;V graph of a filament lamp is a curve that bends towards the V-axis as V increases. "
 "This is because:",
 ["the filament cools with current", "the resistance decreases with current",
  "the resistance increases as temperature rises", "it obeys Ohm's law"], 2,
 "Higher current heats the filament; increasing temperature increases resistance, so I rises less "
 "steeply with V (the curve bends towards the V-axis). The lamp does not obey Ohm's law.")

add(MT9,
 "Two resistors 3.0 &Omega; and 6.0 &Omega; are in parallel. The combined resistance is:",
 ["9.0 &Omega;", "4.5 &Omega;", "2.0 &Omega;", "0.5 &Omega;"], 2,
 "1/R = 1/3.0 + 1/6.0 = 2/6 + 1/6 = 3/6 &rArr; R = 2.0 &Omega;.")

add(MT9,
 "The resistance of a thermistor (NTC) as temperature rises, and of an LDR as light intensity "
 "rises, respectively:",
 ["increases; increases", "decreases; decreases", "increases; decreases",
  "decreases; increases"], 1,
 "An NTC thermistor's resistance decreases as temperature rises; an LDR's resistance decreases as "
 "light intensity rises (both because more charge carriers are freed).")

add(MT9,
 "A 12 V, 36 W lamp operates at its rating. Its resistance is:",
 ["0.33 &Omega;", "3.0 &Omega;", "4.0 &Omega;", "48 &Omega;"], 2,
 "R = V&sup2;/P = 12&sup2;/36 = 144/36 = 4.0 &Omega;.")

add(MT9,
 "Power P is transmitted at voltage V through cables of resistance R. The power lost as heat in the "
 "cables is:",
 ["P&sup2;R/V&sup2;", "PV/R", "V&sup2;/R", "PR/V"], 0,
 "Line current I = P/V. Loss = I&sup2;R = (P/V)&sup2;R = P&sup2;R/V&sup2; &mdash; hence high-V, "
 "low-I transmission minimises loss.")

add(MT9,
 "Two identical resistors are connected first in series, then in parallel, across the same supply. "
 "The ratio (power in parallel : power in series) is:",
 ["1 : 1", "2 : 1", "4 : 1", "1 : 4"], 2,
 "Let each be R. Series total 2R, parallel total R/2. P = V&sup2;/R<sub>tot</sub>. "
 "Ratio = (V&sup2;/(R/2))/(V&sup2;/2R) = (2/R)/(1/2R) = 4. So 4 : 1.")

# ===========================================================================
# TOPIC 10  (9)
# ===========================================================================
add(MT10,
 "A cell of e.m.f. 1.5 V has internal resistance 0.50 &Omega;. When connected to a 1.0 &Omega; "
 "resistor, the terminal p.d. is:",
 ["0.50 V", "1.0 V", "1.25 V", "1.5 V"], 1,
 "I = 1.5/(1.0 + 0.50) = 1.0 A. Terminal p.d. = IR = 1.0 &times; 1.0 = 1.0 V "
 "(= &epsilon; &minus; Ir = 1.5 &minus; 0.5).")

add(MT10,
 "Kirchhoff's first law (current) is a consequence of the conservation of:",
 ["energy", "charge", "momentum", "mass"], 1,
 "The junction (current) law expresses conservation of charge &mdash; charge cannot accumulate at a "
 "point in a steady current.")

add(MT10,
 "In a potential divider, two equal resistors are across a 10 V supply. The output across one "
 "resistor is 5.0 V. If a load equal to R is connected across that resistor, the output becomes:",
 ["5.0 V", "3.3 V", "2.5 V", "6.7 V"], 1,
 "The loaded resistor becomes R/2 (R in parallel with R). V<sub>out</sub> = 10 &times; "
 "(R/2)/(R + R/2) = 10 &times; (1/2)/(3/2) = 10/3 = 3.3 V.")

add(MT10,
 "A battery delivers maximum power to an external resistor R when:",
 ["R is very large", "R = 0", "R equals the internal resistance r", "R is very small"], 2,
 "Maximum power transfer to the load occurs when R = r (matched resistances); efficiency is then "
 "50%.")

add(MT10,
 "The e.m.f. of a source is best defined as the energy transferred per unit charge:",
 ["dissipated in the internal resistance",
  "in driving charge around the complete circuit",
  "in the external circuit only", "when no charge flows"], 1,
 "E.m.f. = total energy transferred (from other forms to electrical) per unit charge driven around "
 "the whole circuit, including the internal resistance.")

add(MT10,
 "Three 6.0 &Omega; resistors are connected in parallel. The combined resistance is:",
 ["18 &Omega;", "6.0 &Omega;", "3.0 &Omega;", "2.0 &Omega;"], 3,
 "Equal resistors in parallel: R/n = 6.0/3 = 2.0 &Omega;.")

add(MT10,
 "A potentiometer is balanced (galvanometer reads zero) at length 45.0 cm for one cell and 60.0 cm "
 "for a second. The ratio of their e.m.f.s (first : second) is:",
 ["3 : 4", "4 : 3", "1 : 1", "9 : 16"], 0,
 "At balance no current flows, so e.m.f. &prop; balance length: 45.0 : 60.0 = 3 : 4.")

add(MT10,
 "As the current drawn from a real battery increases, its terminal potential difference:",
 ["increases", "decreases", "stays equal to the e.m.f.", "becomes zero immediately"], 1,
 "V = &epsilon; &minus; Ir; as I increases the 'lost volts' Ir increases, so the terminal p.d. "
 "decreases.")

add(MT10,
 "In the circuit, a 6.0 V battery (negligible internal resistance) is connected to a 2.0 &Omega; "
 "resistor in series with a parallel pair of 4.0 &Omega; resistors. The current from the battery "
 "is:",
 ["1.0 A", "1.5 A", "2.0 A", "3.0 A"], 1,
 "Parallel pair = 2.0 &Omega;. Total = 2.0 + 2.0 = 4.0 &Omega;. I = 6.0/4.0 = 1.5 A.")

# ===========================================================================
# TOPIC 11  (8)
# ===========================================================================
add(MT11,
 "The nuclide <sup>238</sup><sub>92</sub>U emits an &alpha;-particle. The resulting nuclide has:",
 ["A = 234, Z = 90", "A = 236, Z = 90", "A = 234, Z = 92", "A = 238, Z = 90"], 0,
 "&alpha;-emission removes 2 protons and 2 neutrons: A decreases by 4 (238&rarr;234), Z decreases by "
 "2 (92&rarr;90).")

add(MT11,
 "During &beta;<sup>&minus;</sup> decay, within the nucleus:",
 ["a proton becomes a neutron", "a neutron becomes a proton",
  "an up quark becomes a down quark", "a neutron becomes a positron"], 1,
 "&beta;<sup>&minus;</sup> decay: a neutron &rarr; proton (a down quark changes to an up quark), "
 "emitting an electron and an antineutrino.")

add(MT11,
 "The charge on a neutron (udd) confirms which quark charges?",
 ["u = +&frac13;, d = &minus;&frac23;", "u = +&frac23;, d = &minus;&frac13;",
  "u = &minus;&frac23;, d = +&frac13;", "u = +1, d = 0"], 1,
 "udd: (+&frac23;) + (&minus;&frac13;) + (&minus;&frac13;) = 0. Consistent with u = +&frac23;e, "
 "d = &minus;&frac13;e.")

add(MT11,
 "A meson consists of:",
 ["three quarks", "two quarks", "one quark and one antiquark", "a lepton and a quark"], 2,
 "A meson is a hadron made of one quark and one antiquark; a baryon is made of three quarks.")

add(MT11,
 "&beta;-particles are emitted with a continuous range of energies because:",
 ["the nucleus recoils", "a neutrino/antineutrino shares the energy",
  "&gamma;-rays are also emitted", "the electrons collide with atoms"], 1,
 "The decay energy is shared among three bodies (daughter nucleus, &beta;-particle and "
 "(anti)neutrino), so the &beta;-particle can take any energy up to a maximum &mdash; a continuous "
 "spectrum.")

add(MT11,
 "Which particle is a lepton?",
 ["proton", "neutron", "neutrino", "pion (meson)"], 2,
 "The neutrino is a fundamental lepton. Protons and neutrons are baryons; a pion is a meson &mdash; "
 "all hadrons made of quarks.")

add(MT11,
 "In the &alpha;-scattering experiment, the small fraction of &alpha;-particles deflected through "
 "large angles indicates that the atom's positive charge is:",
 ["spread uniformly through the atom", "concentrated in a tiny nucleus",
  "carried by the electrons", "zero"], 1,
 "Large-angle deflection of the positive &alpha;-particles shows a concentrated positive charge "
 "(and mass) in a very small nucleus &mdash; most of the atom being empty space.")

add(MT11,
 "Which quantities are always conserved in a nuclear decay equation?",
 ["nucleon number and charge", "mass and kinetic energy",
  "proton number and neutron number separately", "number of &alpha;-particles"], 0,
 "Nucleon number and charge (proton number balance) are conserved. Neutron and proton numbers can "
 "individually change (e.g. in &beta;-decay), and rest mass is not conserved (mass&ndash;energy is).")
