# -*- coding: utf-8 -*-
"""Additional extreme-difficulty structured (theory) questions, AS 9702.
PMT / past-paper style. Each entry appends to engine.theory.
Topic label strings are imported from theory_01_10 so questions merge into
the correct topic groups and are numbered continuously."""
from engine import theory as T, frac
from theory_01_10 import T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11


def add(topic, q, marks, ans, svg=""):
    T.append({"topic": topic, "q": q, "marks": marks, "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 1  Physical quantities and units  (extra)
# ===========================================================================

add(T1,
 "The period <span class='eq'>T</span> of oscillation of a liquid drop is thought to depend on its "
 "radius <span class='eq'>r</span>, its density <span class='eq'>&rho;</span> and the surface tension "
 "<span class='eq'>&gamma;</span> (which has base units kg s<sup>&minus;2</sup>). It is proposed that "
 "<span class='eq'>T = k r<sup>a</sup>&rho;<sup>b</sup>&gamma;<sup>c</sup></span>, where "
 "<span class='eq'>k</span> is a dimensionless constant."
 "<ol class='parts'>"
 "<li>Use the method of dimensions (base units) to find the values of <span class='eq'>a</span>, "
 "<span class='eq'>b</span> and <span class='eq'>c</span>.</li>"
 "<li>State one thing this method cannot tell you about the equation.</li></ol>",
 7,
 "<b>(a)</b> Base units: T = s; r = m; &rho; = kg m<sup>&minus;3</sup>; &gamma; = kg s<sup>&minus;2</sup>. "
 "So s = m<sup>a</sup>(kg m<sup>&minus;3</sup>)<sup>b</sup>(kg s<sup>&minus;2</sup>)<sup>c</sup> "
 "= kg<sup>b+c</sup> m<sup>a&minus;3b</sup> s<sup>&minus;2c</sup>.<br>"
 "Match powers: kg: b + c = 0; s: &minus;2c = 1 &rArr; c = &minus;&frac12;, so b = +&frac12;; "
 "m: a &minus; 3b = 0 &rArr; a = 3b = 3/2. "
 "So <b>a = 3/2, b = 1/2, c = &minus;1/2</b> (i.e. T = k&radic;(&rho;r&sup3;/&gamma;)).<br>"
 "<b>(b)</b> It cannot give the value of the dimensionless constant <span class='eq'>k</span> (nor "
 "confirm the equation is physically correct) &mdash; only that it is dimensionally consistent.")

add(T1,
 "A solid cylinder is used to find the density of a metal. Measurements: mass "
 "<span class='eq'>m</span> = (48.6 &plusmn; 0.1) g; diameter <span class='eq'>d</span> = "
 "(12.4 &plusmn; 0.1) mm; length <span class='eq'>L</span> = (35.0 &plusmn; 0.5) mm."
 "<ol class='parts'>"
 "<li>Calculate the density in kg m<sup>&minus;3</sup>.</li>"
 "<li>Determine the percentage uncertainty in the density and hence the absolute uncertainty.</li></ol>",
 8,
 "Volume V = &pi;(d/2)&sup2;L = &pi;(6.2&times;10<sup>&minus;3</sup>)&sup2;(35.0&times;10<sup>&minus;3</sup>) "
 "= &pi; &times; 3.844&times;10<sup>&minus;5</sup> &times; 0.0350 = 4.226&times;10<sup>&minus;6</sup> m&sup3;.<br>"
 "<b>(a)</b> &rho; = m/V = 48.6&times;10<sup>&minus;3</sup>/4.226&times;10<sup>&minus;6</sup> = "
 "<b>1.15&times;10<sup>4</sup> kg m<sup>&minus;3</sup></b>.<br>"
 "<b>(b)</b> %m = 0.1/48.6 = 0.21%; %d = 0.1/12.4 = 0.81% (d is squared &rArr; 1.61%); "
 "%L = 0.5/35.0 = 1.43%. Total %&rho; = 0.21 + 1.61 + 1.43 = <b>3.3%</b>. "
 "&Delta;&rho; = 0.033 &times; 1.15&times;10<sup>4</sup> = 0.38&times;10<sup>3</sup>, so "
 "&rho; = <b>(11.5 &plusmn; 0.4)&times;10<sup>3</sup> kg m<sup>&minus;3</sup></b>.")

add(T1,
 "A swimmer who can swim at 1.2 m s<sup>&minus;1</sup> in still water wishes to cross a river 60 m "
 "wide that flows at 0.90 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>If the swimmer heads straight across (perpendicular to the bank), find the resultant velocity "
 "and how far downstream they land.</li>"
 "<li>Find the direction in which the swimmer should instead head to land directly opposite the "
 "start, and the time this crossing takes.</li></ol>",
 8,
 "<b>(a)</b> Perpendicular component 1.2 m s<sup>&minus;1</sup>, downstream 0.90 m s<sup>&minus;1</sup>. "
 "Resultant = &radic;(1.2&sup2; + 0.90&sup2;) = &radic;(1.44 + 0.81) = &radic;2.25 = "
 "<b>1.5 m s<sup>&minus;1</sup></b> at tan<sup>&minus;1</sup>(0.90/1.2) = 36.9&deg; to the bank "
 "normal. Time across = 60/1.2 = 50 s; drift = 0.90 &times; 50 = <b>45 m downstream</b>.<br>"
 "<b>(b)</b> To land opposite, the upstream component of the swim velocity must cancel the current: "
 "1.2 sin&theta; = 0.90 &rArr; &theta; = sin<sup>&minus;1</sup>(0.75) = <b>48.6&deg; upstream</b> "
 "of the normal. Effective across-speed = 1.2 cos48.6&deg; = 0.794 m s<sup>&minus;1</sup>; "
 "time = 60/0.794 = <b>76 s</b>.")

add(T1,
 "Explain the difference between <b>precision</b> and <b>accuracy</b>. A student takes four readings "
 "of a resistance using two methods. Method P gives 47.1, 47.2, 47.0, 47.1 &Omega;; method Q gives "
 "44.0, 49.5, 46.8, 45.2 &Omega;. The accepted value is 45.4 &Omega;."
 "<ol class='parts'>"
 "<li>State which method is more precise and which is more accurate, with reasons.</li>"
 "<li>Identify the likely type of error in the less accurate method.</li></ol>",
 7,
 "Precision: how closely repeated readings agree with each other (small random scatter). "
 "Accuracy: how close a reading (or the mean) is to the true value.<br>"
 "<b>(a)</b> Method P is <b>more precise</b> (readings tightly clustered, range 0.2 &Omega;) but "
 "<b>less accurate</b> (mean 47.1 &Omega;, far from 45.4). Method Q is less precise (large scatter, "
 "range 5.5 &Omega;) but its mean (46.4 &Omega;) is <b>closer to</b> the true value than P&#39;s... "
 "in fact P&#39;s mean is 47.1 (1.7 off) and Q&#39;s is 46.4 (1.0 off), so Q is more accurate.<br>"
 "<b>(b)</b> Method P shows a consistent offset from the true value with little scatter &mdash; "
 "characteristic of a <b>systematic error</b> (e.g. a zero/calibration error in the meter).")

# ===========================================================================
# TOPIC 2  Kinematics  (extra)
# ===========================================================================

add(T2,
 "A stone is thrown from the top of a cliff 55 m above the sea with a speed of 20 m s<sup>&minus;1</sup> "
 "at 35&deg; <b>above</b> the horizontal. Air resistance is negligible."
 "<ol class='parts'>"
 "<li>Calculate the maximum height above the cliff top reached by the stone.</li>"
 "<li>Calculate the total time of flight until it hits the sea.</li>"
 "<li>Calculate the horizontal distance from the base of the cliff at which it lands.</li></ol>",
 9,
 "u<sub>x</sub> = 20 cos35&deg; = 16.4 m s<sup>&minus;1</sup>; u<sub>y</sub> = 20 sin35&deg; = "
 "11.5 m s<sup>&minus;1</sup> (up).<br>"
 "<b>(a)</b> h<sub>max</sub> = u<sub>y</sub>&sup2;/(2g) = 11.5&sup2;/(2&times;9.81) = 131.6/19.62 = "
 "<b>6.7 m</b> above the cliff top.<br>"
 "<b>(b)</b> Taking up positive, sea at &minus;55 m: &minus;55 = 11.5t &minus; 4.905t&sup2; &rArr; "
 "4.905t&sup2; &minus; 11.5t &minus; 55 = 0. "
 "t = [11.5 &plusmn; &radic;(132.3 + 1079)]/9.81 = [11.5 &plusmn; 34.8]/9.81. "
 "Positive root: t = 46.3/9.81 = <b>4.72 s</b>.<br>"
 "<b>(c)</b> Range = u<sub>x</sub>t = 16.4 &times; 4.72 = <b>77 m</b>.")

add(T2,
 "The graph of velocity against time for a bouncing ball (taking upward as positive) shows a series "
 "of straight sloping lines of equal gradient, with sudden reversals of velocity that decrease in "
 "magnitude at each bounce."
 "<ol class='parts'>"
 "<li>Explain why every sloping section of the graph has the same gradient.</li>"
 "<li>Explain what the sudden vertical jumps represent and why they get shorter each time.</li>"
 "<li>State how the displacement&ndash;time graph would differ in appearance.</li></ol>",
 7,
 "<b>(a)</b> While in the air the only force is gravity, so the acceleration is g downward at all "
 "times; the gradient of a v&ndash;t graph is the acceleration, so every free-flight section has the "
 "same gradient (&minus;9.81 m s<sup>&minus;2</sup>).<br>"
 "<b>(b)</b> Each vertical jump is the rapid reversal of velocity during the brief contact with the "
 "ground (downward velocity to upward velocity). They get shorter because the ball loses kinetic "
 "energy at each bounce (collision is inelastic), so it leaves the ground with a smaller speed each "
 "time.<br>"
 "<b>(c)</b> The displacement&ndash;time graph would be a series of parabolic arcs (not straight "
 "lines), each lower than the last, touching the time axis at each bounce.")

add(T2,
 "A car and a lorry are travelling in the same direction along a straight road. At t = 0 the car, "
 "moving at 8.0 m s<sup>&minus;1</sup>, is 15 m behind the lorry which moves at a constant "
 "12 m s<sup>&minus;1</sup>. At t = 0 the car begins to accelerate uniformly at 2.5 m s<sup>&minus;2</sup>."
 "<ol class='parts'>"
 "<li>Show that the car draws level with the lorry, and find the time taken.</li>"
 "<li>Find the car&#39;s speed at that moment.</li></ol>",
 8,
 "Let the car&#39;s position start at 0 and the lorry&#39;s at +15 m.<br>"
 "Car: x<sub>c</sub> = 8.0t + &frac12;(2.5)t&sup2; = 8.0t + 1.25t&sup2;. Lorry: x<sub>l</sub> = 15 + 12t.<br>"
 "<b>(a)</b> Level when x<sub>c</sub> = x<sub>l</sub>: 8.0t + 1.25t&sup2; = 15 + 12t &rArr; "
 "1.25t&sup2; &minus; 4.0t &minus; 15 = 0. "
 "t = [4.0 &plusmn; &radic;(16 + 75)]/2.5 = [4.0 &plusmn; 9.54]/2.5. "
 "Positive root: t = 13.54/2.5 = <b>5.4 s</b> (a real positive solution exists, so they meet).<br>"
 "<b>(b)</b> v = 8.0 + 2.5 &times; 5.42 = 8.0 + 13.5 = <b>21.6 m s<sup>&minus;1</sup></b>.")

add(T2,
 "Two students investigate the acceleration of free fall by dropping a ball through a set of light "
 "gates and by video analysis. Their processed data give displacement <span class='eq'>s</span> "
 "against time <span class='eq'>t</span> for a ball released from rest."
 "<ol class='parts'>"
 "<li>State what graph they should plot to obtain a straight line, and how <span class='eq'>g</span> "
 "is found from its gradient.</li>"
 "<li>Their straight line does not pass through the origin but has a small positive intercept on the "
 "<span class='eq'>s</span>-axis. Explain what this systematic feature indicates and why the gradient "
 "still gives a valid value of <span class='eq'>g</span>.</li></ol>",
 7,
 "<b>(a)</b> From s = ut + &frac12;gt&sup2; with u = 0, s = &frac12;gt&sup2;. Plot "
 "<span class='eq'>s</span> (y-axis) against <span class='eq'>t&sup2;</span> (x-axis): a straight "
 "line through the origin of gradient &frac12;g, so <b>g = 2 &times; gradient</b>.<br>"
 "<b>(b)</b> A positive intercept on the s-axis means the ball had already fallen a small distance "
 "(or timing started slightly late / the ball had a small initial speed) &mdash; a systematic "
 "offset. Because this adds a constant to every s value, it shifts the whole line up but does not "
 "change its slope; since g is obtained from the <b>gradient</b>, the offset does not affect the "
 "value of g.")

# ===========================================================================
# TOPIC 3  Dynamics  (extra)
# ===========================================================================

add(T3,
 "Two masses, 3.0 kg and 5.0 kg, hang from the ends of a light inextensible string passing over a "
 "frictionless pulley (an Atwood machine). The system is released from rest."
 "<ol class='parts'>"
 "<li>By applying Newton&#39;s second law to each mass, find the acceleration of the system.</li>"
 "<li>Find the tension in the string.</li>"
 "<li>State the force exerted by the string on the pulley axle.</li></ol>",
 9,
 "Let a be the acceleration; the 5.0 kg falls, the 3.0 kg rises.<br>"
 "<b>(a)</b> For 5.0 kg: 5.0g &minus; T = 5.0a. For 3.0 kg: T &minus; 3.0g = 3.0a. "
 "Adding: (5.0 &minus; 3.0)g = 8.0a &rArr; a = 2.0 &times; 9.81/8.0 = "
 "<b>2.45 m s<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> T = 3.0(g + a) = 3.0(9.81 + 2.45) = 3.0 &times; 12.26 = <b>36.8 N</b> "
 "(check: 5.0(g &minus; a) = 5.0 &times; 7.36 = 36.8 N &#10003;).<br>"
 "<b>(c)</b> The string pulls down on the pulley on both sides, so the axle supports "
 "2T = 2 &times; 36.8 = <b>73.6 N</b> (less than the total weight 78.5 N because the system is "
 "accelerating).")

add(T3,
 "Sand falls vertically at a steady rate of 3.0 kg s<sup>&minus;1</sup> onto a horizontal conveyor "
 "belt that is moving at a constant 1.5 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the horizontal force needed to keep the belt moving at constant speed (ignore belt "
 "friction).</li>"
 "<li>Calculate the rate at which kinetic energy is given to the sand.</li>"
 "<li>Explain why the power delivered by the driving force is not equal to your answer to (b), and "
 "find where the difference goes.</li></ol>",
 8,
 "<b>(a)</b> The belt must accelerate the sand from 0 to 1.5 m s<sup>&minus;1</sup>: force = rate of "
 "change of momentum = (dm/dt)v = 3.0 &times; 1.5 = <b>4.5 N</b>.<br>"
 "<b>(b)</b> Rate of KE gain = &frac12;(dm/dt)v&sup2; = &frac12; &times; 3.0 &times; 1.5&sup2; = "
 "<b>3.4 W</b>.<br>"
 "<b>(c)</b> Power delivered by the force = Fv = 4.5 &times; 1.5 = 6.75 W. This is <b>twice</b> the "
 "rate of KE gain. The other 3.4 W is dissipated as heat (and sound) as the sand slips on the belt "
 "before reaching belt speed &mdash; the collisions between sand grains and belt are inelastic.")

add(T3,
 "A ball of mass 0.25 kg is dropped from a height of 1.8 m onto a floor and rebounds to a height of "
 "1.0 m. The ball is in contact with the floor for 0.015 s."
 "<ol class='parts'>"
 "<li>Find the speeds of the ball just before and just after impact.</li>"
 "<li>Find the average resultant force on the ball during contact.</li>"
 "<li>Hence find the average force exerted by the floor on the ball.</li></ol>",
 9,
 "<b>(a)</b> Before: v = &radic;(2 &times; 9.81 &times; 1.8) = &radic;35.3 = 5.94 m s<sup>&minus;1</sup> "
 "(down). After: v = &radic;(2 &times; 9.81 &times; 1.0) = &radic;19.6 = 4.43 m s<sup>&minus;1</sup> "
 "(up).<br>"
 "<b>(b)</b> Take up positive. &Delta;p = m(v<sub>up</sub> &minus; v<sub>down</sub>) = "
 "0.25(4.43 &minus; (&minus;5.94)) = 0.25 &times; 10.37 = 2.59 kg m s<sup>&minus;1</sup>. "
 "Resultant force = &Delta;p/&Delta;t = 2.59/0.015 = <b>173 N</b> (upward).<br>"
 "<b>(c)</b> Resultant = N &minus; mg, so N = 173 + mg = 173 + 0.25 &times; 9.81 = 173 + 2.45 = "
 "<b>175 N</b> (upward). The weight is small compared with the impact force.")

add(T3,
 "A radioactive nucleus of mass 220 u, initially at rest, emits an &alpha;-particle of mass 4.0 u. "
 "The &alpha;-particle leaves with a speed of 1.5 &times; 10<sup>7</sup> m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Using conservation of momentum, find the recoil speed of the daughter nucleus.</li>"
 "<li>Find the ratio of the kinetic energy of the &alpha;-particle to that of the daughter nucleus.</li></ol>",
 8,
 "Daughter mass = 220 &minus; 4.0 = 216 u.<br>"
 "<b>(a)</b> Momentum conserved (initially zero): 0 = 4.0v<sub>&alpha;</sub> + 216v<sub>d</sub> &rArr; "
 "v<sub>d</sub> = &minus;(4.0/216)(1.5&times;10<sup>7</sup>) = "
 "<b>&minus;2.8&times;10<sup>5</sup> m s<sup>&minus;1</sup></b> (opposite direction).<br>"
 "<b>(b)</b> KE = p&sup2;/(2m); the two momenta are equal in magnitude, so "
 "KE<sub>&alpha;</sub>/KE<sub>d</sub> = m<sub>d</sub>/m<sub>&alpha;</sub> = 216/4.0 = <b>54</b>. "
 "The light &alpha;-particle carries 54 times more kinetic energy than the heavy recoiling nucleus.")

# ===========================================================================
# TOPIC 4  Forces, density and pressure  (extra)
# ===========================================================================

add(T4,
 "A uniform diving board of weight 200 N and length 4.0 m is bolted at one end (A) and rests on a "
 "support (B) 1.2 m from A. A diver of weight 650 N stands at the free end (C)."
 "<ol class='parts'>"
 "<li>Taking moments about the support B, find the force the bolt at A exerts on the board, stating "
 "its direction.</li>"
 "<li>Find the force exerted by the support B on the board.</li></ol>",
 9,
 "The board&#39;s weight (200 N) acts at its centre, 2.0 m from A, i.e. 0.8 m to the right of B. "
 "The diver (650 N) is at C, 4.0 &minus; 1.2 = 2.8 m to the right of B. A is 1.2 m to the left of B.<br>"
 "<b>(a)</b> Moments about B (let F<sub>A</sub> be the bolt force): the diver and board weight turn "
 "the board clockwise about B; F<sub>A</sub> must turn it anticlockwise, so the bolt pulls the board "
 "<b>down</b>. F<sub>A</sub> &times; 1.2 = 200 &times; 0.8 + 650 &times; 2.8 = 160 + 1820 = 1980 &rArr; "
 "F<sub>A</sub> = <b>1650 N downward</b>.<br>"
 "<b>(b)</b> Vertical equilibrium: F<sub>B</sub> = total downward forces = 200 + 650 + 1650 = "
 "<b>2500 N upward</b>. (Check moments about A: F<sub>B</sub>&times;1.2 = 200&times;2.0 + 650&times;4.0 "
 "= 400 + 2600 = 3000; F<sub>B</sub> = 2500 N &#10003;)",
 "<svg width='330' height='120' viewBox='0 0 330 120'>"
 "<rect x='30' y='50' width='270' height='10' fill='#cda434' stroke='#333'/>"
 "<rect x='24' y='45' width='8' height='20' fill='#555'/>"
 "<polygon points='108,60 100,85 116,85' fill='#555'/>"
 "<line x1='165' y1='60' x2='165' y2='90' stroke='#093' stroke-width='2'/>"
 "<polygon points='165,90 161,82 169,82' fill='#093'/>"
 "<line x1='295' y1='60' x2='295' y2='95' stroke='#c30' stroke-width='2'/>"
 "<polygon points='295,95 291,87 299,87' fill='#c30'/>"
 "<text x='22' y='42' font-size='10'>A</text><text x='100' y='100' font-size='9'>B</text>"
 "<text x='288' y='45' font-size='10'>C</text>"
 "<text x='150' y='103' font-size='9' fill='#093'>200 N</text>"
 "<text x='278' y='108' font-size='9' fill='#c30'>650 N</text></svg>")

add(T4,
 "A simple mercury barometer consists of a vertical tube, closed at the top, with its open lower end "
 "in a dish of mercury (density 1.36 &times; 10<sup>4</sup> kg m<sup>&minus;3</sup>). The mercury "
 "column stands 756 mm above the surface in the dish."
 "<ol class='parts'>"
 "<li>Calculate the atmospheric pressure.</li>"
 "<li>State what occupies the space above the mercury in the closed tube, and explain why the height "
 "would be unchanged if a wider tube were used.</li></ol>",
 7,
 "<b>(a)</b> p = &rho;gh = 1.36&times;10<sup>4</sup> &times; 9.81 &times; 0.756 = "
 "<b>1.01&times;10<sup>5</sup> Pa</b>.<br>"
 "<b>(b)</b> Above the mercury is a near-<b>vacuum</b> (a little mercury vapour), so it exerts "
 "negligible pressure. The height depends only on the balance between atmospheric pressure and "
 "&rho;gh, which is independent of the tube&#39;s cross-sectional area (a wider tube holds more "
 "mercury but the pressure at the base depends only on the vertical height), so h is unchanged.")

add(T4,
 "A hydrometer floats vertically in a liquid. It consists of a weighted bulb and a thin uniform stem "
 "of cross-sectional area 4.0 &times; 10<sup>&minus;5</sup> m&sup2;. Its total mass is 12 g. In pure "
 "water (1000 kg m<sup>&minus;3</sup>) the water line is at a certain mark on the stem."
 "<ol class='parts'>"
 "<li>Find the total volume submerged when it floats in water.</li>"
 "<li>When placed in a salt solution of density 1050 kg m<sup>&minus;3</sup>, find how far up the "
 "stem the liquid line moves (relative to the water mark).</li></ol>",
 8,
 "Floating: upthrust = weight &rArr; &rho;V<sub>sub</sub>g = mg &rArr; V<sub>sub</sub> = m/&rho;.<br>"
 "<b>(a)</b> In water: V<sub>sub</sub> = 0.012/1000 = <b>1.2&times;10<sup>&minus;5</sup> m&sup3;</b>.<br>"
 "<b>(b)</b> In salt solution: V&#39;<sub>sub</sub> = 0.012/1050 = 1.143&times;10<sup>&minus;5</sup> m&sup3;. "
 "Less volume is submerged, so the hydrometer rises. The change in submerged volume = "
 "1.2&times;10<sup>&minus;5</sup> &minus; 1.143&times;10<sup>&minus;5</sup> = "
 "5.7&times;10<sup>&minus;7</sup> m&sup3;. This corresponds to a length of stem "
 "&Delta;L = &Delta;V/A = 5.7&times;10<sup>&minus;7</sup>/4.0&times;10<sup>&minus;5</sup> = "
 "<b>1.4&times;10<sup>&minus;2</sup> m</b> (about 14 mm higher out of the liquid).")

add(T4,
 "A uniform rod AB of weight 40 N is hinged to a wall at A and held horizontal by a light cable from "
 "B to a point on the wall directly above A, so the cable makes an angle of 40&deg; with the rod. A "
 "load of 60 N hangs from B."
 "<ol class='parts'>"
 "<li>By taking moments about A, find the tension in the cable.</li>"
 "<li>Find the horizontal and vertical components of the force exerted by the hinge on the rod.</li></ol>",
 9,
 "Let the rod length be L. Rod weight (40 N) acts at L/2; load (60 N) and cable act at B (distance L). "
 "Cable tension T has a component perpendicular to the rod of T sin40&deg;.<br>"
 "<b>(a)</b> Moments about A: T sin40&deg; &times; L = 40 &times; (L/2) + 60 &times; L. "
 "Divide by L: T sin40&deg; = 20 + 60 = 80 &rArr; T = 80/sin40&deg; = 80/0.643 = <b>124 N</b>.<br>"
 "<b>(b)</b> Cable pulls towards the wall and upward: horizontal component T cos40&deg; = "
 "124 &times; 0.766 = 95.2 N; vertical component T sin40&deg; = 80 N. "
 "Hinge horizontal force balances T cos40&deg;: H = <b>95 N (away from wall)</b>. "
 "Vertical: V + T sin40&deg; = 40 + 60 &rArr; V = 100 &minus; 80 = <b>20 N upward</b>.")

# ===========================================================================
# TOPIC 5  Work, energy and power  (extra)
# ===========================================================================

add(T5,
 "A car of mass 1100 kg climbs a straight hill inclined at 6.0&deg; to the horizontal at a steady "
 "speed of 18 m s<sup>&minus;1</sup>. The total resistive force (friction + air) is 620 N."
 "<ol class='parts'>"
 "<li>Find the component of the car&#39;s weight acting down the slope.</li>"
 "<li>Find the useful output power of the engine.</li>"
 "<li>The car then reaches a level road. Assuming the engine power and resistive force are unchanged, "
 "find the initial acceleration on the level road.</li></ol>",
 9,
 "<b>(a)</b> W<sub>slope</sub> = mg sin6.0&deg; = 1100 &times; 9.81 &times; 0.1045 = <b>1128 N</b>.<br>"
 "<b>(b)</b> At steady speed the driving force = resistance + weight component = 620 + 1128 = 1748 N. "
 "P = Fv = 1748 &times; 18 = <b>3.1&times;10<sup>4</sup> W</b> (31 kW).<br>"
 "<b>(c)</b> On the level at the same instant (v = 18 m s<sup>&minus;1</sup>): driving force = P/v = "
 "31470/18 = 1748 N. Resultant = driving &minus; resistance = 1748 &minus; 620 = 1128 N. "
 "a = F/m = 1128/1100 = <b>1.03 m s<sup>&minus;2</sup></b>.")

add(T5,
 "A pile driver of mass 250 kg falls freely from rest through 2.4 m onto the top of a pile of mass "
 "150 kg, and the two move together immediately after impact. The pile is then driven 0.12 m into "
 "the ground before stopping."
 "<ol class='parts'>"
 "<li>Find the speed of the driver just before impact.</li>"
 "<li>Find the common speed of driver and pile immediately after the (inelastic) impact.</li>"
 "<li>Find the average resistive force exerted by the ground on the pile.</li></ol>",
 10,
 "<b>(a)</b> v = &radic;(2gh) = &radic;(2 &times; 9.81 &times; 2.4) = &radic;47.1 = "
 "<b>6.86 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Momentum: 250 &times; 6.86 = (250 + 150)v&#39; &rArr; v&#39; = 1715/400 = "
 "<b>4.29 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(c)</b> After impact KE = &frac12;(400)(4.29)&sup2; = 3.68&times;10<sup>3</sup> J. During the "
 "0.12 m of penetration, the ground&#39;s resistance R and gravity both act. Work-energy: "
 "(R &minus; (400)g) &times; 0.12 = KE &rArr; R &times; 0.12 = 3680 + 400&times;9.81&times;0.12 = "
 "3680 + 471 = 4151 &rArr; R = 4151/0.12 = <b>3.5&times;10<sup>4</sup> N</b>.")

add(T5,
 "On a fairground ride a car of total mass 400 kg starts from rest at the top of a track, descends a "
 "vertical drop of 22 m, and then travels round the inside of a vertical circular loop of radius "
 "6.0 m. Friction is negligible."
 "<ol class='parts'>"
 "<li>Find the speed of the car at the bottom of the drop.</li>"
 "<li>Find the speed of the car at the top of the loop.</li>"
 "<li>Determine whether the car maintains contact with the track at the top of the loop, justifying "
 "your answer.</li></ol>",
 9,
 "<b>(a)</b> &frac12;mv&sup2; = mgh &rArr; v = &radic;(2 &times; 9.81 &times; 22) = &radic;431.6 = "
 "<b>20.8 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> The top of the loop is 2r = 12 m above the bottom. Energy: "
 "&frac12;v<sub>top</sub>&sup2; = &frac12;v<sub>bot</sub>&sup2; &minus; g(12) &rArr; "
 "v<sub>top</sub>&sup2; = 431.6 &minus; 2&times;9.81&times;12 = 431.6 &minus; 235.4 = 196.2 &rArr; "
 "v<sub>top</sub> = <b>14.0 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(c)</b> Minimum speed to maintain contact: mg = mv<sub>min</sub>&sup2;/r &rArr; "
 "v<sub>min</sub> = &radic;(gr) = &radic;(9.81 &times; 6.0) = 7.67 m s<sup>&minus;1</sup>. "
 "Since 14.0 &gt; 7.67, the required centripetal force exceeds the weight, so the track must push "
 "inward too &mdash; the car <b>stays in contact</b> with the track.")

add(T5,
 "A wind turbine has blades that sweep out a circle of radius 25 m. Air of density "
 "1.2 kg m<sup>&minus;3</sup> moves towards the turbine at 12 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Show that the mass of air passing through the swept area per second is about 2.8 &times; "
 "10<sup>4</sup> kg s<sup>&minus;1</sup>.</li>"
 "<li>Calculate the maximum theoretical power available in this moving air.</li>"
 "<li>The turbine has an overall efficiency of 35%. Find its electrical power output.</li></ol>",
 9,
 "Swept area A = &pi;r&sup2; = &pi;(25)&sup2; = 1963 m&sup2;.<br>"
 "<b>(a)</b> Mass per second = &rho;Av = 1.2 &times; 1963 &times; 12 = <b>2.83&times;10<sup>4</sup> "
 "kg s<sup>&minus;1</sup></b>. &#10003;<br>"
 "<b>(b)</b> Power in wind = &frac12;(mass/s)v&sup2; = &frac12; &times; 2.83&times;10<sup>4</sup> &times; "
 "12&sup2; = &frac12; &times; 2.83&times;10<sup>4</sup> &times; 144 = <b>2.0&times;10<sup>6</sup> W</b> "
 "(2.0 MW).<br>"
 "<b>(c)</b> Output = 0.35 &times; 2.0&times;10<sup>6</sup> = <b>7.1&times;10<sup>5</sup> W</b> "
 "(0.71 MW).")

# ===========================================================================
# TOPIC 6  Deformation of solids  (extra)
# ===========================================================================

add(T6,
 "A load is suspended from two vertical wires attached side by side to the same support and the same "
 "load bar, so they stretch by the same amount (they are in parallel). Wire S is steel "
 "(E = 2.0 &times; 10<sup>11</sup> Pa) and wire B is brass (E = 1.0 &times; 10<sup>11</sup> Pa); both "
 "have the same length and the same cross-sectional area."
 "<ol class='parts'>"
 "<li>Explain why the two wires have the same strain but different stresses.</li>"
 "<li>Find the ratio of the tension in the steel wire to that in the brass wire.</li>"
 "<li>If the total load is 300 N, find the tension in each wire.</li></ol>",
 8,
 "<b>(a)</b> They share the same support and load bar and extend by the same amount over the same "
 "original length, so strain (= extension/length) is equal. Since stress = E &times; strain and the "
 "two materials have different E, the stresses differ (steel carries more stress for the same "
 "strain).<br>"
 "<b>(b)</b> Same area A and same strain &epsilon;: tension = stress &times; A = E&epsilon;A. "
 "T<sub>S</sub>/T<sub>B</sub> = E<sub>S</sub>/E<sub>B</sub> = 2.0/1.0 = <b>2</b>.<br>"
 "<b>(c)</b> T<sub>S</sub> + T<sub>B</sub> = 300 and T<sub>S</sub> = 2T<sub>B</sub> &rArr; "
 "3T<sub>B</sub> = 300 &rArr; T<sub>B</sub> = <b>100 N</b>, T<sub>S</sub> = <b>200 N</b>.")

add(T6,
 "A nylon climbing rope of unstretched length 50 m and cross-sectional area 8.0 &times; "
 "10<sup>&minus;5</sup> m&sup2; has a Young modulus of 3.0 &times; 10<sup>9</sup> Pa. A climber of "
 "mass 80 kg falls and is brought to rest by the rope, which stretches elastically."
 "<ol class='parts'>"
 "<li>Find the tension in the rope when the climber hangs at rest, and the resulting extension.</li>"
 "<li>Find the elastic potential energy stored in the rope at this extension.</li></ol>",
 8,
 "<b>(a)</b> Static tension = weight = 80 &times; 9.81 = 785 N. "
 "Extension e = FL/(AE) = (785 &times; 50)/(8.0&times;10<sup>&minus;5</sup> &times; 3.0&times;10<sup>9</sup>) "
 "= 39250/2.4&times;10<sup>5</sup> = <b>0.164 m</b>.<br>"
 "<b>(b)</b> Within the limit of proportionality E<sub>P</sub> = &frac12;Fe = "
 "&frac12; &times; 785 &times; 0.164 = <b>64 J</b>. (Equivalently the rope&#39;s stiffness "
 "k = AE/L = 4800 N m<sup>&minus;1</sup>, and &frac12;ke&sup2; = &frac12;&times;4800&times;0.164&sup2; "
 "= 64 J.)")

add(T6,
 "The stress&ndash;strain graph for a metal wire is a straight line from the origin to the limit of "
 "proportionality at a stress of 2.5 &times; 10<sup>8</sup> Pa and strain 1.25 &times; "
 "10<sup>&minus;3</sup>, then curves upward to a maximum (the ultimate tensile stress, UTS) of "
 "4.0 &times; 10<sup>8</sup> Pa before the wire breaks."
 "<ol class='parts'>"
 "<li>Calculate the Young modulus of the metal.</li>"
 "<li>Calculate the elastic potential energy stored per unit volume at the limit of proportionality.</li>"
 "<li>State what the UTS represents.</li></ol>",
 8,
 "<b>(a)</b> E = stress/strain = 2.5&times;10<sup>8</sup>/1.25&times;10<sup>&minus;3</sup> = "
 "<b>2.0&times;10<sup>11</sup> Pa</b>.<br>"
 "<b>(b)</b> Energy per unit volume = area under the stress&ndash;strain line (up to the limit) = "
 "&frac12; &times; stress &times; strain = &frac12; &times; 2.5&times;10<sup>8</sup> &times; "
 "1.25&times;10<sup>&minus;3</sup> = <b>1.6&times;10<sup>5</sup> J m<sup>&minus;3</sup></b>.<br>"
 "<b>(c)</b> The UTS is the <b>maximum stress</b> the material can withstand before it fails "
 "(the greatest tensile stress it can bear).")

add(T6,
 "A student stretches a rubber band and a copper wire, in turn, and plots force against extension for "
 "each through a full loading-then-unloading cycle."
 "<ol class='parts'>"
 "<li>Sketch and describe the shape of each loading&ndash;unloading curve.</li>"
 "<li>Explain what the area enclosed by the rubber band&#39;s loop represents and its practical "
 "consequence.</li>"
 "<li>State why the copper wire, once loaded beyond its elastic limit, does not return to its "
 "original length.</li></ol>",
 8,
 "<b>(a)</b> Rubber: loading and unloading follow different S-shaped curves forming a closed loop "
 "(hysteresis); unloading lies below loading. Copper (small extensions): loading is nearly a straight "
 "line and unloading retraces it; loaded beyond the elastic limit, the unloading line is parallel to "
 "the initial line but offset, ending at a permanent extension.<br>"
 "<b>(b)</b> The area of the rubber loop is the <b>energy dissipated as heat</b> per cycle. "
 "Consequence: repeatedly stretched rubber warms up, and not all stored energy is returned (important "
 "for, e.g., car tyres and shock absorbers).<br>"
 "<b>(c)</b> Beyond the elastic limit the deformation is <b>plastic</b>: planes of atoms have slipped "
 "past one another to new permanent positions, so the wire keeps a permanent extension when unloaded.",
 "<svg width='260' height='150' viewBox='0 0 260 150'>"
 "<line x1='35' y1='125' x2='240' y2='125' stroke='#333'/>"
 "<line x1='35' y1='125' x2='35' y2='15' stroke='#333'/>"
 "<path d='M35 125 C70 118 90 70 150 35' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M150 35 C120 80 70 108 35 125' fill='none' stroke='#c30' stroke-width='2'/>"
 "<text x='150' y='142' font-size='9'>extension</text>"
 "<text x='8' y='75' font-size='9'>force</text>"
 "<text x='95' y='55' font-size='8' fill='#06c'>load</text>"
 "<text x='70' y='118' font-size='8' fill='#c30'>unload</text></svg>")

# ===========================================================================
# TOPIC 7  Waves  (extra)
# ===========================================================================

add(T7,
 "A progressive transverse wave travels in the +x direction along a string. At time t = 0 the "
 "displacement&ndash;position graph is a sine curve of amplitude 8.0 mm and wavelength 0.60 m; the "
 "wave speed is 24 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the frequency and period.</li>"
 "<li>A particle is at maximum positive displacement at t = 0. Find the first two times after t = 0 "
 "when it is at zero displacement.</li>"
 "<li>State the phase difference between two particles 0.15 m apart.</li></ol>",
 8,
 "<b>(a)</b> f = v/&lambda; = 24/0.60 = <b>40 Hz</b>; T = 1/f = <b>0.025 s</b> (25 ms).<br>"
 "<b>(b)</b> Starting at maximum, the particle first reaches zero after a quarter period and again "
 "after three-quarters: t<sub>1</sub> = T/4 = <b>6.25&times;10<sup>&minus;3</sup> s</b>; "
 "t<sub>2</sub> = 3T/4 = <b>1.875&times;10<sup>&minus;2</sup> s</b>.<br>"
 "<b>(c)</b> Phase difference = (0.15/0.60) &times; 360&deg; = <b>90&deg;</b> (&pi;/2 rad).")

add(T7,
 "A train sounds a horn of constant frequency 660 Hz. A stationary observer on the platform hears "
 "the frequency fall from one steady value to another as the train passes through the station "
 "without stopping. (Speed of sound = 340 m s<sup>&minus;1</sup>.)"
 "<ol class='parts'>"
 "<li>The observer measures the approaching frequency as 700 Hz. Calculate the speed of the train.</li>"
 "<li>Calculate the frequency the observer hears as the train recedes.</li></ol>",
 8,
 "<b>(a)</b> Approaching: f<sub>o</sub> = f<sub>s</sub>v/(v &minus; v<sub>s</sub>) &rArr; "
 "700 = 660 &times; 340/(340 &minus; v<sub>s</sub>). "
 "340 &minus; v<sub>s</sub> = 660 &times; 340/700 = 320.6 &rArr; v<sub>s</sub> = "
 "<b>19.4 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Receding: f<sub>o</sub> = 660 &times; 340/(340 + 19.4) = 660 &times; 340/359.4 = "
 "<b>624 Hz</b>.")

add(T7,
 "A laser emits a parallel beam of light of power 2.0 mW and wavelength 630 nm. The beam has a "
 "circular cross-section of diameter 1.2 mm."
 "<ol class='parts'>"
 "<li>Calculate the intensity of the beam.</li>"
 "<li>The beam is expanded so its diameter becomes 6.0 mm with the same power. State the new "
 "intensity and the factor by which the amplitude of the light wave changes.</li></ol>",
 7,
 "<b>(a)</b> Area = &pi;(0.6&times;10<sup>&minus;3</sup>)&sup2; = 1.13&times;10<sup>&minus;6</sup> m&sup2;. "
 "I = P/A = 2.0&times;10<sup>&minus;3</sup>/1.13&times;10<sup>&minus;6</sup> = "
 "<b>1.77&times;10<sup>3</sup> W m<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> Diameter &times;5 &rArr; area &times;25, so with the same power I becomes 1/25 of before: "
 "I&#39; = 1770/25 = <b>71 W m<sup>&minus;2</sup></b>. Since I &prop; amplitude&sup2;, the amplitude "
 "changes by &radic;(1/25) = <b>1/5</b> (falls to one fifth).")

add(T7,
 "Vertically plane-polarised light of intensity I<sub>0</sub> is incident on two polarising filters. "
 "The first has its axis at angle &theta; to the vertical; the second (analyser) has its axis "
 "horizontal."
 "<ol class='parts'>"
 "<li>Write an expression for the intensity transmitted through both filters in terms of "
 "I<sub>0</sub> and &theta;.</li>"
 "<li>Show that this transmitted intensity is a maximum when &theta; = 45&deg;, and find that maximum "
 "in terms of I<sub>0</sub>.</li></ol>",
 8,
 "<b>(a)</b> After filter 1: I<sub>1</sub> = I<sub>0</sub>cos&sup2;&theta;. Filter 2 is at "
 "(90&deg; &minus; &theta;) to filter 1, so I = I<sub>1</sub>cos&sup2;(90&deg; &minus; &theta;) = "
 "I<sub>0</sub>cos&sup2;&theta; sin&sup2;&theta;. Using sin&theta;cos&theta; = &frac12;sin2&theta;: "
 "<b>I = &frac14;I<sub>0</sub>sin&sup2;(2&theta;)</b>.<br>"
 "<b>(b)</b> I is greatest when sin&sup2;(2&theta;) = 1, i.e. 2&theta; = 90&deg; &rArr; "
 "&theta; = 45&deg;. Then I<sub>max</sub> = &frac14;I<sub>0</sub> &times; 1 = "
 "<b>I<sub>0</sub>/4</b>. (With no middle filter the crossed pair would transmit zero.)")

# ===========================================================================
# TOPIC 8  Superposition  (extra)
# ===========================================================================

add(T8,
 "In a Young&#39;s double-slit experiment, light of unknown wavelength illuminates two slits 0.30 mm "
 "apart. On a screen 1.8 m away, the distance across 10 bright-fringe spacings is measured as "
 "31.5 mm."
 "<ol class='parts'>"
 "<li>Calculate the fringe separation and hence the wavelength of the light.</li>"
 "<li>Explain why the distance across several fringes is measured rather than a single fringe "
 "spacing.</li>"
 "<li>State and explain the effect on the pattern of replacing the light with one of longer "
 "wavelength.</li></ol>",
 8,
 "<b>(a)</b> Fringe separation x = 31.5/10 = 3.15 mm = 3.15&times;10<sup>&minus;3</sup> m. "
 "&lambda; = ax/D = (0.30&times;10<sup>&minus;3</sup> &times; 3.15&times;10<sup>&minus;3</sup>)/1.8 = "
 "9.45&times;10<sup>&minus;7</sup>/1.8 = <b>5.3&times;10<sup>&minus;7</sup> m</b> (530 nm).<br>"
 "<b>(b)</b> The fringes are close together, so measuring one spacing has a large percentage "
 "uncertainty; measuring across many spacings and dividing reduces the percentage uncertainty in x "
 "(the absolute measuring uncertainty is spread over a larger distance).<br>"
 "<b>(c)</b> x = &lambda;D/a &prop; &lambda;, so a longer wavelength gives <b>wider</b> fringe spacing "
 "(the pattern spreads out).")

add(T8,
 "A diffraction grating is marked &#39;600 lines per mm&#39;. It is illuminated normally by light "
 "containing two wavelengths, 480 nm and 640 nm."
 "<ol class='parts'>"
 "<li>Calculate the grating spacing.</li>"
 "<li>Calculate the angular separation of the two wavelengths in the first-order spectrum.</li>"
 "<li>Determine the highest order in which the 640 nm line can be seen.</li></ol>",
 9,
 "<b>(a)</b> d = 1/(600&times;10<sup>3</sup>) = <b>1.667&times;10<sup>&minus;6</sup> m</b>.<br>"
 "<b>(b)</b> First order (n = 1): "
 "sin&theta;<sub>480</sub> = 480&times;10<sup>&minus;9</sup>/1.667&times;10<sup>&minus;6</sup> = 0.288 "
 "&rArr; &theta; = 16.7&deg;. "
 "sin&theta;<sub>640</sub> = 640&times;10<sup>&minus;9</sup>/1.667&times;10<sup>&minus;6</sup> = 0.384 "
 "&rArr; &theta; = 22.6&deg;. Angular separation = 22.6 &minus; 16.7 = <b>5.9&deg;</b>.<br>"
 "<b>(c)</b> Highest order for 640 nm: n &le; d/&lambda; = "
 "1.667&times;10<sup>&minus;6</sup>/640&times;10<sup>&minus;9</sup> = 2.6, so <b>n = 2</b>.")

add(T8,
 "A tube of length 0.85 m is open at both ends. The speed of sound in air is 340 m s<sup>&minus;1</sup>. "
 "(Neglect end corrections.)"
 "<ol class='parts'>"
 "<li>Sketch the displacement pattern of the fundamental (first harmonic) and state the positions of "
 "the antinodes.</li>"
 "<li>Calculate the fundamental frequency.</li>"
 "<li>Calculate the frequency of the third harmonic.</li></ol>",
 8,
 "<b>(a)</b> An open&ndash;open tube has displacement <b>antinodes at both open ends</b> and a node "
 "in the middle for the fundamental. The fundamental fits half a wavelength in the tube "
 "(A&ndash;N&ndash;A).<br>"
 "<b>(b)</b> L = &lambda;/2 &rArr; &lambda; = 2L = 1.70 m. f<sub>1</sub> = v/&lambda; = 340/1.70 = "
 "<b>200 Hz</b>.<br>"
 "<b>(c)</b> For an open tube all harmonics are present: f<sub>3</sub> = 3f<sub>1</sub> = "
 "3 &times; 200 = <b>600 Hz</b>.",
 "<svg width='240' height='90' viewBox='0 0 240 90'>"
 "<rect x='30' y='30' width='180' height='30' fill='none' stroke='#333'/>"
 "<line x1='30' y1='30' x2='30' y2='60' stroke='#fff' stroke-width='3'/>"
 "<line x1='210' y1='30' x2='210' y2='60' stroke='#fff' stroke-width='3'/>"
 "<path d='M30 30 Q120 60 210 30' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M30 60 Q120 30 210 60' fill='none' stroke='#06c' stroke-width='1' stroke-dasharray='3 2'/>"
 "<text x='26' y='24' font-size='9'>A</text><text x='206' y='24' font-size='9'>A</text>"
 "<text x='116' y='78' font-size='9'>N</text></svg>")

add(T8,
 "Two loudspeakers, 0.80 m apart, are driven in phase at the same frequency and face a wall 5.0 m "
 "away. A microphone moved along a line parallel to the speakers detects a series of maxima and "
 "minima. Adjacent maxima are found to be 0.66 m apart."
 "<ol class='parts'>"
 "<li>Treating this as a two-source interference pattern, calculate the wavelength of the sound.</li>"
 "<li>Calculate the frequency (speed of sound = 340 m s<sup>&minus;1</sup>).</li>"
 "<li>State and explain what happens to the spacing of the maxima if the frequency is increased.</li></ol>",
 8,
 "<b>(a)</b> Using x = &lambda;D/a with x = 0.66 m, D = 5.0 m, a = 0.80 m: "
 "&lambda; = xa/D = (0.66 &times; 0.80)/5.0 = <b>0.106 m</b> (&asymp; 0.11 m).<br>"
 "<b>(b)</b> f = v/&lambda; = 340/0.106 = <b>3.2&times;10<sup>3</sup> Hz</b> (3.2 kHz).<br>"
 "<b>(c)</b> Higher frequency &rArr; shorter wavelength; since x = &lambda;D/a, the spacing of the "
 "maxima <b>decreases</b> (the pattern gets closer together).")

# ===========================================================================
# TOPIC 9  Electricity  (extra)
# ===========================================================================

add(T9,
 "A metal wire of diameter 0.50 mm carries a current of 1.8 A. The metal has "
 "5.9 &times; 10<sup>28</sup> free electrons per cubic metre."
 "<ol class='parts'>"
 "<li>Calculate the mean drift speed of the electrons.</li>"
 "<li>The wire is joined to a second wire of the same material but half the diameter. Find the drift "
 "speed in the thinner wire and explain your reasoning.</li></ol>",
 8,
 "A = &pi;(0.25&times;10<sup>&minus;3</sup>)&sup2; = 1.963&times;10<sup>&minus;7</sup> m&sup2;.<br>"
 "<b>(a)</b> v = I/(Anq) = 1.8/(1.963&times;10<sup>&minus;7</sup> &times; 5.9&times;10<sup>28</sup> &times; "
 "1.60&times;10<sup>&minus;19</sup>). Denominator = 1.853&times;10<sup>3</sup>. "
 "v = 1.8/1.853&times;10<sup>3</sup> = <b>9.7&times;10<sup>&minus;4</sup> m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> The current is the same (series). Half the diameter &rArr; quarter the area. "
 "Since I = Anvq with I, n, q fixed, v &prop; 1/A, so v increases &times;4: "
 "v&#39; = 4 &times; 9.7&times;10<sup>&minus;4</sup> = <b>3.9&times;10<sup>&minus;3</sup> m s<sup>&minus;1</sup></b>. "
 "Charge conservation requires the same current everywhere, so carriers move faster where the wire is "
 "thinner.")

add(T9,
 "In an experiment to measure the resistivity of a metal, the resistance of a wire is measured for "
 "several lengths, giving a straight-line graph of resistance R against length L. The graph passes "
 "through the origin with a gradient of 6.8 &Omega; m<sup>&minus;1</sup>. The wire has a uniform "
 "diameter of 0.34 mm."
 "<ol class='parts'>"
 "<li>Explain why a graphical method is preferable to a single measurement.</li>"
 "<li>Use the gradient to calculate the resistivity of the metal.</li></ol>",
 8,
 "<b>(a)</b> Plotting many points and drawing a best-fit line averages out random errors in "
 "individual readings and reveals systematic problems (e.g. a non-zero intercept from contact/"
 "lead resistance). A line through the origin here confirms R &prop; L and gives a more reliable "
 "gradient than one measurement.<br>"
 "<b>(b)</b> R = &rho;L/A &rArr; gradient R/L = &rho;/A, so &rho; = gradient &times; A. "
 "A = &pi;(0.17&times;10<sup>&minus;3</sup>)&sup2; = 9.08&times;10<sup>&minus;8</sup> m&sup2;. "
 "&rho; = 6.8 &times; 9.08&times;10<sup>&minus;8</sup> = <b>6.2&times;10<sup>&minus;7</sup> &Omega; m</b>.")

add(T9,
 "A semiconductor diode and a fixed 220 &Omega; resistor are connected in series across a variable "
 "supply. When the supply is 2.0 V, the current is 6.0 mA."
 "<ol class='parts'>"
 "<li>Calculate the potential difference across the resistor and hence across the diode.</li>"
 "<li>Explain why the diode does not obey Ohm&#39;s law, referring to its I&ndash;V characteristic.</li></ol>",
 7,
 "<b>(a)</b> V<sub>R</sub> = IR = 6.0&times;10<sup>&minus;3</sup> &times; 220 = 1.32 V. "
 "By Kirchhoff&#39;s second law V<sub>diode</sub> = 2.0 &minus; 1.32 = <b>0.68 V</b> "
 "(a typical forward turn-on voltage).<br>"
 "<b>(b)</b> Ohm&#39;s law requires current proportional to p.d. (constant resistance). The diode&#39;s "
 "I&ndash;V graph is highly non-linear: almost no current until the forward voltage reaches "
 "&asymp;0.6 V, then a steep rise; and negligible current when reverse-biased. The ratio V/I is not "
 "constant, so the diode is non-ohmic.")

add(T9,
 "An electric shower is rated at 8.5 kW when connected to a 230 V mains supply."
 "<ol class='parts'>"
 "<li>Calculate the current drawn and the resistance of the heating element.</li>"
 "<li>The element is a nichrome wire of resistivity 1.1 &times; 10<sup>&minus;6</sup> &Omega; m and "
 "cross-sectional area 4.0 &times; 10<sup>&minus;7</sup> m&sup2;. Calculate the required length of "
 "wire.</li></ol>",
 8,
 "<b>(a)</b> I = P/V = 8500/230 = <b>37 A</b>. R = V&sup2;/P = 230&sup2;/8500 = 52900/8500 = "
 "<b>6.2 &Omega;</b>.<br>"
 "<b>(b)</b> R = &rho;L/A &rArr; L = RA/&rho; = (6.2 &times; 4.0&times;10<sup>&minus;7</sup>)/"
 "1.1&times;10<sup>&minus;6</sup> = 2.49&times;10<sup>&minus;6</sup>/1.1&times;10<sup>&minus;6</sup> = "
 "<b>2.3 m</b>.")

# ===========================================================================
# TOPIC 10  D.C. circuits  (extra)
# ===========================================================================

add(T10,
 "A battery is connected in turn to two different external resistors. With a 4.0 &Omega; resistor the "
 "current is 0.60 A; with a 9.0 &Omega; resistor the current is 0.30 A."
 "<ol class='parts'>"
 "<li>Set up two equations using &epsilon; = I(R + r) and solve them to find the e.m.f. and internal "
 "resistance of the battery.</li>"
 "<li>Calculate the terminal p.d. in each case and comment.</li></ol>",
 9,
 "<b>(a)</b> &epsilon; = I(R + r): "
 "Case 1: &epsilon; = 0.60(4.0 + r) = 2.40 + 0.60r. "
 "Case 2: &epsilon; = 0.30(9.0 + r) = 2.70 + 0.30r. "
 "Set equal: 2.40 + 0.60r = 2.70 + 0.30r &rArr; 0.30r = 0.30 &rArr; r = <b>1.0 &Omega;</b>. "
 "Then &epsilon; = 2.40 + 0.60 = <b>3.0 V</b>.<br>"
 "<b>(b)</b> Case 1: V = IR = 0.60 &times; 4.0 = 2.4 V. Case 2: V = 0.30 &times; 9.0 = 2.7 V. "
 "The terminal p.d. is higher when the external resistance is larger (smaller current &rArr; smaller "
 "&#39;lost volts&#39; Ir), approaching &epsilon; as R increases.")

add(T10,
 "In the circuit, two cells are connected in the same loop with two resistors. Cell 1 has e.m.f. "
 "6.0 V and internal resistance 0.50 &Omega;; cell 2 has e.m.f. 2.0 V and internal resistance "
 "0.30 &Omega; and is connected so that it opposes cell 1. They drive current through an external "
 "3.2 &Omega; resistor."
 "<ol class='parts'>"
 "<li>Using Kirchhoff&#39;s second law, find the current in the circuit.</li>"
 "<li>Find the potential difference across the 3.2 &Omega; resistor.</li></ol>",
 8,
 "<b>(a)</b> The cells oppose, so the net e.m.f. = 6.0 &minus; 2.0 = 4.0 V. Total resistance = "
 "0.50 + 0.30 + 3.2 = 4.0 &Omega;. Kirchhoff II: &Sigma;&epsilon; = &Sigma;IR &rArr; "
 "4.0 = I &times; 4.0 &rArr; I = <b>1.0 A</b> (driven by the stronger cell).<br>"
 "<b>(b)</b> V = IR = 1.0 &times; 3.2 = <b>3.2 V</b>.",
 "<svg width='300' height='120' viewBox='0 0 300 120'>"
 "<rect x='30' y='30' width='240' height='60' fill='none' stroke='#333'/>"
 "<line x1='90' y1='24' x2='90' y2='36' stroke='#333' stroke-width='2'/><line x1='98' y1='20' x2='98' y2='40' stroke='#333'/>"
 "<text x='84' y='16' font-size='8'>6.0 V</text>"
 "<line x1='210' y1='20' x2='210' y2='40' stroke='#333'/><line x1='218' y1='24' x2='218' y2='36' stroke='#333' stroke-width='2'/>"
 "<text x='200' y='16' font-size='8'>2.0 V (opp.)</text>"
 "<rect x='130' y='84' width='40' height='12' fill='none' stroke='#333'/><text x='128' y='110' font-size='8'>3.2&Omega;</text></svg>")

add(T10,
 "A potential divider is made from a thermistor and a 2.2 k&Omega; fixed resistor in series across a "
 "12 V supply, with the output taken across the fixed resistor. At 20&deg;C the thermistor has "
 "resistance 3.0 k&Omega;; at 60&deg;C it has resistance 0.80 k&Omega;."
 "<ol class='parts'>"
 "<li>Calculate the output voltage at each temperature.</li>"
 "<li>State and explain how this circuit could be used to switch on a cooling fan when the "
 "temperature rises.</li></ol>",
 8,
 "V<sub>out</sub> = V &times; R<sub>fixed</sub>/(R<sub>th</sub> + R<sub>fixed</sub>).<br>"
 "<b>(a)</b> At 20&deg;C: V<sub>out</sub> = 12 &times; 2.2/(3.0 + 2.2) = 12 &times; 2.2/5.2 = "
 "<b>5.1 V</b>. At 60&deg;C: V<sub>out</sub> = 12 &times; 2.2/(0.80 + 2.2) = 12 &times; 2.2/3.0 = "
 "<b>8.8 V</b>.<br>"
 "<b>(b)</b> As temperature rises the thermistor&#39;s resistance falls, so V<sub>out</sub> (across "
 "the fixed resistor) rises. Feeding V<sub>out</sub> to a switching circuit (transistor/relay or "
 "comparator) that turns on the fan once V<sub>out</sub> exceeds a set threshold means the fan "
 "switches on automatically at high temperature.")

add(T10,
 "A uniform potentiometer wire AB is 100.0 cm long and carries a steady current from a driver cell. A "
 "standard cell of e.m.f. 1.018 V is balanced at 63.6 cm from A. An unknown cell is then balanced at "
 "48.2 cm from A."
 "<ol class='parts'>"
 "<li>Explain why no current flows through the cell being tested at the balance point.</li>"
 "<li>Calculate the e.m.f. of the unknown cell.</li>"
 "<li>State one advantage of this method for measuring e.m.f.</li></ol>",
 8,
 "<b>(a)</b> At balance the p.d. across the length of potentiometer wire exactly equals and opposes "
 "the cell&#39;s e.m.f., so there is no net driving p.d. around that loop and the galvanometer reads "
 "zero &mdash; no current flows through the tested cell.<br>"
 "<b>(b)</b> E.m.f. &prop; balance length: &epsilon;<sub>x</sub>/&epsilon;<sub>std</sub> = "
 "L<sub>x</sub>/L<sub>std</sub> &rArr; &epsilon;<sub>x</sub> = 1.018 &times; 48.2/63.6 = "
 "<b>0.771 V</b>.<br>"
 "<b>(c)</b> Because no current is drawn from the cell at balance, there is no &#39;lost volts&#39; "
 "across its internal resistance, so the <b>true e.m.f.</b> is measured (unlike a voltmeter, which "
 "draws current).")

# ===========================================================================
# TOPIC 11  Particle physics  (extra)
# ===========================================================================

add(T11,
 "A nucleus of <sup>228</sup><sub>90</sub>Th decays by emitting an &alpha;-particle to form radium "
 "(Ra), which then decays by emitting a &beta;<sup>&minus;</sup> particle to form actinium (Ac)."
 "<ol class='parts'>"
 "<li>Write the equation for the &alpha;-decay, giving the nucleon and proton numbers of the radium "
 "nuclide.</li>"
 "<li>Write the equation for the &beta;<sup>&minus;</sup>-decay, including the antineutrino, giving "
 "the nucleon and proton numbers of the actinium nuclide.</li></ol>",
 8,
 "<b>(a)</b> <sup>228</sup><sub>90</sub>Th &rarr; <sup>224</sup><sub>88</sub>Ra + "
 "<sup>4</sup><sub>2</sub>&alpha;. Radium: <b>A = 224, Z = 88</b> (A: 228 = 224 + 4; Z: 90 = 88 + 2). "
 "&#10003;<br>"
 "<b>(b)</b> <sup>224</sup><sub>88</sub>Ra &rarr; <sup>224</sup><sub>89</sub>Ac + "
 "<sup>0</sup><sub>&minus;1</sub>e + &#772;&nu;<sub>e</sub>. Actinium: <b>A = 224, Z = 89</b> "
 "(nucleon number unchanged; a neutron becomes a proton so Z rises by 1). Charge: 88 = 89 + (&minus;1) "
 "&#10003;")

add(T11,
 "A &Sigma;<sup>+</sup> baryon has a charge of +1e and the quark composition uus; a K<sup>&minus;</sup> "
 "meson has a charge of &minus;1e."
 "<ol class='parts'>"
 "<li>Verify that the composition uus gives the correct charge for the &Sigma;<sup>+</sup>.</li>"
 "<li>The K<sup>&minus;</sup> is composed of a strange quark and an up antiquark. Show that this "
 "gives a charge of &minus;1e, using the fact that an antiquark has the opposite charge to its "
 "quark.</li></ol>",
 7,
 "Quark charges: u = +&frac23;e, s = &minus;&frac13;e; antiquarks have opposite sign so "
 "&#363; (anti-up) = &minus;&frac23;e.<br>"
 "<b>(a)</b> uus: (+&frac23;) + (+&frac23;) + (&minus;&frac13;) = +1e. &#10003; Correct for "
 "&Sigma;<sup>+</sup>.<br>"
 "<b>(b)</b> K<sup>&minus;</sup> = s + &#363; (strange quark + up antiquark): "
 "(&minus;&frac13;) + (&minus;&frac23;) = &minus;1e. &#10003; A meson (one quark + one antiquark) with "
 "charge &minus;1e.")

add(T11,
 "In a nuclear process, a proton within a nucleus is converted into a neutron."
 "<ol class='parts'>"
 "<li>Name this type of decay and state the two leptons emitted.</li>"
 "<li>Describe the change at the quark level.</li>"
 "<li>Explain why the emitted positron has a range of kinetic energies rather than a single value.</li></ol>",
 7,
 "<b>(a)</b> This is <b>&beta;<sup>+</sup> decay</b>. The particles emitted are a <b>positron</b> "
 "(e<sup>+</sup>) and an <b>electron neutrino</b> (&nu;<sub>e</sub>) &mdash; both leptons.<br>"
 "<b>(b)</b> A proton (uud) becomes a neutron (udd): an <b>up quark changes into a down quark</b>.<br>"
 "<b>(c)</b> The fixed decay energy is shared among three bodies &mdash; the daughter nucleus, the "
 "positron and the neutrino. Because the neutrino carries away a variable share, the positron can "
 "take any energy from zero up to a maximum, giving a continuous energy spectrum.")

add(T11,
 "The masses of some particles are: proton 1.00728 u, neutron 1.00867 u, "
 "helium-4 nucleus 4.00151 u. (1 u = 1.66 &times; 10<sup>&minus;27</sup> kg; "
 "c = 3.00 &times; 10<sup>8</sup> m s<sup>&minus;1</sup>.)"
 "<ol class='parts'>"
 "<li>Calculate the mass defect when two protons and two neutrons combine to form a helium-4 nucleus.</li>"
 "<li>Explain the physical meaning of this mass defect.</li></ol>",
 7,
 "<b>(a)</b> Mass of separate nucleons = 2(1.00728) + 2(1.00867) = 2.01456 + 2.01734 = 4.03190 u. "
 "Mass defect &Delta;m = 4.03190 &minus; 4.00151 = <b>0.03039 u</b> "
 "(= 0.03039 &times; 1.66&times;10<sup>&minus;27</sup> = 5.04&times;10<sup>&minus;29</sup> kg).<br>"
 "<b>(b)</b> The assembled nucleus has less mass than its separate parts. When the nucleons bind "
 "together, energy (the binding energy) is released; by mass&ndash;energy equivalence (E = &Delta;mc&sup2;) "
 "this energy corresponds to the &#39;lost&#39; mass. To pull the nucleus apart again, the same "
 "energy would have to be supplied.")
