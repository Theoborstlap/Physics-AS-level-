# -*- coding: utf-8 -*-
"""150 extreme-difficulty structured (theory) questions, AS 9702 topics 1-11.
Each entry appends to engine.theory."""
from engine import theory as T, frac

def add(topic, q, marks, ans, svg=""):
    T.append({"topic": topic, "q": q, "marks": marks, "ans": ans, "svg": svg})

T1 = "1&nbsp;&nbsp;Physical quantities and units"
T2 = "2&nbsp;&nbsp;Kinematics"

# ===========================================================================
# TOPIC 1  (15 questions)
# ===========================================================================

add(T1,
 "The viscous drag on a small sphere of radius <span class='eq'>r</span> moving slowly at speed "
 "<span class='eq'>v</span> through a fluid of viscosity <span class='eq'>&eta;</span> is "
 "<span class='eq'>F = 6&pi;&eta;rv</span>."
 "<ol class='parts'>"
 "<li>Determine the SI base units of <span class='eq'>&eta;</span>.</li>"
 "<li>A student claims the terminal speed of a sphere falling in the fluid is "
 "<span class='eq'>v = 2r&sup2;(&rho;<sub>s</sub>&minus;&rho;<sub>f</sub>)g / 9&eta;</span>, where the "
 "<span class='eq'>&rho;</span> are densities. By checking homogeneity, state whether this equation "
 "is dimensionally consistent.</li></ol>",
 6,
 "<b>(a)</b> Rearranging, <span class='eq'>&eta; = F/(6&pi;rv)</span>. Base units = "
 "(kg m s<sup>&minus;2</sup>) / (m &middot; m s<sup>&minus;1</sup>) = "
 "<b>kg m<sup>&minus;1</sup> s<sup>&minus;1</sup></b>. (The 6&pi; is a pure number.)<br>"
 "<b>(b)</b> RHS base units: numerator "
 "<span class='eq'>r&sup2;&rho;g</span> = m&sup2; &middot; (kg m<sup>&minus;3</sup>) &middot; (m s<sup>&minus;2</sup>) "
 "= kg m<sup>0</sup> s<sup>&minus;2</sup> = kg s<sup>&minus;2</sup>. Dividing by &eta; "
 "(kg m<sup>&minus;1</sup> s<sup>&minus;1</sup>): "
 "(kg s<sup>&minus;2</sup>)/(kg m<sup>&minus;1</sup> s<sup>&minus;1</sup>) = "
 "m s<sup>&minus;1</sup>. This equals the units of speed, so the equation <b>is homogeneous</b>. "
 "(Note: homogeneity does not prove the numerical factor 2/9 is correct.)")

add(T1,
 "Estimate, showing your reasoning and stating any assumptions, the average useful power developed "
 "by an adult who runs up a flight of stairs of typical height in a typical time. Give your answer to "
 "one significant figure and comment on why more figures would be unjustified.",
 5,
 "Reasonable estimates: mass <span class='eq'>m</span> &asymp; 70 kg; vertical height of one storey "
 "&asymp; 3 m; time to run up &asymp; 5 s.<br>"
 "Useful work against gravity <span class='eq'>W = mg&Delta;h</span> "
 "= 70 &times; 9.81 &times; 3 &asymp; 2060 J.<br>"
 "Power <span class='eq'>P = W/t</span> = 2060 / 5 &asymp; 410 W &rarr; <b>&asymp; 400 W</b> "
 "(4 &times; 10<sup>2</sup> W).<br>"
 "Only 1 s.f. is justified because each input quantity is itself only a rough estimate "
 "(uncertain by tens of per cent), so extra figures would imply a false precision.")

add(T1,
 "A resistance is found from <span class='eq'>R = V/I</span>. In an experiment "
 "<span class='eq'>V = (6.0 &plusmn; 0.1)</span> V and <span class='eq'>I = (0.40 &plusmn; 0.02)</span> A."
 "<ol class='parts'>"
 "<li>Calculate <span class='eq'>R</span> and its absolute uncertainty.</li>"
 "<li>The power is <span class='eq'>P = V&sup2;/R</span>. Determine the percentage uncertainty in "
 "<span class='eq'>P</span>.</li></ol>",
 6,
 "<b>(a)</b> <span class='eq'>R = 6.0/0.40 = 15 &Omega;</span>. Percentage uncertainties: "
 "V: 0.1/6.0 = 1.67%; I: 0.02/0.40 = 5.0%. For a quotient, add: "
 "&Delta;R/R = 6.67%. &Delta;R = 0.0667 &times; 15 = 1.0 &Omega;. "
 "So <b>R = (15 &plusmn; 1) &Omega;</b>.<br>"
 "<b>(b)</b> <span class='eq'>P = V&sup2;/R</span> &rArr; %unc = 2(%V) + (%R) "
 "= 2(1.67%) + 6.67% = 3.33% + 6.67% = <b>10%</b>. "
 "(Equivalently P = V&sup2;/R uses R already containing the I uncertainty; adding independently as "
 "P = VI would give 2&times; nothing &mdash; here use the stated formula.)")

add(T1,
 "Two forces act at a point: <span class='eq'>F<sub>1</sub></span> = 8.0 N due east and "
 "<span class='eq'>F<sub>2</sub></span> = 6.0 N in a direction 60&deg; north of east. "
 "By resolving into components, determine the magnitude and direction of the resultant force.",
 5,
 "Components (east = x, north = y):<br>"
 "x: 8.0 + 6.0 cos60&deg; = 8.0 + 3.0 = 11.0 N.<br>"
 "y: 0 + 6.0 sin60&deg; = 5.20 N.<br>"
 "Magnitude = &radic;(11.0&sup2; + 5.20&sup2;) = &radic;(121 + 27.0) = &radic;148 = <b>12.2 N</b>.<br>"
 "Direction = tan<sup>&minus;1</sup>(5.20/11.0) = <b>25.3&deg; north of east</b>.",
 "<svg width='300' height='170' viewBox='0 0 300 170'>"
 "<line x1='30' y1='140' x2='280' y2='140' stroke='#999'/>"
 "<line x1='30' y1='140' x2='30' y2='20' stroke='#999'/>"
 "<line x1='30' y1='140' x2='190' y2='140' stroke='#06c' stroke-width='2'/>"
 "<polygon points='190,140 182,136 182,144' fill='#06c'/>"
 "<line x1='30' y1='140' x2='90' y2='36' stroke='#c30' stroke-width='2'/>"
 "<polygon points='90,36 84,44 94,46' fill='#c30'/>"
 "<line x1='30' y1='140' x2='250' y2='36' stroke='#093' stroke-width='2' stroke-dasharray='4 3'/>"
 "<text x='150' y='155' font-size='11' fill='#06c'>F1 = 8.0 N (E)</text>"
 "<text x='60' y='30' font-size='11' fill='#c30'>F2 = 6.0 N</text>"
 "<text x='140' y='70' font-size='11' fill='#093'>resultant</text>"
 "<text x='96' y='128' font-size='10'>60&deg;</text></svg>")

add(T1,
 "An aircraft has a velocity relative to the air of 250 m s<sup>&minus;1</sup> due north. A wind blows "
 "from the west (i.e. towards the east) at 40 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Find the velocity of the aircraft relative to the ground (magnitude and direction).</li>"
 "<li>State the direction in which the pilot must instead head, relative to north, so that the "
 "aircraft actually travels due north over the ground, and find the resulting ground speed.</li></ol>",
 7,
 "<b>(a)</b> Ground velocity = air velocity + wind velocity. North component 250, east component 40. "
 "Magnitude = &radic;(250&sup2; + 40&sup2;) = &radic;(62500 + 1600) = &radic;64100 = <b>253 m s<sup>&minus;1</sup></b>. "
 "Direction = tan<sup>&minus;1</sup>(40/250) = 9.1&deg; <b>east of north</b>.<br>"
 "<b>(b)</b> To cancel the eastward drift, the aircraft's own eastward component must be 40 m s<sup>&minus;1</sup> "
 "towards the west. So it heads at angle &theta; west of north with 250 sin&theta; = 40 &rArr; "
 "&theta; = sin<sup>&minus;1</sup>(40/250) = <b>9.2&deg; west of north</b>. "
 "Ground speed (northward) = 250 cos&theta; = 250 &times; 0.987 = <b>247 m s<sup>&minus;1</sup></b>.")

add(T1,
 "Distinguish between <b>random</b> and <b>systematic</b> errors. A micrometer with a zero error of "
 "+0.02 mm (it reads 0.02 mm when fully closed) is used to measure the diameter of a wire; five "
 "readings are 0.52, 0.53, 0.51, 0.54, 0.52 mm."
 "<ol class='parts'>"
 "<li>State the type of error caused by the zero error and its effect on the mean.</li>"
 "<li>Determine the best estimate of the true diameter and its absolute uncertainty.</li></ol>",
 7,
 "Random errors cause readings to scatter unpredictably about the true value (reduced by averaging); "
 "systematic errors shift all readings by the same amount in the same direction (not reduced by averaging).<br>"
 "<b>(a)</b> The zero error is a <b>systematic error</b>; every reading is 0.02 mm too large, so the "
 "mean is 0.02 mm too high.<br>"
 "<b>(b)</b> Mean of readings = (0.52+0.53+0.51+0.54+0.52)/5 = 0.524 mm. Correct for zero error: "
 "0.524 &minus; 0.02 = <b>0.504 mm</b>. Random uncertainty &asymp; half the range = "
 "(0.54&minus;0.51)/2 = 0.015 mm. So diameter = <b>(0.50 &plusmn; 0.02) mm</b> "
 "(uncertainty rounded up to 1 s.f., value to matching decimal place).")

add(T1,
 "The Young modulus <span class='eq'>E</span> of a wire is found from "
 "<span class='eq'>E = 4FL / (&pi;d&sup2;e)</span>. Measured percentage uncertainties are: "
 "<span class='eq'>F</span> 2%, <span class='eq'>L</span> 0.5%, <span class='eq'>d</span> 1.5%, "
 "extension <span class='eq'>e</span> 4%. "
 "Determine the percentage uncertainty in <span class='eq'>E</span> and explain which single "
 "measurement it would be most worthwhile to improve.",
 5,
 "For a product/quotient, add percentage uncertainties, multiplying each by its power. "
 "<span class='eq'>d</span> appears squared, so it contributes 2 &times; 1.5% = 3%.<br>"
 "%E = %F + %L + 2(%d) + %e = 2 + 0.5 + 3 + 4 = <b>9.5%</b> (&asymp; 10%).<br>"
 "The largest single contribution is the extension <span class='eq'>e</span> (4%). Since "
 "<span class='eq'>e</span> is a small quantity (difference of two scale readings), improving how it is "
 "measured &mdash; e.g. using a vernier/travelling microscope or a longer wire to give a larger "
 "<span class='eq'>e</span> &mdash; would most reduce the overall uncertainty.")

add(T1,
 "State what is meant by a <b>scalar</b> and a <b>vector</b> quantity. For each of the following, "
 "state whether it is a scalar or a vector: (i) work done, (ii) momentum, (iii) electric current, "
 "(iv) gravitational field strength, (v) power. Give a reason for classifying electric current as you do.",
 6,
 "A scalar has magnitude only; a vector has magnitude <b>and</b> direction (and adds by the "
 "triangle/parallelogram rule).<br>"
 "(i) work &mdash; <b>scalar</b>; (ii) momentum &mdash; <b>vector</b>; (iii) current &mdash; <b>scalar</b>; "
 "(iv) gravitational field strength &mdash; <b>vector</b>; (v) power &mdash; <b>scalar</b>.<br>"
 "Although current has a direction of flow, currents do not combine by vector addition (they add "
 "algebraically at a junction, as in Kirchhoff's first law), so current is treated as a scalar.")

add(T1,
 "A ball is thrown at a wall and rebounds. Just before impact its velocity is 12 m s<sup>&minus;1</sup> "
 "directed 30&deg; below the horizontal; just after, it is 9.0 m s<sup>&minus;1</sup> directed 40&deg; "
 "above the horizontal. Treating the horizontal (towards the wall) as positive x and upward as positive y, "
 "find the magnitude and direction of the <b>change in velocity</b> &Delta;v.",
 7,
 "Take x towards the wall, y up. Before: v<sub>x</sub> = +12 cos30&deg; = +10.39, "
 "v<sub>y</sub> = &minus;12 sin30&deg; = &minus;6.00 m s<sup>&minus;1</sup>. "
 "After (moving away from wall, so x negative): v<sub>x</sub> = &minus;9.0 cos40&deg; = &minus;6.89, "
 "v<sub>y</sub> = +9.0 sin40&deg; = +5.79 m s<sup>&minus;1</sup>.<br>"
 "&Delta;v = v<sub>after</sub> &minus; v<sub>before</sub>: "
 "&Delta;v<sub>x</sub> = &minus;6.89 &minus; 10.39 = &minus;17.28; "
 "&Delta;v<sub>y</sub> = 5.79 &minus; (&minus;6.00) = +11.79 m s<sup>&minus;1</sup>.<br>"
 "Magnitude = &radic;(17.28&sup2; + 11.79&sup2;) = &radic;(298.6 + 139.0) = &radic;437.6 = "
 "<b>20.9 m s<sup>&minus;1</sup></b>. Direction = tan<sup>&minus;1</sup>(11.79/17.28) = 34.3&deg; above "
 "the horizontal, pointing <b>away from the wall and upward</b> (i.e. 34&deg; above horizontal in the "
 "&minus;x, +y quadrant).")

add(T1,
 "The pressure at depth in a liquid is given by <span class='eq'>p = h&rho;g</span>. "
 "<ol class='parts'>"
 "<li>Show that this equation is homogeneous.</li>"
 "<li>Hence deduce the base units of pressure and confirm they are equivalent to the pascal "
 "expressed in terms of the newton.</li></ol>",
 5,
 "<b>(a)</b> RHS units: <span class='eq'>h&rho;g</span> = m &middot; kg m<sup>&minus;3</sup> &middot; "
 "m s<sup>&minus;2</sup> = kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>. "
 "LHS pressure = force/area = (kg m s<sup>&minus;2</sup>)/m&sup2; = kg m<sup>&minus;1</sup> s<sup>&minus;2</sup>. "
 "Both sides identical &rArr; homogeneous.<br>"
 "<b>(b)</b> Base units of pressure = <b>kg m<sup>&minus;1</sup> s<sup>&minus;2</sup></b>. "
 "1 Pa = 1 N m<sup>&minus;2</sup> = (kg m s<sup>&minus;2</sup>) m<sup>&minus;2</sup> = "
 "kg m<sup>&minus;1</sup> s<sup>&minus;2</sup> &mdash; the same, confirming consistency.")

add(T1,
 "A student measures the period <span class='eq'>T</span> of a pendulum by timing 20 oscillations "
 "with a stopwatch of resolution 0.01 s, obtaining a total time of 18.4 s. The reaction time in "
 "starting/stopping introduces an uncertainty of about &plusmn;0.3 s in the total time."
 "<ol class='parts'>"
 "<li>Explain why timing 20 oscillations rather than 1 is good practice.</li>"
 "<li>Determine <span class='eq'>T</span> and its percentage uncertainty.</li></ol>",
 6,
 "<b>(a)</b> The reaction-time uncertainty (&asymp;0.3 s) is fixed per measurement, so timing many "
 "oscillations makes it a much smaller fraction of the total time; dividing by 20 also divides the "
 "absolute uncertainty in T by 20. This reduces the percentage (random) uncertainty. (The stopwatch "
 "resolution is negligible compared with reaction time.)<br>"
 "<b>(b)</b> T = 18.4/20 = <b>0.920 s</b>. The dominant uncertainty is &plusmn;0.3 s in the total: "
 "%unc = 0.3/18.4 = <b>1.6%</b> (this is the same for the total time and for T, since dividing by an "
 "exact 20 does not change the percentage). Hence T = (0.920 &plusmn; 0.015) s.")

add(T1,
 "Estimate the order of magnitude of the number of air molecules in a typical classroom. "
 "State your assumptions clearly. (Take the number of molecules per mole as "
 "6 &times; 10<sup>23</sup> and the molar volume of a gas as about 0.024 m<sup>3</sup> mol<sup>&minus;1</sup> "
 "at room conditions.)",
 5,
 "Assume a room 8 m &times; 6 m &times; 3 m &asymp; 150 m&sup3;.<br>"
 "Moles of air = volume / molar volume = 150 / 0.024 &asymp; 6.3 &times; 10<sup>3</sup> mol.<br>"
 "Number of molecules = 6.3 &times; 10<sup>3</sup> &times; 6 &times; 10<sup>23</sup> "
 "&asymp; 3.8 &times; 10<sup>27</sup>.<br>"
 "<b>Order of magnitude &asymp; 10<sup>27</sup> molecules.</b> (Any room volume 50&ndash;300 m&sup3; "
 "gives the same order.)")

add(T1,
 "Three coplanar forces act on a point object which is in equilibrium: a known force of 10.0 N acting "
 "horizontally, and two unknown forces <span class='eq'>P</span> and <span class='eq'>Q</span>. "
 "<span class='eq'>P</span> acts at 90&deg; to the 10.0 N force (vertically) and "
 "<span class='eq'>Q</span> acts at 150&deg; to the 10.0 N force (measured anticlockwise). "
 "Using the fact that the vector sum is zero, find <span class='eq'>P</span> and <span class='eq'>Q</span>.",
 7,
 "For equilibrium the components in each direction sum to zero. Let the 10.0 N force be along +x. "
 "Q makes 150&deg; with +x, so Q<sub>x</sub> = Q cos150&deg; = &minus;0.866Q, "
 "Q<sub>y</sub> = Q sin150&deg; = +0.500Q. P is along +y: P<sub>x</sub> = 0, P<sub>y</sub> = P.<br>"
 "x: 10.0 + (&minus;0.866Q) = 0 &rArr; Q = 10.0/0.866 = <b>11.5 N</b>.<br>"
 "y: P + 0.500Q = 0 &rArr; P = &minus;0.500 &times; 11.5 = &minus;5.77 N, i.e. "
 "<b>P = 5.8 N directed vertically downward</b> (opposite to the assumed +y). "
 "A closed vector triangle confirms equilibrium.")

add(T1,
 "The drag force on a car at speed <span class='eq'>v</span> is modelled by "
 "<span class='eq'>F = bv&sup2;</span>. "
 "<ol class='parts'>"
 "<li>Determine the SI base units of the constant <span class='eq'>b</span>.</li>"
 "<li>The power needed to overcome this drag is <span class='eq'>P = Fv</span>. Show, using units, "
 "that <span class='eq'>P = bv&sup3;</span> is homogeneous.</li></ol>",
 5,
 "<b>(a)</b> b = F/v&sup2; = (kg m s<sup>&minus;2</sup>)/(m s<sup>&minus;1</sup>)&sup2; "
 "= (kg m s<sup>&minus;2</sup>)/(m&sup2; s<sup>&minus;2</sup>) = <b>kg m<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> bv&sup3; = kg m<sup>&minus;1</sup> &times; (m s<sup>&minus;1</sup>)&sup3; "
 "= kg m<sup>&minus;1</sup> &times; m&sup3; s<sup>&minus;3</sup> = kg m&sup2; s<sup>&minus;3</sup>. "
 "Power = energy/time = (kg m&sup2; s<sup>&minus;2</sup>)/s = kg m&sup2; s<sup>&minus;3</sup>. "
 "Identical &rArr; homogeneous.")

add(T1,
 "A quantity is calculated from <span class='eq'>g = 4&pi;&sup2;L/T&sup2;</span> in a pendulum experiment. "
 "<span class='eq'>L</span> = (1.000 &plusmn; 0.002) m and the period is measured as "
 "<span class='eq'>T</span> = (2.008 &plusmn; 0.005) s."
 "<ol class='parts'>"
 "<li>Calculate <span class='eq'>g</span>.</li>"
 "<li>Determine the absolute uncertainty in <span class='eq'>g</span> and state the result to an "
 "appropriate number of significant figures.</li></ol>",
 7,
 "<b>(a)</b> g = 4&pi;&sup2; &times; 1.000 / (2.008)&sup2; = 39.478 / 4.032 = "
 "<b>9.79 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> %L = 0.002/1.000 = 0.20%; %T = 0.005/2.008 = 0.249%, and T is squared so contributes "
 "2 &times; 0.249% = 0.498%. Total %g = 0.20% + 0.50% = 0.70%. "
 "&Delta;g = 0.0070 &times; 9.79 = 0.068 &asymp; 0.07 m s<sup>&minus;2</sup>. "
 "Result: <b>g = (9.79 &plusmn; 0.07) m s<sup>&minus;2</sup></b>.")


# ===========================================================================
# TOPIC 2  Kinematics  (16 questions)
# ===========================================================================

add(T2,
 "A ball is projected from the ground with speed 25 m s<sup>&minus;1</sup> at 40&deg; above the "
 "horizontal. Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Calculate the maximum height reached.</li>"
 "<li>Calculate the horizontal range.</li>"
 "<li>Determine the speed and direction of the ball 2.5 s after projection.</li></ol>",
 8,
 "Resolve: u<sub>x</sub> = 25 cos40&deg; = 19.15 m s<sup>&minus;1</sup>; "
 "u<sub>y</sub> = 25 sin40&deg; = 16.07 m s<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> At max height v<sub>y</sub> = 0: v<sub>y</sub>&sup2; = u<sub>y</sub>&sup2; &minus; 2gh "
 "&rArr; h = 16.07&sup2;/(2&times;9.81) = 258/19.62 = <b>13.2 m</b>.<br>"
 "<b>(b)</b> Time of flight: t = 2u<sub>y</sub>/g = 2&times;16.07/9.81 = 3.28 s. "
 "Range = u<sub>x</sub>t = 19.15 &times; 3.28 = <b>62.8 m</b>.<br>"
 "<b>(c)</b> At t = 2.5 s: v<sub>x</sub> = 19.15 (constant); "
 "v<sub>y</sub> = 16.07 &minus; 9.81&times;2.5 = 16.07 &minus; 24.53 = &minus;8.46 m s<sup>&minus;1</sup> "
 "(downward). Speed = &radic;(19.15&sup2; + 8.46&sup2;) = &radic;(366.7 + 71.6) = &radic;438.3 = "
 "<b>20.9 m s<sup>&minus;1</sup></b>, directed tan<sup>&minus;1</sup>(8.46/19.15) = <b>23.8&deg; below "
 "the horizontal</b>.",
 "<svg width='320' height='150' viewBox='0 0 320 150'>"
 "<line x1='20' y1='130' x2='300' y2='130' stroke='#999'/>"
 "<path d='M20 130 Q160 -20 300 130' fill='none' stroke='#06c' stroke-width='2'/>"
 "<line x1='20' y1='130' x2='60' y2='96' stroke='#c30' stroke-width='2'/>"
 "<polygon points='60,96 52,98 57,104' fill='#c30'/>"
 "<text x='30' y='120' font-size='10'>40&deg;</text>"
 "<text x='150' y='30' font-size='10' fill='#06c'>path (no air resistance)</text>"
 "<text x='250' y='125' font-size='10'>range</text></svg>")

