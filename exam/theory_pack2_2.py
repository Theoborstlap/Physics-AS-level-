# -*- coding: utf-8 -*-
"""PACK 2 - Structured (theory) questions, topics 5-8. AS 9702."""
from engine import theory as T

T5 = "5&nbsp;&nbsp;Work, energy and power"
T6 = "6&nbsp;&nbsp;Deformation of solids"
T7 = "7&nbsp;&nbsp;Waves"
T8 = "8&nbsp;&nbsp;Superposition"


def add(topic, q, marks, ans, svg=""):
    T.append({"topic": topic, "q": q, "marks": marks, "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 5  Work, energy and power
# ===========================================================================
add(T5,
 "A cyclist and bicycle of total mass 90 kg free-wheel from rest down a hill, descending a vertical "
 "height of 25 m. At the bottom the speed is 18 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the loss in gravitational potential energy.</li>"
 "<li>Calculate the kinetic energy at the bottom, and hence the energy dissipated by resistive "
 "forces.</li></ol>",
 7,
 "<b>(a)</b> &Delta;E<sub>P</sub> = mg&Delta;h = 90 &times; 9.81 &times; 25 = <b>2.21 &times; "
 "10<sup>4</sup> J</b>.<br>"
 "<b>(b)</b> E<sub>K</sub> = &frac12;mv&sup2; = &frac12;(90)(18)&sup2; = 1.46&times;10<sup>4</sup> J. "
 "Energy dissipated = 2.21&times;10<sup>4</sup> &minus; 1.46&times;10<sup>4</sup> = "
 "<b>7.5 &times; 10<sup>3</sup> J</b>.")

add(T5,
 "A pump raises water from a well 8.0 m deep and delivers it at the surface through a nozzle at a "
 "speed of 6.0 m s<sup>&minus;1</sup>. Water is raised at a rate of 3.0 kg s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the power needed to lift the water.</li>"
 "<li>Calculate the additional power needed to give the water its kinetic energy.</li>"
 "<li>State the minimum input power of the pump.</li></ol>",
 8,
 "<b>(a)</b> Rate of gain of PE = (m/t)gh = 3.0 &times; 9.81 &times; 8.0 = <b>235 W</b>.<br>"
 "<b>(b)</b> Rate of gain of KE = &frac12;(m/t)v&sup2; = &frac12;(3.0)(6.0)&sup2; = <b>54 W</b>.<br>"
 "<b>(c)</b> Minimum input power = 235 + 54 = <b>289 W</b> (&asymp; 0.29 kW).")

add(T5,
 "A car of mass 1200 kg accelerates from 10 m s<sup>&minus;1</sup> to 30 m s<sup>&minus;1</sup> along "
 "a level road in a distance of 250 m. A constant resistive force of 500 N acts throughout."
 "<ol class='parts'>"
 "<li>Calculate the gain in kinetic energy.</li>"
 "<li>Calculate the work done against resistance.</li>"
 "<li>Hence find the average driving force provided by the engine.</li></ol>",
 8,
 "<b>(a)</b> &Delta;E<sub>K</sub> = &frac12;(1200)(30&sup2; &minus; 10&sup2;) = "
 "&frac12;(1200)(800) = <b>4.8 &times; 10<sup>5</sup> J</b>.<br>"
 "<b>(b)</b> W<sub>res</sub> = 500 &times; 250 = <b>1.25 &times; 10<sup>5</sup> J</b>.<br>"
 "<b>(c)</b> Work by engine = &Delta;E<sub>K</sub> + W<sub>res</sub> = 4.8&times;10<sup>5</sup> + "
 "1.25&times;10<sup>5</sup> = 6.05&times;10<sup>5</sup> J. Driving force = 6.05&times;10<sup>5</sup>/250 = "
 "<b>2.4 &times; 10<sup>3</sup> N</b>.")

add(T5,
 "A ski-lift carries skiers up a slope inclined at 15&deg; to the horizontal at a steady speed of "
 "2.5 m s<sup>&minus;1</sup>. The total mass being carried is 1800 kg and friction is negligible."
 "<ol class='parts'>"
 "<li>Calculate the tension in the tow cable.</li>"
 "<li>Calculate the power delivered by the motor.</li></ol>",
 7,
 "<b>(a)</b> At steady speed, cable tension = weight component along slope = mg sin15&deg; = "
 "1800 &times; 9.81 &times; 0.259 = <b>4.57 &times; 10<sup>3</sup> N</b>.<br>"
 "<b>(b)</b> P = Fv = 4.57&times;10<sup>3</sup> &times; 2.5 = <b>1.14 &times; 10<sup>4</sup> W</b> "
 "(&asymp; 11 kW).")

add(T5,
 "Derive the equation <span class='eq'>P = Fv</span> for the power delivered by a constant force F to "
 "an object moving at constant velocity v in the direction of the force."
 "<ol class='parts'>"
 "<li>Show the derivation from the definitions of work and power.</li>"
 "<li>A locomotive develops a useful power of 750 kW while pulling a train at a constant "
 "40 m s<sup>&minus;1</sup>. Find the total resistive force on the train.</li></ol>",
 6,
 "<b>(a)</b> Work done in time t: W = Fs, where s = vt. Power P = W/t = Fs/t = F(vt)/t = <b>Fv</b>.<br>"
 "<b>(b)</b> At constant speed the driving force equals the resistance. F = P/v = "
 "750&times;10<sup>3</sup>/40 = <b>1.9 &times; 10<sup>4</sup> N</b>.")

add(T5,
 "A stone of mass 0.40 kg is projected vertically upward with an initial kinetic energy of 32 J. Air "
 "resistance does 6.0 J of work on the stone during its ascent."
 "<ol class='parts'>"
 "<li>Using energy conservation, calculate the maximum height reached.</li>"
 "<li>State how the maximum height would compare if air resistance were negligible, without "
 "recalculating.</li></ol>",
 6,
 "<b>(a)</b> Energy available to become PE = 32 &minus; 6.0 = 26 J. mgh = 26 &rArr; "
 "h = 26/(0.40 &times; 9.81) = <b>6.6 m</b>.<br>"
 "<b>(b)</b> With no air resistance all 32 J would become PE, giving a <b>greater</b> maximum height "
 "(about 8.2 m).")

add(T5,
 "An electric motor rated at 250 W is used to raise a load of mass 30 kg vertically through 4.0 m. "
 "The operation takes 8.0 s."
 "<ol class='parts'>"
 "<li>Calculate the useful output power.</li>"
 "<li>Calculate the efficiency of the motor.</li></ol>",
 6,
 "<b>(a)</b> Useful work = mgh = 30 &times; 9.81 &times; 4.0 = 1177 J. Useful power = 1177/8.0 = "
 "<b>147 W</b>.<br>"
 "<b>(b)</b> Efficiency = useful output/total input = 147/250 = 0.59 = <b>59%</b>.")

add(T5,
 "A roller-coaster car of mass 500 kg passes the top of a hill at 8.0 m s<sup>&minus;1</sup>. It then "
 "descends 18 m to the lowest point of the track. A constant frictional force does 2.0 &times; "
 "10<sup>4</sup> J of work during the descent."
 "<ol class='parts'>"
 "<li>Calculate the speed of the car at the lowest point.</li></ol>",
 6,
 "Energy: &frac12;mv&sup2; = &frac12;mu&sup2; + mgh &minus; W<sub>f</sub>.<br>"
 "&frac12;(500)v&sup2; = &frac12;(500)(8.0)&sup2; + 500(9.81)(18) &minus; 2.0&times;10<sup>4</sup> "
 "= 1.60&times;10<sup>4</sup> + 8.83&times;10<sup>4</sup> &minus; 2.0&times;10<sup>4</sup> = "
 "8.43&times;10<sup>4</sup> J. v&sup2; = 2(8.43&times;10<sup>4</sup>)/500 = 337 &rArr; v = "
 "<b>18.4 m s<sup>&minus;1</sup></b>.")

add(T5,
 "Derive the formula for kinetic energy <span class='eq'>E<sub>K</sub> = &frac12;mv&sup2;</span> "
 "starting from a constant resultant force F accelerating a mass m from rest to speed v."
 "<ol class='parts'>"
 "<li>Give the derivation using an equation of motion and the definition of work.</li>"
 "<li>State the assumption about the force.</li></ol>",
 6,
 "<b>(a)</b> Work done by F over distance s is W = Fs = (ma)s. From v&sup2; = u&sup2; + 2as with "
 "u = 0: as = v&sup2;/2. So W = m(as) = m(v&sup2;/2) = <b>&frac12;mv&sup2;</b>, which is the kinetic "
 "energy gained.<br>"
 "<b>(b)</b> The resultant force (and hence acceleration) is assumed constant, and all the work goes "
 "into kinetic energy.")

add(T5,
 "A wind turbine converts the kinetic energy of moving air into electrical energy. Air of density "
 "1.2 kg m<sup>&minus;3</sup> moves at 9.0 m s<sup>&minus;1</sup> towards blades that sweep out an "
 "area of 1400 m&sup2;."
 "<ol class='parts'>"
 "<li>Calculate the mass of air passing through the swept area each second.</li>"
 "<li>Calculate the maximum power available from this air.</li></ol>",
 7,
 "<b>(a)</b> m/t = &rho;Av = 1.2 &times; 1400 &times; 9.0 = <b>1.51 &times; 10<sup>4</sup> "
 "kg s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> P = &frac12;(m/t)v&sup2; = &frac12;(1.51&times;10<sup>4</sup>)(9.0)&sup2; = "
 "&frac12;(1.51&times;10<sup>4</sup>)(81) = <b>6.1 &times; 10<sup>5</sup> W</b>.")

add(T5,
 "A 60 kg athlete runs up a flight of stairs of total vertical height 5.0 m in 4.2 s."
 "<ol class='parts'>"
 "<li>Calculate the useful power developed against gravity.</li>"
 "<li>Explain why the athlete&#39;s total metabolic power output is considerably greater than this "
 "value.</li></ol>",
 5,
 "<b>(a)</b> P = mgh/t = 60 &times; 9.81 &times; 5.0/4.2 = 2943/4.2 = <b>701 W</b>.<br>"
 "<b>(b)</b> Much energy is also used to accelerate limbs, overcome internal friction, and is lost as "
 "heat in the muscles; the human body is only partly efficient, so the metabolic (chemical) power "
 "input far exceeds the useful mechanical power against gravity.")

add(T5,
 "A car of mass 1000 kg has a maximum useful engine power of 42 kW. It travels up a slope inclined at "
 "5.0&deg; to the horizontal against a constant resistive force of 600 N."
 "<ol class='parts'>"
 "<li>Calculate the maximum steady speed the car can maintain up the slope.</li></ol>",
 6,
 "At maximum steady speed the driving force F = total opposing force = mg sin5.0&deg; + 600 = "
 "1000(9.81)(0.0872) + 600 = 855 + 600 = 1455 N.<br>"
 "P = Fv &rArr; v = P/F = 42000/1455 = <b>28.9 m s<sup>&minus;1</sup></b>.")

add(T5,
 "A ball of mass 0.20 kg is dropped onto a spring of force constant 800 N m<sup>&minus;1</sup> from a "
 "height of 1.2 m above the top of the spring. Assume no energy is lost."
 "<ol class='parts'>"
 "<li>Calculate the speed of the ball as it first touches the spring.</li>"
 "<li>By equating energy, estimate the maximum compression of the spring (you may neglect the small "
 "extra fall during compression).</li></ol>",
 7,
 "<b>(a)</b> v = &radic;(2gh) = &radic;(2 &times; 9.81 &times; 1.2) = <b>4.85 m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Neglecting the extra fall, the ball&#39;s energy on reaching the spring = mgh = "
 "0.20&times;9.81&times;1.2 = 2.35 J stored as &frac12;kx&sup2;: x = &radic;(2E/k) = "
 "&radic;(2&times;2.35/800) = &radic;(5.88&times;10<sup>&minus;3</sup>) = "
 "<b>7.7 &times; 10<sup>&minus;2</sup> m</b> (about 7.7 cm).")

# ===========================================================================
# TOPIC 6  Deformation of solids
# ===========================================================================
add(T6,
 "A steel wire of natural length 2.5 m and diameter 0.80 mm is stretched by a force of 65 N. The "
 "Young modulus of steel is 2.0 &times; 10<sup>11</sup> Pa."
 "<ol class='parts'>"
 "<li>Calculate the stress in the wire.</li>"
 "<li>Calculate the extension produced.</li></ol>",
 7,
 "A = &pi;(0.40&times;10<sup>&minus;3</sup>)&sup2; = 5.03&times;10<sup>&minus;7</sup> m&sup2;.<br>"
 "<b>(a)</b> Stress = F/A = 65/5.03&times;10<sup>&minus;7</sup> = <b>1.29 &times; 10<sup>8</sup> Pa</b>.<br>"
 "<b>(b)</b> Strain = stress/E = 1.29&times;10<sup>8</sup>/2.0&times;10<sup>11</sup> = "
 "6.46&times;10<sup>&minus;4</sup>. Extension = strain &times; L = 6.46&times;10<sup>&minus;4</sup> "
 "&times; 2.5 = <b>1.6 &times; 10<sup>&minus;3</sup> m</b> (1.6 mm).")

add(T6,
 "Describe an experiment to determine the Young modulus of a metal in the form of a long wire."
 "<ol class='parts'>"
 "<li>State the measurements taken and the instrument used for each.</li>"
 "<li>Explain how a graph is used to obtain the Young modulus, and why a long thin wire is used.</li></ol>",
 7,
 "<b>(a)</b> Measure the original length L (metre rule / tape), the diameter d at several points "
 "(micrometer) to find A = &pi;d&sup2;/4, the added load F (known masses &times; g), and the "
 "extension e for each load (marker + travelling microscope or a Vernier scale).<br>"
 "<b>(b)</b> Plot F against e: within the limit of proportionality this is a straight line of "
 "gradient F/e. Since E = (F/e)(L/A), E = gradient &times; L/A. A long thin wire gives a larger, more "
 "easily measured extension (e = FL/AE), reducing the percentage uncertainty.")

add(T6,
 "A copper wire and a steel wire have the same length and the same diameter and are joined end to end "
 "so they hang vertically in series, supporting a load of 40 N. E<sub>copper</sub> = 1.2 &times; "
 "10<sup>11</sup> Pa, E<sub>steel</sub> = 2.0 &times; 10<sup>11</sup> Pa."
 "<ol class='parts'>"
 "<li>Explain why the two wires experience the same stress but different strains.</li>"
 "<li>Find the ratio of the extension of the copper wire to that of the steel wire.</li></ol>",
 7,
 "<b>(a)</b> In series each wire carries the same tension (40 N) and has the same area, so stress "
 "(= F/A) is equal. Since strain = stress/E and E differs, the strains differ (copper strains more "
 "because its E is smaller).<br>"
 "<b>(b)</b> Same length and stress: e = (stress/E)L, so e &prop; 1/E. "
 "e<sub>Cu</sub>/e<sub>steel</sub> = E<sub>steel</sub>/E<sub>Cu</sub> = 2.0/1.2 = <b>1.7</b>.")

add(T6,
 "A spring obeys Hooke&#39;s law and extends by 4.0 cm when a force of 5.0 N is applied."
 "<ol class='parts'>"
 "<li>Calculate the spring constant.</li>"
 "<li>Calculate the elastic potential energy stored at this extension.</li>"
 "<li>Calculate the extra energy needed to stretch it a further 2.0 cm.</li></ol>",
 7,
 "<b>(a)</b> k = F/x = 5.0/0.040 = <b>125 N m<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> E = &frac12;kx&sup2; = &frac12;(125)(0.040)&sup2; = <b>0.10 J</b>.<br>"
 "<b>(c)</b> At 6.0 cm: E&#39; = &frac12;(125)(0.060)&sup2; = 0.225 J. Extra = 0.225 &minus; 0.10 = "
 "<b>0.13 J</b> (more than the first because energy &prop; x&sup2;).")

add(T6,
 "Two identical springs, each of spring constant 50 N m<sup>&minus;1</sup>, support a load of 12 N."
 "<ol class='parts'>"
 "<li>Calculate the extension if the springs are connected in parallel (side by side).</li>"
 "<li>Calculate the extension if the springs are connected in series (end to end).</li></ol>",
 6,
 "<b>(a)</b> Parallel: k<sub>eff</sub> = 50 + 50 = 100 N m<sup>&minus;1</sup>. x = F/k = 12/100 = "
 "<b>0.12 m</b>.<br>"
 "<b>(b)</b> Series: 1/k<sub>eff</sub> = 1/50 + 1/50 &rArr; k<sub>eff</sub> = 25 N m<sup>&minus;1</sup>. "
 "x = 12/25 = <b>0.48 m</b>.")

add(T6,
 "The force&ndash;extension graph for a metal wire is a straight line from the origin up to a force "
 "of 30 N at an extension of 1.5 mm (the limit of proportionality), after which it curves and the "
 "wire eventually breaks at an extension of 6.0 mm."
 "<ol class='parts'>"
 "<li>Calculate the spring constant (stiffness) of the wire in its linear region.</li>"
 "<li>Calculate the elastic potential energy stored at the limit of proportionality.</li>"
 "<li>State whether the deformation at 6.0 mm is elastic or plastic, with a reason.</li></ol>",
 7,
 "<b>(a)</b> k = F/x = 30/1.5&times;10<sup>&minus;3</sup> = <b>2.0 &times; 10<sup>4</sup> "
 "N m<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> E = &frac12;Fx = &frac12;(30)(1.5&times;10<sup>&minus;3</sup>) = "
 "<b>2.25 &times; 10<sup>&minus;2</sup> J</b>.<br>"
 "<b>(c)</b> <b>Plastic</b>: 6.0 mm is well beyond the elastic limit, so the wire would not return to "
 "its original length if unloaded (permanent deformation).")

add(T6,
 "Define stress, strain and the Young modulus, and state the unit of each."
 "<ol class='parts'>"
 "<li>Give the three definitions and units.</li>"
 "<li>Explain why strain has no unit.</li></ol>",
 6,
 "<b>(a)</b> Stress = force per unit cross-sectional area (F/A), unit Pa (N m<sup>&minus;2</sup>). "
 "Strain = extension per unit original length (e/L), no unit. Young modulus E = stress/strain, unit "
 "Pa.<br>"
 "<b>(b)</b> Strain is a ratio of two lengths (extension &divide; original length), so the units "
 "cancel and it is a pure number.")

add(T6,
 "A nylon rope of cross-sectional area 1.2 &times; 10<sup>&minus;4</sup> m&sup2; and Young modulus "
 "3.0 &times; 10<sup>9</sup> Pa hangs vertically with length 20 m. A climber of weight 700 N hangs "
 "from its lower end."
 "<ol class='parts'>"
 "<li>Calculate the stress in the rope.</li>"
 "<li>Calculate the extension of the rope.</li></ol>",
 6,
 "<b>(a)</b> Stress = F/A = 700/1.2&times;10<sup>&minus;4</sup> = <b>5.8 &times; 10<sup>6</sup> Pa</b>.<br>"
 "<b>(b)</b> Strain = stress/E = 5.83&times;10<sup>6</sup>/3.0&times;10<sup>9</sup> = "
 "1.94&times;10<sup>&minus;3</sup>. Extension = strain &times; L = 1.94&times;10<sup>&minus;3</sup> "
 "&times; 20 = <b>3.9 &times; 10<sup>&minus;2</sup> m</b> (3.9 cm).")

add(T6,
 "Distinguish between elastic and plastic deformation, and explain the meaning of the elastic limit."
 "<ol class='parts'>"
 "<li>Give the distinction and define the elastic limit.</li>"
 "<li>State what is meant by the limit of proportionality and how it relates to Hooke&#39;s law.</li></ol>",
 6,
 "<b>(a)</b> Elastic deformation: the material returns to its original shape/size when the load is "
 "removed. Plastic deformation: the material keeps a permanent change of shape after unloading. The "
 "<b>elastic limit</b> is the maximum load (or stress) beyond which the deformation becomes "
 "permanent (plastic).<br>"
 "<b>(b)</b> The limit of proportionality is the point up to which extension is proportional to load "
 "(the force&ndash;extension graph is a straight line); Hooke&#39;s law (F = kx) holds only up to "
 "this point.")

add(T6,
 "A stress&ndash;strain graph is plotted for a ductile metal. It rises linearly, then reaches a peak "
 "(the ultimate tensile stress) before the metal necks and fractures."
 "<ol class='parts'>"
 "<li>Explain what happens to the specimen physically after the peak of the graph.</li>"
 "<li>State what the area under a stress&ndash;strain graph, up to fracture, represents.</li></ol>",
 5,
 "<b>(a)</b> Beyond the peak the metal undergoes plastic flow: a narrow region &#39;necks&#39; "
 "(reduces in cross-section), so the stress needed appears to fall until the specimen fractures "
 "there.<br>"
 "<b>(b)</b> The area under the stress&ndash;strain graph represents the <b>energy per unit volume</b> "
 "(work done per unit volume) needed to stretch the material &mdash; a measure of its toughness.")

add(T6,
 "A load is applied to a wire and then removed. The loading and unloading lines on a "
 "force&ndash;extension graph do not coincide, and the unloading line returns to a non-zero "
 "extension."
 "<ol class='parts'>"
 "<li>Explain what this tells you about how the wire was loaded.</li>"
 "<li>State what the area between the loading and unloading lines represents.</li></ol>",
 5,
 "<b>(a)</b> The wire was loaded <b>beyond its elastic limit</b>, so it deformed plastically and did "
 "not return to its original length &mdash; hence the permanent (non-zero) extension on unloading.<br>"
 "<b>(b)</b> The area enclosed between the loading and unloading curves represents the energy "
 "dissipated (as heat) in permanently deforming the wire.")

add(T6,
 "A vertical steel wire supports a mass. When the mass is 2.0 kg the extension is 0.60 mm; the wire "
 "obeys Hooke&#39;s law over this range."
 "<ol class='parts'>"
 "<li>Calculate the spring constant of the wire.</li>"
 "<li>Predict the extension for a 3.5 kg mass, and state the assumption made.</li></ol>",
 6,
 "<b>(a)</b> Force = 2.0 &times; 9.81 = 19.6 N. k = F/x = 19.6/0.60&times;10<sup>&minus;3</sup> = "
 "<b>3.27 &times; 10<sup>4</sup> N m<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> Force = 3.5 &times; 9.81 = 34.3 N. x = F/k = 34.3/3.27&times;10<sup>4</sup> = "
 "<b>1.05 &times; 10<sup>&minus;3</sup> m</b> (1.05 mm). Assumption: the wire still obeys Hooke&#39;s "
 "law (load within the limit of proportionality).")

# ===========================================================================
# TOPIC 7  Waves
# ===========================================================================
add(T7,
 "A progressive sound wave of frequency 256 Hz travels through air at 340 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the wavelength.</li>"
 "<li>Calculate the phase difference, in radians, between two points 0.44 m apart along the "
 "direction of travel.</li></ol>",
 7,
 "<b>(a)</b> &lambda; = v/f = 340/256 = <b>1.33 m</b>.<br>"
 "<b>(b)</b> Phase difference = (&Delta;x/&lambda;) &times; 2&pi; = (0.44/1.328) &times; 2&pi; = "
 "0.331 &times; 2&pi; = <b>2.1 rad</b> (about 0.66&pi;).")

add(T7,
 "A cathode-ray oscilloscope (CRO) displays the waveform of a sound. The time-base is set to "
 "2.0 ms per division and the trace shows one complete cycle across 4.0 divisions. The y-gain is "
 "0.50 V per division and the trace has a peak height of 3.0 divisions from the centre line."
 "<ol class='parts'>"
 "<li>Calculate the frequency of the sound.</li>"
 "<li>State the peak voltage of the signal.</li></ol>",
 7,
 "<b>(a)</b> Period T = 4.0 &times; 2.0&times;10<sup>&minus;3</sup> = 8.0&times;10<sup>&minus;3</sup> s. "
 "f = 1/T = 1/8.0&times;10<sup>&minus;3</sup> = <b>125 Hz</b>.<br>"
 "<b>(b)</b> Peak voltage = 3.0 &times; 0.50 = <b>1.5 V</b>.")

add(T7,
 "A point source emits sound uniformly in all directions with a power of 1.6 W."
 "<ol class='parts'>"
 "<li>Calculate the intensity of the sound at a distance of 4.0 m from the source.</li>"
 "<li>State how the amplitude of the wave at 8.0 m compares with that at 4.0 m, justifying your "
 "answer.</li></ol>",
 7,
 "<b>(a)</b> I = P/(4&pi;r&sup2;) = 1.6/(4&pi; &times; 4.0&sup2;) = 1.6/201 = "
 "<b>8.0 &times; 10<sup>&minus;3</sup> W m<sup>&minus;2</sup></b>.<br>"
 "<b>(b)</b> Doubling r to 8.0 m reduces I by a factor 4 (inverse-square). Since I &prop; "
 "amplitude&sup2;, the amplitude falls by a factor &radic;4 = 2, i.e. to <b>half</b> its value at "
 "4.0 m.")

add(T7,
 "Compare transverse and longitudinal waves."
 "<ol class='parts'>"
 "<li>State the difference in terms of the direction of oscillation relative to the direction of "
 "energy transfer, giving one example of each.</li>"
 "<li>State which type can be polarised, and why.</li></ol>",
 6,
 "<b>(a)</b> In a transverse wave the oscillations are perpendicular to the direction of energy "
 "travel (e.g. electromagnetic waves, waves on a string); in a longitudinal wave the oscillations "
 "are parallel to the direction of travel, producing compressions and rarefactions (e.g. sound).<br>"
 "<b>(b)</b> Only <b>transverse</b> waves can be polarised, because polarisation restricts "
 "oscillations to a single plane &mdash; this is only possible when the oscillation is perpendicular "
 "to the direction of travel (longitudinal oscillations are already along one axis).")

add(T7,
 "A source of sound emits a note of frequency 480 Hz. It moves directly towards a stationary "
 "observer at 30 m s<sup>&minus;1</sup>. The speed of sound in air is 340 m s<sup>&minus;1</sup>."
 "<ol class='parts'>"
 "<li>Calculate the frequency heard by the observer.</li>"
 "<li>State and explain qualitatively what the observer hears just after the source passes.</li></ol>",
 7,
 "<b>(a)</b> Approaching: f<sub>o</sub> = f<sub>s</sub>v/(v &minus; v<sub>s</sub>) = "
 "480 &times; 340/(340 &minus; 30) = 480 &times; 340/310 = <b>527 Hz</b>.<br>"
 "<b>(b)</b> After passing, the source recedes, so f<sub>o</sub> = f<sub>s</sub>v/(v + v<sub>s</sub>) "
 "= 480 &times; 340/370 = 441 Hz &mdash; the pitch drops suddenly to a lower, steady value.")

add(T7,
 "Light is plane-polarised by passing through a polarising filter. It then passes through a second "
 "filter (analyser) whose transmission axis is at 30&deg; to that of the first."
 "<ol class='parts'>"
 "<li>State Malus&#39;s law and use it to find the fraction of the intensity transmitted by the "
 "second filter.</li>"
 "<li>The analyser is now rotated to 90&deg;. State the transmitted intensity and explain.</li></ol>",
 6,
 "<b>(a)</b> Malus: I = I<sub>0</sub>cos&sup2;&theta;, where &theta; is the angle between the "
 "polarisation direction and the analyser axis. Fraction = cos&sup2;30&deg; = (0.866)&sup2; = "
 "<b>0.75</b> (75%).<br>"
 "<b>(b)</b> At 90&deg;, cos&sup2;90&deg; = 0, so <b>no light</b> is transmitted &mdash; the "
 "filters are &#39;crossed&#39; and the transmitted electric-field component is zero.")

add(T7,
 "State the approximate range of wavelengths in free space for the principal regions of the "
 "electromagnetic spectrum."
 "<ol class='parts'>"
 "<li>List, in order of increasing wavelength, the regions from &gamma;-rays to radio waves with an "
 "approximate wavelength for each.</li>"
 "<li>State what all electromagnetic waves have in common in free space, and the range visible to "
 "the eye.</li></ol>",
 7,
 "<b>(a)</b> &gamma;-rays (&lt; 10<sup>&minus;11</sup> m); X-rays (10<sup>&minus;11</sup>&ndash;"
 "10<sup>&minus;9</sup> m); ultraviolet (10<sup>&minus;9</sup>&ndash;4&times;10<sup>&minus;7</sup> m); "
 "visible (4&ndash;7 &times; 10<sup>&minus;7</sup> m); infrared (7&times;10<sup>&minus;7</sup>&ndash;"
 "10<sup>&minus;3</sup> m); microwaves (10<sup>&minus;3</sup>&ndash;10<sup>&minus;1</sup> m); "
 "radio waves (&gt; 10<sup>&minus;1</sup> m).<br>"
 "<b>(b)</b> All are transverse and travel at the same speed c = 3.0&times;10<sup>8</sup> "
 "m s<sup>&minus;1</sup> in free space; the eye sees <b>400&ndash;700 nm</b>.")

add(T7,
 "A wave travelling along a string is described by a displacement&ndash;time graph for one particle "
 "showing simple harmonic oscillation of amplitude 5.0 mm and period 0.40 s."
 "<ol class='parts'>"
 "<li>State the frequency of the wave.</li>"
 "<li>If the wave speed is 12 m s<sup>&minus;1</sup>, calculate the wavelength.</li>"
 "<li>Explain the difference between the displacement&ndash;time graph for one particle and a "
 "displacement&ndash;position graph of the whole wave at one instant.</li></ol>",
 7,
 "<b>(a)</b> f = 1/T = 1/0.40 = <b>2.5 Hz</b>.<br>"
 "<b>(b)</b> &lambda; = v/f = 12/2.5 = <b>4.8 m</b>.<br>"
 "<b>(c)</b> A displacement&ndash;time graph shows how one particle&#39;s displacement varies with "
 "time (period T on the axis); a displacement&ndash;position graph is a snapshot of all particles at "
 "one instant (wavelength &lambda; on the axis). They can look similar but the axes represent "
 "different quantities.")

add(T7,
 "Unpolarised light of intensity I<sub>0</sub> passes through two polarising filters whose axes are "
 "parallel."
 "<ol class='parts'>"
 "<li>State the intensity transmitted after the first filter (in terms of I<sub>0</sub>).</li>"
 "<li>A third filter is inserted between them with its axis at 45&deg; to both. Find the final "
 "intensity in terms of I<sub>0</sub>.</li></ol>",
 7,
 "<b>(a)</b> An ideal polariser transmits half of unpolarised light: <b>I<sub>0</sub>/2</b> "
 "(now plane-polarised along the first axis).<br>"
 "<b>(b)</b> After the middle filter (at 45&deg;): (I<sub>0</sub>/2)cos&sup2;45&deg; = "
 "(I<sub>0</sub>/2)(0.5) = I<sub>0</sub>/4. After the last filter (at 45&deg; to the middle one): "
 "(I<sub>0</sub>/4)cos&sup2;45&deg; = <b>I<sub>0</sub>/8</b>. (Inserting a filter lets light through "
 "a previously crossed pair.)")

add(T7,
 "Explain what is meant by the statement that a progressive wave transfers energy."
 "<ol class='parts'>"
 "<li>Describe, for a wave on the surface of water, what is transferred and what is not.</li>"
 "<li>State how the intensity of a progressive wave depends on its amplitude.</li></ol>",
 5,
 "<b>(a)</b> The wave transfers energy through the medium in the direction of travel, but the water "
 "particles themselves only oscillate about fixed mean positions &mdash; there is no net transfer of "
 "matter (a floating object bobs up and down but does not travel with the wave).<br>"
 "<b>(b)</b> Intensity is proportional to the square of the amplitude (I &prop; A&sup2;).")

add(T7,
 "A sound source and a stationary observer are used to demonstrate the Doppler effect. The observed "
 "frequency is 1.10 times the source frequency."
 "<ol class='parts'>"
 "<li>State whether the source is approaching or receding, and explain.</li>"
 "<li>Calculate the speed of the source (speed of sound = 340 m s<sup>&minus;1</sup>).</li></ol>",
 6,
 "<b>(a)</b> Observed frequency is higher than the source frequency, so the source is "
 "<b>approaching</b> (the wavefronts are compressed in front of a moving source).<br>"
 "<b>(b)</b> f<sub>o</sub> = f<sub>s</sub>v/(v &minus; v<sub>s</sub>) &rArr; 1.10 = 340/(340 &minus; "
 "v<sub>s</sub>) &rArr; 340 &minus; v<sub>s</sub> = 340/1.10 = 309 &rArr; v<sub>s</sub> = <b>31 m "
 "s<sup>&minus;1</sup></b>.")

add(T7,
 "State what is meant by the polarisation of a wave, and describe how a polarising filter affects "
 "unpolarised light passing through it."
 "<ol class='parts'>"
 "<li>Define polarisation.</li>"
 "<li>Describe an everyday application of polarising filters and the physics behind it.</li></ol>",
 6,
 "<b>(a)</b> Polarisation is the restriction of the oscillations of a transverse wave to a single "
 "plane containing the direction of travel. A polarising filter transmits only the component of the "
 "electric field parallel to its transmission axis, so emerging light is plane-polarised (and about "
 "half the intensity for unpolarised input).<br>"
 "<b>(b)</b> Polarising sunglasses reduce glare: light reflected from horizontal surfaces (water, "
 "roads) is partially horizontally polarised, and the glasses&#39; vertical axis blocks this "
 "component, cutting the reflected glare.")

# ===========================================================================
# TOPIC 8  Superposition
# ===========================================================================
add(T8,
 "In a double-slit experiment, coherent light of wavelength 590 nm passes through two slits "
 "separated by 0.45 mm. Fringes are observed on a screen 2.2 m from the slits."
 "<ol class='parts'>"
 "<li>Calculate the separation of adjacent bright fringes.</li>"
 "<li>State and explain what happens to the fringe separation if the slit separation is increased.</li></ol>",
 7,
 "<b>(a)</b> x = &lambda;D/a = (590&times;10<sup>&minus;9</sup> &times; 2.2)/0.45&times;10<sup>&minus;3</sup> "
 "= 1.298&times;10<sup>&minus;6</sup>/4.5&times;10<sup>&minus;4</sup> = <b>2.9 &times; 10<sup>&minus;3</sup> m</b> "
 "(2.9 mm).<br>"
 "<b>(b)</b> Since x = &lambda;D/a, increasing a <b>decreases</b> x &mdash; the fringes move closer "
 "together.")

add(T8,
 "Explain what is meant by the terms coherence and interference, and state the conditions needed to "
 "observe a stable two-source interference pattern with light."
 "<ol class='parts'>"
 "<li>Define coherence and interference.</li>"
 "<li>List the conditions for observable, stable fringes.</li></ol>",
 6,
 "<b>(a)</b> Two sources are coherent if they have a constant phase difference (and the same "
 "frequency). Interference is the superposition of waves from two (or more) sources to give a "
 "resultant of larger or smaller amplitude (constructive/destructive).<br>"
 "<b>(b)</b> The sources must be coherent (constant phase difference, same frequency), have "
 "approximately equal amplitudes, and (for transverse waves such as light) be polarised in the same "
 "plane; the path difference should be comparable to the wavelength so fringes are resolvable.")

add(T8,
 "A diffraction grating has 500 lines per millimetre. It is illuminated normally by monochromatic "
 "light of wavelength 6.0 &times; 10<sup>&minus;7</sup> m."
 "<ol class='parts'>"
 "<li>Calculate the grating spacing.</li>"
 "<li>Calculate the angle of diffraction of the second-order maximum.</li>"
 "<li>Determine the total number of bright maxima observable.</li></ol>",
 9,
 "<b>(a)</b> d = 1/(500&times;10<sup>3</sup>) = <b>2.0 &times; 10<sup>&minus;6</sup> m</b>.<br>"
 "<b>(b)</b> d sin&theta; = n&lambda;: sin&theta; = 2 &times; 6.0&times;10<sup>&minus;7</sup>/"
 "2.0&times;10<sup>&minus;6</sup> = 0.60 &rArr; &theta; = <b>37&deg;</b>.<br>"
 "<b>(c)</b> Maximum order: n &le; d/&lambda; = 2.0&times;10<sup>&minus;6</sup>/6.0&times;10<sup>&minus;7</sup> "
 "= 3.3 &rArr; n<sub>max</sub> = 3. Orders 0, &plusmn;1, &plusmn;2, &plusmn;3 &rArr; "
 "<b>7 maxima</b>.")

add(T8,
 "A stationary wave is set up on a stretched string of length 1.2 m fixed at both ends. The string "
 "vibrates in its third harmonic (three loops)."
 "<ol class='parts'>"
 "<li>Sketch the shape of the string, marking nodes (N) and antinodes (A).</li>"
 "<li>Calculate the wavelength.</li>"
 "<li>If the wave speed on the string is 240 m s<sup>&minus;1</sup>, calculate the frequency.</li></ol>",
 8,
 "<b>(a)</b> Three loops between the fixed ends: N&ndash;A&ndash;N&ndash;A&ndash;N&ndash;A&ndash;N "
 "(nodes at both ends and at two interior points, antinodes at the centre of each loop).<br>"
 "<b>(b)</b> Three half-wavelengths fit the string: 3(&lambda;/2) = 1.2 &rArr; &lambda; = <b>0.80 m</b>.<br>"
 "<b>(c)</b> f = v/&lambda; = 240/0.80 = <b>300 Hz</b>.",
 "<svg width='240' height='70' viewBox='0 0 240 70'>"
 "<line x1='20' y1='35' x2='220' y2='35' stroke='#bbb' stroke-dasharray='3 3'/>"
 "<path d='M20 35 Q53 10 86 35 Q120 60 153 35 Q186 10 220 35' fill='none' stroke='#06c' stroke-width='2'/>"
 "<path d='M20 35 Q53 60 86 35 Q120 10 153 35 Q186 60 220 35' fill='none' stroke='#06c' stroke-width='1' stroke-dasharray='3 2'/>"
 "<text x='16' y='48' font-size='8'>N</text><text x='82' y='48' font-size='8'>N</text>"
 "<text x='149' y='48' font-size='8'>N</text><text x='216' y='48' font-size='8'>N</text>"
 "<text x='48' y='8' font-size='8'>A</text></svg>")

add(T8,
 "A tube closed at one end and open at the other has a length of 0.60 m. The speed of sound in air is "
 "340 m s<sup>&minus;1</sup>. (Neglect end corrections.)"
 "<ol class='parts'>"
 "<li>Sketch the displacement pattern of the fundamental and state where the node and antinode are.</li>"
 "<li>Calculate the fundamental frequency.</li>"
 "<li>State the frequency of the next possible harmonic.</li></ol>",
 8,
 "<b>(a)</b> A closed&ndash;open tube has a displacement <b>node at the closed end</b> and an "
 "<b>antinode at the open end</b>; the fundamental fits a quarter-wavelength.<br>"
 "<b>(b)</b> L = &lambda;/4 &rArr; &lambda; = 4L = 2.4 m. f<sub>1</sub> = v/&lambda; = 340/2.4 = "
 "<b>142 Hz</b>.<br>"
 "<b>(c)</b> A closed tube supports only odd harmonics, so the next is the third harmonic: "
 "3 &times; 142 = <b>425 Hz</b>.")

add(T8,
 "Microwaves from a source are directed at a metal plate, and a probe detector is moved along the "
 "line between the source and plate. The detector signal rises and falls, with minima 15 mm apart."
 "<ol class='parts'>"
 "<li>Explain why a stationary wave is formed in this region.</li>"
 "<li>Calculate the wavelength and hence the frequency of the microwaves.</li></ol>",
 7,
 "<b>(a)</b> The incident microwaves reflect from the metal plate; the reflected wave superposes on "
 "the incident wave (same frequency, travelling in opposite directions), producing a stationary wave "
 "with fixed nodes and antinodes.<br>"
 "<b>(b)</b> Adjacent minima (nodes) are half a wavelength apart, so &lambda; = 2 &times; 15 = 30 mm "
 "= 0.030 m. f = c/&lambda; = 3.0&times;10<sup>8</sup>/0.030 = <b>1.0 &times; 10<sup>10</sup> Hz</b>.")

add(T8,
 "Explain, using the principle of superposition, how a stationary wave differs from a progressive "
 "wave."
 "<ol class='parts'>"
 "<li>State the principle of superposition.</li>"
 "<li>Give two differences between a stationary wave and a progressive wave (energy and amplitude).</li></ol>",
 6,
 "<b>(a)</b> When two or more waves meet at a point, the resultant displacement equals the vector sum "
 "of the individual displacements at that point.<br>"
 "<b>(b)</b> (i) A progressive wave transfers energy along its direction of travel; a stationary "
 "wave stores energy and transfers none along the wave. (ii) In a progressive wave every point has "
 "the same amplitude; in a stationary wave the amplitude varies with position from zero at nodes to "
 "a maximum at antinodes. (Also: all points between adjacent nodes oscillate in phase in a "
 "stationary wave.)")

add(T8,
 "Light of wavelength 480 nm illuminates a double slit, giving fringes of separation 1.8 mm on a "
 "screen 1.5 m away."
 "<ol class='parts'>"
 "<li>Calculate the slit separation.</li>"
 "<li>The blue light is replaced by red light of wavelength 660 nm. Calculate the new fringe "
 "separation.</li></ol>",
 7,
 "<b>(a)</b> a = &lambda;D/x = (480&times;10<sup>&minus;9</sup> &times; 1.5)/1.8&times;10<sup>&minus;3</sup> "
 "= 7.2&times;10<sup>&minus;7</sup>/1.8&times;10<sup>&minus;3</sup> = <b>4.0 &times; 10<sup>&minus;4</sup> m</b> "
 "(0.40 mm).<br>"
 "<b>(b)</b> x &prop; &lambda; (same a, D): x&#39; = 1.8 &times; 660/480 = <b>2.5 mm</b>.")

add(T8,
 "Explain the meaning of diffraction, and describe an experiment using a ripple tank to show how the "
 "amount of diffraction depends on the gap width compared with the wavelength."
 "<ol class='parts'>"
 "<li>Define diffraction.</li>"
 "<li>Describe the observations for a gap much wider than, and a gap comparable to, the wavelength.</li></ol>",
 6,
 "<b>(a)</b> Diffraction is the spreading of a wave as it passes through a gap or around an "
 "obstacle.<br>"
 "<b>(b)</b> In a ripple tank, straight water waves pass through a gap between two barriers. When the "
 "gap is much wider than the wavelength, the waves pass through nearly straight with only slight "
 "spreading at the edges; when the gap is about the same size as the wavelength, the waves spread out "
 "in strong semicircular arcs beyond the gap.")

add(T8,
 "Describe how a diffraction grating can be used to determine the wavelength of monochromatic light."
 "<ol class='parts'>"
 "<li>State the apparatus and measurements taken.</li>"
 "<li>State the equation used and how the wavelength is calculated.</li></ol>",
 6,
 "<b>(a)</b> Direct a narrow beam of the monochromatic light normally at a grating of known spacing "
 "d (from lines per metre). Measure the angle &theta; of a diffracted order (e.g. first order) using "
 "a rotating table/protractor, ideally measuring the angle to the order on both sides and halving to "
 "reduce error.<br>"
 "<b>(b)</b> Use d sin&theta; = n&lambda;, so &lambda; = d sin&theta;/n. Repeating for several "
 "orders and averaging improves reliability.")

add(T8,
 "Two coherent loudspeakers face an area and produce sound of the same frequency in phase. A listener "
 "walking across the area hears alternating loud and quiet regions."
 "<ol class='parts'>"
 "<li>Explain, in terms of path difference, why loud and quiet regions occur.</li>"
 "<li>State the path difference (in terms of wavelength &lambda;) at a point of minimum loudness.</li></ol>",
 6,
 "<b>(a)</b> Sound from the two speakers travels different distances to a given point. Where the path "
 "difference is a whole number of wavelengths the waves arrive in phase and interfere "
 "constructively (loud); where it is an odd number of half-wavelengths they arrive out of phase and "
 "interfere destructively (quiet).<br>"
 "<b>(b)</b> Minimum loudness (destructive): path difference = (n + &frac12;)&lambda;, i.e. "
 "&frac12;&lambda;, 3&frac12;... &lambda; &mdash; an odd number of half-wavelengths.")

add(T8,
 "A grating spectrum is produced when white light passes through a diffraction grating."
 "<ol class='parts'>"
 "<li>Explain why the central (zero-order) image is white but the higher orders are spectra.</li>"
 "<li>State which colour is diffracted through the largest angle in a given order, with a reason.</li></ol>",
 6,
 "<b>(a)</b> At the zero order (n = 0) the path difference is zero for all wavelengths, so all "
 "colours arrive in phase and overlap to give white. For n &ge; 1, the diffraction angle depends on "
 "&lambda; (d sin&theta; = n&lambda;), so different colours emerge at different angles and separate "
 "into a spectrum.<br>"
 "<b>(b)</b> <b>Red</b> is diffracted most in each order, because it has the longest wavelength and "
 "sin&theta; &prop; &lambda;.")
