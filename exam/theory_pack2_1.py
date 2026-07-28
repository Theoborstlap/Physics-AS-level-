# -*- coding: utf-8 -*-
"""PACK 2 - Structured (theory) questions, topics 1-4. AS 9702.
Appends to engine.theory. All content is new and distinct from Pack 1."""
from engine import theory as T

T1 = "1&nbsp;&nbsp;Physical quantities and units"
T2 = "2&nbsp;&nbsp;Kinematics"
T3 = "3&nbsp;&nbsp;Dynamics"
T4 = "4&nbsp;&nbsp;Forces, density and pressure"


def add(topic, q, marks, ans, svg=""):
    T.append({"topic": topic, "q": q, "marks": marks, "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 1
# ===========================================================================
add(T1,
 "The drag force on a car is modelled by <span class='eq'>F = &frac12;C&rho;Av&sup2;</span>, where "
 "&rho; is the air density, A the frontal area and v the speed."
 "<ol class='parts'>"
 "<li>Use SI base units to show that the constant C is dimensionless.</li>"
 "<li>A car of frontal area 2.1 m&sup2; travelling at 25 m s<sup>&minus;1</sup> in air of density "
 "1.2 kg m<sup>&minus;3</sup> experiences a drag force of 560 N. Calculate C.</li></ol>",
 7,
 "<b>(a)</b> &rho;Av&sup2; has base units (kg m<sup>&minus;3</sup>)(m&sup2;)(m&sup2; s<sup>&minus;2</sup>) "
 "= kg m s<sup>&minus;2</sup> = N, the unit of F. So &frac12;C must be dimensionless &rArr; "
 "<b>C is dimensionless</b>.<br>"
 "<b>(b)</b> C = 2F/(&rho;Av&sup2;) = 2&times;560/(1.2&times;2.1&times;25&sup2;) = "
 "1120/1575 = <b>0.71</b>.")

add(T1,
 "Estimates are an important physics skill."
 "<ol class='parts'>"
 "<li>Estimate the number of times a human heart beats in a lifetime, showing your assumptions.</li>"
 "<li>Given that a heart pumps about 70 cm&sup3; of blood per beat, estimate the total volume of "
 "blood pumped in a lifetime.</li></ol>",
 6,
 "<b>(a)</b> Assume ~70 beats per minute and a lifetime of ~75 years. "
 "Beats = 70 &times; 60 &times; 24 &times; 365 &times; 75 &asymp; <b>3 &times; 10<sup>9</sup> beats</b> "
 "(any answer 2&ndash;4 &times; 10<sup>9</sup> acceptable).<br>"
 "<b>(b)</b> Volume &asymp; 3&times;10<sup>9</sup> &times; 70&times;10<sup>&minus;6</sup> m&sup3; = "
 "<b>2 &times; 10<sup>5</sup> m&sup3;</b> (about 2&times;10<sup>8</sup> litres).")

add(T1,
 "Express each of the following derived units in terms of SI base units only."
 "<ol class='parts'>"
 "<li>the pascal (Pa)</li><li>the watt (W)</li><li>the volt (V)</li></ol>",
 6,
 "<b>(a)</b> Pa = N m<sup>&minus;2</sup> = kg m s<sup>&minus;2</sup> &middot; m<sup>&minus;2</sup> = "
 "<b>kg m<sup>&minus;1</sup> s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> W = J s<sup>&minus;1</sup> = kg m&sup2; s<sup>&minus;2</sup> &middot; s<sup>&minus;1</sup> = "
 "<b>kg m&sup2; s<sup>&minus;3</sup></b>.<br>"
 "<b>(c)</b> V = W A<sup>&minus;1</sup> = kg m&sup2; s<sup>&minus;3</sup> &middot; A<sup>&minus;1</sup> = "
 "<b>kg m&sup2; s<sup>&minus;3</sup> A<sup>&minus;1</sup></b>.")

add(T1,
 "A student times a simple pendulum, for which <span class='eq'>T = 2&pi;&radic;(L/g)</span>. "
 "They measure the length L = (0.994 &plusmn; 0.002) m and the time for 20 complete oscillations as "
 "(39.8 &plusmn; 0.4) s."
 "<ol class='parts'>"
 "<li>Calculate a value for g.</li>"
 "<li>Determine the percentage uncertainty in g and hence its absolute uncertainty.</li></ol>",
 8,
 "T = 39.8/20 = 1.99 s.<br>"
 "<b>(a)</b> g = 4&pi;&sup2;L/T&sup2; = 4&pi;&sup2;(0.994)/1.99&sup2; = 39.24/3.960 = "
 "<b>9.91 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> %L = 0.002/0.994 = 0.20%; %T = 0.4/39.8 = 1.005%, and T is squared &rArr; 2.01%. "
 "%g = 0.20 + 2.01 = <b>2.2%</b>. &Delta;g = 0.022 &times; 9.91 = 0.22 &rArr; "
 "g = <b>(9.9 &plusmn; 0.2) m s<sup>&minus;2</sup></b>.")

add(T1,
 "In an experiment the potential difference across a resistor is (6.0 &plusmn; 0.1) V and the current "
 "is (0.25 &plusmn; 0.01) A."
 "<ol class='parts'>"
 "<li>Calculate the resistance.</li>"
 "<li>Determine the absolute uncertainty in the resistance and state the result appropriately.</li></ol>",
 5,
 "<b>(a)</b> R = V/I = 6.0/0.25 = <b>24 &Omega;</b>.<br>"
 "<b>(b)</b> %R = %V + %I = 0.1/6.0 + 0.01/0.25 = 1.67% + 4.0% = 5.67%. "
 "&Delta;R = 0.0567 &times; 24 = 1.4 &rArr; R = <b>(24 &plusmn; 1) &Omega;</b>.")

add(T1,
 "A 12 N weight hangs from a light string. A horizontal force H is applied to the weight so that the "
 "string makes an angle of 25&deg; with the vertical and the weight is in equilibrium."
 "<ol class='parts'>"
 "<li>Draw a free-body diagram and resolve forces to find the tension in the string.</li>"
 "<li>Find the horizontal force H.</li></ol>",
 6,
 "Three forces: weight 12 N (down), tension T (along string), horizontal push H.<br>"
 "<b>(a)</b> Vertical: T cos25&deg; = 12 &rArr; T = 12/0.906 = <b>13.2 N</b>.<br>"
 "<b>(b)</b> Horizontal: H = T sin25&deg; = 13.2 &times; 0.423 = <b>5.6 N</b>.")

add(T1,
 "Two forces of magnitude 5.0 N and 8.0 N act at a point with an angle of 50&deg; between them."
 "<ol class='parts'>"
 "<li>Calculate the magnitude of their resultant.</li>"
 "<li>Find the angle between the resultant and the 8.0 N force.</li></ol>",
 6,
 "<b>(a)</b> R&sup2; = 5.0&sup2; + 8.0&sup2; + 2(5.0)(8.0)cos50&deg; = 25 + 64 + 80(0.643) = 140.4 &rArr; "
 "R = <b>11.9 N</b>.<br>"
 "<b>(b)</b> tan&alpha; = 5.0 sin50&deg;/(8.0 + 5.0 cos50&deg;) = 3.83/11.21 = 0.342 &rArr; "
 "&alpha; = <b>18.9&deg;</b> from the 8.0 N force.")

add(T1,
 "An analogue ammeter reads 0.20 A when no current passes through it. A student then uses it to "
 "record four readings of a steady current: 2.05, 2.07, 2.06, 2.04 A."
 "<ol class='parts'>"
 "<li>Name the type of error indicated by the reading of 0.20 A with no current, and state the "
 "corrected mean current.</li>"
 "<li>Comment on the precision of the four readings, and explain why high precision does not "
 "guarantee an accurate result here.</li></ol>",
 6,
 "<b>(a)</b> A non-zero reading with no current is a <b>zero (systematic) error</b>. Mean reading = "
 "2.055 A; corrected current = 2.055 &minus; 0.20 = <b>1.86 A</b>.<br>"
 "<b>(b)</b> The readings agree to within &plusmn;0.02 A, so they are <b>precise</b> (small random "
 "scatter). But precision only reflects repeatability; the constant 0.20 A zero error shifts every "
 "reading the same way, so the uncorrected values are systematically too high &mdash; precise but "
 "inaccurate until corrected.")

add(T1,
 "The speed <span class='eq'>v</span> of a transverse wave on a stretched string is thought to "
 "depend on the tension <span class='eq'>T</span> in the string and its mass per unit length "
 "<span class='eq'>&mu;</span> (base units kg m<sup>&minus;1</sup>), such that "
 "<span class='eq'>v = kT<sup>a</sup>&mu;<sup>b</sup></span> with k a dimensionless constant."
 "<ol class='parts'>"
 "<li>Use base units to determine a and b.</li>"
 "<li>Write down the resulting relationship.</li></ol>",
 7,
 "Base units: v = m s<sup>&minus;1</sup>; T = kg m s<sup>&minus;2</sup>; &mu; = kg m<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> m s<sup>&minus;1</sup> = (kg m s<sup>&minus;2</sup>)<sup>a</sup>(kg m<sup>&minus;1</sup>)<sup>b</sup> "
 "= kg<sup>a+b</sup> m<sup>a&minus;b</sup> s<sup>&minus;2a</sup>. "
 "s: &minus;2a = &minus;1 &rArr; a = &frac12;. kg: a + b = 0 &rArr; b = &minus;&frac12;. "
 "(check m: a &minus; b = 1 &#10003;). So <b>a = &frac12;, b = &minus;&frac12;</b>.<br>"
 "<b>(b)</b> <b>v = k&radic;(T/&mu;)</b>.")

add(T1,
 "Estimate the average pressure exerted on the floor by a person of mass 70 kg standing still. "
 "State clearly the estimate you make for the contact area and give your answer to an appropriate "
 "number of significant figures.",
 4,
 "Weight = 70 &times; 9.81 = 687 N. Estimate the contact area of two shoes as about 0.02 m&sup2; "
 "(&asymp; 200 cm&sup2;). p = F/A = 687/0.02 &asymp; <b>3 &times; 10<sup>4</sup> Pa</b> "
 "(any 2&ndash;5 &times; 10<sup>4</sup> Pa with a sensible area is acceptable).")

add(T1,
 "A block of weight 45 N rests on a frictionless slope inclined at 30&deg; to the horizontal."
 "<ol class='parts'>"
 "<li>Resolve the weight into components parallel and perpendicular to the slope.</li>"
 "<li>State the magnitude of the force, directed up the slope, needed to hold the block at rest.</li></ol>",
 4,
 "<b>(a)</b> Parallel to slope: 45 sin30&deg; = <b>22.5 N</b>. Perpendicular: 45 cos30&deg; = "
 "<b>39.0 N</b>.<br>"
 "<b>(b)</b> To hold the block, the up-slope force must balance the parallel component: "
 "<b>22.5 N</b>.",
 "<svg width='230' height='120' viewBox='0 0 230 120'>"
 "<polygon points='20,100 210,100 20,30' fill='#eef' stroke='#333'/>"
 "<rect x='70' y='58' width='26' height='16' fill='#c96' stroke='#333' transform='rotate(-21.8 83 66)'/>"
 "<line x1='83' y1='66' x2='83' y2='96' stroke='#093' stroke-width='2'/>"
 "<polygon points='83,96 79,88 87,88' fill='#093'/>"
 "<text x='70' y='112' font-size='9' fill='#093'>45 N</text>"
 "<text x='40' y='96' font-size='9'>30&deg;</text></svg>")

add(T1,
 "A ball moving due east at 5.0 m s<sup>&minus;1</sup> is struck and afterwards moves due north at "
 "5.0 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>By drawing a vector diagram, find the magnitude of the change in velocity.</li>"
 "<li>State the direction of this change.</li></ol>",
 5,
 "Change in velocity = v<sub>final</sub> &minus; v<sub>initial</sub> = (north 5.0) + (west 5.0) "
 "(subtracting an eastward vector adds a westward one).<br>"
 "<b>(a)</b> |&Delta;v| = &radic;(5.0&sup2; + 5.0&sup2;) = <b>7.1 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Directed <b>45&deg; west of north</b> (i.e. towards the north-west).")

add(T1,
 "A steel ball bearing has mass (28.2 &plusmn; 0.1) g and diameter (19.0 &plusmn; 0.1) mm."
 "<ol class='parts'>"
 "<li>Calculate the density of the steel.</li>"
 "<li>Determine the percentage uncertainty in the density.</li></ol>",
 7,
 "V = (&pi;/6)d&sup3; = (&pi;/6)(0.0190)&sup3; = 3.59 &times; 10<sup>&minus;6</sup> m&sup3;.<br>"
 "<b>(a)</b> &rho; = m/V = 0.0282/3.59&times;10<sup>&minus;6</sup> = "
 "<b>7.9 &times; 10<sup>3</sup> kg m<sup>&minus;3</sup></b>.<br>"
 "<b>(b)</b> %m = 0.1/28.2 = 0.35%; %d = 0.1/19.0 = 0.53%, and d is cubed &rArr; 1.58%. "
 "%&rho; = 0.35 + 1.58 = <b>1.9%</b>.")

# ===========================================================================
# TOPIC 2
# ===========================================================================
add(T2,
 "A football is kicked from level ground with a speed of 22 m s<sup>&minus;1</sup> at 40&deg; above "
 "the horizontal. Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Calculate the maximum height reached.</li>"
 "<li>Calculate the time of flight.</li>"
 "<li>Calculate the horizontal range.</li></ol>",
 8,
 "u<sub>x</sub> = 22 cos40&deg; = 16.9; u<sub>y</sub> = 22 sin40&deg; = 14.1 m s<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> H = u<sub>y</sub>&sup2;/(2g) = 14.1&sup2;/19.62 = <b>10.2 m</b>.<br>"
 "<b>(b)</b> t = 2u<sub>y</sub>/g = 2&times;14.1/9.81 = <b>2.88 s</b>.<br>"
 "<b>(c)</b> R = u<sub>x</sub>t = 16.9 &times; 2.88 = <b>48.6 m</b>.")

add(T2,
 "A car starts from rest and accelerates uniformly at 2.0 m s<sup>&minus;2</sup> for 6.0 s. It then "
 "travels at constant speed for 20 s, before decelerating uniformly at 3.0 m s<sup>&minus;2</sup> to "
 "rest."
 "<ol class='parts'>"
 "<li>Find the maximum speed reached.</li>"
 "<li>Find the total distance travelled.</li>"
 "<li>Find the average speed for the whole journey.</li></ol>",
 9,
 "<b>(a)</b> v = u + at = 0 + 2.0&times;6.0 = <b>12 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Phase 1: s = &frac12;(2.0)(6.0)&sup2; = 36 m. Phase 2: s = 12&times;20 = 240 m. "
 "Phase 3: time = 12/3.0 = 4.0 s, s = &frac12;(12)(4.0) = 24 m. Total = 36 + 240 + 24 = <b>300 m</b>.<br>"
 "<b>(c)</b> Total time = 6.0 + 20 + 4.0 = 30 s. Average speed = 300/30 = <b>10 m s<sup>&minus;1</sup></b>.")

add(T2,
 "A ball is thrown horizontally at 15 m s<sup>&minus;1</sup> from the top of a vertical cliff of "
 "height 45 m. Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Calculate the time taken to reach the sea.</li>"
 "<li>Calculate the horizontal distance travelled.</li>"
 "<li>Calculate the magnitude and direction of the velocity as it hits the sea.</li></ol>",
 8,
 "<b>(a)</b> 45 = &frac12;gt&sup2; &rArr; t = &radic;(90/9.81) = <b>3.03 s</b>.<br>"
 "<b>(b)</b> Range = 15 &times; 3.03 = <b>45.4 m</b>.<br>"
 "<b>(c)</b> v<sub>y</sub> = gt = 9.81 &times; 3.03 = 29.7 m s<sup>&minus;1</sup>. "
 "Speed = &radic;(15&sup2; + 29.7&sup2;) = <b>33.3 m s<sup>&minus;1</sup></b> at "
 "tan<sup>&minus;1</sup>(29.7/15) = <b>63&deg; below the horizontal</b>.")

add(T2,
 "In a reaction-time test, a ruler is released from rest and a student catches it after it has fallen "
 "0.18 m."
 "<ol class='parts'>"
 "<li>Calculate the student&#39;s reaction time.</li>"
 "<li>State one assumption made.</li></ol>",
 4,
 "<b>(a)</b> s = &frac12;gt&sup2; &rArr; t = &radic;(2s/g) = &radic;(0.36/9.81) = <b>0.19 s</b>.<br>"
 "<b>(b)</b> Air resistance is negligible (or the ruler is released cleanly and caught the instant "
 "the student reacts).")

add(T2,
 "A ball is thrown vertically upward from ground level with a speed of 25 m s<sup>&minus;1</sup>. "
 "Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Find the two times at which the ball is at a height of 20 m.</li>"
 "<li>Explain physically why there are two such times.</li></ol>",
 6,
 "<b>(a)</b> 20 = 25t &minus; &frac12;(9.81)t&sup2; &rArr; 4.905t&sup2; &minus; 25t + 20 = 0. "
 "t = [25 &plusmn; &radic;(625 &minus; 392.4)]/9.81 = [25 &plusmn; 15.25]/9.81. "
 "t = <b>0.99 s</b> and <b>4.10 s</b>.<br>"
 "<b>(b)</b> The ball passes 20 m once on the way up and again on the way down; between these times it "
 "rises to its maximum height and returns.")

add(T2,
 "The velocity&ndash;time graph of a cyclist over 40 s consists of three straight sections: a rise "
 "from 0 to 8.0 m s<sup>&minus;1</sup> in the first 10 s, a constant 8.0 m s<sup>&minus;1</sup> for "
 "the next 20 s, and a fall from 8.0 m s<sup>&minus;1</sup> to 2.0 m s<sup>&minus;1</sup> over the "
 "final 10 s."
 "<ol class='parts'>"
 "<li>Describe the motion in each of the three sections.</li>"
 "<li>Calculate the total distance travelled by finding the area under the graph.</li></ol>",
 7,
 "<b>(a)</b> 0&ndash;10 s: uniform acceleration (0.80 m s<sup>&minus;2</sup>); 10&ndash;30 s: constant "
 "velocity (zero acceleration); 30&ndash;40 s: uniform deceleration (0.60 m s<sup>&minus;2</sup>).<br>"
 "<b>(b)</b> Area = &frac12;(10)(8.0) + (20)(8.0) + &frac12;(8.0 + 2.0)(10) = 40 + 160 + 50 = "
 "<b>250 m</b>.")

add(T2,
 "Describe an experiment to determine the acceleration of free fall <span class='eq'>g</span> using "
 "an electronically timed falling steel ball. Your answer should include:"
 "<ol class='parts'>"
 "<li>the measurements taken and the apparatus used;</li>"
 "<li>how a graph is used to obtain g and reduce the effect of random error.</li></ol>",
 6,
 "<b>(a)</b> A steel ball is released from an electromagnet; a timer starts as the ball is released "
 "and stops when it strikes a trap-door/light gate. Measure the fall distance s (metre rule) for "
 "several values and the corresponding fall time t (electronic timer). Repeat each and average.<br>"
 "<b>(b)</b> Since s = &frac12;gt&sup2;, plot s against t&sup2;: a straight line through the origin of "
 "gradient &frac12;g, so g = 2 &times; gradient. Using many points and a best-fit line averages out "
 "random timing errors and reveals any systematic offset (e.g. a non-zero intercept).")

add(T2,
 "A stone falls freely past two marks P and Q on a wall. It passes P and then Q, a distance 1.50 m "
 "lower, 0.100 s later."
 "<ol class='parts'>"
 "<li>Find the speed of the stone at P.</li>"
 "<li>Find the height above P from which the stone was dropped from rest.</li></ol>",
 8,
 "<b>(a)</b> Between P and Q: s = ut + &frac12;gt&sup2; &rArr; 1.50 = u(0.100) + &frac12;(9.81)(0.100)&sup2; "
 "= 0.100u + 0.049 &rArr; u = 1.451/0.100 = <b>14.5 m s<sup>&minus;1</sup></b> (speed at P).<br>"
 "<b>(b)</b> From rest to P: u&sup2; = 2gh &rArr; h = 14.5&sup2;/(2&times;9.81) = 210/19.62 = "
 "<b>10.7 m</b>.")

add(T2,
 "A projectile is launched from ground level at 20 m s<sup>&minus;1</sup> at 55&deg; above the "
 "horizontal towards a vertical wall of height 4.0 m situated 6.0 m away."
 "<ol class='parts'>"
 "<li>Find the time to reach the wall horizontally.</li>"
 "<li>Determine whether the projectile clears the top of the wall, and by how much.</li></ol>",
 7,
 "u<sub>x</sub> = 20 cos55&deg; = 11.5; u<sub>y</sub> = 20 sin55&deg; = 16.4 m s<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> t = 6.0/11.5 = <b>0.52 s</b>.<br>"
 "<b>(b)</b> y = u<sub>y</sub>t &minus; &frac12;gt&sup2; = 16.4(0.523) &minus; 4.905(0.523)&sup2; = "
 "8.57 &minus; 1.34 = 7.2 m. Since 7.2 m &gt; 4.0 m, it <b>clears the wall by about 3.2 m</b>.")

add(T2,
 "A ball A is released from rest at the top of a tower of height 30 m. At the same instant a ball B "
 "is thrown vertically upward from the base of the tower with a speed of 15 m s<sup>&minus;1</sup>. "
 "Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Find the time at which the two balls are at the same height.</li>"
 "<li>Find that height above the ground.</li></ol>",
 7,
 "Measure heights from the ground. A: y<sub>A</sub> = 30 &minus; &frac12;gt&sup2;. "
 "B: y<sub>B</sub> = 15t &minus; &frac12;gt&sup2;.<br>"
 "<b>(a)</b> Equal: 30 &minus; &frac12;gt&sup2; = 15t &minus; &frac12;gt&sup2; &rArr; 30 = 15t &rArr; "
 "t = <b>2.0 s</b> (the &minus;&frac12;gt&sup2; terms cancel).<br>"
 "<b>(b)</b> y = 15(2.0) &minus; &frac12;(9.81)(2.0)&sup2; = 30 &minus; 19.6 = <b>10.4 m</b>.")

add(T2,
 "A body starts from rest and moves with uniform acceleration 4.0 m s<sup>&minus;2</sup> in a straight "
 "line."
 "<ol class='parts'>"
 "<li>Show that the distance travelled during the 5th second of its motion is 18 m.</li>"
 "<li>Explain why this exceeds the distance travelled in the 1st second.</li></ol>",
 5,
 "<b>(a)</b> Distance in nth second = s<sub>n</sub> &minus; s<sub>n&minus;1</sub> = "
 "&frac12;a(2n &minus; 1). For n = 5: &frac12;(4.0)(9) = <b>18 m</b>. &#10003;<br>"
 "<b>(b)</b> The body is continually speeding up, so it covers more ground in each successive second; "
 "in the 1st second (n = 1) the distance is only &frac12;(4.0)(1) = 2.0 m.")

add(T2,
 "A ball is thrown vertically upward and returns to the thrower&#39;s hand. Air resistance is "
 "negligible."
 "<ol class='parts'>"
 "<li>Sketch the acceleration&ndash;time graph for the whole motion.</li>"
 "<li>Sketch the velocity&ndash;time graph, and mark the point corresponding to maximum height.</li>"
 "<li>State what feature of the velocity&ndash;time graph represents the displacement.</li></ol>",
 6,
 "<b>(a)</b> A horizontal line at &minus;9.81 m s<sup>&minus;2</sup> for the whole time "
 "(acceleration is constant, downward, even at the top).<br>"
 "<b>(b)</b> A straight line of constant negative gradient starting at +u, crossing zero at the top "
 "(maximum height) and reaching &minus;u on return.<br>"
 "<b>(c)</b> The <b>area between the line and the time axis</b> gives the displacement (positive area "
 "up, negative area down; net area zero as it returns).")

add(T2,
 "Two cars are 200 m apart on a straight road and move directly towards each other. Car X travels at "
 "a constant 12 m s<sup>&minus;1</sup>; car Y travels at a constant 8.0 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>State the speed of X relative to Y.</li>"
 "<li>Find the time before they meet and the distance each has travelled.</li></ol>",
 5,
 "<b>(a)</b> Closing (relative) speed = 12 + 8.0 = <b>20 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Time = 200/20 = <b>10 s</b>. X travels 12&times;10 = <b>120 m</b>; Y travels 8.0&times;10 = "
 "<b>80 m</b> (sum = 200 m &#10003;).")

# ===========================================================================
# TOPIC 3
# ===========================================================================
add(T3,
 "A block of mass 4.0 kg is released on a slope inclined at 25&deg; to the horizontal. A constant "
 "frictional force of 6.0 N acts on the block as it slides down."
 "<ol class='parts'>"
 "<li>Calculate the resultant force on the block along the slope.</li>"
 "<li>Calculate its acceleration.</li></ol>",
 6,
 "<b>(a)</b> Weight component down slope = mg sin25&deg; = 4.0&times;9.81&times;0.423 = 16.6 N. "
 "Resultant = 16.6 &minus; 6.0 = <b>10.6 N</b> down the slope.<br>"
 "<b>(b)</b> a = F/m = 10.6/4.0 = <b>2.7 m s<sup>&minus;2</sup></b>.")

add(T3,
 "A gun fires bullets of mass 20 g horizontally at a speed of 400 m s<sup>&minus;1</sup>, at a rate "
 "of 5.0 bullets per second."
 "<ol class='parts'>"
 "<li>Calculate the momentum of one bullet.</li>"
 "<li>Calculate the mean force needed to hold the gun steady.</li></ol>",
 5,
 "<b>(a)</b> p = mv = 0.020 &times; 400 = <b>8.0 kg m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Mean force = rate of change of momentum = 8.0 &times; 5.0 = <b>40 N</b> "
 "(directed backwards on the gun; the holder supplies 40 N forwards).")

add(T3,
 "A puck A of mass 0.50 kg moving at 4.0 m s<sup>&minus;1</sup> strikes a stationary puck B of mass "
 "0.30 kg on a frictionless surface. After the collision A moves at 2.0 m s<sup>&minus;1</sup> at "
 "30&deg; to its original direction."
 "<ol class='parts'>"
 "<li>Using conservation of momentum in two perpendicular directions, find the speed of B after the "
 "collision.</li>"
 "<li>Find the direction in which B moves.</li></ol>",
 9,
 "Take x along A&#39;s original direction.<br>"
 "<b>x:</b> 0.50(4.0) = 0.50(2.0)cos30&deg; + 0.30v<sub>Bx</sub> &rArr; 2.0 = 0.866 + 0.30v<sub>Bx</sub> "
 "&rArr; v<sub>Bx</sub> = 3.78 m s<sup>&minus;1</sup>.<br>"
 "<b>y:</b> 0 = 0.50(2.0)sin30&deg; + 0.30v<sub>By</sub> &rArr; 0.30v<sub>By</sub> = &minus;0.50 &rArr; "
 "v<sub>By</sub> = &minus;1.67 m s<sup>&minus;1</sup>.<br>"
 "<b>(a)</b> v<sub>B</sub> = &radic;(3.78&sup2; + 1.67&sup2;) = &radic;17.1 = "
 "<b>4.1 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Angle = tan<sup>&minus;1</sup>(1.67/3.78) = <b>24&deg; on the opposite side</b> of the "
 "original direction to A.")

add(T3,
 "Two identical trolleys each of mass m undergo a head-on elastic collision on a frictionless track. "
 "Before the collision one moves at speed u and the other is stationary."
 "<ol class='parts'>"
 "<li>Using conservation of momentum and conservation of kinetic energy, show that the trolleys "
 "exchange velocities.</li>"
 "<li>State the relationship between relative speed of approach and relative speed of separation for "
 "any elastic collision.</li></ol>",
 6,
 "<b>(a)</b> Momentum: mu = mv<sub>1</sub> + mv<sub>2</sub> &rArr; u = v<sub>1</sub> + v<sub>2</sub>. "
 "KE: &frac12;mu&sup2; = &frac12;mv<sub>1</sub>&sup2; + &frac12;mv<sub>2</sub>&sup2; &rArr; "
 "u&sup2; = v<sub>1</sub>&sup2; + v<sub>2</sub>&sup2;. From the first, u&sup2; = (v<sub>1</sub> + "
 "v<sub>2</sub>)&sup2; = v<sub>1</sub>&sup2; + 2v<sub>1</sub>v<sub>2</sub> + v<sub>2</sub>&sup2;, so "
 "2v<sub>1</sub>v<sub>2</sub> = 0. Hence one final velocity is 0 and the other is u: they "
 "<b>exchange velocities</b> (v<sub>1</sub> = 0, v<sub>2</sub> = u).<br>"
 "<b>(b)</b> Relative speed of approach = relative speed of separation.")

add(T3,
 "A trolley of mass 2.0 kg moving at 3.0 m s<sup>&minus;1</sup> collides with and sticks to a "
 "stationary trolley of mass 1.0 kg."
 "<ol class='parts'>"
 "<li>Calculate the common velocity after the collision.</li>"
 "<li>Calculate the kinetic energy lost in the collision and state what happens to this energy.</li></ol>",
 7,
 "<b>(a)</b> Momentum: 2.0&times;3.0 = (2.0 + 1.0)v &rArr; v = 6.0/3.0 = <b>2.0 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> KE before = &frac12;(2.0)(3.0)&sup2; = 9.0 J; KE after = &frac12;(3.0)(2.0)&sup2; = 6.0 J. "
 "Loss = <b>3.0 J</b>, transferred to heat and sound (deformation of the trolleys); momentum is still "
 "conserved.")

add(T3,
 "A resultant force acts on a stationary object of mass 5.0 kg for 4.0 s. The force&ndash;time graph "
 "is a straight line rising from 0 to 20 N over the 4.0 s."
 "<ol class='parts'>"
 "<li>Explain how the impulse can be found from the graph, and calculate it.</li>"
 "<li>Find the final speed of the object.</li></ol>",
 6,
 "<b>(a)</b> Impulse = change of momentum = area under the force&ndash;time graph = "
 "&frac12;(4.0)(20) = <b>40 N s</b>.<br>"
 "<b>(b)</b> Impulse = mv &minus; mu = mv (starts at rest) &rArr; v = 40/5.0 = "
 "<b>8.0 m s<sup>&minus;1</sup></b>.")

add(T3,
 "A cannon of mass 800 kg fires a shell of mass 5.0 kg horizontally at 200 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the recoil speed of the cannon.</li>"
 "<li>Compare the kinetic energy of the shell with that of the cannon, and comment.</li></ol>",
 6,
 "<b>(a)</b> Momentum conserved (initially zero): 800v = 5.0&times;200 &rArr; v = 1000/800 = "
 "<b>1.25 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> KE<sub>shell</sub> = &frac12;(5.0)(200)&sup2; = 1.0&times;10<sup>5</sup> J; "
 "KE<sub>cannon</sub> = &frac12;(800)(1.25)&sup2; = 625 J. The shell has far more KE (ratio 160:1). "
 "Momentum is shared equally in magnitude, but KE = p&sup2;/2m, so the lighter shell carries most of "
 "the energy.")

add(T3,
 "A skydiver of total mass 85 kg jumps from a stationary balloon."
 "<ol class='parts'>"
 "<li>Sketch and describe the velocity&ndash;time graph from jumping until landing, referring to the "
 "forces at each stage (before and after opening the parachute).</li>"
 "<li>State the condition for terminal velocity.</li></ol>",
 7,
 "<b>(a)</b> Just after jumping, weight &gt; drag, so the diver accelerates but the acceleration "
 "decreases as drag rises with speed; the velocity curve rises and levels off at a first (high) "
 "terminal velocity. When the parachute opens, drag suddenly exceeds weight, so the diver decelerates "
 "(curve falls), then levels off at a lower terminal velocity until landing.<br>"
 "<b>(b)</b> Terminal velocity is reached when the resistive (drag) force equals the weight, so the "
 "resultant force is zero and the velocity is constant.",
 "<svg width='250' height='130' viewBox='0 0 250 130'>"
 "<line x1='30' y1='110' x2='235' y2='110' stroke='#333'/>"
 "<line x1='30' y1='110' x2='30' y2='15' stroke='#333'/>"
 "<path d='M30 110 C55 70 80 45 110 45' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M110 45 C120 45 125 80 150 88' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M150 88 L225 88' fill='none' stroke='#06c' stroke-width='2'/>"
 "<text x='6' y='60' font-size='9'>v</text><text x='210' y='124' font-size='9'>t</text>"
 "<text x='96' y='40' font-size='8'>chute opens</text></svg>")

add(T3,
 "A person of mass 60 kg stands on bathroom scales inside a lift."
 "<ol class='parts'>"
 "<li>Find the reading (in newtons) when the lift accelerates upward at 1.5 m s<sup>&minus;2</sup>.</li>"
 "<li>Find the reading when the lift accelerates downward at 1.5 m s<sup>&minus;2</sup>.</li>"
 "<li>State the reading if the lift cable breaks and it falls freely.</li></ol>",
 7,
 "Reading = normal force N. Newton II (up positive): N &minus; mg = ma.<br>"
 "<b>(a)</b> N = m(g + a) = 60(9.81 + 1.5) = <b>679 N</b>.<br>"
 "<b>(b)</b> N = m(g &minus; a) = 60(9.81 &minus; 1.5) = <b>499 N</b>.<br>"
 "<b>(c)</b> In free fall a = g, so N = m(g &minus; g) = <b>0 N</b> (apparent weightlessness).")

add(T3,
 "A block of mass 3.0 kg rests on a horizontal table and is connected by a light string over a "
 "frictionless pulley at the edge to a hanging mass of 2.0 kg. A constant frictional force of 5.0 N "
 "acts on the block."
 "<ol class='parts'>"
 "<li>Calculate the acceleration of the system.</li>"
 "<li>Calculate the tension in the string.</li></ol>",
 9,
 "<b>(a)</b> Hanging mass: 2.0g &minus; T = 2.0a. Block: T &minus; 5.0 = 3.0a. Adding: "
 "2.0g &minus; 5.0 = 5.0a &rArr; a = (19.62 &minus; 5.0)/5.0 = <b>2.9 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> T = 3.0a + 5.0 = 3.0(2.92) + 5.0 = <b>13.8 N</b> "
 "(check: 2.0(9.81 &minus; 2.92) = 13.8 N &#10003;).",
 "<svg width='250' height='120' viewBox='0 0 250 120'>"
 "<rect x='20' y='40' width='150' height='10' fill='#ccc' stroke='#333'/>"
 "<rect x='55' y='22' width='34' height='18' fill='#c96' stroke='#333'/>"
 "<circle cx='175' cy='40' r='7' fill='none' stroke='#333'/>"
 "<line x1='89' y1='31' x2='168' y2='33' stroke='#333'/>"
 "<line x1='182' y1='40' x2='182' y2='85' stroke='#333'/>"
 "<rect x='170' y='85' width='24' height='20' fill='#69c' stroke='#333'/>"
 "<text x='60' y='19' font-size='9'>3.0 kg</text><text x='168' y='102' font-size='8'>2.0 kg</text></svg>")

add(T3,
 "A ball A of mass 2.0 kg moving at 5.0 m s<sup>&minus;1</sup> makes a head-on elastic collision with "
 "a stationary ball B of mass 3.0 kg."
 "<ol class='parts'>"
 "<li>Using conservation of momentum and the elastic-collision relation (relative approach speed = "
 "relative separation speed), find the velocity of each ball after the collision.</li>"
 "<li>Verify that kinetic energy is conserved.</li></ol>",
 8,
 "Let final velocities be v<sub>A</sub>, v<sub>B</sub>.<br>"
 "Momentum: 2.0(5.0) = 2.0v<sub>A</sub> + 3.0v<sub>B</sub> &rArr; 10 = 2v<sub>A</sub> + 3v<sub>B</sub>. "
 "Elastic: v<sub>B</sub> &minus; v<sub>A</sub> = 5.0. Solving: v<sub>A</sub> = "
 "<b>&minus;1.0 m s<sup>&minus;1</sup></b> (rebounds), v<sub>B</sub> = <b>4.0 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> KE before = &frac12;(2.0)(5.0)&sup2; = 25 J. KE after = &frac12;(2.0)(1.0)&sup2; + "
 "&frac12;(3.0)(4.0)&sup2; = 1.0 + 24 = 25 J. &#10003; Kinetic energy is conserved.")

add(T3,
 "A ball of mass 0.15 kg travelling horizontally at 12 m s<sup>&minus;1</sup> strikes a vertical wall "
 "and rebounds horizontally at 8.0 m s<sup>&minus;1</sup>. The contact time is 0.020 s."
 "<ol class='parts'>"
 "<li>Calculate the change in momentum of the ball.</li>"
 "<li>Calculate the average force exerted by the wall on the ball.</li></ol>",
 7,
 "Take the initial direction as positive.<br>"
 "<b>(a)</b> &Delta;p = m(v &minus; u) = 0.15(&minus;8.0 &minus; 12) = 0.15(&minus;20) = "
 "<b>&minus;3.0 kg m s<sup>&minus;1</sup></b> (magnitude 3.0, directed away from the wall).<br>"
 "<b>(b)</b> F = &Delta;p/&Delta;t = 3.0/0.020 = <b>150 N</b>.")

add(T3,
 "Two trolleys are held together with a compressed spring between them; trolley P has mass 1.5 kg and "
 "trolley Q has mass 0.50 kg. When released, Q moves off at 3.0 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Find the speed of trolley P.</li>"
 "<li>Find the elastic potential energy that was stored in the spring.</li></ol>",
 7,
 "<b>(a)</b> Momentum conserved (initially zero): 1.5v<sub>P</sub> = 0.50&times;3.0 &rArr; v<sub>P</sub> = "
 "1.5/1.5 = <b>1.0 m s<sup>&minus;1</sup></b> (opposite direction to Q).<br>"
 "<b>(b)</b> Energy = &frac12;(1.5)(1.0)&sup2; + &frac12;(0.50)(3.0)&sup2; = 0.75 + 2.25 = <b>3.0 J</b>.")

add(T3,
 "State Newton&#39;s third law of motion."
 "<ol class='parts'>"
 "<li>A book rests on a table. Identify the force that pairs with the gravitational pull of the Earth "
 "on the book, and the force that pairs with the table&#39;s push up on the book.</li>"
 "<li>Explain, using Newton&#39;s laws, how the exhaust gases from a rocket propel it forward.</li></ol>",
 5,
 "Newton III: when body A exerts a force on body B, body B exerts an equal and opposite force on A "
 "(same type, same line of action).<br>"
 "<b>(a)</b> The Earth&#39;s pull on the book pairs with the <b>book&#39;s gravitational pull on the "
 "Earth</b>. The table&#39;s push up on the book pairs with the <b>book&#39;s push down on the "
 "table</b>. (These are different pairs &mdash; not weight and normal force.)<br>"
 "<b>(b)</b> The rocket exerts a backward force on the exhaust gases, expelling them; by Newton III "
 "the gases exert an equal forward force on the rocket, giving it forward momentum (momentum is "
 "conserved).")

# ===========================================================================
# TOPIC 4
# ===========================================================================
add(T4,
 "A uniform beam AB of length 5.0 m and weight 120 N rests horizontally on two supports, one at each "
 "end. A load of 300 N is placed 1.5 m from end A."
 "<ol class='parts'>"
 "<li>By taking moments about A, find the force exerted by the support at B.</li>"
 "<li>Hence find the force exerted by the support at A.</li></ol>",
 8,
 "The beam&#39;s weight acts at its midpoint, 2.5 m from A.<br>"
 "<b>(a)</b> Moments about A: R<sub>B</sub>(5.0) = 120(2.5) + 300(1.5) = 300 + 450 = 750 &rArr; "
 "R<sub>B</sub> = <b>150 N</b>.<br>"
 "<b>(b)</b> Vertical equilibrium: R<sub>A</sub> + R<sub>B</sub> = 120 + 300 = 420 &rArr; "
 "R<sub>A</sub> = 420 &minus; 150 = <b>270 N</b>.",
 "<svg width='300' height='95' viewBox='0 0 300 95'>"
 "<rect x='30' y='40' width='240' height='9' fill='#cda434' stroke='#333'/>"
 "<polygon points='30,49 22,66 38,66' fill='#555'/><polygon points='270,49 262,66 278,66' fill='#555'/>"
 "<line x1='102' y1='49' x2='102' y2='80' stroke='#c30' stroke-width='2'/>"
 "<polygon points='102,80 98,72 106,72' fill='#c30'/>"
 "<line x1='150' y1='49' x2='150' y2='75' stroke='#093' stroke-width='2'/>"
 "<polygon points='150,75 146,67 154,67' fill='#093'/>"
 "<text x='24' y='36' font-size='10'>A</text><text x='264' y='36' font-size='10'>B</text>"
 "<text x='86' y='92' font-size='8' fill='#c30'>300 N</text>"
 "<text x='138' y='92' font-size='8' fill='#093'>120 N</text></svg>")

add(T4,
 "A uniform ladder of weight 200 N and length 8.0 m leans against a smooth vertical wall, making an "
 "angle of 60&deg; with the horizontal ground. The ground is rough."
 "<ol class='parts'>"
 "<li>By taking moments about the foot of the ladder, find the horizontal force exerted by the wall.</li>"
 "<li>State the frictional force at the ground and the normal force from the ground.</li></ol>",
 9,
 "The wall is smooth, so it exerts only a horizontal normal force N<sub>W</sub>. The weight acts at "
 "the centre, 4.0 m along the ladder.<br>"
 "<b>(a)</b> Moments about the foot: N<sub>W</sub>(8.0 sin60&deg;) = 200(4.0 cos60&deg;) &rArr; "
 "N<sub>W</sub>(6.93) = 200(2.0) = 400 &rArr; N<sub>W</sub> = <b>57.7 N</b>.<br>"
 "<b>(b)</b> Horizontal equilibrium: friction = N<sub>W</sub> = <b>57.7 N</b>. Vertical equilibrium: "
 "normal force from ground = weight = <b>200 N</b>.")

add(T4,
 "Explain what is meant by a couple, and define the torque of a couple. A driver turns a steering "
 "wheel of diameter 0.36 m by applying two equal, oppositely directed tangential forces of 25 N at "
 "opposite ends of a diameter."
 "<ol class='parts'>"
 "<li>Calculate the torque of the couple.</li>"
 "<li>State why the resultant force on the wheel is zero yet it still turns.</li></ol>",
 5,
 "A couple is a pair of equal, opposite, parallel forces whose lines of action do not coincide; its "
 "torque = one force &times; perpendicular distance between them.<br>"
 "<b>(a)</b> Torque = F &times; d = 25 &times; 0.36 = <b>9.0 N m</b>.<br>"
 "<b>(b)</b> The two forces are equal and opposite, so they add to zero resultant force (no linear "
 "acceleration), but because they act along different lines they produce a net turning effect "
 "(rotation only).")

add(T4,
 "An alloy is made by mixing 0.30 kg of metal A (density 2700 kg m<sup>&minus;3</sup>) with 0.50 kg "
 "of metal B (density 8900 kg m<sup>&minus;3</sup>). Assume the volumes add."
 "<ol class='parts'>"
 "<li>Calculate the total volume of the alloy.</li>"
 "<li>Calculate the density of the alloy.</li></ol>",
 6,
 "<b>(a)</b> V<sub>A</sub> = 0.30/2700 = 1.11&times;10<sup>&minus;4</sup> m&sup3;; "
 "V<sub>B</sub> = 0.50/8900 = 5.62&times;10<sup>&minus;5</sup> m&sup3;. "
 "V = 1.11&times;10<sup>&minus;4</sup> + 5.62&times;10<sup>&minus;5</sup> = "
 "<b>1.67&times;10<sup>&minus;4</sup> m&sup3;</b>.<br>"
 "<b>(b)</b> &rho; = (0.30 + 0.50)/1.67&times;10<sup>&minus;4</sup> = 0.80/1.67&times;10<sup>&minus;4</sup> "
 "= <b>4.8&times;10<sup>3</sup> kg m<sup>&minus;3</sup></b>.")

add(T4,
 "A diver is 12 m below the surface of a lake. Atmospheric pressure is 1.01 &times; 10<sup>5</sup> Pa "
 "and the density of water is 1000 kg m<sup>&minus;3</sup>."
 "<ol class='parts'>"
 "<li>Calculate the pressure due to the water alone at this depth.</li>"
 "<li>Calculate the total pressure acting on the diver.</li></ol>",
 6,
 "<b>(a)</b> &Delta;p = &rho;gh = 1000 &times; 9.81 &times; 12 = <b>1.18 &times; 10<sup>5</sup> Pa</b>.<br>"
 "<b>(b)</b> Total = atmospheric + water = 1.01&times;10<sup>5</sup> + 1.18&times;10<sup>5</sup> = "
 "<b>2.19 &times; 10<sup>5</sup> Pa</b>.")

add(T4,
 "A U-tube contains water. Oil, which does not mix with water, is poured into the left arm. When "
 "equilibrium is reached, the oil column is 15 cm tall and its lower surface is level with the water "
 "in the right arm; the water rises 12 cm above this level on the right."
 "<ol class='parts'>"
 "<li>State why the pressures at the level of the oil&ndash;water boundary are equal in the two arms.</li>"
 "<li>Calculate the density of the oil.</li></ol>",
 6,
 "<b>(a)</b> Points at the same height in a connected static fluid are at the same pressure; at the "
 "oil&ndash;water boundary level the pressure from the oil column (left) equals the pressure from the "
 "water column (right).<br>"
 "<b>(b)</b> &rho;<sub>oil</sub>g(0.15) = &rho;<sub>water</sub>g(0.12) &rArr; &rho;<sub>oil</sub> = "
 "1000 &times; 0.12/0.15 = <b>800 kg m<sup>&minus;3</sup></b>.")

add(T4,
 "An object weighs 5.0 N when hung from a spring balance in air, and 3.2 N when fully immersed in "
 "water (density 1000 kg m<sup>&minus;3</sup>)."
 "<ol class='parts'>"
 "<li>Calculate the upthrust and hence the volume of the object.</li>"
 "<li>Calculate the density of the object.</li></ol>",
 8,
 "<b>(a)</b> Upthrust = 5.0 &minus; 3.2 = 1.8 N. Upthrust = &rho;<sub>w</sub>gV &rArr; "
 "V = 1.8/(1000&times;9.81) = <b>1.83&times;10<sup>&minus;4</sup> m&sup3;</b>.<br>"
 "<b>(b)</b> Mass = W/g = 5.0/9.81 = 0.510 kg. &rho; = m/V = 0.510/1.83&times;10<sup>&minus;4</sup> = "
 "<b>2.8&times;10<sup>3</sup> kg m<sup>&minus;3</sup></b>.")

add(T4,
 "A rectangular wooden block of base area 0.040 m&sup2; and height 0.20 m floats upright in water "
 "(density 1000 kg m<sup>&minus;3</sup>) with 0.15 m of its height submerged."
 "<ol class='parts'>"
 "<li>Calculate the weight of the block.</li>"
 "<li>A load is placed on top so the block just becomes fully submerged. Calculate the weight of the "
 "load.</li></ol>",
 7,
 "<b>(a)</b> Floating: weight = upthrust = &rho;gV<sub>sub</sub> = 1000&times;9.81&times;(0.040&times;0.15) "
 "= 1000&times;9.81&times;6.0&times;10<sup>&minus;3</sup> = <b>58.9 N</b>.<br>"
 "<b>(b)</b> Fully submerged upthrust = &rho;g(0.040&times;0.20) = 1000&times;9.81&times;8.0&times;10<sup>&minus;3</sup> "
 "= 78.5 N. Extra upthrust supports the load: W<sub>load</sub> = 78.5 &minus; 58.9 = <b>19.6 N</b>.")

add(T4,
 "A uniform horizontal rod AB of weight 30 N and length 1.2 m is hinged at A. It is held horizontal "
 "by a light string attached at B, which makes an angle of 35&deg; with the rod. A 50 N weight hangs "
 "from B."
 "<ol class='parts'>"
 "<li>By taking moments about A, find the tension in the string.</li>"
 "<li>Find the vertical component of the force exerted by the hinge on the rod.</li></ol>",
 8,
 "<b>(a)</b> The string&#39;s upward (perpendicular) component at B is T sin35&deg;. Moments about A: "
 "T sin35&deg;(1.2) = 30(0.6) + 50(1.2) &rArr; T sin35&deg; = (18 + 60)/1.2 = 65 &rArr; "
 "T = 65/0.574 = <b>113 N</b>.<br>"
 "<b>(b)</b> Vertical equilibrium: V + T sin35&deg; = 30 + 50 &rArr; V = 80 &minus; 65 = "
 "<b>15 N (upward)</b>.")

add(T4,
 "A meter rule is balanced horizontally on a knife edge. When a 0.50 N weight is hung at the 10 cm "
 "mark, the rule has to be moved so that it balances on the knife edge placed at the 42 cm mark."
 "<ol class='parts'>"
 "<li>State where the weight of a uniform meter rule acts.</li>"
 "<li>By taking moments about the knife edge, find the weight of the rule.</li></ol>",
 7,
 "<b>(a)</b> At its <b>centre of gravity</b>, the 50 cm mark (uniform rule).<br>"
 "<b>(b)</b> Moments about the 42 cm knife edge: the 0.50 N weight (at 10 cm, i.e. 32 cm away) turns "
 "one way; the rule&#39;s weight W (at 50 cm, i.e. 8 cm away) turns the other. "
 "0.50 &times; 0.32 = W &times; 0.08 &rArr; W = 0.16/0.08 = <b>2.0 N</b>.")

add(T4,
 "A hydraulic jack has a small piston of area 2.0 cm&sup2; and a large piston of area 50 cm&sup2;. A "
 "force of 40 N is applied to the small piston."
 "<ol class='parts'>"
 "<li>State the principle that makes this device work.</li>"
 "<li>Calculate the force produced at the large piston.</li>"
 "<li>Explain why this does not violate conservation of energy.</li></ol>",
 6,
 "<b>(a)</b> Pressure applied to an enclosed fluid is transmitted equally throughout it, so the "
 "pressure is the same on both pistons.<br>"
 "<b>(b)</b> p = F<sub>1</sub>/A<sub>1</sub> = F<sub>2</sub>/A<sub>2</sub> &rArr; F<sub>2</sub> = "
 "40 &times; 50/2.0 = <b>1000 N</b>.<br>"
 "<b>(c)</b> The large piston moves a much smaller distance (25&times; less) than the small piston, so "
 "work in = work out (ignoring friction); force is multiplied but distance is reduced.")

add(T4,
 "A load of 500 N hangs in equilibrium from a point O, held by a horizontal tie rope and a supporting "
 "cable that makes an angle of 40&deg; with the vertical."
 "<ol class='parts'>"
 "<li>Draw a triangle of forces for point O.</li>"
 "<li>Calculate the tension in the cable and the tension in the horizontal tie.</li></ol>",
 7,
 "Three forces act at O: the 500 N weight (down), the cable tension T (up along the cable, 40&deg; "
 "from vertical) and the horizontal tie tension H.<br>"
 "<b>(a)</b> A closed triangle: 500 N vertical, H horizontal, T as the hypotenuse.<br>"
 "<b>(b)</b> Vertical: T cos40&deg; = 500 &rArr; T = 500/0.766 = <b>653 N</b>. "
 "Horizontal: H = T sin40&deg; = 653 &times; 0.643 = <b>420 N</b>.")

add(T4,
 "Explain, in terms of pressure, why an object experiences an upthrust when immersed in a fluid, and "
 "state Archimedes&#39; principle. A solid cube of side 0.10 m is fully submerged in water so that "
 "its top face is 0.20 m below the surface."
 "<ol class='parts'>"
 "<li>Calculate the difference in water pressure between the bottom and top faces.</li>"
 "<li>Hence calculate the upthrust, and confirm it equals &rho;gV.</li></ol>",
 7,
 "Upthrust arises because pressure increases with depth, so the fluid pushes up on the lower face "
 "more strongly than it pushes down on the upper face. Archimedes: the upthrust equals the weight of "
 "fluid displaced.<br>"
 "<b>(a)</b> Bottom face is 0.30 m deep, top face 0.20 m deep. &Delta;p = &rho;g&Delta;h = "
 "1000&times;9.81&times;0.10 = <b>981 Pa</b>.<br>"
 "<b>(b)</b> Upthrust = &Delta;p &times; area = 981 &times; (0.10)&sup2; = 981 &times; 0.010 = "
 "<b>9.81 N</b>. Also &rho;gV = 1000&times;9.81&times;(0.10)&sup3; = 9.81 N &#10003;.")