add(T2,
 "The graph shows how the velocity of a train varies with time over a 100 s journey between two "
 "stations. Using the graph:"
 "<ol class='parts'>"
 "<li>describe the motion in each of the three phases;</li>"
 "<li>determine the total distance travelled between the stations;</li>"
 "<li>calculate the magnitude of the (constant) deceleration in the final phase.</li></ol>",
 8,
 "<b>(a)</b> 0&ndash;20 s: uniform acceleration from rest to 24 m s<sup>&minus;1</sup>; "
 "20&ndash;70 s: constant velocity 24 m s<sup>&minus;1</sup>; "
 "70&ndash;100 s: uniform deceleration to rest.<br>"
 "<b>(b)</b> Distance = area under graph. Phase 1 (triangle) = &frac12;&times;20&times;24 = 240 m; "
 "Phase 2 (rectangle) = 50&times;24 = 1200 m; Phase 3 (triangle) = &frac12;&times;30&times;24 = 360 m. "
 "Total = 240 + 1200 + 360 = <b>1800 m</b>.<br>"
 "<b>(c)</b> Deceleration = gradient magnitude = 24/(100&minus;70) = 24/30 = "
 "<b>0.80 m s<sup>&minus;2</sup></b>.",
 "<svg width='320' height='170' viewBox='0 0 320 170'>"
 "<line x1='40' y1='140' x2='300' y2='140' stroke='#333'/>"
 "<line x1='40' y1='140' x2='40' y2='20' stroke='#333'/>"
 "<polyline points='40,140 110,50 230,50 290,140' fill='none' stroke='#06c' stroke-width='2'/>"
 "<text x='150' y='160' font-size='10'>time / s</text>"
 "<text x='2' y='80' font-size='10'>v / m s&#8315;&#185;</text>"
 "<text x='95' y='150' font-size='9'>20</text><text x='220' y='150' font-size='9'>70</text>"
 "<text x='283' y='150' font-size='9'>100</text><text x='24' y='54' font-size='9'>24</text></svg>")

add(T2,
 "A stone is dropped from rest at the top of a cliff. During the last second before it hits the sea, "
 "it falls a distance equal to one quarter of the total height of the cliff. Ignoring air resistance, "
 "determine the height of the cliff. (Take g = 9.81 m s<sup>&minus;2</sup>.)",
 7,
 "Let total fall time be T and height H = &frac12;gT&sup2;. Distance fallen in first (T&minus;1) s: "
 "&frac12;g(T&minus;1)&sup2;. The last second's fall = H &minus; &frac12;g(T&minus;1)&sup2; = &frac14;H.<br>"
 "So &frac12;g(T&minus;1)&sup2; = &frac34;H = &frac34;(&frac12;gT&sup2;). Cancel &frac12;g: "
 "(T&minus;1)&sup2; = &frac34;T&sup2; &rArr; T&minus;1 = (&radic;3/2)T = 0.8660T &rArr; "
 "0.1340T = 1 &rArr; T = 7.46 s.<br>"
 "H = &frac12; &times; 9.81 &times; 7.46&sup2; = &frac12; &times; 9.81 &times; 55.7 = "
 "<b>273 m</b> (2.7 &times; 10<sup>2</sup> m).")

add(T2,
 "Describe an experiment, using a falling object and appropriate apparatus, to determine the "
 "acceleration of free fall g. Include: the measurements taken, how they are used, one significant "
 "source of error, and how it is reduced.",
 7,
 "A steel ball is released from an electromagnet; switching off the magnet simultaneously starts an "
 "electronic timer. The ball falls a measured height h (metre rule) and strikes a trapdoor switch, "
 "stopping the timer, giving time t.<br>"
 "Using h = &frac12;gt&sup2;, a graph of h (y-axis) against t&sup2; (x-axis) is a straight line "
 "through the origin of gradient &frac12;g, so g = 2 &times; gradient. Repeating for several heights "
 "and plotting reduces random error and averages out timing scatter.<br>"
 "A significant systematic error is the delay between cutting the current and the ball actually "
 "releasing (residual magnetism), which makes t too large. This is reduced by using the graphical "
 "gradient method (a constant time offset shifts the line but changes its intercept, not its gradient), "
 "so g is unaffected.")

add(T2,
 "Two cars, A and B, travel along the same straight road. At t = 0 both are level. A moves at a "
 "constant 30 m s<sup>&minus;1</sup>. B starts from rest at t = 0 with constant acceleration "
 "4.0 m s<sup>&minus;2</sup>."
 "<ol class='parts'>"
 "<li>Find the time at which B catches up with A.</li>"
 "<li>Find the distance travelled by then.</li>"
 "<li>Find B's speed at that instant and comment on why it exceeds A's speed.</li></ol>",
 8,
 "<b>(a)</b> Equal displacement: 30t = &frac12;(4.0)t&sup2; = 2t&sup2; &rArr; 2t&sup2; &minus; 30t = 0 "
 "&rArr; t(2t &minus; 30) = 0 &rArr; t = <b>15 s</b> (rejecting t = 0).<br>"
 "<b>(b)</b> Distance = 30 &times; 15 = <b>450 m</b>.<br>"
 "<b>(c)</b> v<sub>B</sub> = 0 + 4.0&times;15 = <b>60 m s<sup>&minus;1</sup></b>. B is faster because, "
 "although they cover the same distance in the same time (so equal <i>average</i> speeds of "
 "30 m s<sup>&minus;1</sup>), B started slower and finished faster; its speed at the catch-up point is "
 "twice the average, i.e. 60 m s<sup>&minus;1</sup>.")

add(T2,
 "A displacement&ndash;time graph for an object moving in a straight line is a smooth curve. "
 "State how you would obtain, from such a graph, (i) the instantaneous velocity at a point and "
 "(ii) the instantaneous acceleration. Explain why the second is harder to obtain accurately.",
 6,
 "<b>(i)</b> The instantaneous velocity is the gradient of the tangent to the s&ndash;t curve at that "
 "point (draw the tangent, take &Delta;s/&Delta;t over a large span of the tangent line).<br>"
 "<b>(ii)</b> Acceleration is the rate of change of velocity, so first obtain velocities at several "
 "points (tangent gradients), plot a v&ndash;t graph, and take the gradient of <i>that</i> graph.<br>"
 "It is harder/less accurate because it requires differentiating twice: each tangent drawn by eye "
 "carries appreciable uncertainty, and taking the gradient of a graph that is itself built from "
 "uncertain gradients compounds the error.")

add(T2,
 "A projectile is launched horizontally from the top of a tower of height 45 m with speed "
 "18 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the time to reach the ground.</li>"
 "<li>Calculate the horizontal distance from the base of the tower where it lands.</li>"
 "<li>Determine the angle the velocity makes with the horizontal on landing.</li></ol>",
 7,
 "<b>(a)</b> Vertical: 45 = &frac12;(9.81)t&sup2; &rArr; t&sup2; = 9.174 &rArr; t = <b>3.03 s</b>.<br>"
 "<b>(b)</b> Horizontal distance = 18 &times; 3.03 = <b>54.5 m</b>.<br>"
 "<b>(c)</b> v<sub>y</sub> = gt = 9.81 &times; 3.03 = 29.7 m s<sup>&minus;1</sup>; v<sub>x</sub> = 18. "
 "Angle below horizontal = tan<sup>&minus;1</sup>(29.7/18) = <b>58.8&deg;</b>.")

add(T2,
 "Explain, in terms of the independence of horizontal and vertical motion, why a bullet fired "
 "horizontally and a bullet dropped from the same height at the same instant reach the ground at "
 "the same time (ignoring air resistance and Earth's curvature). State what would change if air "
 "resistance were significant.",
 6,
 "Vertical and horizontal motions are independent. Both bullets start with zero vertical velocity and "
 "experience the same downward acceleration g; the horizontal velocity of the fired bullet has no "
 "vertical component and does not affect the vertical motion. Hence both take the same time "
 "t = &radic;(2h/g) to fall the same height h and land together.<br>"
 "With significant air resistance, the drag force acts opposite to the actual velocity, which for the "
 "fast horizontally-moving bullet has an upward vertical component; this reduces its vertical "
 "acceleration, so the fired bullet would take slightly <b>longer</b> to land, and the two would no "
 "longer land simultaneously.")

add(T2,
 "A car accelerates uniformly from 8.0 m s<sup>&minus;1</sup> to 20 m s<sup>&minus;1</sup> while "
 "travelling 168 m."
 "<ol class='parts'>"
 "<li>Calculate the acceleration.</li>"
 "<li>Calculate the time taken.</li>"
 "<li>Calculate the distance travelled during the final 2.0 s of this period.</li></ol>",
 8,
 "<b>(a)</b> v&sup2; = u&sup2; + 2as: 20&sup2; = 8.0&sup2; + 2a(168) &rArr; 400 = 64 + 336a &rArr; "
 "a = 336/336 = <b>1.00 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> v = u + at: 20 = 8.0 + 1.00t &rArr; t = <b>12 s</b>.<br>"
 "<b>(c)</b> Final 2.0 s is from t = 10 s to 12 s. At t = 10 s, v = 8.0 + 1.00&times;10 = 18 m s<sup>&minus;1</sup>. "
 "Distance = 18(2.0) + &frac12;(1.00)(2.0)&sup2; = 36 + 2.0 = <b>38 m</b>.")

add(T2,
 "The velocity&ndash;time graph shown consists of a curve whose gradient decreases with time, "
 "levelling off to a horizontal asymptote. State what kind of motion this represents, sketch the "
 "corresponding acceleration&ndash;time graph, and identify a real physical situation the graph could "
 "describe.",
 6,
 "The velocity increases but at a decreasing rate, approaching a constant (maximum) value &mdash; "
 "the object approaches a <b>terminal velocity</b>. The acceleration (gradient of v&ndash;t) starts "
 "large and positive and decreases towards zero: an a&ndash;t graph that is a decaying curve from a "
 "high value at t = 0 down to a = 0.<br>"
 "Physical situation: an object (e.g. a skydiver or a ball bearing) falling through a fluid under gravity "
 "with a drag force that increases with speed, until drag equals weight and the resultant force "
 "(hence acceleration) becomes zero.",
 "<svg width='300' height='130' viewBox='0 0 300 130'>"
 "<line x1='30' y1='110' x2='150' y2='110' stroke='#333'/>"
 "<line x1='30' y1='110' x2='30' y2='15' stroke='#333'/>"
 "<path d='M30 110 C70 40 110 30 145 30' fill='none' stroke='#06c' stroke-width='2'/>"
 "<line x1='30' y1='30' x2='145' y2='30' stroke='#999' stroke-dasharray='3 3'/>"
 "<text x='60' y='125' font-size='9'>v&ndash;t</text>"
 "<line x1='175' y1='110' x2='295' y2='110' stroke='#333'/>"
 "<line x1='175' y1='110' x2='175' y2='15' stroke='#333'/>"
 "<path d='M175 25 C205 95 240 108 290 109' fill='none' stroke='#c30' stroke-width='2'/>"
 "<text x='205' y='125' font-size='9'>a&ndash;t</text></svg>")

add(T2,
 "A ball is thrown vertically upward from a height of 1.5 m above the ground with an initial speed of "
 "12 m s<sup>&minus;1</sup>. Taking upward as positive and g = 9.81 m s<sup>&minus;2</sup>:"
 "<ol class='parts'>"
 "<li>find the total time before it strikes the ground;</li>"
 "<li>find its speed just before impact;</li>"
 "<li>sketch (with values) the velocity&ndash;time graph for the whole motion.</li></ol>",
 8,
 "Take the ground as displacement s = &minus;1.5 m relative to the launch point.<br>"
 "<b>(a)</b> s = ut + &frac12;at&sup2;: &minus;1.5 = 12t &minus; 4.905t&sup2;. "
 "Rearranged: 4.905t&sup2; &minus; 12t &minus; 1.5 = 0. "
 "t = [12 &plusmn; &radic;(144 + 29.43)]/(9.81) = [12 &plusmn; 13.17]/9.81. "
 "Take positive root: t = 25.17/9.81 = <b>2.57 s</b>.<br>"
 "<b>(b)</b> v = u + at = 12 &minus; 9.81&times;2.57 = &minus;13.2 m s<sup>&minus;1</sup>, "
 "i.e. speed <b>13.2 m s<sup>&minus;1</sup></b> downward. (Check: v&sup2; = 12&sup2; + 2(9.81)(1.5) "
 "= 144 + 29.4 = 173.4, v = 13.2.)<br>"
 "<b>(c)</b> A straight line of constant negative gradient (&minus;9.81 m s<sup>&minus;2</sup>) "
 "starting at +12 m s<sup>&minus;1</sup>, crossing v = 0 at t = 1.22 s (top of flight), reaching "
 "&minus;13.2 m s<sup>&minus;1</sup> at t = 2.57 s.")

add(T2,
 "An object moves so that its displacement is given by successive equal time intervals of 1.0 s: "
 "the distances travelled in the 1st, 2nd, 3rd and 4th seconds are 5, 15, 25 and 35 m respectively. "
 "<ol class='parts'>"
 "<li>Show that the motion is uniformly accelerated and find the acceleration.</li>"
 "<li>Find the initial velocity.</li></ol>",
 7,
 "For uniform acceleration from initial velocity u, the distance in the n-th second is "
 "s<sub>n</sub> = u + &frac12;a(2n&minus;1). The differences between consecutive seconds are constant: "
 "15&minus;5 = 10, 25&minus;15 = 10, 35&minus;25 = 10 m. A constant difference confirms uniform "
 "acceleration.<br>"
 "<b>(a)</b> The common difference equals a &times; (1.0 s)&sup2;... more precisely s<sub>n+1</sub> "
 "&minus; s<sub>n</sub> = a(&Delta;t)&sup2; with &Delta;t = 1 s? Using s<sub>n</sub> = u + &frac12;a(2n&minus;1): "
 "difference = a. So <b>a = 10 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> 1st second: s<sub>1</sub> = u + &frac12;a = u + 5 = 5 &rArr; <b>u = 0</b> "
 "(the object starts from rest).")

add(T2,
 "A cyclist travels the first half of a straight journey at 6.0 m s<sup>&minus;1</sup> and the second "
 "half (equal distance) at 12 m s<sup>&minus;1</sup>. Later the cyclist repeats the journey travelling "
 "at 6.0 m s<sup>&minus;1</sup> for the first half of the <i>time</i> and 12 m s<sup>&minus;1</sup> for "
 "the second half of the time."
 "<ol class='parts'>"
 "<li>Find the average speed for the equal-distance journey.</li>"
 "<li>Find the average speed for the equal-time journey.</li>"
 "<li>Explain which is larger and why.</li></ol>",
 8,
 "<b>(a)</b> For equal distances d each: total distance 2d, total time = d/6 + d/12 = d(2+1)/12 = 3d/12 = d/4. "
 "Average = 2d/(d/4) = <b>8.0 m s<sup>&minus;1</sup></b> (the harmonic mean).<br>"
 "<b>(b)</b> For equal times T each: distances 6T and 12T, total 18T over 2T. "
 "Average = 18T/2T = <b>9.0 m s<sup>&minus;1</sup></b> (the arithmetic mean).<br>"
 "<b>(c)</b> The equal-time average (9.0) is larger. In the equal-distance case more time is spent at "
 "the slower speed (it takes longer to cover the slow half), which weights the average towards the "
 "lower speed; the arithmetic mean is always &ge; the harmonic mean.")

add(T2,
 "During a tennis serve the ball is struck at a height of 2.4 m and travels horizontally (initially) "
 "at 40 m s<sup>&minus;1</sup> towards the net 12 m away. The net is 0.91 m high. Ignoring air "
 "resistance and any vertical launch component, determine whether the ball clears the net, and by "
 "what margin.",
 7,
 "Horizontal: time to reach the net t = 12/40 = 0.30 s.<br>"
 "Vertical drop in this time: &Delta;y = &frac12;gt&sup2; = &frac12;(9.81)(0.30)&sup2; "
 "= &frac12;(9.81)(0.090) = 0.441 m.<br>"
 "Height of ball at net = 2.4 &minus; 0.441 = 1.96 m.<br>"
 "Since 1.96 m &gt; 0.91 m, the ball <b>clears the net</b>, by 1.96 &minus; 0.91 = "
 "<b>1.05 m</b> (&asymp; 1.0 m).")

add(T2,
 "A lift (elevator) starts from rest, accelerates upward at 1.2 m s<sup>&minus;2</sup> for 3.0 s, "
 "then moves at constant velocity for 5.0 s, then decelerates uniformly to rest in a further 2.0 s."
 "<ol class='parts'>"
 "<li>Sketch the velocity&ndash;time graph.</li>"
 "<li>Find the total distance travelled.</li>"
 "<li>Find the average velocity for the whole journey.</li></ol>",
 8,
 "Peak velocity v = 0 + 1.2&times;3.0 = 3.6 m s<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> Straight rise 0 &rarr; 3.6 m s<sup>&minus;1</sup> over 0&ndash;3 s; flat at 3.6 over "
 "3&ndash;8 s; straight fall 3.6 &rarr; 0 over 8&ndash;10 s.<br>"
 "<b>(b)</b> Areas: accel &frac12;(3.0)(3.6) = 5.4 m; constant (5.0)(3.6) = 18.0 m; "
 "decel &frac12;(2.0)(3.6) = 3.6 m. Total = <b>27 m</b>.<br>"
 "<b>(c)</b> Total time = 10 s, so average velocity = 27/10 = <b>2.7 m s<sup>&minus;1</sup></b> upward.")

add(T2,
 "A particle is projected up a smooth plane inclined at 25&deg; to the horizontal with an initial speed "
 "of 9.0 m s<sup>&minus;1</sup> along the plane. The component of gravitational acceleration along the "
 "plane is g sin25&deg;."
 "<ol class='parts'>"
 "<li>Find the distance travelled up the plane before it momentarily stops.</li>"
 "<li>Find the time taken to return to its starting point.</li></ol>",
 7,
 "Deceleration along plane a = g sin25&deg; = 9.81 &times; 0.4226 = 4.15 m s<sup>&minus;2</sup>.<br>"
 "<b>(a)</b> v&sup2; = u&sup2; &minus; 2as, v = 0: s = u&sup2;/(2a) = 9.0&sup2;/(2&times;4.15) "
 "= 81/8.30 = <b>9.76 m</b> (&asymp; 9.8 m).<br>"
 "<b>(b)</b> Time up: t<sub>up</sub> = u/a = 9.0/4.15 = 2.17 s. By symmetry (smooth plane), time down "
 "equals time up, so total time = 2 &times; 2.17 = <b>4.34 s</b> (&asymp; 4.3 s).")


# ===========================================================================
# TOPIC 3  Dynamics  (18 questions)
# ===========================================================================
T3 = "3&nbsp;&nbsp;Dynamics"

add(T3,
 "State Newton's second law in terms of momentum. A jet of water from a hose leaves a nozzle of "
 "cross-sectional area 4.0 &times; 10<sup>&minus;4</sup> m&sup2; at a speed of 25 m s<sup>&minus;1</sup> "
 "and strikes a vertical wall at right angles, running down the wall without rebounding. "
 "(Density of water = 1.0 &times; 10<sup>3</sup> kg m<sup>&minus;3</sup>.)"
 "<ol class='parts'>"
 "<li>Calculate the mass of water hitting the wall per second.</li>"
 "<li>Calculate the force exerted on the wall.</li></ol>",
 7,
 "Newton's second law: the resultant force on a body equals the rate of change of its momentum, "
 "F = &Delta;p/&Delta;t (in the direction of the force).<br>"
 "<b>(a)</b> Mass per second = &rho;Av = 1.0&times;10<sup>3</sup> &times; 4.0&times;10<sup>&minus;4</sup> "
 "&times; 25 = <b>10 kg s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> The water's horizontal velocity changes from 25 m s<sup>&minus;1</sup> to 0 (it does not "
 "rebound). Rate of change of momentum = (mass/s) &times; &Delta;v = 10 &times; 25 = <b>250 N</b>. "
 "By Newton's third law the wall pushes back on the water with 250 N, so the water exerts 250 N on "
 "the wall.")

add(T3,
 "A trolley of mass 0.80 kg moving at 3.0 m s<sup>&minus;1</sup> collides head-on with a stationary "
 "trolley of mass 1.2 kg. After the collision they move off separately; the 0.80 kg trolley continues "
 "in the same direction at 0.60 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Find the velocity of the 1.2 kg trolley after the collision.</li>"
 "<li>Determine whether the collision is elastic, showing your working.</li></ol>",
 8,
 "<b>(a)</b> Conservation of momentum: 0.80(3.0) = 0.80(0.60) + 1.2v. "
 "2.40 = 0.48 + 1.2v &rArr; v = 1.92/1.2 = <b>1.6 m s<sup>&minus;1</sup></b> (same direction).<br>"
 "<b>(b)</b> KE before = &frac12;(0.80)(3.0)&sup2; = 3.60 J. "
 "KE after = &frac12;(0.80)(0.60)&sup2; + &frac12;(1.2)(1.6)&sup2; = 0.144 + 1.536 = 1.68 J. "
 "KE is not conserved (3.60 J &rarr; 1.68 J), so the collision is <b>inelastic</b>. "
 "(Alternatively: relative speed of approach 3.0 vs relative speed of separation 1.6&minus;0.6 = 1.0 "
 "&mdash; not equal, so inelastic.)")

add(T3,
 "A ball of mass 0.15 kg strikes a wall horizontally at 8.0 m s<sup>&minus;1</sup> and rebounds "
 "horizontally at 6.0 m s<sup>&minus;1</sup>. The contact time is 0.020 s."
 "<ol class='parts'>"
 "<li>Calculate the magnitude of the change in momentum of the ball.</li>"
 "<li>Calculate the average force exerted by the wall on the ball.</li>"
 "<li>State the force exerted by the ball on the wall and justify it.</li></ol>",
 7,
 "Take the initial direction as positive.<br>"
 "<b>(a)</b> &Delta;p = m(v &minus; u) = 0.15(&minus;6.0 &minus; 8.0) = 0.15(&minus;14.0) "
 "= &minus;2.10 kg m s<sup>&minus;1</sup>; magnitude <b>2.1 kg m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> F = &Delta;p/&Delta;t = 2.10/0.020 = <b>105 N</b> (directed away from the wall).<br>"
 "<b>(c)</b> By Newton's third law the ball exerts an equal and opposite force of <b>105 N</b> on the "
 "wall, directed into the wall. The two forces act on different bodies, are equal in magnitude, "
 "opposite in direction and of the same type (contact).")

add(T3,
 "Explain, using Newton's laws, why a person of weight 700 N standing in a lift experiences a "
 "different reading on bathroom scales placed under their feet when the lift (a) accelerates upward "
 "at 2.0 m s<sup>&minus;2</sup> and (b) accelerates downward at 2.0 m s<sup>&minus;2</sup>. "
 "Calculate the scale readings.",
 8,
 "The scales read the normal contact force N they exert on the person (Newton's third law). "
 "Mass m = 700/9.81 = 71.4 kg. Resultant force = ma (Newton's second law), with up positive.<br>"
 "<b>(a)</b> N &minus; mg = ma &rArr; N = m(g + a) = 71.4(9.81 + 2.0) = 71.4 &times; 11.81 = "
 "<b>843 N</b>. The reading increases because an upward resultant force is needed, so N must exceed "
 "the weight.<br>"
 "<b>(b)</b> N &minus; mg = m(&minus;a) &rArr; N = m(g &minus; a) = 71.4(9.81 &minus; 2.0) "
 "= 71.4 &times; 7.81 = <b>558 N</b>. The reading decreases because the resultant force is downward, "
 "so N is less than the weight.")

add(T3,
 "A rocket works by ejecting exhaust gas. In a test, a rocket ejects gas at a rate of "
 "45 kg s<sup>&minus;1</sup> with a speed of 1200 m s<sup>&minus;1</sup> relative to the rocket."
 "<ol class='parts'>"
 "<li>Calculate the thrust produced.</li>"
 "<li>If the rocket has an initial total mass of 6.0 &times; 10<sup>3</sup> kg, find its initial "
 "acceleration at lift-off (vertically upward).</li></ol>",
 7,
 "<b>(a)</b> Thrust = rate of change of momentum of the exhaust = (dm/dt)v "
 "= 45 &times; 1200 = 54000 N = <b>5.4 &times; 10<sup>4</sup> N</b>.<br>"
 "<b>(b)</b> Weight = mg = 6.0&times;10<sup>3</sup> &times; 9.81 = 5.886&times;10<sup>4</sup> N. "
 "Resultant upward force = thrust &minus; weight = 5.4&times;10<sup>4</sup> &minus; 5.886&times;10<sup>4</sup> "
 "= &minus;4.86&times;10<sup>3</sup> N. This is negative, so the rocket <b>cannot lift off</b> initially "
 "(thrust &lt; weight); acceleration would only become positive once enough fuel has burned to reduce "
 "the weight below the thrust.")

add(T3,
 "Two ice skaters, of masses 60 kg and 45 kg, stand at rest facing each other and push apart. "
 "The 60 kg skater moves off at 1.5 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Find the speed of the 45 kg skater.</li>"
 "<li>Find the total kinetic energy generated and state where it came from.</li>"
 "<li>State the total momentum of the system after the push and explain your answer.</li></ol>",
 7,
 "<b>(a)</b> Momentum conserved (initially zero): 0 = 60(1.5) + 45(&minus;v) &rArr; "
 "v = 90/45 = <b>2.0 m s<sup>&minus;1</sup></b> in the opposite direction.<br>"
 "<b>(b)</b> KE = &frac12;(60)(1.5)&sup2; + &frac12;(45)(2.0)&sup2; = 67.5 + 90 = <b>157.5 J</b>. "
 "This came from chemical (stored) energy in the skaters' muscles, converted to kinetic energy.<br>"
 "<b>(c)</b> The total momentum after the push is <b>zero</b>, the same as before. There is no "
 "external resultant horizontal force (the ice is frictionless), so by conservation of momentum the "
 "vector sum of the two equal-and-opposite momenta remains zero.")

add(T3,
 "A ball A of mass m moving at speed u makes a one-dimensional elastic collision with a stationary "
 "ball B of mass 3m. Using conservation of momentum and the elastic-collision condition, determine "
 "the velocities of A and B after the collision in terms of u, and comment on the direction of A's "
 "motion.",
 8,
 "Let final velocities be v<sub>A</sub> and v<sub>B</sub>.<br>"
 "Momentum: mu = mv<sub>A</sub> + 3mv<sub>B</sub> &rArr; u = v<sub>A</sub> + 3v<sub>B</sub>.<br>"
 "Elastic &rArr; relative speed of approach = relative speed of separation: "
 "u = v<sub>B</sub> &minus; v<sub>A</sub>.<br>"
 "Subtract: from the two equations, adding v<sub>A</sub>: substitute v<sub>A</sub> = v<sub>B</sub> &minus; u "
 "into the first: u = (v<sub>B</sub> &minus; u) + 3v<sub>B</sub> = 4v<sub>B</sub> &minus; u &rArr; "
 "v<sub>B</sub> = u/2. Then v<sub>A</sub> = u/2 &minus; u = <b>&minus;u/2</b>.<br>"
 "So B moves off at <b>u/2</b> forward, and A <b>rebounds backward at u/2</b>. Since B is more "
 "massive than A, A bounces back &mdash; consistent with an elastic collision with a heavier target.")

add(T3,
 "Define linear momentum and state the principle of conservation of momentum, including the "
 "condition under which it applies. Explain how this principle is consistent with Newton's third law "
 "for two interacting bodies.",
 6,
 "Linear momentum p = mv, the product of an object's mass and its velocity (a vector). "
 "The principle of conservation of momentum states that the total momentum of a system of "
 "interacting bodies remains constant provided no resultant <b>external</b> force acts on the system.<br>"
 "Consistency with Newton's third law: during an interaction, body 1 exerts force F on body 2 and, by "
 "the third law, body 2 exerts &minus;F on body 1. These act for the same time t, so the impulses are "
 "Ft and &minus;Ft &mdash; equal and opposite. The momentum gained by one equals the momentum lost "
 "by the other, so the total momentum is unchanged.")

add(T3,
 "An object of mass 2.0 kg experiences a resultant force that varies with time as shown: the force "
 "rises linearly from 0 to 12 N over the first 4.0 s, then stays constant at 12 N for the next 3.0 s. "
 "The object starts from rest."
 "<ol class='parts'>"
 "<li>Use the area under the force&ndash;time graph to find the impulse over the 7.0 s.</li>"
 "<li>Hence find the final velocity.</li></ol>",
 7,
 "<b>(a)</b> Impulse = area under F&ndash;t graph. Triangle (0&ndash;4 s): &frac12;(4.0)(12) = 24 N s. "
 "Rectangle (4&ndash;7 s): (3.0)(12) = 36 N s. Total impulse = 24 + 36 = <b>60 N s</b>.<br>"
 "<b>(b)</b> Impulse = change in momentum = m&Delta;v: 60 = 2.0 &times; v (starts from rest) &rArr; "
 "v = <b>30 m s<sup>&minus;1</sup></b>.",
 "<svg width='300' height='150' viewBox='0 0 300 150'>"
 "<line x1='40' y1='120' x2='280' y2='120' stroke='#333'/>"
 "<line x1='40' y1='120' x2='40' y2='20' stroke='#333'/>"
 "<polyline points='40,120 160,40 280,40' fill='none' stroke='#06c' stroke-width='2'/>"
 "<line x1='160' y1='120' x2='160' y2='40' stroke='#999' stroke-dasharray='3 3'/>"
 "<text x='150' y='138' font-size='10'>time / s</text>"
 "<text x='6' y='75' font-size='10'>F / N</text>"
 "<text x='150' y='133' font-size='9'>4.0</text><text x='272' y='133' font-size='9'>7.0</text>"
 "<text x='20' y='45' font-size='9'>12</text></svg>")

add(T3,
 "A raindrop falling through still air reaches a terminal velocity."
 "<ol class='parts'>"
 "<li>Explain, in terms of the forces acting, how terminal velocity is reached.</li>"
 "<li>Sketch and describe the acceleration&ndash;time graph from the instant the drop starts to fall.</li>"
 "<li>State and explain what happens to the terminal velocity if the drop coalesces with others to "
 "form a larger drop.</li></ol>",
 8,
 "<b>(a)</b> Initially only weight acts, so acceleration = g. As speed increases, the drag "
 "(air-resistance) force increases. The resultant force (weight &minus; drag) decreases, so the "
 "acceleration decreases. When drag has grown equal to weight, the resultant force is zero, "
 "acceleration is zero and the drop falls at constant (terminal) velocity.<br>"
 "<b>(b)</b> Acceleration starts at g (&asymp; 9.81 m s<sup>&minus;2</sup>) and decreases as a decaying "
 "curve towards zero (never negative).<br>"
 "<b>(c)</b> A larger drop has a greater weight-to-drag ratio (weight &prop; volume &prop; r&sup3;, "
 "while drag depends on a lower power of r, roughly the cross-sectional area &prop; r&sup2;). A greater "
 "speed is therefore needed before drag balances weight, so the terminal velocity <b>increases</b>.")

add(T3,
 "A 1500 kg car travelling at 20 m s<sup>&minus;1</sup> collides with and sticks to a stationary "
 "900 kg car (a perfectly inelastic collision). The combined wreck then slides to rest on a road for "
 "which the constant resistive (frictional) force is 8.4 &times; 10<sup>3</sup> N."
 "<ol class='parts'>"
 "<li>Find the common velocity immediately after impact.</li>"
 "<li>Find the distance the wreck slides before stopping.</li>"
 "<li>Find the kinetic energy lost in the collision itself.</li></ol>",
 9,
 "<b>(a)</b> Momentum: 1500(20) = (1500 + 900)v &rArr; 30000 = 2400v &rArr; "
 "v = <b>12.5 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> KE after impact = &frac12;(2400)(12.5)&sup2; = 1.875&times;10<sup>5</sup> J. "
 "Work done against friction = Fd: 8.4&times;10<sup>3</sup> &times; d = 1.875&times;10<sup>5</sup> &rArr; "
 "d = <b>22.3 m</b>.<br>"
 "<b>(c)</b> KE before impact = &frac12;(1500)(20)&sup2; = 3.00&times;10<sup>5</sup> J. "
 "KE lost in collision = 3.00&times;10<sup>5</sup> &minus; 1.875&times;10<sup>5</sup> "
 "= <b>1.13&times;10<sup>5</sup> J</b> (transferred to heat, sound and deformation).")

add(T3,
 "A particle of mass 2.0 kg moving at 4.0 m s<sup>&minus;1</sup> along the +x direction collides with "
 "a 3.0 kg particle at rest. After the collision the 2.0 kg particle moves at 2.0 m s<sup>&minus;1</sup> "
 "at 60&deg; above the +x axis. Using conservation of momentum in two dimensions, find the velocity "
 "(magnitude and direction) of the 3.0 kg particle after the collision.",
 9,
 "Momentum conserved in x and y. Before: p<sub>x</sub> = 2.0&times;4.0 = 8.0, p<sub>y</sub> = 0.<br>"
 "2.0 kg after: v<sub>x</sub> = 2.0 cos60&deg; = 1.0, v<sub>y</sub> = 2.0 sin60&deg; = 1.732 m s<sup>&minus;1</sup>. "
 "Its momentum: (2.0, 3.46) kg m s<sup>&minus;1</sup>.<br>"
 "3.0 kg particle momentum = total &minus; that of 2.0 kg: "
 "x: 8.0 &minus; 2.0 = 6.0; y: 0 &minus; 3.46 = &minus;3.46 kg m s<sup>&minus;1</sup>.<br>"
 "Speed = &radic;(6.0&sup2; + 3.46&sup2;)/3.0 = &radic;(36 + 12.0)/3.0 = &radic;48/3.0 "
 "= 6.93/3.0 = <b>2.3 m s<sup>&minus;1</sup></b>. "
 "Direction = tan<sup>&minus;1</sup>(3.46/6.0) = <b>30&deg; below the +x axis</b>.")

add(T3,
 "A constant horizontal force of 50 N is applied to a 12 kg box on a rough horizontal floor. The box "
 "accelerates at 2.5 m s<sup>&minus;2</sup>."
 "<ol class='parts'>"
 "<li>Find the frictional force acting on the box.</li>"
 "<li>The force is then removed. Find the deceleration of the box, assuming the frictional force is "
 "unchanged, and the distance it travels before stopping if it was moving at 6.0 m s<sup>&minus;1</sup> "
 "when the force was removed.</li></ol>",
 8,
 "<b>(a)</b> Resultant = ma = 12 &times; 2.5 = 30 N. Applied 50 N, so friction = 50 &minus; 30 = "
 "<b>20 N</b> (opposing motion).<br>"
 "<b>(b)</b> With the applied force removed, only friction acts: deceleration = F/m = 20/12 = "
 "1.67 m s<sup>&minus;2</sup>. Distance: v&sup2; = u&sup2; &minus; 2as, 0 = 6.0&sup2; &minus; 2(1.67)s "
 "&rArr; s = 36/3.33 = <b>10.8 m</b>.")

add(T3,
 "Explain the distinction between mass and weight. A probe of mass 250 kg is taken to a planet where "
 "the gravitational field strength is 3.7 N kg<sup>&minus;1</sup>. "
 "<ol class='parts'>"
 "<li>State its mass and calculate its weight on the planet.</li>"
 "<li>Calculate the resultant force and acceleration if a 1200 N thrust acts vertically upward on the "
 "probe at the planet's surface.</li></ol>",
 7,
 "Mass is the quantity of matter / the property resisting change in motion (a scalar, in kg), the same "
 "everywhere. Weight is the gravitational force on the mass, W = mg, a vector in N that depends on the "
 "local field strength.<br>"
 "<b>(a)</b> Mass = <b>250 kg</b> (unchanged). Weight = mg = 250 &times; 3.7 = <b>925 N</b>.<br>"
 "<b>(b)</b> Resultant (up positive) = 1200 &minus; 925 = 275 N upward. "
 "Acceleration = 275/250 = <b>1.1 m s<sup>&minus;2</sup></b> upward.")

add(T3,
 "A chain of total mass 3.0 kg and length 2.0 m hangs vertically with its lower end just touching a "
 "table. It is released and falls; as it lands, the links come to rest on the table. Consider the "
 "instant when a length x of chain has already landed."
 "<ol class='parts'>"
 "<li>Explain why the force the table exerts on the chain is greater than the weight of the chain "
 "already at rest on it.</li>"
 "<li>Outline the two contributions to this force.</li></ol>",
 6,
 "<b>(a)</b> As well as supporting the weight of the stationary chain already on it, the table must "
 "also bring the moving links to rest as they arrive, i.e. it exerts a force to change their momentum "
 "(F = rate of change of momentum). This extra impulsive force makes the total force exceed the "
 "static weight of the landed portion.<br>"
 "<b>(b)</b> (i) The <b>weight</b> of the length x already lying on the table, (&rho;<sub>L</sub>x)g "
 "where &rho;<sub>L</sub> = mass per unit length; (ii) the <b>rate of change of momentum</b> of the "
 "links arriving each second, (&rho;<sub>L</sub>v)&times;v = &rho;<sub>L</sub>v&sup2;, where v is the "
 "speed of the arriving links. The total is the sum of these two terms.")

add(T3,
 "State Newton's first law. A book rests on a table. Identify the forces on the book, state which "
 "pairs are Newton's-third-law pairs, and explain why the upward push of the table on the book and "
 "the weight of the book are <b>not</b> a Newton's-third-law pair even though they are equal and "
 "opposite here.",
 6,
 "Newton's first law: an object continues at rest or at constant velocity unless acted on by a "
 "resultant external force.<br>"
 "Forces on the book: its weight W (Earth pulling book down) and the normal contact force N (table "
 "pushing book up).<br>"
 "Third-law pairs: (i) Earth pulls book down (W) &harr; book pulls Earth up with equal force; "
 "(ii) table pushes book up (N) &harr; book pushes table down with equal force.<br>"
 "N and W are not a third-law pair because they act on the <b>same</b> body (the book), are forces of "
 "different types (contact vs gravitational), and involve only the book&ndash;Earth or book&ndash;table "
 "interactions separately. They are equal here only because the book is in equilibrium (first law), "
 "not because of the third law &mdash; if the table accelerated, N would no longer equal W.")

add(T3,
 "Two gliders on a frictionless air track approach each other: glider P (0.30 kg) moves right at "
 "0.80 m s<sup>&minus;1</sup>; glider Q (0.50 kg) moves left at 0.40 m s<sup>&minus;1</sup>. They "
 "collide and the collision is perfectly elastic. Find the velocity of each glider after the collision.",
 9,
 "Take right as positive. Momentum: 0.30(0.80) + 0.50(&minus;0.40) = 0.24 &minus; 0.20 = 0.04 kg m s<sup>&minus;1</sup>. "
 "So 0.30v<sub>P</sub> + 0.50v<sub>Q</sub> = 0.04. &nbsp;(1)<br>"
 "Elastic: relative speed of approach = relative speed of separation. "
 "Approach = 0.80 &minus; (&minus;0.40) = 1.20 m s<sup>&minus;1</sup>. So v<sub>Q</sub> &minus; v<sub>P</sub> = 1.20. &nbsp;(2)<br>"
 "From (2) v<sub>Q</sub> = v<sub>P</sub> + 1.20. Sub into (1): 0.30v<sub>P</sub> + 0.50(v<sub>P</sub> + 1.20) = 0.04 "
 "&rArr; 0.80v<sub>P</sub> + 0.60 = 0.04 &rArr; v<sub>P</sub> = &minus;0.56/0.80 = <b>&minus;0.70 m s<sup>&minus;1</sup></b> "
 "(P moves left at 0.70). v<sub>Q</sub> = &minus;0.70 + 1.20 = <b>+0.50 m s<sup>&minus;1</sup></b> (Q moves right). "
 "Check KE: before 0.096 + 0.040 = 0.136 J; after &frac12;(0.30)(0.70)&sup2; + &frac12;(0.50)(0.50)&sup2; "
 "= 0.0735 + 0.0625 = 0.136 J &mdash; conserved. &#10003;")

add(T3,
 "A fireworks shell of mass 2.0 kg is moving vertically upward at 15 m s<sup>&minus;1</sup> when it "
 "explodes into two fragments. One fragment of mass 0.80 kg is thrown vertically downward at "
 "12 m s<sup>&minus;1</sup> immediately after the explosion."
 "<ol class='parts'>"
 "<li>Find the velocity of the other fragment immediately after the explosion.</li>"
 "<li>State and justify the total momentum immediately before and after the explosion.</li></ol>",
 7,
 "Take upward positive. Mass of second fragment = 2.0 &minus; 0.80 = 1.20 kg.<br>"
 "<b>(a)</b> Momentum: 2.0(15) = 0.80(&minus;12) + 1.20v &rArr; 30 = &minus;9.6 + 1.20v &rArr; "
 "1.20v = 39.6 &rArr; v = <b>+33 m s<sup>&minus;1</sup></b> (upward).<br>"
 "<b>(b)</b> The total momentum is 30 kg m s<sup>&minus;1</sup> upward both immediately before and "
 "immediately after. During the very short explosion the internal forces are far larger than the "
 "external force (gravity), so to a good approximation there is no external impulse and momentum is "
 "conserved.")


# ===========================================================================
# TOPIC 4  Forces, density and pressure  (13 questions)
# ===========================================================================
T4 = "4&nbsp;&nbsp;Forces, density and pressure"

add(T4,
 "A uniform beam AB of weight 240 N and length 3.0 m is pivoted at a point 1.0 m from end A. A load "
 "of weight W hangs from end A, and a downward force is applied at end B to keep the beam "
 "horizontal and in equilibrium."
 "<ol class='parts'>"
 "<li>Taking moments about the pivot, find the relationship needed for equilibrium if no force acts "
 "at B and only W balances the beam's weight.</li>"
 "<li>Hence find the value of W that keeps the beam horizontal with no force at B.</li></ol>",
 7,
 "The beam's weight (240 N) acts at its centre of gravity, the midpoint, which is 1.5 m from A, i.e. "
 "0.5 m to the right of the pivot. W acts at A, 1.0 m to the left of the pivot.<br>"
 "<b>(a)</b> Principle of moments about the pivot: clockwise moment = anticlockwise moment. "
 "Anticlockwise (W at A): W &times; 1.0. Clockwise (weight at centre): 240 &times; 0.5.<br>"
 "<b>(b)</b> W &times; 1.0 = 240 &times; 0.5 = 120 &rArr; <b>W = 120 N</b>.",
 "<svg width='320' height='120' viewBox='0 0 320 120'>"
 "<rect x='30' y='55' width='260' height='10' fill='#cda434' stroke='#333'/>"
 "<polygon points='116,66 106,96 126,96' fill='#555'/>"
 "<line x1='30' y1='65' x2='30' y2='100' stroke='#c30' stroke-width='2'/>"
 "<polygon points='30,100 26,92 34,92' fill='#c30'/>"
 "<line x1='160' y1='65' x2='160' y2='95' stroke='#093' stroke-width='2'/>"
 "<polygon points='160,95 156,87 164,87' fill='#093'/>"
 "<text x='24' y='50' font-size='10'>A</text><text x='286' y='50' font-size='10'>B</text>"
 "<text x='18' y='112' font-size='9' fill='#c30'>W</text>"
 "<text x='150' y='112' font-size='9' fill='#093'>240 N</text>"
 "<text x='100' y='110' font-size='9'>pivot</text></svg>")

add(T4,
 "Define the <b>moment of a force</b> and the <b>torque of a couple</b>. A steering wheel of diameter "
 "0.36 m is turned by a driver applying two equal, oppositely-directed tangential forces of 15 N at "
 "opposite ends of a diameter."
 "<ol class='parts'>"
 "<li>Calculate the torque of the couple.</li>"
 "<li>Explain why a couple produces rotation but no translational acceleration.</li></ol>",
 6,
 "The moment of a force about a point = force &times; perpendicular distance from the point to the "
 "line of action of the force. The torque of a couple = one force &times; the perpendicular distance "
 "between the two forces.<br>"
 "<b>(a)</b> Separation = diameter = 0.36 m. Torque = 15 &times; 0.36 = <b>5.4 N m</b>.<br>"
 "<b>(b)</b> A couple consists of two equal and opposite forces, so their vector sum (resultant force) "
 "is zero &mdash; hence no translational acceleration (Newton's second law). However, because the "
 "forces act along different lines, they produce a net turning effect (torque), causing rotation.")

add(T4,
 "A rectangular block of dimensions 0.20 m &times; 0.15 m &times; 0.10 m has a mass of 8.1 kg."
 "<ol class='parts'>"
 "<li>Calculate its density.</li>"
 "<li>Calculate the maximum and minimum pressures it can exert when resting on a horizontal surface "
 "on different faces.</li></ol>",
 7,
 "Volume = 0.20 &times; 0.15 &times; 0.10 = 3.0&times;10<sup>&minus;3</sup> m&sup3;. "
 "Weight = 8.1 &times; 9.81 = 79.5 N.<br>"
 "<b>(a)</b> Density = m/V = 8.1 / 3.0&times;10<sup>&minus;3</sup> = <b>2700 kg m<sup>&minus;3</sup></b>.<br>"
 "<b>(b)</b> Maximum pressure uses the smallest face: 0.15&times;0.10 = 0.015 m&sup2;: "
 "p<sub>max</sub> = 79.5/0.015 = <b>5.3&times;10<sup>3</sup> Pa</b>. "
 "Minimum pressure uses the largest face: 0.20&times;0.15 = 0.030 m&sup2;: "
 "p<sub>min</sub> = 79.5/0.030 = <b>2.65&times;10<sup>3</sup> Pa</b>.")

add(T4,
 "Starting from the definitions of pressure and density, derive the expression &Delta;p = &rho;g&Delta;h "
 "for the pressure difference between two points separated by a vertical height &Delta;h in a fluid of "
 "uniform density &rho;.",
 6,
 "Consider a horizontal area A at depth, supporting the column of fluid of height &Delta;h above it. "
 "Volume of the column = A&Delta;h; mass = &rho;A&Delta;h. Weight of column "
 "= mg = &rho;A&Delta;h g.<br>"
 "This weight is supported by the extra pressure &Delta;p acting over area A, giving a force "
 "F = &Delta;p &times; A. In equilibrium these balance:<br>"
 "&Delta;p &times; A = &rho;A&Delta;h g &rArr; <b>&Delta;p = &rho;g&Delta;h</b> "
 "(the area A cancels, so the result is independent of the column's cross-section).")

add(T4,
 "A U-tube contains water. Oil of density 800 kg m<sup>&minus;3</sup> is poured into the left arm and "
 "floats on the water without mixing. The oil column is 12 cm long. When equilibrium is reached, the "
 "water level in the right arm is higher than the oil&ndash;water boundary in the left arm."
 "<ol class='parts'>"
 "<li>Explain why there is a height difference.</li>"
 "<li>Calculate the difference in the levels of the two liquid surfaces "
 "(density of water = 1000 kg m<sup>&minus;3</sup>).</li></ol>",
 7,
 "<b>(a)</b> At the level of the oil&ndash;water interface, the pressure from both arms must be equal "
 "(same fluid, connected). The oil is less dense, so a taller oil column is needed to produce the same "
 "pressure as the shorter, denser water column in the other arm &mdash; hence the surfaces differ in "
 "height.<br>"
 "<b>(b)</b> Equate pressures at the interface level: &rho;<sub>oil</sub>gh<sub>oil</sub> = "
 "&rho;<sub>water</sub>gh<sub>water</sub>. So h<sub>water</sub> = "
 "(800/1000) &times; 0.12 = 0.096 m = 9.6 cm of water balances the 12 cm oil column. "
 "The difference in the top surface levels = 12 &minus; 9.6 = <b>2.4 cm</b>.")

add(T4,
 "An object of volume 5.0 &times; 10<sup>&minus;4</sup> m&sup3; and weight 6.0 N is fully submerged "
 "and held stationary in water (density 1000 kg m<sup>&minus;3</sup>)."
 "<ol class='parts'>"
 "<li>Calculate the upthrust on the object.</li>"
 "<li>Determine the tension in the string holding it, and state whether the string is above or below "
 "the object.</li>"
 "<li>Explain the origin of the upthrust in terms of pressure.</li></ol>",
 8,
 "<b>(a)</b> Upthrust = &rho;gV = 1000 &times; 9.81 &times; 5.0&times;10<sup>&minus;4</sup> = "
 "<b>4.9 N</b>.<br>"
 "<b>(b)</b> Weight (6.0 N down) &gt; upthrust (4.9 N up), so the object tends to sink; the string "
 "must pull <b>upward</b> (attached above). Equilibrium: T + upthrust = weight &rArr; "
 "T = 6.0 &minus; 4.9 = <b>1.1 N</b>.<br>"
 "<b>(c)</b> Pressure in a fluid increases with depth (&Delta;p = &rho;g&Delta;h). The pressure on the "
 "bottom face of the object is greater than on the top face, so the upward force on the bottom exceeds "
 "the downward force on the top. This net upward force is the upthrust.")

add(T4,
 "A non-uniform plank of length 4.0 m rests horizontally on two supports, one at each end. The "
 "support at end A reads 320 N and the support at end B reads 480 N."
 "<ol class='parts'>"
 "<li>Find the weight of the plank.</li>"
 "<li>Find the distance of the centre of gravity from end A.</li></ol>",
 7,
 "<b>(a)</b> Vertical equilibrium: weight = sum of support forces = 320 + 480 = <b>800 N</b>.<br>"
 "<b>(b)</b> Take moments about A (let centre of gravity be distance d from A). "
 "The weight (800 N) acts at d; support B (480 N) acts at 4.0 m. "
 "Moments about A: 800 &times; d = 480 &times; 4.0 &rArr; d = 1920/800 = <b>2.4 m from A</b>. "
 "(Check: it is nearer B, consistent with B carrying more load.)")

add(T4,
 "State the two conditions for a rigid body to be in equilibrium. A ladder leans against a smooth "
 "vertical wall, resting on rough ground. Explain, without calculation, why the frictional force at "
 "the ground is essential for equilibrium and in which direction it acts.",
 6,
 "Conditions for equilibrium: (i) the resultant force in any direction is zero (no translational "
 "acceleration); (ii) the resultant torque (moment) about any point is zero (no angular acceleration).<br>"
 "The smooth wall can only exert a horizontal (normal) force on the ladder, pushing it away from the "
 "wall. For horizontal equilibrium this must be balanced by an equal and opposite horizontal force at "
 "the base. Only friction can provide this, so friction is essential and acts <b>horizontally towards "
 "the wall</b> (preventing the base from sliding outward). Without it, there would be an unbalanced "
 "horizontal force and the ladder would slip.")

add(T4,
 "Three coplanar forces act on a body in equilibrium. Forces of 6.0 N and 8.0 N act at right angles to "
 "each other. "
 "<ol class='parts'>"
 "<li>Use a vector triangle to find the magnitude and direction of the third force.</li>"
 "<li>State the general rule that three forces in equilibrium must satisfy when drawn head-to-tail.</li></ol>",
 6,
 "<b>(a)</b> The third force must balance the resultant of the other two. Resultant of the 6.0 N and "
 "8.0 N perpendicular forces = &radic;(6.0&sup2; + 8.0&sup2;) = &radic;100 = 10 N, at "
 "tan<sup>&minus;1</sup>(6.0/8.0) = 36.9&deg; from the 8.0 N force. The third force is <b>10 N</b>, "
 "acting in exactly the <b>opposite direction</b> to this resultant (i.e. 180&deg; from it).<br>"
 "<b>(b)</b> When three forces in equilibrium are drawn head-to-tail (each starting where the previous "
 "ends), they form a <b>closed triangle</b> &mdash; the vector sum is zero.",
 "<svg width='240' height='150' viewBox='0 0 240 150'>"
 "<line x1='30' y1='120' x2='150' y2='120' stroke='#06c' stroke-width='2'/>"
 "<polygon points='150,120 142,116 142,124' fill='#06c'/>"
 "<line x1='150' y1='120' x2='150' y2='40' stroke='#c30' stroke-width='2'/>"
 "<polygon points='150,40 146,48 154,48' fill='#c30'/>"
 "<line x1='150' y1='40' x2='30' y2='120' stroke='#093' stroke-width='2'/>"
 "<polygon points='30,120 40,118 36,110' fill='#093'/>"
 "<text x='80' y='135' font-size='10' fill='#06c'>8.0 N</text>"
 "<text x='154' y='85' font-size='10' fill='#c30'>6.0 N</text>"
 "<text x='60' y='75' font-size='10' fill='#093'>10 N</text></svg>")

add(T4,
 "A hydraulic press has a small piston of area 2.0 &times; 10<sup>&minus;4</sup> m&sup2; and a large "
 "piston of area 5.0 &times; 10<sup>&minus;2</sup> m&sup2;. A force of 40 N is applied to the small "
 "piston."
 "<ol class='parts'>"
 "<li>Using the fact that pressure is transmitted equally through the fluid, find the force on the "
 "large piston.</li>"
 "<li>The small piston moves down 0.30 m. Find the distance the large piston rises, and show energy "
 "is conserved.</li></ol>",
 8,
 "<b>(a)</b> Pressure = F/A is the same on both pistons: p = 40 / 2.0&times;10<sup>&minus;4</sup> = "
 "2.0&times;10<sup>5</sup> Pa. Force on large piston = pA = 2.0&times;10<sup>5</sup> &times; "
 "5.0&times;10<sup>&minus;2</sup> = <b>1.0&times;10<sup>4</sup> N</b>.<br>"
 "<b>(b)</b> Incompressible fluid: volume displaced is equal. A<sub>1</sub>d<sub>1</sub> = "
 "A<sub>2</sub>d<sub>2</sub> &rArr; d<sub>2</sub> = (2.0&times;10<sup>&minus;4</sup> &times; 0.30)/"
 "(5.0&times;10<sup>&minus;2</sup>) = <b>1.2&times;10<sup>&minus;3</sup> m</b>. "
 "Energy check: input work = 40 &times; 0.30 = 12 J; output work = 1.0&times;10<sup>4</sup> &times; "
 "1.2&times;10<sup>&minus;3</sup> = 12 J. Equal &mdash; energy conserved (force multiplied, distance "
 "reduced).")

add(T4,
 "A uniform rod of weight 50 N and length 1.2 m is hinged at a wall at end A and held horizontal by a "
 "cable attached at end B, making an angle of 30&deg; with the rod. "
 "<ol class='parts'>"
 "<li>By taking moments about A, find the tension in the cable.</li>"
 "<li>Hence state one advantage of taking moments about A rather than about the centre.</li></ol>",
 7,
 "<b>(a)</b> The rod's weight (50 N) acts at its midpoint, 0.60 m from A. The cable tension T at B has "
 "a component perpendicular to the rod of T sin30&deg;, acting at 1.2 m from A. "
 "Moments about A: T sin30&deg; &times; 1.2 = 50 &times; 0.60 &rArr; "
 "T &times; 0.5 &times; 1.2 = 30 &rArr; 0.60T = 30 &rArr; T = <b>50 N</b>.<br>"
 "<b>(b)</b> Taking moments about A <b>eliminates the unknown hinge force</b> (which acts at A and "
 "therefore has zero moment about A), so the equation contains only the tension &mdash; simplifying "
 "the solution.")

add(T4,
 "A helium balloon of volume 0.40 m&sup3; is filled with helium of density 0.18 kg m<sup>&minus;3</sup>. "
 "The mass of the (empty) balloon fabric and its attachments is 0.050 kg. The surrounding air has "
 "density 1.2 kg m<sup>&minus;3</sup>."
 "<ol class='parts'>"
 "<li>Calculate the upthrust on the balloon.</li>"
 "<li>Determine the maximum additional load the balloon can just lift.</li></ol>",
 8,
 "<b>(a)</b> Upthrust = weight of displaced air = &rho;<sub>air</sub>gV = 1.2 &times; 9.81 &times; 0.40 "
 "= <b>4.71 N</b>.<br>"
 "<b>(b)</b> Downward weights: helium = 0.18 &times; 0.40 &times; 9.81 = 0.706 N; fabric = "
 "0.050 &times; 9.81 = 0.491 N; load = mg. For the balloon to just lift: "
 "upthrust = total weight &rArr; 4.71 = 0.706 + 0.491 + m(9.81) &rArr; "
 "m(9.81) = 3.51 &rArr; m = <b>0.358 kg</b> (&asymp; 0.36 kg).")

add(T4,
 "Explain what is meant by the <b>centre of gravity</b> of an object. Describe how you would find the "
 "centre of gravity of an irregular flat lamina experimentally, and explain the physics that makes the "
 "method work.",
 6,
 "The centre of gravity is the single point at which the entire weight of the object may be taken to "
 "act.<br>"
 "Method: suspend the lamina freely from a pin through a hole near its edge and let it hang in "
 "equilibrium. Hang a plumb line from the same pin and mark the vertical line on the lamina. Repeat "
 "from a different point. The centre of gravity is where the lines intersect.<br>"
 "Physics: when freely suspended, the object settles so that its centre of gravity lies vertically "
 "below the pivot &mdash; otherwise the weight would exert a moment about the pivot and cause "
 "rotation. Since the centre of gravity lies on each plumb-line, their intersection locates it.")


# ===========================================================================
# TOPIC 5  Work, energy and power  (14 questions)
# ===========================================================================
T5 = "5&nbsp;&nbsp;Work, energy and power"

add(T5,
 "A cyclist and bicycle of total mass 90 kg free-wheel from rest down a hill that drops a vertical "
 "height of 40 m over a slope length of 500 m. At the bottom the speed is 22 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the loss in gravitational potential energy.</li>"
 "<li>Calculate the kinetic energy gained.</li>"
 "<li>Hence find the average resistive force acting along the slope.</li></ol>",
 8,
 "<b>(a)</b> &Delta;E<sub>P</sub> = mg&Delta;h = 90 &times; 9.81 &times; 40 = "
 "<b>3.53&times;10<sup>4</sup> J</b>.<br>"
 "<b>(b)</b> E<sub>K</sub> = &frac12;mv&sup2; = &frac12; &times; 90 &times; 22&sup2; = "
 "&frac12; &times; 90 &times; 484 = <b>2.18&times;10<sup>4</sup> J</b>.<br>"
 "<b>(c)</b> Energy dissipated by resistance = &Delta;E<sub>P</sub> &minus; E<sub>K</sub> = "
 "3.53&times;10<sup>4</sup> &minus; 2.18&times;10<sup>4</sup> = 1.35&times;10<sup>4</sup> J. "
 "Work done against resistance = F &times; (slope length): 1.35&times;10<sup>4</sup> = F &times; 500 "
 "&rArr; F = <b>27 N</b>.")

add(T5,
 "Derive the expression P = Fv for the power delivered by a constant force F acting on an object "
 "moving at constant velocity v in the direction of the force. A car engine delivers a useful power "
 "of 24 kW to drive a car at a steady 30 m s<sup>&minus;1</sup> on a level road."
 "<ol class='parts'>"
 "<li>Calculate the total resistive force at this speed.</li>"
 "<li>If the resistive force is proportional to v&sup2;, find the useful power needed to travel at "
 "40 m s<sup>&minus;1</sup>.</li></ol>",
 8,
 "Derivation: work done in time t by force F moving the object a distance s = Fs. "
 "Power P = work/time = Fs/t = F(s/t) = <b>Fv</b> (since v = s/t).<br>"
 "<b>(a)</b> At steady speed, driving force = resistive force. P = Fv &rArr; "
 "F = P/v = 24000/30 = <b>800 N</b>.<br>"
 "<b>(b)</b> F &prop; v&sup2;, so at 40 m s<sup>&minus;1</sup>: F&prime; = 800 &times; (40/30)&sup2; "
 "= 800 &times; 1.778 = 1422 N. P&prime; = F&prime;v&prime; = 1422 &times; 40 = "
 "<b>5.7&times;10<sup>4</sup> W</b> (57 kW). (Note P &prop; v&sup3;: 24 &times; (40/30)&sup3; = 56.9 kW.)")

add(T5,
 "A pump raises water from a well 8.0 m deep and delivers it at the surface through a pipe at a speed "
 "of 3.0 m s<sup>&minus;1</sup>. The mass of water delivered per second is 15 kg."
 "<ol class='parts'>"
 "<li>Calculate the power needed to raise the water (gain in gravitational PE per second).</li>"
 "<li>Calculate the power needed to give the water its kinetic energy.</li>"
 "<li>If the pump's input power is 2.0 kW, calculate its efficiency.</li></ol>",
 8,
 "<b>(a)</b> P<sub>PE</sub> = (mass/s)g&Delta;h = 15 &times; 9.81 &times; 8.0 = <b>1177 W</b>.<br>"
 "<b>(b)</b> P<sub>KE</sub> = &frac12;(mass/s)v&sup2; = &frac12; &times; 15 &times; 3.0&sup2; = "
 "&frac12; &times; 15 &times; 9.0 = <b>67.5 W</b>.<br>"
 "<b>(c)</b> Useful output = 1177 + 67.5 = 1245 W. Efficiency = useful/input = 1245/2000 = 0.62 = "
 "<b>62%</b>.")

add(T5,
 "A ball of mass 0.20 kg is dropped from a height of 2.0 m onto a hard floor and rebounds to a height "
 "of 1.4 m."
 "<ol class='parts'>"
 "<li>Calculate the speed of the ball just before and just after the bounce.</li>"
 "<li>Calculate the energy lost in the bounce and express it as a percentage of the initial PE.</li>"
 "<li>State the main form into which the lost energy is transferred.</li></ol>",
 8,
 "<b>(a)</b> Before: v = &radic;(2gh) = &radic;(2 &times; 9.81 &times; 2.0) = &radic;39.24 = "
 "<b>6.26 m s<sup>&minus;1</sup></b>. After: v = &radic;(2 &times; 9.81 &times; 1.4) = &radic;27.47 = "
 "<b>5.24 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Initial PE = mgh = 0.20 &times; 9.81 &times; 2.0 = 3.92 J. Rebound PE = "
 "0.20 &times; 9.81 &times; 1.4 = 2.75 J. Energy lost = 3.92 &minus; 2.75 = <b>1.18 J</b> "
 "= (1.18/3.92) &times; 100 = <b>30%</b> of the initial PE.<br>"
 "<b>(c)</b> Mainly <b>internal (thermal) energy</b> (heating of ball and floor), with some sound.")

add(T5,
 "A skier of mass 70 kg starts from rest at the top of a slope and reaches a speed of 18 m s<sup>&minus;1</sup> "
 "at the bottom, having descended a vertical height of 25 m along a track of length 90 m. "
 "<ol class='parts'>"
 "<li>Show that the motion is not frictionless and find the total energy dissipated.</li>"
 "<li>Find the average frictional force and the efficiency of the descent in converting PE to KE.</li></ol>",
 8,
 "<b>(a)</b> If frictionless, v = &radic;(2gh) = &radic;(2 &times; 9.81 &times; 25) = 22.1 m s<sup>&minus;1</sup>, "
 "but the actual speed is only 18 m s<sup>&minus;1</sup>, so energy is lost.<br>"
 "PE lost = mgh = 70 &times; 9.81 &times; 25 = 1.717&times;10<sup>4</sup> J. "
 "KE gained = &frac12;(70)(18)&sup2; = 1.134&times;10<sup>4</sup> J. "
 "Energy dissipated = 1.717&times;10<sup>4</sup> &minus; 1.134&times;10<sup>4</sup> = "
 "<b>5.83&times;10<sup>3</sup> J</b>.<br>"
 "<b>(b)</b> Friction force = dissipated energy / distance = 5.83&times;10<sup>3</sup>/90 = "
 "<b>65 N</b>. Efficiency = KE/PE = 1.134&times;10<sup>4</sup>/1.717&times;10<sup>4</sup> = "
 "<b>66%</b>.")

add(T5,
 "State the principle of conservation of energy. A 0.050 kg arrow is fired vertically upward and "
 "leaves the bow with 30 J of kinetic energy. Air resistance does 6.0 J of work on the arrow during "
 "the ascent."
 "<ol class='parts'>"
 "<li>Find the maximum height reached.</li>"
 "<li>Explain why the arrow returns to the ground with less than 30 J of kinetic energy.</li></ol>",
 7,
 "Conservation of energy: energy cannot be created or destroyed, only transferred from one form to "
 "another; the total energy of an isolated system is constant.<br>"
 "<b>(a)</b> At maximum height all KE has become PE plus work done against air resistance: "
 "30 = mgh + 6.0 &rArr; mgh = 24 J &rArr; h = 24/(0.050 &times; 9.81) = <b>48.9 m</b>.<br>"
 "<b>(b)</b> On the way down, air resistance again does negative work on the arrow, dissipating more "
 "energy as heat. So of the 24 J of PE at the top, less than 24 J returns as KE at the ground, "
 "and the arrow arrives with less KE than the 30 J it started with.")

add(T5,
 "A conveyor belt lifts gravel at a rate of 25 kg s<sup>&minus;1</sup> onto a platform 4.0 m higher "
 "than the loading point. The gravel is placed on the belt essentially at rest and leaves it moving "
 "at the belt speed of 1.5 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the power needed to raise the gravel.</li>"
 "<li>Calculate the additional power needed to give the gravel its kinetic energy.</li>"
 "<li>State one reason the motor's actual power input must exceed the sum of these.</li></ol>",
 7,
 "<b>(a)</b> P<sub>PE</sub> = (mass/s)g&Delta;h = 25 &times; 9.81 &times; 4.0 = <b>981 W</b>.<br>"
 "<b>(b)</b> P<sub>KE</sub> = &frac12;(mass/s)v&sup2; = &frac12; &times; 25 &times; 1.5&sup2; = "
 "&frac12; &times; 25 &times; 2.25 = <b>28 W</b>.<br>"
 "<b>(c)</b> The motor must also do work against friction in the belt/bearings and against any drag, "
 "and some energy is dissipated as heat and sound; the belt is not 100% efficient, so input power "
 "exceeds the useful 1009 W.")

add(T5,
 "A 1200 kg car accelerates on a level road from 10 m s<sup>&minus;1</sup> to 25 m s<sup>&minus;1</sup> "
 "in 8.0 s. The average resistive force during this time is 500 N."
 "<ol class='parts'>"
 "<li>Calculate the gain in kinetic energy.</li>"
 "<li>Calculate the average driving force provided by the engine.</li>"
 "<li>Calculate the average useful output power of the engine over this period.</li></ol>",
 9,
 "<b>(a)</b> &Delta;E<sub>K</sub> = &frac12;m(v&sup2; &minus; u&sup2;) = &frac12;(1200)(25&sup2; &minus; 10&sup2;) "
 "= 600(625 &minus; 100) = 600 &times; 525 = <b>3.15&times;10<sup>5</sup> J</b>.<br>"
 "<b>(b)</b> Distance travelled = average speed &times; time = &frac12;(10 + 25) &times; 8.0 = 140 m. "
 "Work by driving force = &Delta;E<sub>K</sub> + work against resistance = 3.15&times;10<sup>5</sup> + "
 "500 &times; 140 = 3.15&times;10<sup>5</sup> + 7.0&times;10<sup>4</sup> = 3.85&times;10<sup>5</sup> J. "
 "Driving force = 3.85&times;10<sup>5</sup>/140 = <b>2750 N</b>.<br>"
 "<b>(c)</b> Useful output power = total work by driving force / time = 3.85&times;10<sup>5</sup>/8.0 "
 "= <b>4.8&times;10<sup>4</sup> W</b> (48 kW).")

add(T5,
 "A simple pendulum bob of mass 0.30 kg is pulled aside so that it rises a vertical height of 0.20 m "
 "above its lowest point, then released."
 "<ol class='parts'>"
 "<li>Find the speed of the bob at the lowest point (neglecting resistance).</li>"
 "<li>The string is 1.0 m long. Find the tension in the string at the lowest point.</li></ol>",
 8,
 "<b>(a)</b> Energy conservation: &frac12;mv&sup2; = mgh &rArr; v = &radic;(2gh) = "
 "&radic;(2 &times; 9.81 &times; 0.20) = &radic;3.924 = <b>1.98 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> At the lowest point the bob moves in a circle, so the resultant upward force provides the "
 "centripetal force: T &minus; mg = mv&sup2;/r. "
 "T = m(g + v&sup2;/r) = 0.30(9.81 + 3.924/1.0) = 0.30 &times; 13.73 = <b>4.1 N</b>. "
 "(The tension exceeds the weight because it must also supply the centripetal force.)")

add(T5,
 "Define <b>efficiency</b>. An electric motor rated at 500 W is used to lift a 30 kg load. In a test, "
 "it raises the load 6.0 m in 5.0 s at constant speed."
 "<ol class='parts'>"
 "<li>Calculate the useful power output.</li>"
 "<li>Calculate the efficiency.</li>"
 "<li>Explain, in energy terms, where the 'lost' input energy goes.</li></ol>",
 7,
 "Efficiency = (useful energy or power output) / (total energy or power input), a ratio (often &times;100%).<br>"
 "<b>(a)</b> Useful work = mgh = 30 &times; 9.81 &times; 6.0 = 1766 J. "
 "Useful power = 1766/5.0 = <b>353 W</b>.<br>"
 "<b>(b)</b> Efficiency = 353/500 = 0.71 = <b>71%</b>.<br>"
 "<b>(c)</b> The remaining 147 W is dissipated mainly as heat &mdash; in the motor windings "
 "(resistive I&sup2;R heating), in friction in the bearings and gears, and a little as sound. "
 "Energy is conserved: input = useful output + energy dissipated.")

add(T5,
 "A spring-loaded toy of mass 0.040 kg is compressed against a spring storing 0.90 J of elastic "
 "potential energy, then released to fire vertically upward. Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Assuming all the elastic PE becomes kinetic energy, find the launch speed.</li>"
 "<li>Find the maximum height reached above the launch point.</li></ol>",
 7,
 "<b>(a)</b> E<sub>elastic</sub> = &frac12;mv&sup2; &rArr; 0.90 = &frac12;(0.040)v&sup2; &rArr; "
 "v&sup2; = 1.80/0.040 = 45 &rArr; v = &radic;45 = <b>6.7 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> At maximum height all KE becomes PE: mgh = 0.90 &rArr; "
 "h = 0.90/(0.040 &times; 9.81) = <b>2.3 m</b>. (Equivalently the 0.90 J stored is entirely converted "
 "to gravitational PE at the top.)")

add(T5,
 "Explain why, for a car braking to rest, the braking distance is proportional to the square of the "
 "initial speed (assuming a constant braking force). A car travelling at 15 m s<sup>&minus;1</sup> "
 "stops in 18 m. Estimate its stopping distance from 30 m s<sup>&minus;1</sup> with the same braking "
 "force.",
 6,
 "The braking force F does work Fd to remove the kinetic energy: Fd = &frac12;mv&sup2;. For a fixed F "
 "and m, d = (m/2F)v&sup2;, so d &prop; v&sup2; &mdash; doubling the speed quadruples the braking "
 "distance.<br>"
 "Since d &prop; v&sup2;: d<sub>2</sub>/d<sub>1</sub> = (v<sub>2</sub>/v<sub>1</sub>)&sup2; = "
 "(30/15)&sup2; = 4. So d<sub>2</sub> = 4 &times; 18 = <b>72 m</b>.")

add(T5,
 "A ski-lift carries skiers up a 30&deg; slope at a constant 2.5 m s<sup>&minus;1</sup>. Each chair "
 "plus skier has an average mass of 85 kg and there are 40 loaded chairs on the ascending side at any "
 "instant. Friction is negligible."
 "<ol class='parts'>"
 "<li>Find the component of weight along the slope for one chair.</li>"
 "<li>Find the total useful power the motor must supply to the ascending chairs.</li></ol>",
 8,
 "<b>(a)</b> Component of weight down the slope = mg sin30&deg; = 85 &times; 9.81 &times; 0.5 = "
 "<b>417 N</b> per chair.<br>"
 "<b>(b)</b> Total force to be overcome = 40 &times; 417 = 1.668&times;10<sup>4</sup> N. "
 "The chairs move along the slope at 2.5 m s<sup>&minus;1</sup>, so useful power = Fv = "
 "1.668&times;10<sup>4</sup> &times; 2.5 = <b>4.2&times;10<sup>4</sup> W</b> (42 kW). "
 "(Equivalently, each chair rises vertically at 2.5 sin30&deg; = 1.25 m s<sup>&minus;1</sup>, giving "
 "the same total via mg &times; v<sub>vertical</sub>.)")

add(T5,
 "A 0.60 kg block slides along a horizontal frictionless surface at 5.0 m s<sup>&minus;1</sup>, then "
 "encounters a rough patch 2.0 m long where the frictional force is 1.8 N, after which the surface is "
 "frictionless again and rises into a smooth ramp."
 "<ol class='parts'>"
 "<li>Find the block's kinetic energy after crossing the rough patch.</li>"
 "<li>Find the maximum vertical height it rises up the ramp.</li></ol>",
 7,
 "<b>(a)</b> Initial KE = &frac12;(0.60)(5.0)&sup2; = 7.5 J. Work done against friction = "
 "1.8 &times; 2.0 = 3.6 J. KE after rough patch = 7.5 &minus; 3.6 = <b>3.9 J</b>.<br>"
 "<b>(b)</b> On the smooth ramp KE converts to PE: mgh = 3.9 &rArr; "
 "h = 3.9/(0.60 &times; 9.81) = <b>0.66 m</b>.")


# ===========================================================================
# TOPIC 6  Deformation of solids  (11 questions)
# ===========================================================================
T6 = "6&nbsp;&nbsp;Deformation of solids"

add(T6,
 "A steel wire of natural length 2.5 m and diameter 0.40 mm is stretched by a load of 45 N, producing "
 "an extension of 2.8 mm. "
 "<ol class='parts'>"
 "<li>Calculate the stress in the wire.</li>"
 "<li>Calculate the strain.</li>"
 "<li>Hence calculate the Young modulus of steel.</li></ol>",
 8,
 "Cross-sectional area A = &pi;(d/2)&sup2; = &pi;(0.20&times;10<sup>&minus;3</sup>)&sup2; = "
 "1.257&times;10<sup>&minus;7</sup> m&sup2;.<br>"
 "<b>(a)</b> Stress = F/A = 45 / 1.257&times;10<sup>&minus;7</sup> = "
 "<b>3.58&times;10<sup>8</sup> Pa</b>.<br>"
 "<b>(b)</b> Strain = e/L = 2.8&times;10<sup>&minus;3</sup>/2.5 = "
 "<b>1.12&times;10<sup>&minus;3</sup></b> (no units).<br>"
 "<b>(c)</b> E = stress/strain = 3.58&times;10<sup>8</sup>/1.12&times;10<sup>&minus;3</sup> = "
 "<b>3.2&times;10<sup>11</sup> Pa</b>.")

add(T6,
 "Describe an experiment to determine the Young modulus of a metal in the form of a long wire. "
 "State the measurements taken and the instrument used for each, how the result is obtained, and "
 "two precautions that improve accuracy.",
 8,
 "Clamp a long, thin wire horizontally over a pulley (or vertically from a support) with a reference "
 "marker; hang loads from the free end.<br>"
 "Measurements: original length L (metre rule); diameter d at several points and orientations "
 "(micrometer screw gauge), then average and use A = &pi;d&sup2;/4; extension e for each load "
 "(vernier scale/travelling microscope against the marker); load F = mg (known slotted masses).<br>"
 "Plot F (y) against e (x): gradient = EA/L, so E = gradient &times; L/A. (Or plot stress against "
 "strain; gradient = E.)<br>"
 "Precautions: use a long, thin wire so the extension is large and measurable; measure diameter in "
 "several places (wire may not be uniform) and average; keep temperature constant; ensure loading "
 "stays within the limit of proportionality (and use a comparison wire to allow for support "
 "yielding/thermal effects).")

add(T6,
 "The force&ndash;extension graph for a spring is a straight line from the origin up to a load of "
 "12 N at an extension of 6.0 cm, beyond which the line curves (the limit of proportionality is "
 "reached at 12 N)."
 "<ol class='parts'>"
 "<li>Calculate the spring constant.</li>"
 "<li>Calculate the elastic potential energy stored at an extension of 6.0 cm.</li>"
 "<li>State what the area under the graph beyond the limit of proportionality represents.</li></ol>",
 7,
 "<b>(a)</b> k = F/x = 12/0.060 = <b>200 N m<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Within the linear region E<sub>P</sub> = &frac12;Fx = &frac12; &times; 12 &times; 0.060 = "
 "<b>0.36 J</b> (= &frac12;kx&sup2; = &frac12; &times; 200 &times; 0.060&sup2; = 0.36 J).<br>"
 "<b>(c)</b> The area under the curve beyond the limit of proportionality still represents the "
 "<b>work done</b> in stretching the spring (energy transferred to it), but this is no longer given "
 "by &frac12;Fx and not all of it is recoverable elastic PE if the elastic limit is exceeded.",
 "<svg width='280' height='170' viewBox='0 0 280 170'>"
 "<line x1='40' y1='140' x2='260' y2='140' stroke='#333'/>"
 "<line x1='40' y1='140' x2='40' y2='20' stroke='#333'/>"
 "<line x1='40' y1='140' x2='170' y2='50' stroke='#06c' stroke-width='2'/>"
 "<path d='M170 50 Q210 30 240 28' fill='none' stroke='#06c' stroke-width='2'/>"
 "<line x1='170' y1='50' x2='170' y2='140' stroke='#999' stroke-dasharray='3 3'/>"
 "<text x='150' y='158' font-size='10'>extension / cm</text>"
 "<text x='6' y='80' font-size='10'>F / N</text>"
 "<text x='150' y='152' font-size='9'>6.0</text><text x='20' y='55' font-size='9'>12</text>"
 "<circle cx='170' cy='50' r='3' fill='#c30'/>"
 "<text x='150' y='42' font-size='8' fill='#c30'>limit</text></svg>")

add(T6,
 "Two wires, X and Y, are made of the same material. Y has twice the diameter and half the length of "
 "X. The same load is hung from each."
 "<ol class='parts'>"
 "<li>Compare the stress in Y with that in X.</li>"
 "<li>Compare the extension of Y with that of X.</li></ol>",
 7,
 "Same material &rArr; same Young modulus E. Let X have diameter d, length L; then Y has diameter 2d, "
 "length L/2. Area &prop; d&sup2;, so A<sub>Y</sub> = 4A<sub>X</sub>.<br>"
 "<b>(a)</b> Stress = F/A. Same F, but A<sub>Y</sub> = 4A<sub>X</sub>, so "
 "stress<sub>Y</sub> = &frac14; stress<sub>X</sub> &mdash; the stress in Y is <b>one quarter</b> that "
 "in X.<br>"
 "<b>(b)</b> Extension e = FL/(AE). Compared with X: e<sub>Y</sub>/e<sub>X</sub> = "
 "(L<sub>Y</sub>/L<sub>X</sub>) &times; (A<sub>X</sub>/A<sub>Y</sub>) = (&frac12;) &times; (&frac14;) = "
 "&frac18;. The extension of Y is <b>one eighth</b> that of X.")

add(T6,
 "Distinguish between <b>elastic</b> and <b>plastic</b> deformation, and define the <b>elastic limit</b>. "
 "A metal wire is loaded beyond its elastic limit and then completely unloaded. Sketch and describe "
 "the loading and unloading force&ndash;extension lines, and identify what the area between them "
 "represents.",
 7,
 "Elastic deformation: the material returns to its original dimensions when the load is removed. "
 "Plastic deformation: the material does not fully return; a permanent extension remains. "
 "The elastic limit is the maximum load (or stress) beyond which the material no longer returns to its "
 "original length &mdash; deformation becomes permanent.<br>"
 "Loading beyond the elastic limit follows a curve; on unloading, the line comes back roughly parallel "
 "to the initial straight (elastic) portion but is displaced, meeting the extension axis at a non-zero "
 "(permanent) extension. The two lines form a loop.<br>"
 "The area enclosed between the loading and unloading lines represents the <b>energy dissipated</b> "
 "(as heat) in permanently deforming the material.",
 "<svg width='260' height='170' viewBox='0 0 260 170'>"
 "<line x1='40' y1='140' x2='240' y2='140' stroke='#333'/>"
 "<line x1='40' y1='140' x2='40' y2='20' stroke='#333'/>"
 "<path d='M40 140 L120 60 Q160 35 190 30' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M190 30 L100 140' fill='none' stroke='#c30' stroke-width='2'/>"
 "<text x='150' y='158' font-size='10'>extension</text>"
 "<text x='10' y='80' font-size='10'>force</text>"
 "<text x='150' y='45' font-size='8' fill='#06c'>loading</text>"
 "<text x='120' y='120' font-size='8' fill='#c30'>unloading</text>"
 "<text x='84' y='152' font-size='8'>permanent</text></svg>")

add(T6,
 "A vertical spring of spring constant 25 N m<sup>&minus;1</sup> hangs with a 0.15 kg mass attached "
 "at rest."
 "<ol class='parts'>"
 "<li>Find the extension of the spring.</li>"
 "<li>The mass is pulled down a further 4.0 cm and released. Using energy methods, find the elastic "
 "PE stored at the moment of release relative to the equilibrium position, and hence the maximum "
 "speed of the mass as it passes back through equilibrium.</li></ol>",
 8,
 "<b>(a)</b> At equilibrium spring force = weight: kx = mg &rArr; x = mg/k = "
 "(0.15 &times; 9.81)/25 = <b>0.0589 m</b> (5.9 cm).<br>"
 "<b>(b)</b> Additional stretch A = 0.040 m. The extra elastic PE relative to equilibrium is "
 "&frac12;kA&sup2; = &frac12; &times; 25 &times; 0.040&sup2; = 0.020 J. As it returns to equilibrium "
 "this converts to kinetic energy (the gravitational term is already accounted for by measuring from "
 "equilibrium): &frac12;mv&sup2; = 0.020 &rArr; v = &radic;(2 &times; 0.020/0.15) = &radic;0.267 = "
 "<b>0.52 m s<sup>&minus;1</sup></b>.")

add(T6,
 "Define <b>stress</b>, <b>strain</b> and the <b>Young modulus</b>, giving the SI unit of each. "
 "Explain why the Young modulus is a property of the material, whereas the spring constant is a "
 "property of the particular specimen.",
 6,
 "Stress = force per unit cross-sectional area, &sigma; = F/A (unit Pa = N m<sup>&minus;2</sup>). "
 "Strain = extension per unit original length, &epsilon; = x/L (no unit). "
 "Young modulus = stress/strain, E = &sigma;/&epsilon; (unit Pa) &mdash; valid within the limit of "
 "proportionality.<br>"
 "E is intrinsic to the material because dividing by area and by original length removes the "
 "dependence on the specimen's size and shape; a given material always has the same E. The spring "
 "constant k = F/x depends on the object's dimensions (length and cross-section) as well as the "
 "material, so two springs of the same material but different dimensions have different k.")

add(T6,
 "A composite hangs from a support: a steel wire of stiffness (force constant) 800 N m<sup>&minus;1</sup> "
 "is joined end-to-end (in series) to a second wire of stiffness 1200 N m<sup>&minus;1</sup>. A load "
 "of 24 N is hung from the lower end."
 "<ol class='parts'>"
 "<li>Explain why the two wires experience the same force.</li>"
 "<li>Find the total extension of the combination.</li></ol>",
 7,
 "<b>(a)</b> The wires are in series, so the load is transmitted undiminished through both: the tension "
 "is the same (24 N) throughout, otherwise the massless junction would have a resultant force and "
 "accelerate. Hence each wire carries the full 24 N.<br>"
 "<b>(b)</b> Extension of each: e = F/k. Steel: 24/800 = 0.030 m; second: 24/1200 = 0.020 m. "
 "Total extension = 0.030 + 0.020 = <b>0.050 m</b>. "
 "(Equivalently the combined stiffness is 1/k = 1/800 + 1/1200 &rArr; k = 480 N m<sup>&minus;1</sup>, "
 "giving e = 24/480 = 0.050 m.)")

add(T6,
 "The graph of stress against strain for a ductile metal wire is drawn. Mark and explain the "
 "significance of (i) the region where the graph is a straight line through the origin, (ii) the point "
 "where the graph first departs from a straight line, and (iii) the region of large strain for small "
 "increases in stress.",
 6,
 "(i) The initial straight line through the origin is the region where <b>stress &prop; strain</b> "
 "(Hooke's law obeyed); the gradient is the Young modulus. The material is elastic here.<br>"
 "(ii) The point where the line first curves is the <b>limit of proportionality</b> &mdash; beyond it "
 "stress is no longer proportional to strain (the elastic limit lies close to or just beyond this "
 "point; beyond the elastic limit deformation becomes permanent).<br>"
 "(iii) The region where the strain increases greatly for little extra stress is the region of "
 "<b>plastic (ductile) flow / yielding</b>; the wire is being permanently stretched and will not "
 "return to its original length.")

add(T6,
 "A rubber cord and a metal wire are each stretched and then released. State and explain, with "
 "reference to their force&ndash;extension behaviour, one important way in which rubber differs from "
 "the metal in how it stores and returns energy.",
 5,
 "For the metal (loaded within its elastic limit) the loading and unloading force&ndash;extension "
 "lines coincide (a straight line), so essentially all the work done in stretching is returned as "
 "elastic PE on release &mdash; little energy is lost.<br>"
 "Rubber shows <b>hysteresis</b>: its loading and unloading curves differ, forming a loop, and the "
 "unloading line lies below the loading line. Less energy is returned than was put in; the area of the "
 "loop represents energy converted to heat, so the rubber warms up when repeatedly stretched and "
 "released.")

add(T6,
 "A wire obeys Hooke's law up to a load of 60 N, at which its extension is 4.0 mm. "
 "<ol class='parts'>"
 "<li>Calculate the work done in stretching it to this extension.</li>"
 "<li>An identical wire is stretched to only 3.0 mm. Calculate the elastic PE stored, and state what "
 "fraction of the answer to (a) this represents.</li></ol>",
 7,
 "Spring constant k = F/x = 60/4.0&times;10<sup>&minus;3</sup> = 1.5&times;10<sup>4</sup> N m<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> W = &frac12;Fx = &frac12; &times; 60 &times; 4.0&times;10<sup>&minus;3</sup> = "
 "<b>0.12 J</b>.<br>"
 "<b>(b)</b> E<sub>P</sub> = &frac12;kx&sup2; = &frac12; &times; 1.5&times;10<sup>4</sup> &times; "
 "(3.0&times;10<sup>&minus;3</sup>)&sup2; = &frac12; &times; 1.5&times;10<sup>4</sup> &times; "
 "9.0&times;10<sup>&minus;6</sup> = <b>0.0675 J</b>. As a fraction of (a): 0.0675/0.12 = "
 "<b>0.56</b> (= (3.0/4.0)&sup2; = 9/16, since E<sub>P</sub> &prop; x&sup2;).")


# ===========================================================================
# TOPIC 7  Waves  (15 questions)
# ===========================================================================
T7 = "7&nbsp;&nbsp;Waves"

add(T7,
 "Define <b>displacement</b>, <b>amplitude</b>, <b>frequency</b> and <b>phase difference</b> for a "
 "progressive wave. Two points on a progressive wave of wavelength 0.80 m are separated by 0.30 m "
 "along the direction of travel."
 "<ol class='parts'>"
 "<li>Calculate their phase difference in degrees and in radians.</li>"
 "<li>State the smallest separation of two points that oscillate in antiphase.</li></ol>",
 7,
 "Displacement: distance of a particle from its equilibrium position (with direction). Amplitude: the "
 "maximum displacement. Frequency: number of complete oscillations per unit time. Phase difference: "
 "the fraction of a cycle (expressed as an angle) by which one oscillation leads or lags another.<br>"
 "<b>(a)</b> One wavelength = 360&deg; = 2&pi; rad. Phase difference = (0.30/0.80) &times; 360&deg; = "
 "<b>135&deg;</b> = (0.30/0.80) &times; 2&pi; = <b>2.36 rad</b> (= 3&pi;/4).<br>"
 "<b>(b)</b> Antiphase means a phase difference of 180&deg;, i.e. half a wavelength: "
 "smallest separation = &lambda;/2 = <b>0.40 m</b>.")

add(T7,
 "The trace on a cathode-ray oscilloscope (CRO) shows a sinusoidal signal. The time-base is set to "
 "2.0 ms per division and one complete cycle occupies 3.5 divisions horizontally. The y-gain is "
 "0.50 V per division and the trace has a peak-to-peak height of 6.0 divisions."
 "<ol class='parts'>"
 "<li>Calculate the frequency of the signal.</li>"
 "<li>Calculate the amplitude (peak voltage) of the signal.</li></ol>",
 6,
 "<b>(a)</b> Period T = 3.5 div &times; 2.0 ms/div = 7.0 ms = 7.0&times;10<sup>&minus;3</sup> s. "
 "Frequency f = 1/T = 1/7.0&times;10<sup>&minus;3</sup> = <b>143 Hz</b>.<br>"
 "<b>(b)</b> Peak-to-peak voltage = 6.0 div &times; 0.50 V/div = 3.0 V. "
 "Amplitude (peak) = half of this = <b>1.5 V</b>.")

add(T7,
 "Derive the wave equation v = f&lambda; from the definitions of speed, frequency and wavelength. "
 "A sound wave of frequency 256 Hz travels in air at 340 m s<sup>&minus;1</sup> and then passes into "
 "water where its speed becomes 1480 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Find its wavelength in air and in water.</li>"
 "<li>State, with a reason, what happens to the frequency as the wave crosses into the water.</li></ol>",
 7,
 "Derivation: in one period T the wave advances exactly one wavelength &lambda;. Speed = distance/time "
 "= &lambda;/T. Since f = 1/T, v = &lambda;/T = f&lambda;.<br>"
 "<b>(a)</b> Air: &lambda; = v/f = 340/256 = <b>1.33 m</b>. Water: &lambda; = 1480/256 = "
 "<b>5.78 m</b>.<br>"
 "<b>(b)</b> The frequency is <b>unchanged</b> (256 Hz). Frequency is set by the source; the number of "
 "wavefronts arriving per second must equal the number leaving the boundary per second, so f is "
 "continuous across the boundary while v and &lambda; change.")

add(T7,
 "A point source emits sound uniformly in all directions with a power of 0.80 W."
 "<ol class='parts'>"
 "<li>Calculate the intensity at a distance of 5.0 m from the source.</li>"
 "<li>At what distance is the intensity one quarter of this value?</li>"
 "<li>State how the amplitude of the wave at that greater distance compares with the amplitude at "
 "5.0 m.</li></ol>",
 7,
 "<b>(a)</b> Intensity I = power/area = P/(4&pi;r&sup2;) = 0.80/(4&pi; &times; 5.0&sup2;) = "
 "0.80/314 = <b>2.5&times;10<sup>&minus;3</sup> W m<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> I &prop; 1/r&sup2;. For I to fall to &frac14;, r&sup2; must increase &times;4, so r "
 "increases &times;2: r = <b>10 m</b>.<br>"
 "<b>(c)</b> Intensity &prop; amplitude&sup2;, so if I becomes &frac14;, the amplitude becomes "
 "&radic;(&frac14;) = <b>&frac12;</b> of the amplitude at 5.0 m.")

add(T7,
 "Compare <b>transverse</b> and <b>longitudinal</b> waves, giving one example of each from the "
 "syllabus. Explain, in terms of the direction of particle oscillation, why one of these wave types "
 "can be polarised and the other cannot.",
 6,
 "Transverse wave: particle oscillations are perpendicular to the direction of energy travel "
 "(e.g. electromagnetic waves / waves on a string). Longitudinal wave: particle oscillations are "
 "parallel to the direction of energy travel, producing compressions and rarefactions "
 "(e.g. sound waves).<br>"
 "Polarisation restricts the oscillations to a single plane. Only transverse waves can be polarised, "
 "because their oscillations are perpendicular to the propagation direction and so there are many "
 "possible planes to select from. In a longitudinal wave the oscillation is along the single "
 "propagation direction, so there is no choice of plane to restrict &mdash; it cannot be polarised.")

add(T7,
 "A police car siren emits sound of frequency 900 Hz. The car moves at 30 m s<sup>&minus;1</sup> "
 "along a straight road; the speed of sound is 340 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the frequency heard by a stationary observer as the car approaches.</li>"
 "<li>Calculate the frequency heard as the car recedes.</li>"
 "<li>Explain physically why the approaching frequency is higher.</li></ol>",
 8,
 "Use f<sub>o</sub> = f<sub>s</sub> v/(v &plusmn; v<sub>s</sub>), minus for approach.<br>"
 "<b>(a)</b> Approaching: f<sub>o</sub> = 900 &times; 340/(340 &minus; 30) = 900 &times; 340/310 = "
 "<b>987 Hz</b>.<br>"
 "<b>(b)</b> Receding: f<sub>o</sub> = 900 &times; 340/(340 + 30) = 900 &times; 340/370 = "
 "<b>827 Hz</b>.<br>"
 "<b>(c)</b> As the source approaches, each successive wavefront is emitted from a position closer to "
 "the observer, so the wavefronts are 'bunched' &mdash; the wavelength reaching the observer is "
 "shortened. Since the wave speed in air is unchanged, a shorter wavelength means a higher observed "
 "frequency.")

add(T7,
 "State the approximate range of wavelengths (in free space) of the following regions of the "
 "electromagnetic spectrum and place them in order of increasing wavelength: X-rays, microwaves, "
 "visible light, infrared. State two properties that all electromagnetic waves share.",
 6,
 "Order of increasing wavelength: X-rays (&asymp; 10<sup>&minus;10</sup> m) &lt; visible "
 "(400&ndash;700 nm, i.e. &asymp; 4&ndash;7 &times; 10<sup>&minus;7</sup> m) &lt; infrared "
 "(&asymp; 10<sup>&minus;6</sup> to 10<sup>&minus;3</sup> m) &lt; microwaves "
 "(&asymp; 10<sup>&minus;3</sup> to 10<sup>&minus;1</sup> m).<br>"
 "Shared properties (any two): all are transverse waves; all travel at the same speed "
 "c = 3.0&times;10<sup>8</sup> m s<sup>&minus;1</sup> in free space; all can be polarised; all can be "
 "reflected, refracted, diffracted and can interfere; all transfer energy.")

add(T7,
 "Unpolarised light of intensity I<sub>0</sub> passes through a polarising filter, then through a "
 "second (analyser) whose transmission axis is at 60&deg; to the first."
 "<ol class='parts'>"
 "<li>State the intensity of the light after the first filter (in terms of I<sub>0</sub>).</li>"
 "<li>Use Malus's law to find the intensity after the second filter.</li>"
 "<li>State the effect on the final intensity of rotating the analyser to 90&deg; to the first.</li></ol>",
 7,
 "<b>(a)</b> An ideal polariser transmits half the incident unpolarised intensity: "
 "I<sub>1</sub> = <b>&frac12;I<sub>0</sub></b> (and the transmitted light is now plane-polarised).<br>"
 "<b>(b)</b> Malus: I = I<sub>1</sub>cos&sup2;&theta; = &frac12;I<sub>0</sub> &times; cos&sup2;60&deg; = "
 "&frac12;I<sub>0</sub> &times; (0.5)&sup2; = &frac12;I<sub>0</sub> &times; 0.25 = "
 "<b>0.125 I<sub>0</sub></b> (I<sub>0</sub>/8).<br>"
 "<b>(c)</b> At 90&deg;, cos&sup2;90&deg; = 0, so the final intensity is <b>zero</b> &mdash; crossed "
 "polarisers block the light.")

add(T7,
 "A wave travelling in the +x direction is described by a displacement&ndash;position graph "
 "(a 'snapshot' at one instant) and, separately, by a displacement&ndash;time graph for one particle. "
 "State what physical quantity is read directly from each graph, and explain how the two graphs "
 "differ even though both look sinusoidal.",
 6,
 "From the displacement&ndash;<b>position</b> graph (a snapshot of the whole wave at one instant) you "
 "read the <b>wavelength</b> &lambda; (distance between adjacent points in phase) and the amplitude.<br>"
 "From the displacement&ndash;<b>time</b> graph for a single particle you read the <b>period</b> T "
 "(and hence frequency f = 1/T) and the amplitude.<br>"
 "They differ because the horizontal axes represent different quantities (distance vs time): the "
 "position graph shows how displacement varies across space at a frozen instant, whereas the time "
 "graph shows how one fixed particle's displacement varies as time passes. Both are sinusoidal but "
 "carry different information (&lambda; vs T).")

add(T7,
 "A loudspeaker connected to a signal generator produces a sound of constant frequency. As the "
 "output power of the generator is doubled, describe and explain the change (if any) in "
 "(i) the frequency of the sound, (ii) the wavelength, and (iii) the amplitude of the air-particle "
 "oscillations, assuming the speed of sound is constant.",
 6,
 "(i) Frequency is unchanged &mdash; it is set by the signal generator, not by the power.<br>"
 "(ii) Wavelength is unchanged: with v = f&lambda; and both v and f constant, &lambda; is fixed.<br>"
 "(iii) Intensity &prop; power, and intensity &prop; amplitude&sup2;. Doubling the power doubles the "
 "intensity, so the amplitude increases by a factor &radic;2 &asymp; 1.41 &mdash; the air particles "
 "oscillate through larger displacements, making the sound louder.")

add(T7,
 "The speed of a transverse wave on a stretched string depends on the tension and the mass per unit "
 "length. In an investigation, a wave of frequency 50 Hz on a string has a wavelength of 1.2 m."
 "<ol class='parts'>"
 "<li>Calculate the wave speed.</li>"
 "<li>The tension is then increased so the speed becomes 90 m s<sup>&minus;1</sup> while the "
 "frequency is kept at 50 Hz. Find the new wavelength.</li></ol>",
 6,
 "<b>(a)</b> v = f&lambda; = 50 &times; 1.2 = <b>60 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> With f fixed at 50 Hz and v = 90 m s<sup>&minus;1</sup>: &lambda; = v/f = 90/50 = "
 "<b>1.8 m</b>. (The wavelength increases because the wave now travels faster at the same frequency.)")

add(T7,
 "Explain what is meant by saying that a progressive wave <b>transfers energy</b> without transferring "
 "matter. Use the example of a cork floating on water as a water wave passes to support your "
 "explanation.",
 5,
 "As a progressive wave travels, each particle of the medium oscillates about a fixed equilibrium "
 "position, passing on energy to the next particle, but the particles themselves are not carried along "
 "with the wave &mdash; there is no net transport of matter in the direction of travel.<br>"
 "A cork on water bobs up and down (and slightly back and forth) as the wave passes but stays in "
 "roughly the same place; it is not carried across the pond. Its gain in energy (kinetic and "
 "potential as it rises) shows that energy has been delivered to it by the wave, even though the water "
 "(and the cork) has not moved along with the wave.")

add(T7,
 "A beam of vertically plane-polarised light of intensity I<sub>0</sub> is incident on a series of "
 "three polarising filters whose transmission axes are at 0&deg;, 45&deg; and 90&deg; to the vertical "
 "respectively."
 "<ol class='parts'>"
 "<li>Find the intensity transmitted through all three, in terms of I<sub>0</sub>.</li>"
 "<li>Compare this with the intensity if the middle filter were removed, and comment.</li></ol>",
 7,
 "<b>(a)</b> The light is already polarised along 0&deg;. After filter 1 (axis 0&deg;): I<sub>0</sub> "
 "(unchanged). After filter 2 (45&deg;): I<sub>0</sub>cos&sup2;45&deg; = 0.5 I<sub>0</sub>. "
 "After filter 3 (45&deg; from filter 2): 0.5 I<sub>0</sub> &times; cos&sup2;45&deg; = "
 "0.5 &times; 0.5 I<sub>0</sub> = <b>0.25 I<sub>0</sub></b>.<br>"
 "<b>(b)</b> Without the middle filter, filters 1 and 3 are crossed (0&deg; and 90&deg;), so "
 "I<sub>0</sub>cos&sup2;90&deg; = <b>0</b>. Remarkably, inserting an extra filter between crossed "
 "polarisers lets light through (0.25 I<sub>0</sub>), because the middle filter rotates the plane of "
 "polarisation in two 45&deg; steps rather than one blocked 90&deg; step.")

add(T7,
 "A microwave source and detector are used to show that microwaves are transverse and to measure "
 "their properties. Describe (i) how you would demonstrate that the microwaves are polarised, and "
 "(ii) outline how you could estimate the wavelength using a metal reflector.",
 6,
 "<b>(i) Polarisation:</b> place a metal grille (parallel wires) between the transmitter and receiver "
 "and rotate it about the beam axis. The detected signal varies from a maximum to (near) zero as the "
 "grille is rotated through 90&deg;. This dependence on orientation shows the wave is plane-polarised "
 "&mdash; and hence transverse (a longitudinal wave would show no such variation).<br>"
 "<b>(ii) Wavelength:</b> direct the transmitter at a flat metal reflector so the reflected and "
 "incident waves superpose to form a stationary wave. Move the detector along the beam and locate "
 "adjacent minima (nodes); the distance between adjacent nodes is &lambda;/2, so &lambda; = twice that "
 "spacing.")


# ===========================================================================
# TOPIC 8  Superposition  (13 questions)
# ===========================================================================
T8 = "8&nbsp;&nbsp;Superposition"

add(T8,
 "State the <b>principle of superposition</b>. In a Young's double-slit experiment, coherent light of "
 "wavelength 590 nm illuminates two slits 0.45 mm apart, and fringes are observed on a screen 2.4 m "
 "away."
 "<ol class='parts'>"
 "<li>Calculate the fringe separation.</li>"
 "<li>Calculate the distance from the central bright fringe to the 4th-order bright fringe.</li></ol>",
 7,
 "Principle of superposition: when two or more waves meet at a point, the resultant displacement is "
 "the vector sum of the individual displacements at that point.<br>"
 "<b>(a)</b> Fringe separation x = &lambda;D/a = (590&times;10<sup>&minus;9</sup> &times; 2.4)/"
 "(0.45&times;10<sup>&minus;3</sup>) = 1.416&times;10<sup>&minus;6</sup>/4.5&times;10<sup>&minus;4</sup> "
 "= <b>3.1&times;10<sup>&minus;3</sup> m</b> (3.1 mm).<br>"
 "<b>(b)</b> Distance to the 4th bright fringe = 4x = 4 &times; 3.1&times;10<sup>&minus;3</sup> = "
 "<b>1.26&times;10<sup>&minus;2</sup> m</b> (&asymp; 12.6 mm).",
 "<svg width='320' height='140' viewBox='0 0 320 140'>"
 "<line x1='40' y1='70' x2='90' y2='70' stroke='#333'/>"
 "<rect x='90' y='20' width='6' height='40' fill='#333'/><rect x='90' y='80' width='6' height='40' fill='#333'/>"
 "<rect x='90' y='62' width='6' height='16' fill='#fff' stroke='#333'/>"
 "<line x1='96' y1='66' x2='280' y2='40' stroke='#06c'/><line x1='96' y1='74' x2='280' y2='100' stroke='#06c'/>"
 "<line x1='280' y1='15' x2='280' y2='125' stroke='#333' stroke-width='2'/>"
 "<circle cx='280' cy='70' r='3' fill='#c30'/><circle cx='280' cy='55' r='2' fill='#c30'/>"
 "<circle cx='280' cy='85' r='2' fill='#c30'/>"
 "<text x='55' y='60' font-size='9'>light</text><text x='100' y='16' font-size='9'>slits (a)</text>"
 "<text x='245' y='135' font-size='9'>screen</text><text x='170' y='30' font-size='9'>D</text></svg>")

add(T8,
 "Explain the meaning of the terms <b>interference</b> and <b>coherence</b>. State the conditions "
 "necessary for a stable two-source interference pattern of light to be observed, and explain why two "
 "separate filament lamps of the same colour cannot produce such a pattern.",
 7,
 "Interference: the superposition of two (or more) waves to give a resultant of larger or smaller "
 "amplitude &mdash; constructive where they arrive in phase, destructive where in antiphase. "
 "Coherence: two sources are coherent if they maintain a <b>constant phase difference</b> (which "
 "requires the same frequency).<br>"
 "Conditions for observable fringes: the sources must be coherent (constant phase difference, same "
 "frequency), have roughly equal amplitudes (for good contrast), and (for transverse waves) the same "
 "polarisation; the path difference must be within the coherence length.<br>"
 "Two separate lamps emit light in short, random bursts with rapidly and randomly changing phase, so "
 "their phase difference is not constant &mdash; they are incoherent. Any interference pattern changes "
 "far too quickly to be seen, averaging out to uniform illumination.")

add(T8,
 "A stationary (standing) wave is set up on a string of length 1.5 m fixed at both ends, vibrating in "
 "its third harmonic (three loops)."
 "<ol class='parts'>"
 "<li>Sketch the string, marking nodes (N) and antinodes (A).</li>"
 "<li>Determine the wavelength.</li>"
 "<li>If the wave speed on the string is 120 m s<sup>&minus;1</sup>, find the frequency.</li></ol>",
 7,
 "<b>(a)</b> Three loops between the fixed ends: nodes at both ends and at two interior points "
 "(4 nodes total), with an antinode at the centre of each loop (3 antinodes): "
 "N&ndash;A&ndash;N&ndash;A&ndash;N&ndash;A&ndash;N.<br>"
 "<b>(b)</b> Each loop is &lambda;/2 long; three loops span the length: 3(&lambda;/2) = 1.5 m &rArr; "
 "&lambda; = 2 &times; 1.5/3 = <b>1.0 m</b>.<br>"
 "<b>(c)</b> f = v/&lambda; = 120/1.0 = <b>120 Hz</b>.",
 "<svg width='300' height='90' viewBox='0 0 300 90'>"
 "<line x1='30' y1='45' x2='280' y2='45' stroke='#ccc'/>"
 "<path d='M30 45 Q71 15 113 45 Q154 75 196 45 Q237 15 280 45' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M30 45 Q71 75 113 45 Q154 15 196 45 Q237 75 280 45' fill='none' stroke='#06c' stroke-width='1' stroke-dasharray='3 2'/>"
 "<text x='26' y='60' font-size='9'>N</text><text x='108' y='60' font-size='9'>N</text>"
 "<text x='192' y='60' font-size='9'>N</text><text x='276' y='60' font-size='9'>N</text>"
 "<text x='66' y='12' font-size='9'>A</text><text x='150' y='12' font-size='9'>A</text>"
 "<text x='232' y='12' font-size='9'>A</text></svg>")

add(T8,
 "A diffraction grating has 500 lines per millimetre. It is illuminated normally by monochromatic "
 "light of wavelength 640 nm."
 "<ol class='parts'>"
 "<li>Calculate the grating spacing d.</li>"
 "<li>Calculate the angle of the second-order maximum.</li>"
 "<li>Determine the highest order that can be observed.</li></ol>",
 8,
 "<b>(a)</b> d = 1/(500 lines per mm) = 1/(500&times;10<sup>3</sup> lines per m) = "
 "2.0&times;10<sup>&minus;6</sup> m.<br>"
 "<b>(b)</b> d sin&theta; = n&lambda;: sin&theta; = 2 &times; 640&times;10<sup>&minus;9</sup>/"
 "2.0&times;10<sup>&minus;6</sup> = 1.28&times;10<sup>&minus;6</sup>/2.0&times;10<sup>&minus;6</sup> = "
 "0.640 &rArr; &theta; = <b>39.8&deg;</b>.<br>"
 "<b>(c)</b> Maximum order when sin&theta; &le; 1: n &le; d/&lambda; = "
 "2.0&times;10<sup>&minus;6</sup>/640&times;10<sup>&minus;9</sup> = 3.13. So the highest order is "
 "<b>n = 3</b>.")

add(T8,
 "Explain the formation of a stationary wave on a stretched string in terms of two progressive waves. "
 "State two ways in which a stationary wave differs from a progressive wave.",
 7,
 "A stationary wave forms when two progressive waves of the same frequency, wavelength and (ideally) "
 "amplitude travel in opposite directions along the string and superpose &mdash; typically an incident "
 "wave and its reflection from a fixed end. At points where the two waves are always in antiphase they "
 "cancel, giving permanent <b>nodes</b> (zero amplitude); where they are always in phase they reinforce, "
 "giving <b>antinodes</b> (maximum amplitude).<br>"
 "Differences (any two): (i) in a stationary wave energy is stored/not transferred along the wave, "
 "whereas a progressive wave transfers energy; (ii) amplitude varies with position (nodes to "
 "antinodes) in a stationary wave but is the same for all particles in a progressive wave; "
 "(iii) between adjacent nodes all particles oscillate in phase in a stationary wave, whereas phase "
 "changes continuously along a progressive wave.")

add(T8,
 "Explain the meaning of <b>diffraction</b>. Describe, using a ripple tank, how the extent of "
 "diffraction of water waves through a gap depends on the size of the gap relative to the wavelength, "
 "and state the condition for the most pronounced diffraction.",
 6,
 "Diffraction is the spreading of a wave as it passes through a gap or around an obstacle/edge, into "
 "the region that would otherwise be a geometrical shadow.<br>"
 "In a ripple tank, straight water waves are directed at a gap in a barrier. When the gap is much "
 "wider than the wavelength, the waves pass through with only slight spreading at the edges. As the "
 "gap is narrowed towards the wavelength, the emerging waves spread out much more, becoming nearly "
 "circular. The most pronounced diffraction occurs when the <b>gap width is approximately equal to the "
 "wavelength</b>.")

add(T8,
 "In a double-slit experiment the fringe separation is measured for red light and then for blue light "
 "with the same slits and screen distance."
 "<ol class='parts'>"
 "<li>State and explain which colour gives the wider fringe spacing.</li>"
 "<li>The screen is then moved twice as far away. State the effect on the fringe separation.</li>"
 "<li>Instead, the slit separation is doubled. State the effect on the fringe separation.</li></ol>",
 6,
 "Fringe separation x = &lambda;D/a.<br>"
 "<b>(a)</b> Red light gives wider fringes: x &prop; &lambda;, and red light has the longer "
 "wavelength than blue.<br>"
 "<b>(b)</b> x &prop; D, so doubling D <b>doubles</b> the fringe separation.<br>"
 "<b>(c)</b> x &prop; 1/a, so doubling the slit separation <b>halves</b> the fringe separation.")

add(T8,
 "A tube closed at one end and open at the other resonates with sound. The shortest air column that "
 "gives resonance with a tuning fork of frequency 512 Hz is 16.2 cm long. (Speed of sound in air = "
 "330 m s<sup>&minus;1</sup>; ignore end corrections.)"
 "<ol class='parts'>"
 "<li>Sketch the displacement pattern for this fundamental resonance, marking the node and antinode.</li>"
 "<li>Show that the data are consistent with the speed of sound quoted.</li></ol>",
 7,
 "<b>(a)</b> For a closed tube the closed end is a displacement <b>node</b> and the open end is an "
 "<b>antinode</b>. The fundamental has a quarter-wavelength in the tube: N at the closed end, A at "
 "the open end.<br>"
 "<b>(b)</b> Length = &lambda;/4 &rArr; &lambda; = 4 &times; 0.162 = 0.648 m. "
 "Then v = f&lambda; = 512 &times; 0.648 = <b>332 m s<sup>&minus;1</sup></b>, which agrees with "
 "330 m s<sup>&minus;1</sup> to within about 0.5% &mdash; consistent (the small excess is largely due "
 "to the neglected end correction).",
 "<svg width='120' height='150' viewBox='0 0 120 150'>"
 "<rect x='40' y='20' width='40' height='115' fill='none' stroke='#333' stroke-width='2'/>"
 "<line x1='40' y1='20' x2='80' y2='20' stroke='#fff' stroke-width='3'/>"
 "<path d='M60 135 Q30 78 60 20' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M60 135 Q90 78 60 20' fill='none' stroke='#06c' stroke-width='1' stroke-dasharray='3 2'/>"
 "<text x='84' y='138' font-size='9'>N</text><text x='84' y='24' font-size='9'>A</text>"
 "<text x='30' y='148' font-size='8'>closed</text></svg>")

add(T8,
 "Two identical loudspeakers, driven in phase by the same signal generator at a frequency of 1.7 kHz, "
 "are placed 1.5 m apart facing a listener who walks along a line parallel to the speakers. The "
 "listener notices alternate loud and quiet points. (Speed of sound = 340 m s<sup>&minus;1</sup>.)"
 "<ol class='parts'>"
 "<li>Explain the origin of the loud and quiet points.</li>"
 "<li>State the path difference (in wavelengths) at a quiet point nearest the centre.</li></ol>",
 7,
 "&lambda; = v/f = 340/1700 = 0.20 m.<br>"
 "<b>(a)</b> Sound from the two coherent speakers superposes. Where the path difference is a whole "
 "number of wavelengths (n&lambda;) the waves arrive in phase and interfere constructively &rArr; loud "
 "points; where it is an odd number of half-wavelengths ((n+&frac12;)&lambda;) they arrive in "
 "antiphase and interfere destructively &rArr; quiet points.<br>"
 "<b>(b)</b> The first quiet point either side of the centre occurs where the path difference is "
 "<b>&frac12;&lambda;</b> (= 0.10 m).")

add(T8,
 "Describe how a diffraction grating can be used to measure the wavelength of monochromatic light. "
 "State the measurements taken and how the wavelength is calculated, and explain one advantage of "
 "using a grating rather than a double slit for this purpose.",
 7,
 "Shine the light normally onto a grating of known spacing d (from the lines per metre). Measure the "
 "angle &theta; of a diffracted maximum of order n (e.g. using a spectrometer table or by measuring "
 "the distance of the maximum from the straight-through beam and the grating&ndash;screen distance, "
 "then &theta; = tan<sup>&minus;1</sup>(y/L)). Apply d sin&theta; = n&lambda;, so "
 "&lambda; = d sin&theta;/n. Repeat for several orders and average.<br>"
 "Advantage over a double slit: a grating has many slits, so the maxima are much <b>sharper and "
 "brighter</b>, and the diffraction angles are large, allowing &theta; (and hence &lambda;) to be "
 "measured much more precisely.")

add(T8,
 "White light is passed through a diffraction grating."
 "<ol class='parts'>"
 "<li>Explain why the central (zero-order) maximum is white but the higher orders are spread into "
 "spectra.</li>"
 "<li>State, with a reason, which colour is diffracted through the largest angle in a given order.</li></ol>",
 6,
 "<b>(a)</b> At the zero order (n = 0), d sin&theta; = 0 for all wavelengths, so &theta; = 0 for every "
 "colour &mdash; all wavelengths are transmitted straight through together and combine to give white. "
 "For n &ge; 1, sin&theta; = n&lambda;/d depends on &lambda;, so each colour is diffracted through a "
 "different angle, spreading the light into a spectrum.<br>"
 "<b>(b)</b> Since sin&theta; &prop; &lambda;, the longest wavelength is diffracted most: "
 "<b>red</b> light is diffracted through the largest angle in a given order (violet the least).")

add(T8,
 "Microwaves of wavelength 2.8 cm from a transmitter are reflected back by a metal sheet, forming a "
 "stationary wave. A small probe detector is moved along the line between transmitter and sheet."
 "<ol class='parts'>"
 "<li>Explain what the detector registers as it is moved, and why.</li>"
 "<li>Calculate the distance the detector moves between five successive positions of minimum signal.</li></ol>",
 6,
 "<b>(a)</b> The incident and reflected microwaves superpose to form a stationary wave with fixed "
 "nodes and antinodes. As the probe moves, the detected signal rises and falls: it registers minima "
 "at the nodes (waves in antiphase, cancel) and maxima at the antinodes (in phase, reinforce).<br>"
 "<b>(b)</b> Adjacent nodes are &lambda;/2 = 1.4 cm apart. Five successive minima span four gaps: "
 "distance = 4 &times; 1.4 = <b>5.6 cm</b>.")

add(T8,
 "In a Young's double-slit arrangement, the fringes are found to have low contrast (bright fringes not "
 "very bright, dark fringes not fully dark). Suggest two possible reasons for the poor contrast and, "
 "for each, state how it could be improved.",
 6,
 "Reason 1: the two slits transmit unequal amplitudes (e.g. slits of different width or uneven "
 "illumination), so destructive interference is incomplete and dark fringes are not fully dark. "
 "Improve by making the slits equal in width and illuminating them symmetrically.<br>"
 "Reason 2: the source is not sufficiently monochromatic (a range of wavelengths gives overlapping "
 "fringe patterns of different spacing that wash out) or the slit&ndash;source arrangement gives poor "
 "coherence. Improve by using monochromatic (e.g. laser or filtered) light and a single narrow "
 "source slit to ensure coherence. (Also reducing background/ambient light raises contrast.)")


# ===========================================================================
# TOPIC 9  Electricity  (13 questions)
# ===========================================================================
T9 = "9&nbsp;&nbsp;Electricity"

add(T9,
 "A copper wire of cross-sectional area 1.5 &times; 10<sup>&minus;6</sup> m&sup2; carries a current "
 "of 3.2 A. Copper has 8.5 &times; 10<sup>28</sup> free electrons per cubic metre."
 "<ol class='parts'>"
 "<li>Calculate the drift speed of the electrons.</li>"
 "<li>Comment on the size of your answer, given that electrical signals travel near the speed of "
 "light.</li></ol>",
 7,
 "<b>(a)</b> I = Anvq &rArr; v = I/(Anq) = 3.2/(1.5&times;10<sup>&minus;6</sup> &times; "
 "8.5&times;10<sup>28</sup> &times; 1.60&times;10<sup>&minus;19</sup>). "
 "Denominator = 1.5&times;10<sup>&minus;6</sup> &times; 8.5&times;10<sup>28</sup> &times; "
 "1.60&times;10<sup>&minus;19</sup> = 2.04&times;10<sup>4</sup>. "
 "v = 3.2/2.04&times;10<sup>4</sup> = <b>1.6&times;10<sup>&minus;4</sup> m s<sup>&minus;1</sup></b> "
 "(&asymp; 0.16 mm s<sup>&minus;1</sup>).<br>"
 "<b>(b)</b> The drift speed is extremely small, yet a lamp lights almost instantly. This is because "
 "the electric field is established through the whole circuit at near light speed, so all the "
 "free electrons everywhere start drifting almost simultaneously &mdash; it is not necessary for an "
 "electron to travel from switch to lamp.")

add(T9,
 "State what is meant by 'the charge on charge carriers is quantised'. A charge of 96 C flows past a "
 "point in a conductor in 40 s."
 "<ol class='parts'>"
 "<li>Calculate the current.</li>"
 "<li>Calculate the number of electrons that pass the point in this time.</li></ol>",
 6,
 "Quantised charge means charge exists only in whole-number multiples of the elementary charge "
 "e = 1.60&times;10<sup>&minus;19</sup> C; you cannot have a fraction of e as free charge.<br>"
 "<b>(a)</b> I = Q/t = 96/40 = <b>2.4 A</b>.<br>"
 "<b>(b)</b> Number of electrons = Q/e = 96/1.60&times;10<sup>&minus;19</sup> = "
 "<b>6.0&times;10<sup>20</sup></b>.")

add(T9,
 "Define <b>potential difference</b> across a component. A 12 V battery drives a current of 0.50 A "
 "through a motor for 2.0 minutes, lifting a load."
 "<ol class='parts'>"
 "<li>Calculate the charge that flows.</li>"
 "<li>Calculate the electrical energy transferred.</li>"
 "<li>If the motor lifts a 1.5 kg load by 40 cm in this time, find its efficiency.</li></ol>",
 8,
 "Potential difference across a component = the electrical energy transferred to other forms per unit "
 "charge passing through it (V = W/Q).<br>"
 "<b>(a)</b> Q = It = 0.50 &times; 120 = <b>60 C</b>.<br>"
 "<b>(b)</b> W = VQ = 12 &times; 60 = <b>720 J</b> (= VIt).<br>"
 "<b>(c)</b> Useful output = mgh = 1.5 &times; 9.81 &times; 0.40 = 5.89 J. "
 "Efficiency = 5.89/720 = 0.0082 = <b>0.82%</b> (very low &mdash; most energy is dissipated as heat "
 "in the windings and against friction).")

add(T9,
 "The I&ndash;V characteristics of a metallic conductor at constant temperature, a filament lamp, and "
 "a semiconductor diode differ markedly."
 "<ol class='parts'>"
 "<li>Sketch all three characteristics on the same axes.</li>"
 "<li>Explain the shape of the filament-lamp characteristic.</li>"
 "<li>State how the resistance of the diode varies as the forward voltage increases from zero.</li></ol>",
 8,
 "<b>(a)</b> Metallic conductor: a straight line through the origin (constant gradient). "
 "Filament lamp: an S-shaped curve through the origin that becomes less steep (gradient decreases) as "
 "|V| increases. Diode: negligible current for reverse and small forward voltages, then a sharp rise "
 "in current above the forward 'turn-on' voltage (&asymp; 0.6 V); essentially zero current when "
 "reverse-biased.<br>"
 "<b>(b)</b> As the current increases, the filament heats up; the higher temperature increases the "
 "resistance (metal ions vibrate more, impeding electron flow), so a given increase in V produces a "
 "smaller increase in I &mdash; hence the curve bends over.<br>"
 "<b>(c)</b> The diode's resistance is very high at zero/low forward voltage and <b>decreases</b> "
 "rapidly once the turn-on voltage is exceeded (it conducts freely).",
 "<svg width='300' height='150' viewBox='0 0 300 150'>"
 "<line x1='30' y1='80' x2='280' y2='80' stroke='#333'/>"
 "<line x1='150' y1='15' x2='150' y2='145' stroke='#333'/>"
 "<line x1='60' y1='120' x2='240' y2='40' stroke='#06c' stroke-width='2'/>"
 "<path d='M150 80 C185 78 215 62 245 30' fill='none' stroke='#093' stroke-width='2'/>"
 "<path d='M55 130 C120 90 148 82 150 80 L150 80 C165 79 175 60 178 20' fill='none' stroke='#c30' stroke-width='2'/>"
 "<text x='250' y='95' font-size='9'>V</text><text x='156' y='24' font-size='9'>I</text>"
 "<text x='210' y='45' font-size='8' fill='#06c'>metal</text>"
 "<text x='215' y='30' font-size='8' fill='#093'>lamp</text>"
 "<text x='120' y='30' font-size='8' fill='#c30'>diode</text></svg>")

add(T9,
 "State <b>Ohm's law</b>. A nichrome wire has resistance 6.0 &Omega;. A second nichrome wire of the "
 "same material has twice the length and half the diameter of the first."
 "<ol class='parts'>"
 "<li>Calculate the resistance of the second wire.</li>"
 "<li>Explain, using R = &rho;L/A, each factor by which the resistance changes.</li></ol>",
 7,
 "Ohm's law: the current in a metallic conductor is directly proportional to the potential difference "
 "across it, provided physical conditions (especially temperature) remain constant.<br>"
 "<b>(a)</b> R = &rho;L/A. Doubling length &times;2. Half the diameter &rArr; area &times;&frac14; "
 "(A &prop; d&sup2;), so 1/A &times;4. Overall factor = 2 &times; 4 = 8. "
 "R<sub>2</sub> = 8 &times; 6.0 = <b>48 &Omega;</b>.<br>"
 "<b>(b)</b> L doubles &rArr; R doubles (longer path, more collisions). The diameter halving reduces "
 "the cross-sectional area to one quarter, and since R &prop; 1/A this multiplies R by 4. The two "
 "effects combine to multiply R by 8.")

add(T9,
 "A resistivity experiment gives, for a wire of uniform diameter 0.38 mm and length 1.20 m, a "
 "resistance of 4.6 &Omega;."
 "<ol class='parts'>"
 "<li>Calculate the resistivity of the material.</li>"
 "<li>The diameter is measured with a micrometer to &plusmn;0.01 mm and the length to &plusmn;1 cm. "
 "State which measurement contributes most to the percentage uncertainty in the resistivity, and why.</li></ol>",
 8,
 "A = &pi;d&sup2;/4 = &pi;(0.38&times;10<sup>&minus;3</sup>)&sup2;/4 = 1.134&times;10<sup>&minus;7</sup> m&sup2;.<br>"
 "<b>(a)</b> &rho; = RA/L = (4.6 &times; 1.134&times;10<sup>&minus;7</sup>)/1.20 = "
 "5.216&times;10<sup>&minus;7</sup>/1.20 = <b>4.3&times;10<sup>&minus;7</sup> &Omega; m</b>.<br>"
 "<b>(b)</b> Percentage uncertainties: length 1/120 &asymp; 0.83%; diameter 0.01/0.38 = 2.6%, but d is "
 "<b>squared</b> in the area, so it contributes 2 &times; 2.6% = 5.2%. The <b>diameter</b> dominates, "
 "both because its fractional uncertainty is larger and because it enters as d&sup2;.")

add(T9,
 "Define <b>resistance</b>. A 60 W, 240 V lamp and a 100 W, 240 V lamp are each operated at their "
 "rated values."
 "<ol class='parts'>"
 "<li>Calculate the operating resistance of each lamp.</li>"
 "<li>State, with a reason, which lamp has the thicker or shorter filament (assuming same material and "
 "operating temperature).</li></ol>",
 7,
 "Resistance = the ratio of the potential difference across a component to the current through it, "
 "R = V/I.<br>"
 "<b>(a)</b> P = V&sup2;/R &rArr; R = V&sup2;/P. 60 W lamp: R = 240&sup2;/60 = 57600/60 = "
 "<b>960 &Omega;</b>. 100 W lamp: R = 240&sup2;/100 = <b>576 &Omega;</b>.<br>"
 "<b>(b)</b> The 100 W lamp has the lower resistance. Since R = &rho;L/A, a lower R means a shorter "
 "and/or thicker filament; the higher-power (100 W) lamp therefore has the <b>thicker (or shorter) "
 "filament</b> to allow a larger current at the same voltage.")

add(T9,
 "Explain, in terms of charge carriers, why the resistance of (i) a thermistor decreases as its "
 "temperature rises and (ii) a light-dependent resistor (LDR) decreases as light intensity increases. "
 "Contrast this with the behaviour of a metal as its temperature rises.",
 7,
 "<b>(i) Thermistor:</b> it is a semiconductor. As temperature rises, more electrons gain enough "
 "energy to become free charge carriers, so the number density n of carriers increases greatly. "
 "This increase outweighs the increased vibration of the lattice, so resistance falls.<br>"
 "<b>(ii) LDR:</b> incident light delivers energy that frees more charge carriers, again increasing n "
 "and so decreasing the resistance as intensity increases.<br>"
 "<b>Metal contrast:</b> in a metal the number of free electrons is essentially fixed; raising the "
 "temperature makes the positive ions vibrate more, scattering the electrons more often, so the "
 "resistance <b>increases</b>.")

add(T9,
 "A 2.5 kW electric heater is designed for a 230 V mains supply."
 "<ol class='parts'>"
 "<li>Calculate the current it draws and its resistance.</li>"
 "<li>The heater is instead connected to a 115 V supply. Assuming its resistance is unchanged, "
 "calculate the power now dissipated and comment on the result.</li></ol>",
 7,
 "<b>(a)</b> I = P/V = 2500/230 = <b>10.9 A</b>. R = V/I = 230/10.9 = <b>21.2 &Omega;</b> "
 "(or R = V&sup2;/P = 230&sup2;/2500 = 21.2 &Omega;).<br>"
 "<b>(b)</b> P = V&sup2;/R = 115&sup2;/21.2 = 13225/21.2 = <b>625 W</b>. "
 "Halving the voltage quarters the power (P &prop; V&sup2;), so the heater delivers only one quarter "
 "of its rated output &mdash; it would heat much less effectively.")

add(T9,
 "The current in a conductor is not the same thing as the drift of individual electrons. Using "
 "I = Anvq, explain what happens to the drift speed when a wire of the same material narrows to half "
 "its cross-sectional area, if the current is unchanged. State what this implies about charge "
 "conservation.",
 6,
 "For a given material n and q are fixed, and the current I is the same all along a series conductor "
 "(charge is conserved &mdash; charge cannot pile up). Since I = Anvq, if A halves then v must double "
 "to keep I = Anvq constant. So the electrons drift <b>twice as fast</b> in the narrow section.<br>"
 "This is consistent with conservation of charge: the same number of coulombs pass every "
 "cross-section per second, so where the wire is thinner the carriers simply move faster to carry the "
 "identical current.")

add(T9,
 "A student has a length of resistance wire and wants a 5.0 &Omega; resistor. The wire has resistance "
 "2.0 &Omega; per metre."
 "<ol class='parts'>"
 "<li>Find the length needed.</li>"
 "<li>The student instead cuts three equal lengths of this same 2.5 m wire and connects them in "
 "parallel. Find the resistance of the combination.</li></ol>",
 7,
 "<b>(a)</b> Length = R/(resistance per metre) = 5.0/2.0 = <b>2.5 m</b>.<br>"
 "<b>(b)</b> A 2.5 m length has resistance 2.5 &times; 2.0 = 5.0 &Omega;. Cut into three equal "
 "pieces: each is 5.0/3 = 1.667 &Omega;. In parallel: 1/R = 3/1.667 = 1.80, "
 "so R = <b>0.56 &Omega;</b>. (Equivalently three equal resistors in parallel give R<sub>each</sub>/3 "
 "= 1.667/3 = 0.56 &Omega;.)")

add(T9,
 "A 100 m length of overhead power cable has a total resistance of 0.40 &Omega; and carries a "
 "current of 250 A."
 "<ol class='parts'>"
 "<li>Calculate the power dissipated as heat in the cable.</li>"
 "<li>Explain, with reference to P = I&sup2;R, why electrical power is transmitted at high voltage "
 "and low current.</li></ol>",
 6,
 "<b>(a)</b> P = I&sup2;R = 250&sup2; &times; 0.40 = 62500 &times; 0.40 = <b>2.5&times;10<sup>4</sup> W</b> "
 "(25 kW).<br>"
 "<b>(b)</b> For a given power P = VI to be delivered, using a higher voltage allows a smaller current. "
 "Since the heating loss in the cables is I&sup2;R, reducing the current has a large effect "
 "(loss &prop; I&sup2;): e.g. halving the current quarters the wasted power. Transmitting at high "
 "voltage and low current therefore minimises energy wasted as heat in the transmission lines.")

add(T9,
 "Two wires P and Q are connected in series across a battery. P has resistance 4.0 &Omega; and Q has "
 "resistance 8.0 &Omega;."
 "<ol class='parts'>"
 "<li>Compare the current in P with that in Q.</li>"
 "<li>Compare the power dissipated in P with that in Q.</li>"
 "<li>Explain your answer to (b) using P = I&sup2;R.</li></ol>",
 6,
 "<b>(a)</b> In series the current is the <b>same</b> through both: I<sub>P</sub> = I<sub>Q</sub>.<br>"
 "<b>(b)</b> Power in Q is twice that in P: P<sub>Q</sub>/P<sub>P</sub> = 8.0/4.0 = 2. So Q "
 "dissipates <b>twice</b> the power of P.<br>"
 "<b>(c)</b> With the same current I in both, P = I&sup2;R &prop; R. Since Q has double the resistance "
 "of P, it dissipates double the power. (The larger resistor gets hotter in a series circuit.)")


# ===========================================================================
# TOPIC 10  D.C. circuits  (14 questions)
# ===========================================================================
T10 = "10&nbsp;&nbsp;D.C. circuits"

add(T10,
 "A cell of e.m.f. 1.5 V and internal resistance 0.50 &Omega; is connected to an external resistor "
 "of 2.5 &Omega;."
 "<ol class='parts'>"
 "<li>Calculate the current in the circuit.</li>"
 "<li>Calculate the terminal potential difference.</li>"
 "<li>Calculate the power wasted inside the cell.</li></ol>",
 7,
 "<b>(a)</b> &epsilon; = I(R + r): I = &epsilon;/(R + r) = 1.5/(2.5 + 0.50) = 1.5/3.0 = "
 "<b>0.50 A</b>.<br>"
 "<b>(b)</b> Terminal p.d. V = IR = 0.50 &times; 2.5 = <b>1.25 V</b> "
 "(= &epsilon; &minus; Ir = 1.5 &minus; 0.50&times;0.50 = 1.25 V).<br>"
 "<b>(c)</b> Power in internal resistance = I&sup2;r = 0.50&sup2; &times; 0.50 = "
 "<b>0.125 W</b>.")

add(T10,
 "State <b>Kirchhoff's first and second laws</b>, and state the conservation principle underlying "
 "each. Explain briefly why the first law must hold at any junction in a circuit that carries a "
 "steady current.",
 6,
 "First law: the sum of the currents entering a junction equals the sum of the currents leaving it "
 "(&Sigma;I<sub>in</sub> = &Sigma;I<sub>out</sub>). This follows from conservation of <b>charge</b>.<br>"
 "Second law: around any closed loop, the sum of the e.m.f.s equals the sum of the p.d.s "
 "(&Sigma;&epsilon; = &Sigma;IR). This follows from conservation of <b>energy</b>.<br>"
 "The first law must hold for a steady current because charge cannot accumulate at a junction "
 "(there is no build-up): every coulomb per second arriving must leave, otherwise charge (and hence "
 "the current) would change with time, contradicting the steady state.")

add(T10,
 "Derive, using Kirchhoff's laws, the formula for the combined resistance of two resistors "
 "R<sub>1</sub> and R<sub>2</sub> connected in parallel across a supply of p.d. V.",
 6,
 "The two resistors share the same p.d. V (both across the supply). "
 "By Kirchhoff's first law the total current splits: I = I<sub>1</sub> + I<sub>2</sub>.<br>"
 "For each resistor I<sub>1</sub> = V/R<sub>1</sub> and I<sub>2</sub> = V/R<sub>2</sub>. "
 "For the single equivalent resistance R: I = V/R.<br>"
 "Substituting: V/R = V/R<sub>1</sub> + V/R<sub>2</sub>. Dividing through by V gives "
 "<b>1/R = 1/R<sub>1</sub> + 1/R<sub>2</sub></b>.")

add(T10,
 "In the circuit, a 12 V battery of negligible internal resistance is connected to a 3.0 &Omega; "
 "resistor in series with a parallel combination of a 6.0 &Omega; and a 12 &Omega; resistor."
 "<ol class='parts'>"
 "<li>Find the total resistance.</li>"
 "<li>Find the current drawn from the battery.</li>"
 "<li>Find the current in the 12 &Omega; resistor.</li></ol>",
 8,
 "<b>(a)</b> Parallel pair: 1/R<sub>p</sub> = 1/6.0 + 1/12 = 2/12 + 1/12 = 3/12 &rArr; "
 "R<sub>p</sub> = 4.0 &Omega;. Total = 3.0 + 4.0 = <b>7.0 &Omega;</b>.<br>"
 "<b>(b)</b> I = V/R = 12/7.0 = <b>1.71 A</b>.<br>"
 "<b>(c)</b> P.d. across the parallel pair = I &times; R<sub>p</sub> = 1.71 &times; 4.0 = 6.86 V. "
 "Current in 12 &Omega;: I = 6.86/12 = <b>0.57 A</b>.",
 "<svg width='300' height='130' viewBox='0 0 300 130'>"
 "<line x1='30' y1='30' x2='30' y2='100' stroke='#333'/><line x1='26' y1='55' x2='34' y2='55' stroke='#333'/>"
 "<line x1='24' y1='62' x2='36' y2='62' stroke='#333' stroke-width='2'/>"
 "<line x1='30' y1='30' x2='90' y2='30' stroke='#333'/>"
 "<rect x='90' y='24' width='40' height='12' fill='none' stroke='#333'/><text x='95' y='20' font-size='8'>3.0&Omega;</text>"
 "<line x1='130' y1='30' x2='200' y2='30' stroke='#333'/>"
 "<line x1='200' y1='30' x2='200' y2='45' stroke='#333'/><line x1='200' y1='30' x2='260' y2='30' stroke='#333'/>"
 "<rect x='180' y='45' width='40' height='12' fill='none' stroke='#333'/><text x='185' y='42' font-size='8'>6.0&Omega;</text>"
 "<line x1='200' y1='57' x2='200' y2='100' stroke='#333'/>"
 "<rect x='240' y='45' width='40' height='12' fill='none' stroke='#333' transform='translate(20,0)'/>"
 "<text x='250' y='42' font-size='8'>12&Omega;</text>"
 "<line x1='260' y1='30' x2='260' y2='45' stroke='#333'/><line x1='260' y1='57' x2='260' y2='100' stroke='#333'/>"
 "<line x1='30' y1='100' x2='260' y2='100' stroke='#333'/>"
 "<text x='6' y='70' font-size='8'>12 V</text></svg>")

add(T10,
 "Distinguish between the <b>e.m.f.</b> of a source and the <b>potential difference</b> across its "
 "terminals, in terms of energy. Explain why the terminal p.d. falls below the e.m.f. when the source "
 "delivers a current, and describe one situation in which the terminal p.d. equals the e.m.f.",
 6,
 "The e.m.f. is the electrical energy transferred (from other forms) per unit charge driven around the "
 "<b>complete</b> circuit by the source. The terminal p.d. is the electrical energy transferred to the "
 "<b>external</b> circuit per unit charge.<br>"
 "When a current I flows, some energy per unit charge is dissipated inside the source across its "
 "internal resistance r (an amount Ir). Hence V = &epsilon; &minus; Ir &lt; &epsilon;.<br>"
 "The terminal p.d. equals the e.m.f. when no current flows (open circuit, I = 0), so there is no "
 "'lost volts' Ir &mdash; for example when the terminal p.d. is measured by a voltmeter of "
 "(ideally) infinite resistance.")

add(T10,
 "A potential divider consists of two fixed resistors, R<sub>1</sub> = 4.0 k&Omega; (top) and "
 "R<sub>2</sub> = 6.0 k&Omega; (bottom), across a 9.0 V supply, with the output taken across "
 "R<sub>2</sub>."
 "<ol class='parts'>"
 "<li>Calculate the output voltage on no load.</li>"
 "<li>A voltmeter of resistance 6.0 k&Omega; is now connected across the output. Calculate the new "
 "output reading, and comment.</li></ol>",
 8,
 "<b>(a)</b> V<sub>out</sub> = V R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>) = "
 "9.0 &times; 6.0/(4.0 + 6.0) = 9.0 &times; 0.60 = <b>5.4 V</b>.<br>"
 "<b>(b)</b> The 6.0 k&Omega; voltmeter is in parallel with R<sub>2</sub> (6.0 k&Omega;): "
 "combined = (6.0 &times; 6.0)/(6.0 + 6.0) = 3.0 k&Omega;. "
 "V<sub>out</sub> = 9.0 &times; 3.0/(4.0 + 3.0) = 9.0 &times; 3.0/7.0 = <b>3.9 V</b>.<br>"
 "Comment: the reading has dropped substantially (5.4 &rarr; 3.9 V) &mdash; the voltmeter 'loads' the "
 "divider by drawing current. A high-resistance voltmeter would disturb the circuit far less.")

add(T10,
 "Explain the principle of a <b>potentiometer</b> used as a means of comparing two potential "
 "differences, and describe the role of the galvanometer in the null method. State one advantage of "
 "this method over using a voltmeter.",
 7,
 "A potentiometer is a uniform resistance wire carrying a steady current from a driver cell, so the "
 "p.d. along it is proportional to length. A source to be measured is connected (via a galvanometer) "
 "between one end and a sliding contact. The contact is moved until the galvanometer reads "
 "<b>zero</b> (the balance/null point): then the p.d. of the source equals the p.d. across that "
 "length of wire, so p.d. &prop; balance length. Comparing two sources' balance lengths gives the "
 "ratio of their p.d.s (V<sub>1</sub>/V<sub>2</sub> = L<sub>1</sub>/L<sub>2</sub>).<br>"
 "The galvanometer detects the balance condition: at null it carries no current, indicating the two "
 "p.d.s are equal and opposite.<br>"
 "Advantage: at balance the source drives <b>no current</b>, so no current flows through its internal "
 "resistance &mdash; the true e.m.f./p.d. is measured without the 'lost volts' error that a "
 "current-drawing voltmeter would introduce.")

add(T10,
 "Two identical cells, each of e.m.f. 1.5 V and internal resistance 0.30 &Omega;, are connected to a "
 "1.4 &Omega; external resistor."
 "<ol class='parts'>"
 "<li>Find the current if the cells are connected in series.</li>"
 "<li>Find the current if the cells are connected in parallel.</li></ol>",
 8,
 "<b>(a)</b> Series: total e.m.f. = 1.5 + 1.5 = 3.0 V; total internal resistance = 0.30 + 0.30 = "
 "0.60 &Omega;. I = 3.0/(1.4 + 0.60) = 3.0/2.0 = <b>1.5 A</b>.<br>"
 "<b>(b)</b> Parallel: e.m.f. stays 1.5 V; internal resistances in parallel = 0.30/2 = 0.15 &Omega;. "
 "I = 1.5/(1.4 + 0.15) = 1.5/1.55 = <b>0.97 A</b>. "
 "(Series gives more current here because the doubled e.m.f. outweighs the increased internal "
 "resistance for this relatively small external resistor.)")

add(T10,
 "A thermistor is used in a potential divider to make a temperature-sensing circuit that switches on "
 "a warning when the temperature becomes too high. The thermistor (negative temperature coefficient) "
 "is placed in series with a fixed resistor across a 6.0 V supply."
 "<ol class='parts'>"
 "<li>State how the thermistor's resistance changes as temperature rises.</li>"
 "<li>Explain how you would connect the output so that the output voltage <b>rises</b> as the "
 "temperature rises, and justify your choice.</li></ol>",
 7,
 "<b>(a)</b> As temperature rises, the thermistor's resistance <b>decreases</b>.<br>"
 "<b>(b)</b> Take the output across the <b>fixed resistor</b> (i.e. put the thermistor in the 'top' "
 "position). Then V<sub>out</sub> = V &times; R<sub>fixed</sub>/(R<sub>thermistor</sub> + R<sub>fixed</sub>). "
 "As temperature rises, R<sub>thermistor</sub> falls, so the denominator falls and the fraction "
 "increases &mdash; V<sub>out</sub> rises. This rising voltage can be fed to a switching circuit to "
 "trigger the warning at high temperature.")

add(T10,
 "In the circuit shown, a 6.0 V battery of internal resistance 0.50 &Omega; supplies two resistors: "
 "R<sub>1</sub> = 10 &Omega; in parallel with R<sub>2</sub> = 15 &Omega;. Use Kirchhoff's laws to "
 "find the terminal p.d. and the current in each resistor.",
 8,
 "Parallel combination: 1/R<sub>p</sub> = 1/10 + 1/15 = 3/30 + 2/30 = 5/30 &rArr; R<sub>p</sub> = "
 "6.0 &Omega;.<br>"
 "Total current from battery (loop, Kirchhoff II): &epsilon; = I(R<sub>p</sub> + r): "
 "6.0 = I(6.0 + 0.50) &rArr; I = 6.0/6.5 = 0.923 A.<br>"
 "Terminal p.d. = &epsilon; &minus; Ir = 6.0 &minus; 0.923&times;0.50 = <b>5.54 V</b> "
 "(= p.d. across the parallel pair).<br>"
 "Currents (Kirchhoff I): I<sub>1</sub> = 5.54/10 = <b>0.55 A</b>; I<sub>2</sub> = 5.54/15 = "
 "<b>0.37 A</b>. Check: 0.55 + 0.37 = 0.92 A = total. &#10003;")

add(T10,
 "A battery of e.m.f. &epsilon; and internal resistance r delivers current to a variable external "
 "resistance R. Explain how the terminal p.d. and the power delivered to R vary as R is decreased "
 "from a very large value towards zero, and state the condition for maximum power transfer to R.",
 7,
 "As R decreases, the current I = &epsilon;/(R + r) increases. The terminal p.d. "
 "V = &epsilon; &minus; Ir therefore <b>decreases</b>: from &epsilon; (open circuit, R &rarr; &infin;) "
 "down towards 0 (short circuit, R &rarr; 0).<br>"
 "The power in R, P = I&sup2;R = &epsilon;&sup2;R/(R + r)&sup2;, is zero at both extremes "
 "(R &rarr; 0 gives R&rarr;0; R &rarr; &infin; gives I&rarr;0), so it rises to a maximum in between. "
 "Maximum power is delivered to R when <b>R = r</b> (the external resistance matches the internal "
 "resistance); then the transfer efficiency is 50%.")

add(T10,
 "A student connects a 12 V battery (internal resistance 1.0 &Omega;) to a network: a 4.0 &Omega; "
 "resistor in series with two 6.0 &Omega; resistors that are in parallel with each other."
 "<ol class='parts'>"
 "<li>Find the current drawn from the battery.</li>"
 "<li>Find the power dissipated in the 4.0 &Omega; resistor.</li>"
 "<li>Find the total power delivered by the battery and the fraction wasted internally.</li></ol>",
 9,
 "Two 6.0 &Omega; in parallel = 3.0 &Omega;. External total = 4.0 + 3.0 = 7.0 &Omega;. "
 "Including internal: 7.0 + 1.0 = 8.0 &Omega;.<br>"
 "<b>(a)</b> I = &epsilon;/(R + r) = 12/8.0 = <b>1.5 A</b>.<br>"
 "<b>(b)</b> P<sub>4&Omega;</sub> = I&sup2;R = 1.5&sup2; &times; 4.0 = 2.25 &times; 4.0 = "
 "<b>9.0 W</b>.<br>"
 "<b>(c)</b> Total power from battery = &epsilon;I = 12 &times; 1.5 = 18 W. "
 "Wasted internally = I&sup2;r = 1.5&sup2; &times; 1.0 = 2.25 W. "
 "Fraction wasted = 2.25/18 = <b>0.125 (12.5%)</b>.")

add(T10,
 "Describe how a light-dependent resistor (LDR) can be used in a potential divider to switch on a "
 "lamp automatically when it gets dark. Draw/describe the arrangement and explain the operation.",
 6,
 "Connect the LDR in series with a fixed resistor across a supply, taking the output across the "
 "<b>LDR</b> to a switching circuit (transistor/relay).<br>"
 "In the light the LDR has low resistance, so only a small fraction of the supply voltage appears "
 "across it &mdash; V<sub>out</sub> is low and the lamp stays off. As it gets dark the LDR's "
 "resistance rises sharply, so a larger share of the supply voltage now appears across the LDR &mdash; "
 "V<sub>out</sub> rises. When V<sub>out</sub> exceeds the switching threshold, the circuit turns the "
 "lamp on. (Swapping the LDR and fixed resistor would instead switch the lamp on in bright light.)")

add(T10,
 "Two resistors of 200 &Omega; and 300 &Omega; are available. A 5.0 V supply of negligible internal "
 "resistance is connected across them."
 "<ol class='parts'>"
 "<li>Find the total power dissipated when they are in series and when they are in parallel.</li>"
 "<li>State which arrangement dissipates more power and explain why using P = V&sup2;/R.</li></ol>",
 7,
 "<b>(a)</b> Series: R = 200 + 300 = 500 &Omega;; P = V&sup2;/R = 5.0&sup2;/500 = 25/500 = "
 "<b>0.050 W</b>. Parallel: 1/R = 1/200 + 1/300 = 3/600 + 2/600 = 5/600 &rArr; R = 120 &Omega;; "
 "P = 25/120 = <b>0.208 W</b>.<br>"
 "<b>(b)</b> The <b>parallel</b> arrangement dissipates more power. Both resistors have the full 5.0 V "
 "across them in parallel, and with P = V&sup2;/R a smaller total resistance (120 &Omega; vs "
 "500 &Omega;) at the same voltage means greater power. (In series the shared voltage and larger "
 "total resistance reduce the power.)")


# ===========================================================================
# TOPIC 11  Particle physics  (9 questions)
# ===========================================================================
T11 = "11&nbsp;&nbsp;Particle physics"

add(T11,
 "In the &alpha;-particle scattering experiment, a beam of &alpha;-particles is directed at a thin "
 "gold foil. Most pass almost straight through, a small fraction are deflected through large angles, "
 "and a very few are reflected back."
 "<ol class='parts'>"
 "<li>State what each of these three observations tells us about the atom.</li>"
 "<li>Explain why a thin foil and a vacuum are used.</li></ol>",
 7,
 "<b>(a)</b> Most pass straight through &rArr; the atom is mostly empty space. "
 "A small fraction deflected through large angles &rArr; there is a concentrated region of positive "
 "charge (the &alpha;-particles are positive and repelled). "
 "A very few rebounding almost backwards &rArr; this positive charge (and almost all the mass) is "
 "concentrated in a very small, dense <b>nucleus</b> that can turn a fast &alpha;-particle around.<br>"
 "<b>(b)</b> A thin foil ensures &alpha;-particles pass through with (mostly) a single scattering "
 "event, so deflections are due to individual nuclei; a vacuum prevents the &alpha;-particles from "
 "being absorbed or scattered by air molecules before reaching the foil/detector.")

add(T11,
 "A nuclide is written as <sup>A</sup><sub>Z</sub>X."
 "<ol class='parts'>"
 "<li>State what A and Z represent.</li>"
 "<li>The nuclide <sup>238</sup><sub>92</sub>U decays by &alpha;-emission to thorium (Th). Write the "
 "balanced decay equation and state the values of A and Z for the thorium nuclide.</li>"
 "<li>Explain what is conserved in the decay.</li></ol>",
 7,
 "<b>(a)</b> A = nucleon (mass) number = number of protons + neutrons; Z = proton (atomic) number = "
 "number of protons (which also equals the nuclear charge in units of e).<br>"
 "<b>(b)</b> <sup>238</sup><sub>92</sub>U &rarr; <sup>234</sup><sub>90</sub>Th + "
 "<sup>4</sup><sub>2</sub>&alpha; (i.e. <sup>4</sup><sub>2</sub>He). Thorium: <b>A = 234, Z = 90</b>.<br>"
 "<b>(c)</b> Both <b>nucleon number</b> (238 = 234 + 4) and <b>charge</b>/proton number "
 "(92 = 90 + 2) are conserved (as are mass&ndash;energy and momentum).")

add(T11,
 "Describe the composition, relative mass and relative charge of &alpha;-, &beta;<sup>&minus;</sup>- "
 "and &gamma;-radiations. Explain why &alpha;-particles from a given decay have discrete energies "
 "whereas &beta;-particles have a continuous range of energies.",
 8,
 "&alpha;: a helium nucleus (2 protons + 2 neutrons); relative mass 4 (u), relative charge +2e. "
 "&beta;<sup>&minus;</sup>: a fast electron; relative mass &asymp; 1/1840 u, charge &minus;e. "
 "&gamma;: a high-energy photon (electromagnetic); zero mass, zero charge.<br>"
 "In &alpha;-decay the energy released is shared between just two bodies (the &alpha;-particle and the "
 "recoiling nucleus), so conservation of momentum and energy fixes the &alpha; energy at discrete "
 "value(s) &mdash; a line spectrum. In &beta;-decay a third particle, the (anti)neutrino, is also "
 "emitted; the fixed decay energy is shared among <b>three</b> bodies in varying proportions, so the "
 "&beta;-particle can take any energy up to a maximum &mdash; giving a continuous spectrum.")

add(T11,
 "State what is meant by an <b>antiparticle</b>. Write the nuclear equation for the &beta;<sup>+</sup> "
 "decay of a nucleus <sup>A</sup><sub>Z</sub>X, naming all particles produced, and state the change "
 "(if any) in A and Z.",
 7,
 "An antiparticle has the same mass as its corresponding particle but the opposite charge (and other "
 "opposite quantum properties); e.g. the positron is the antiparticle of the electron.<br>"
 "&beta;<sup>+</sup> decay: a proton changes to a neutron, emitting a positron and an electron "
 "neutrino: <sup>A</sup><sub>Z</sub>X &rarr; <sup>A</sup><sub>Z&minus;1</sub>Y + "
 "<sup>0</sup><sub>+1</sub>e + &nu;<sub>e</sub> (positron e<sup>+</sup> and neutrino &nu;).<br>"
 "Nucleon number A is <b>unchanged</b>; proton number Z <b>decreases by 1</b> (charge conserved: "
 "Z = (Z&minus;1) + 1).")

add(T11,
 "Quarks are fundamental particles."
 "<ol class='parts'>"
 "<li>State the charges (in units of e) of the up, down and strange quarks.</li>"
 "<li>Show that the quark composition of a proton (uud) and a neutron (udd) gives the correct charges.</li>"
 "<li>State the composition of a baryon and of a meson in terms of quarks.</li></ol>",
 7,
 "<b>(a)</b> up: +&frac23;e; down: &minus;&frac13;e; strange: &minus;&frac13;e. "
 "(Each corresponding antiquark has the opposite charge.)<br>"
 "<b>(b)</b> Proton uud: (+&frac23;) + (+&frac23;) + (&minus;&frac13;) = +1e. &#10003; "
 "Neutron udd: (+&frac23;) + (&minus;&frac13;) + (&minus;&frac13;) = 0. &#10003;<br>"
 "<b>(c)</b> A baryon is composed of <b>three quarks</b>; a meson is composed of <b>one quark and one "
 "antiquark</b>.")

add(T11,
 "Describe, in terms of quarks, the changes that occur during (i) &beta;<sup>&minus;</sup> decay and "
 "(ii) &beta;<sup>+</sup> decay. State which fundamental particles (leptons) are emitted in each.",
 7,
 "<b>(i) &beta;<sup>&minus;</sup> decay:</b> a neutron becomes a proton, i.e. a <b>down quark changes "
 "to an up quark</b> (udd &rarr; uud). An electron and an electron <b>antineutrino</b> "
 "(&#772;&nu;<sub>e</sub>) are emitted.<br>"
 "<b>(ii) &beta;<sup>+</sup> decay:</b> a proton becomes a neutron, i.e. an <b>up quark changes to a "
 "down quark</b> (uud &rarr; udd). A positron and an electron <b>neutrino</b> (&nu;<sub>e</sub>) are "
 "emitted.<br>"
 "Electrons, positrons and neutrinos are all leptons (fundamental particles).")

add(T11,
 "The unified atomic mass unit (u) is used as a unit of mass in nuclear physics."
 "<ol class='parts'>"
 "<li>State the approximate value of 1 u in kilograms.</li>"
 "<li>A carbon-12 nucleus has 6 protons and 6 neutrons. Using masses of 1.007 u (proton) and "
 "1.009 u (neutron), calculate the total mass of the separate nucleons in u, and comment on why this "
 "exceeds 12 u.</li></ol>",
 6,
 "<b>(a)</b> 1 u &asymp; 1.66&times;10<sup>&minus;27</sup> kg.<br>"
 "<b>(b)</b> Total = 6(1.007) + 6(1.009) = 6.042 + 6.054 = <b>12.096 u</b>. This is greater than the "
 "12 u mass of the assembled carbon-12 nucleus: when the nucleons bind together, energy (the binding "
 "energy) is released, and by mass&ndash;energy equivalence this appears as a loss of mass (the "
 "'mass defect'). So the bound nucleus is lighter than its separated parts.")

add(T11,
 "Classify each of the following as a lepton, a baryon or a meson, giving a brief reason: "
 "(i) a proton, (ii) an electron, (iii) a particle consisting of an up quark and a down antiquark, "
 "(iv) a neutrino.",
 6,
 "(i) Proton &mdash; a <b>baryon</b>: it is made of three quarks (uud).<br>"
 "(ii) Electron &mdash; a <b>lepton</b>: it is a fundamental particle, not made of quarks.<br>"
 "(iii) up + anti-down &mdash; a <b>meson</b>: one quark plus one antiquark (this is a &pi;<sup>+</sup>).<br>"
 "(iv) Neutrino &mdash; a <b>lepton</b>: a fundamental particle (emitted in &beta;-decay).")

add(T11,
 "A nucleus <sup>14</sup><sub>6</sub>C undergoes &beta;<sup>&minus;</sup> decay to nitrogen (N)."
 "<ol class='parts'>"
 "<li>Write the full decay equation, including the antineutrino.</li>"
 "<li>State how the nucleon number and proton number of the daughter compare with the parent, and "
 "confirm charge is conserved.</li></ol>",
 6,
 "<b>(a)</b> <sup>14</sup><sub>6</sub>C &rarr; <sup>14</sup><sub>7</sub>N + "
 "<sup>0</sup><sub>&minus;1</sub>e + &#772;&nu;<sub>e</sub> (an electron and an electron "
 "antineutrino).<br>"
 "<b>(b)</b> Nucleon number is unchanged (14 &rarr; 14); proton number increases by 1 (6 &rarr; 7) as "
 "a neutron converts to a proton. Charge: parent +6e = daughter (+7e) + electron (&minus;e) + "
 "antineutrino (0) = +6e. &#10003; Charge is conserved.")
