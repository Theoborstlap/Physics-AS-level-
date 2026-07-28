# -*- coding: utf-8 -*-
"""PACK 2 - Structured (theory) questions, topics 9-11. AS 9702."""
from engine import theory as T

T9 = "9&nbsp;&nbsp;Electricity"
T10 = "10&nbsp;&nbsp;D.C. circuits"
T11 = "11&nbsp;&nbsp;Particle physics"


def add(topic, q, marks, ans, svg=""):
    T.append({"topic": topic, "q": q, "marks": marks, "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 9  Electricity
# ===========================================================================
add(T9,
 "A copper wire carries a current of 3.5 A. The wire has a cross-sectional area of 1.5 &times; "
 "10<sup>&minus;6</sup> m&sup2; and the number density of free electrons is 8.5 &times; "
 "10<sup>28</sup> m<sup>&minus;3</sup>."
 "<ol class='parts'>"
 "<li>Calculate the mean drift velocity of the electrons.</li>"
 "<li>Comment on the size of your answer and explain how a lamp can light almost instantly.</li></ol>",
 7,
 "<b>(a)</b> v = I/(nAq) = 3.5/(8.5&times;10<sup>28</sup> &times; 1.5&times;10<sup>&minus;6</sup> &times; "
 "1.60&times;10<sup>&minus;19</sup>) = 3.5/2.04&times;10<sup>4</sup> = "
 "<b>1.7 &times; 10<sup>&minus;4</sup> m s<sup>&minus;1</sup></b>.<br>"
 "<b>(b)</b> The drift speed is tiny (&lt; 1 mm s<sup>&minus;1</sup>). A lamp lights almost at once "
 "because the electric field is set up along the wire at close to the speed of light, so free "
 "electrons everywhere &mdash; including in the lamp &mdash; begin to drift almost simultaneously.")

add(T9,
 "A charge of 90 C passes through a lamp in 1.0 minute. The lamp is connected to a 12 V supply."
 "<ol class='parts'>"
 "<li>Calculate the current in the lamp.</li>"
 "<li>Calculate the power dissipated and the energy transferred in this time.</li></ol>",
 7,
 "<b>(a)</b> I = Q/t = 90/60 = <b>1.5 A</b>.<br>"
 "<b>(b)</b> P = VI = 12 &times; 1.5 = <b>18 W</b>. Energy = Pt = 18 &times; 60 = <b>1.08 &times; "
 "10<sup>3</sup> J</b> (equivalently W = QV = 90 &times; 12 = 1080 J).")

add(T9,
 "Define the resistance of a component, and state Ohm&#39;s law."
 "<ol class='parts'>"
 "<li>Give both statements precisely.</li>"
 "<li>A component obeys V = IR with R = 15 &Omega;. Calculate the power dissipated when the current "
 "is 0.40 A, using two different formulae as a check.</li></ol>",
 6,
 "<b>(a)</b> Resistance = potential difference across a component divided by the current through it "
 "(R = V/I). Ohm&#39;s law: the current in a metallic conductor is directly proportional to the "
 "potential difference across it, provided physical conditions (especially temperature) are "
 "constant.<br>"
 "<b>(b)</b> P = I&sup2;R = (0.40)&sup2;(15) = <b>2.4 W</b>. Check: V = IR = 6.0 V, P = VI = "
 "6.0 &times; 0.40 = 2.4 W &#10003;.")

add(T9,
 "A metal wire has resistance 4.0 &Omega;. A second wire of the same material has twice the length "
 "and half the diameter of the first."
 "<ol class='parts'>"
 "<li>Explain how resistance depends on length and cross-sectional area.</li>"
 "<li>Calculate the resistance of the second wire.</li></ol>",
 7,
 "<b>(a)</b> R = &rho;L/A: resistance is proportional to length and inversely proportional to "
 "cross-sectional area.<br>"
 "<b>(b)</b> Twice the length &rArr; &times;2. Half the diameter &rArr; area &times;&frac14; &rArr; "
 "R &times;4. Combined factor = 2 &times; 4 = 8. R = 8 &times; 4.0 = <b>32 &Omega;</b>.")

add(T9,
 "Sketch and describe the I&ndash;V characteristic of a filament lamp."
 "<ol class='parts'>"
 "<li>Describe the shape of the graph.</li>"
 "<li>Explain, in terms of the behaviour of the metal, why the resistance increases as the current "
 "increases.</li></ol>",
 6,
 "<b>(a)</b> The graph is an S-shaped curve through the origin: for small currents it is nearly "
 "straight, but the gradient decreases (the curve bends towards the V-axis) as V and I increase, "
 "showing that V/I (resistance) rises.<br>"
 "<b>(b)</b> A larger current dissipates more power, heating the filament. The higher temperature "
 "makes the metal ions vibrate more, so free electrons collide with them more frequently, impeding "
 "the flow &mdash; hence the resistance increases.")

add(T9,
 "A nichrome wire of length 1.5 m and diameter 0.30 mm has a resistivity of 1.1 &times; "
 "10<sup>&minus;6</sup> &Omega; m."
 "<ol class='parts'>"
 "<li>Calculate the resistance of the wire.</li>"
 "<li>Calculate the power dissipated when a p.d. of 6.0 V is applied across it.</li></ol>",
 7,
 "A = &pi;(0.15&times;10<sup>&minus;3</sup>)&sup2; = 7.07&times;10<sup>&minus;8</sup> m&sup2;.<br>"
 "<b>(a)</b> R = &rho;L/A = (1.1&times;10<sup>&minus;6</sup> &times; 1.5)/7.07&times;10<sup>&minus;8</sup> "
 "= 1.65&times;10<sup>&minus;6</sup>/7.07&times;10<sup>&minus;8</sup> = <b>23 &Omega;</b>.<br>"
 "<b>(b)</b> P = V&sup2;/R = 6.0&sup2;/23.3 = 36/23.3 = <b>1.5 W</b>.")

add(T9,
 "Explain how the resistance of (a) a thermistor and (b) a light-dependent resistor (LDR) changes "
 "with external conditions, and describe one use of each."
 "<ol class='parts'>"
 "<li>State the behaviour of each component.</li>"
 "<li>State a practical use of each.</li></ol>",
 6,
 "<b>(a)</b> A thermistor (negative temperature coefficient) has resistance that <b>decreases as "
 "temperature increases</b>, because more charge carriers are freed. An LDR has resistance that "
 "<b>decreases as light intensity increases</b>, for the same reason (light frees charge carriers).<br>"
 "<b>(b)</b> Thermistor: temperature sensing / thermostat control. LDR: automatic lighting / "
 "light-level switching (e.g. street lamps).")

add(T9,
 "An electric kettle is rated at 2.2 kW, 230 V."
 "<ol class='parts'>"
 "<li>Calculate the operating current and the resistance of the element.</li>"
 "<li>Calculate the time taken to raise the temperature of 0.50 kg of water by 80 K, assuming all "
 "the energy heats the water. (Specific heat capacity of water = 4200 J kg<sup>&minus;1</sup> "
 "K<sup>&minus;1</sup>.)</li></ol>",
 8,
 "<b>(a)</b> I = P/V = 2200/230 = <b>9.6 A</b>. R = V&sup2;/P = 230&sup2;/2200 = <b>24 &Omega;</b>.<br>"
 "<b>(b)</b> Energy needed = mc&Delta;&theta; = 0.50 &times; 4200 &times; 80 = 1.68&times;10<sup>5</sup> J. "
 "t = E/P = 1.68&times;10<sup>5</sup>/2200 = <b>76 s</b>.")

add(T9,
 "Two wires, X and Y, are made of the same material and have the same length. X has twice the "
 "cross-sectional area of Y. They are connected in parallel across a battery."
 "<ol class='parts'>"
 "<li>Compare the resistances of X and Y.</li>"
 "<li>Compare the currents in, and the drift velocities of electrons in, the two wires.</li></ol>",
 7,
 "<b>(a)</b> R = &rho;L/A. Same &rho; and L; X has twice the area, so R<sub>X</sub> = &frac12;R<sub>Y</sub> "
 "(X has half the resistance).<br>"
 "<b>(b)</b> Same p.d. across each (parallel). I = V/R, so I<sub>X</sub> = 2I<sub>Y</sub> (X carries "
 "twice the current). Drift velocity v = I/(nAq): I<sub>X</sub>/A<sub>X</sub> = (2I<sub>Y</sub>)/(2A<sub>Y</sub>) "
 "= I<sub>Y</sub>/A<sub>Y</sub>, so the <b>drift velocities are equal</b>.")

add(T9,
 "Define the potential difference across a component in terms of energy."
 "<ol class='parts'>"
 "<li>Give the definition and the defining equation.</li>"
 "<li>A charge of 25 mC passes through a resistor and transfers 0.30 J of energy to it. Calculate "
 "the p.d. across the resistor.</li></ol>",
 5,
 "<b>(a)</b> The p.d. across a component is the electrical energy transferred to other forms per "
 "unit charge passing through it: V = W/Q.<br>"
 "<b>(b)</b> V = W/Q = 0.30/25&times;10<sup>&minus;3</sup> = <b>12 V</b>.")

add(T9,
 "A student investigates how the resistance of a length of resistance wire varies and obtains a "
 "current of 0.25 A when the p.d. is 5.0 V."
 "<ol class='parts'>"
 "<li>Calculate the resistance.</li>"
 "<li>The temperature of the wire then rises and the current falls to 0.22 A at the same p.d. "
 "Calculate the new resistance and comment on whether the wire is ohmic.</li></ol>",
 6,
 "<b>(a)</b> R = V/I = 5.0/0.25 = <b>20 &Omega;</b>.<br>"
 "<b>(b)</b> R&#39; = 5.0/0.22 = <b>23 &Omega;</b>. The resistance changed when conditions "
 "(temperature) changed, so over this range it is <b>not behaving ohmically</b> &mdash; Ohm&#39;s "
 "law requires constant temperature.")

add(T9,
 "A semiconductor diode is connected in series with a resistor and a variable d.c. supply so that it "
 "is forward biased."
 "<ol class='parts'>"
 "<li>Sketch the I&ndash;V characteristic of the diode for both forward and reverse bias.</li>"
 "<li>Explain the purpose of the series resistor.</li></ol>",
 6,
 "<b>(a)</b> Forward bias: negligible current until about 0.6 V, then the current rises very steeply. "
 "Reverse bias: only a tiny (effectively zero) current for all reverse voltages up to breakdown.<br>"
 "<b>(b)</b> Once conducting, the diode&#39;s resistance is very low, so the current could rise "
 "dangerously; the series resistor limits the current to a safe value and takes the extra p.d.")

add(T9,
 "A 12 V car battery delivers a current of 40 A to a starter motor for 3.0 s."
 "<ol class='parts'>"
 "<li>Calculate the charge delivered and the energy transferred.</li>"
 "<li>The motor is 60% efficient. Calculate the useful mechanical energy output.</li></ol>",
 6,
 "<b>(a)</b> Q = It = 40 &times; 3.0 = <b>120 C</b>. Energy = VIt = 12 &times; 40 &times; 3.0 = "
 "<b>1.44 &times; 10<sup>3</sup> J</b>.<br>"
 "<b>(b)</b> Useful output = 0.60 &times; 1.44&times;10<sup>3</sup> = <b>864 J</b>.")

add(T9,
 "State what is meant by an electric current in terms of charge carriers, and explain what is meant "
 "by saying charge is quantised."
 "<ol class='parts'>"
 "<li>Define electric current and give the quantisation of charge.</li>"
 "<li>A current of 0.16 A flows for 5.0 s. Calculate the number of electrons that pass a point.</li></ol>",
 6,
 "<b>(a)</b> Current is the rate of flow of charge (I = &Delta;Q/&Delta;t). Charge is quantised: it "
 "exists only in whole-number multiples of the elementary charge e = 1.60&times;10<sup>&minus;19</sup> C.<br>"
 "<b>(b)</b> Q = It = 0.16 &times; 5.0 = 0.80 C. Number = Q/e = 0.80/1.60&times;10<sup>&minus;19</sup> = "
 "<b>5.0 &times; 10<sup>18</sup> electrons</b>.")

# ===========================================================================
# TOPIC 10  D.C. circuits
# ===========================================================================
add(T10,
 "A battery of e.m.f. 9.0 V and internal resistance 1.5 &Omega; is connected to an external resistor "
 "of 6.0 &Omega;."
 "<ol class='parts'>"
 "<li>Calculate the current in the circuit.</li>"
 "<li>Calculate the terminal potential difference and the power dissipated inside the battery.</li></ol>",
 7,
 "<b>(a)</b> I = &epsilon;/(R + r) = 9.0/(6.0 + 1.5) = 9.0/7.5 = <b>1.2 A</b>.<br>"
 "<b>(b)</b> Terminal p.d. = IR = 1.2 &times; 6.0 = <b>7.2 V</b> (or &epsilon; &minus; Ir = 9.0 &minus; "
 "1.8). Power in internal resistance = I&sup2;r = (1.2)&sup2;(1.5) = <b>2.2 W</b>.")

add(T10,
 "State Kirchhoff&#39;s first and second laws, and state the conservation principle underlying each."
 "<ol class='parts'>"
 "<li>Give both laws and the corresponding conservation law.</li>"
 "<li>At a junction, currents of 2.0 A and 1.5 A flow in, and currents of 0.80 A and I flow out. "
 "Find I.</li></ol>",
 6,
 "<b>(a)</b> First law: the sum of currents into a junction equals the sum of currents out "
 "(conservation of charge). Second law: around any closed loop, the sum of the e.m.f.s equals the "
 "sum of the p.d.s (conservation of energy).<br>"
 "<b>(b)</b> In = out: 2.0 + 1.5 = 0.80 + I &rArr; I = 3.5 &minus; 0.80 = <b>2.7 A</b>.")

add(T10,
 "Three resistors of 2.0 &Omega;, 3.0 &Omega; and 6.0 &Omega; are available."
 "<ol class='parts'>"
 "<li>Calculate the combined resistance if all three are connected in series.</li>"
 "<li>Calculate the combined resistance if all three are connected in parallel.</li>"
 "<li>Calculate the combined resistance if the 3.0 &Omega; and 6.0 &Omega; are in parallel and this "
 "combination is in series with the 2.0 &Omega;.</li></ol>",
 8,
 "<b>(a)</b> Series: 2.0 + 3.0 + 6.0 = <b>11 &Omega;</b>.<br>"
 "<b>(b)</b> Parallel: 1/R = 1/2.0 + 1/3.0 + 1/6.0 = 0.5 + 0.333 + 0.167 = 1.0 &rArr; R = "
 "<b>1.0 &Omega;</b>.<br>"
 "<b>(c)</b> 3.0 &Omega; ∥ 6.0 &Omega;: 1/R = 1/3.0 + 1/6.0 = 0.5 &rArr; R = 2.0 &Omega;. In series "
 "with 2.0 &Omega;: 2.0 + 2.0 = <b>4.0 &Omega;</b>.")

add(T10,
 "A battery of e.m.f. E and internal resistance r is connected to a variable external resistor R. "
 "When R = 2.0 &Omega; the current is 2.0 A; when R = 5.0 &Omega; the current is 1.0 A."
 "<ol class='parts'>"
 "<li>Write two equations and solve them for E and r.</li>"
 "<li>Calculate the current that would flow if the battery terminals were short-circuited.</li></ol>",
 8,
 "<b>(a)</b> E = I(R + r): 2.0(2.0 + r) = 4.0 + 2.0r; 1.0(5.0 + r) = 5.0 + r. Equating: "
 "4.0 + 2.0r = 5.0 + r &rArr; r = <b>1.0 &Omega;</b>. Then E = 5.0 + 1.0 = <b>6.0 V</b>.<br>"
 "<b>(b)</b> Short circuit (R = 0): I = E/r = 6.0/1.0 = <b>6.0 A</b>.")

add(T10,
 "Distinguish between the electromotive force (e.m.f.) of a source and the potential difference "
 "(p.d.) across its terminals."
 "<ol class='parts'>"
 "<li>Define each in terms of energy per unit charge.</li>"
 "<li>Explain why the terminal p.d. is always less than the e.m.f. when the source supplies current, "
 "and equal to it when no current flows.</li></ol>",
 6,
 "<b>(a)</b> E.m.f. is the electrical energy transferred per unit charge by the source in driving "
 "charge around the whole circuit; terminal p.d. is the energy transferred per unit charge to the "
 "external components.<br>"
 "<b>(b)</b> When current I flows, energy Ir per unit charge is dissipated in the internal "
 "resistance, so terminal p.d. = E &minus; Ir &lt; E. When I = 0 there are no &#39;lost volts&#39; "
 "(Ir = 0), so the terminal p.d. equals the e.m.f.")

add(T10,
 "In the circuit shown, a 12 V battery of negligible internal resistance is connected to a 4.0 "
 "&Omega; resistor in series with a parallel combination of a 6.0 &Omega; and a 12 &Omega; resistor."
 "<ol class='parts'>"
 "<li>Calculate the total resistance of the circuit and the current drawn from the battery.</li>"
 "<li>Calculate the current in the 6.0 &Omega; resistor.</li></ol>",
 8,
 "<b>(a)</b> Parallel pair: 1/R = 1/6.0 + 1/12 = 0.25 &rArr; R = 4.0 &Omega;. Total = 4.0 + 4.0 = "
 "8.0 &Omega;. Current from battery I = 12/8.0 = <b>1.5 A</b>.<br>"
 "<b>(b)</b> P.d. across the parallel pair = 1.5 &times; 4.0 = 6.0 V. Current in 6.0 &Omega; = "
 "6.0/6.0 = <b>1.0 A</b> (the other 0.5 A is in the 12 &Omega;).",
 "<svg width='300' height='110' viewBox='0 0 300 110'>"
 "<line x1='20' y1='20' x2='20' y2='90' stroke='#333'/>"
 "<line x1='16' y1='45' x2='24' y2='45' stroke='#333' stroke-width='3'/><line x1='14' y1='55' x2='26' y2='55' stroke='#333'/>"
 "<text x='0' y='53' font-size='8'>12V</text>"
 "<line x1='20' y1='20' x2='90' y2='20' stroke='#333'/>"
 "<rect x='90' y='13' width='40' height='14' fill='none' stroke='#333'/><text x='96' y='11' font-size='8'>4.0&Omega;</text>"
 "<line x1='130' y1='20' x2='200' y2='20' stroke='#333'/>"
 "<line x1='200' y1='20' x2='200' y2='40' stroke='#333'/><rect x='180' y='40' width='40' height='13' fill='none' stroke='#333'/><text x='224' y='50' font-size='8'>6.0&Omega;</text>"
 "<line x1='200' y1='20' x2='260' y2='20' stroke='#333'/><line x1='260' y1='20' x2='260' y2='40' stroke='#333'/><rect x='240' y='40' width='40' height='13' fill='none' stroke='#333'/><text x='244' y='68' font-size='8'>12&Omega;</text>"
 "<line x1='180' y1='53' x2='280' y2='53' stroke='#333'/><line x1='230' y1='53' x2='230' y2='90' stroke='#333'/>"
 "<line x1='20' y1='90' x2='230' y2='90' stroke='#333'/></svg>")

add(T10,
 "A potential divider consists of two fixed resistors, R<sub>1</sub> = 3.0 k&Omega; and R<sub>2</sub> "
 "= 9.0 k&Omega;, connected in series across a 6.0 V supply. The output is taken across R<sub>2</sub>."
 "<ol class='parts'>"
 "<li>Calculate the output voltage.</li>"
 "<li>A voltmeter of resistance 18 k&Omega; is connected across the output. Calculate the new output "
 "voltage and comment.</li></ol>",
 8,
 "<b>(a)</b> V<sub>out</sub> = V &times; R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>) = "
 "6.0 &times; 9.0/12.0 = <b>4.5 V</b>.<br>"
 "<b>(b)</b> R<sub>2</sub> ∥ 18 k&Omega; = (9.0 &times; 18)/(9.0 + 18) = 162/27 = 6.0 k&Omega;. "
 "V<sub>out</sub> = 6.0 &times; 6.0/(3.0 + 6.0) = <b>4.0 V</b>. The voltmeter draws current and "
 "&#39;loads&#39; the divider, reducing the output below the ideal 4.5 V.")

add(T10,
 "Explain the principle of a potentiometer used to compare two e.m.f.s, and describe the role of the "
 "galvanometer."
 "<ol class='parts'>"
 "<li>Explain how a balance point is found and what it represents.</li>"
 "<li>A cell balances at 55.0 cm and a second cell at 43.0 cm on the same uniform wire. If the first "
 "cell has e.m.f. 1.50 V, find the e.m.f. of the second.</li></ol>",
 7,
 "<b>(a)</b> A steady current flows through a uniform wire from a driver cell, giving a p.d. "
 "proportional to length. The cell under test is connected (through a galvanometer) to one end and a "
 "sliding contact; the contact is moved until the galvanometer reads zero (balance). At balance the "
 "wire&#39;s p.d. over that length equals the cell&#39;s e.m.f. and no current is drawn from the "
 "cell.<br>"
 "<b>(b)</b> E &prop; length: E<sub>2</sub> = 1.50 &times; 43.0/55.0 = <b>1.17 V</b>.")

add(T10,
 "A light-dependent resistor (LDR) is connected in series with a 1.5 k&Omega; fixed resistor across "
 "a 9.0 V supply. The output is taken across the fixed resistor and fed to a circuit that switches "
 "on a lamp when the output exceeds 6.0 V."
 "<ol class='parts'>"
 "<li>In darkness the LDR has a resistance of 9.0 k&Omega;. Calculate the output voltage and state "
 "whether the lamp is on.</li>"
 "<li>Explain what happens to the output as it becomes brighter, and hence why this arrangement "
 "switches the lamp on at night.</li></ol>",
 7,
 "<b>(a)</b> V<sub>out</sub> = 9.0 &times; 1.5/(9.0 + 1.5) = 9.0 &times; 1.5/10.5 = <b>1.3 V</b>. "
 "Since 1.3 V &lt; 6.0 V, the lamp is <b>off</b> in darkness... which is the wrong way round for a "
 "night-light, so the output would instead be taken across the LDR (see (b)).<br>"
 "<b>(b)</b> As it gets brighter the LDR resistance falls, so the p.d. across the fixed resistor "
 "rises (and that across the LDR falls). To switch a lamp on at night, the output is taken across "
 "the LDR: in darkness the LDR resistance is high, giving a high output that exceeds the threshold "
 "and turns the lamp on.")

add(T10,
 "A network has a 6.0 V cell (negligible internal resistance) connected across two parallel "
 "branches: branch 1 is a single 10 &Omega; resistor; branch 2 is a 4.0 &Omega; and a 2.0 &Omega; "
 "resistor in series."
 "<ol class='parts'>"
 "<li>Calculate the current in each branch.</li>"
 "<li>Calculate the total current drawn from the cell and the total power delivered.</li></ol>",
 7,
 "<b>(a)</b> Branch 1: I = 6.0/10 = <b>0.60 A</b>. Branch 2: R = 4.0 + 2.0 = 6.0 &Omega;, "
 "I = 6.0/6.0 = <b>1.0 A</b>.<br>"
 "<b>(b)</b> Total current = 0.60 + 1.0 = <b>1.6 A</b>. Power = VI = 6.0 &times; 1.6 = <b>9.6 W</b>.")

add(T10,
 "Two cells are connected in series with each other and with a resistor. Cell A has e.m.f. 1.5 V and "
 "internal resistance 0.20 &Omega;; cell B has e.m.f. 1.5 V and internal resistance 0.30 &Omega;. "
 "They drive a current through an external 2.5 &Omega; resistor."
 "<ol class='parts'>"
 "<li>Calculate the current in the circuit.</li>"
 "<li>Calculate the terminal p.d. across cell B.</li></ol>",
 7,
 "<b>(a)</b> Total e.m.f. = 1.5 + 1.5 = 3.0 V. Total resistance = 2.5 + 0.20 + 0.30 = 3.0 &Omega;. "
 "I = 3.0/3.0 = <b>1.0 A</b>.<br>"
 "<b>(b)</b> Terminal p.d. of B = &epsilon;<sub>B</sub> &minus; Ir<sub>B</sub> = 1.5 &minus; "
 "1.0 &times; 0.30 = <b>1.2 V</b>.")

add(T10,
 "Using Kirchhoff&#39;s laws, derive the formula for the combined resistance of two resistors "
 "R<sub>1</sub> and R<sub>2</sub> connected in parallel."
 "<ol class='parts'>"
 "<li>Give the derivation, stating which law is used at each step.</li>"
 "<li>Hence find the single resistance equivalent to 8.0 &Omega; and 8.0 &Omega; in parallel.</li></ol>",
 7,
 "<b>(a)</b> Both resistors have the same p.d. V (parallel). By Kirchhoff&#39;s first law the total "
 "current splits: I = I<sub>1</sub> + I<sub>2</sub>. Using V = IR for each: "
 "V/R = V/R<sub>1</sub> + V/R<sub>2</sub>. Dividing by V: <b>1/R = 1/R<sub>1</sub> + 1/R<sub>2</sub></b>.<br>"
 "<b>(b)</b> 1/R = 1/8.0 + 1/8.0 = 1/4.0 &rArr; R = <b>4.0 &Omega;</b>.")

# ===========================================================================
# TOPIC 11  Particle physics
# ===========================================================================
add(T11,
 "In the &alpha;-particle scattering experiment, a beam of &alpha;-particles is directed at a thin "
 "gold foil. Most pass straight through, a few are deflected through large angles, and a very small "
 "number bounce almost straight back."
 "<ol class='parts'>"
 "<li>State what each of these three observations tells us about the atom.</li>"
 "<li>Explain why the nucleus must be both very small and positively charged.</li></ol>",
 7,
 "<b>(a)</b> Most pass straight through &rArr; the atom is mostly empty space. A few deflected "
 "through large angles &rArr; there is a concentrated region of positive charge that repels them. A "
 "very few bounce back &rArr; this region (the nucleus) is very small and contains most of the "
 "atom&#39;s mass.<br>"
 "<b>(b)</b> Only a tiny fraction rebound, so the charged core occupies a very small volume; the "
 "&alpha;-particles (positive) are repelled, so the core must be positively charged.")

add(T11,
 "A nuclide is represented as <sup>27</sup><sub>13</sub>Al."
 "<ol class='parts'>"
 "<li>State the number of protons, neutrons and electrons in a neutral atom of this nuclide.</li>"
 "<li>Explain what is meant by an isotope, and give the notation for an aluminium isotope with two "
 "more neutrons.</li></ol>",
 6,
 "<b>(a)</b> Protons = 13; neutrons = 27 &minus; 13 = 14; electrons (neutral atom) = 13.<br>"
 "<b>(b)</b> Isotopes are nuclei of the same element (same proton number) with different numbers of "
 "neutrons (different nucleon number). Two more neutrons gives nucleon number 29: "
 "<b><sup>29</sup><sub>13</sub>Al</b>.")

add(T11,
 "Describe the composition, relative mass and relative charge of &alpha;-, &beta;<sup>&minus;</sup>- "
 "and &gamma;-radiations."
 "<ol class='parts'>"
 "<li>Give the nature, mass and charge of each.</li>"
 "<li>State which is the most ionising and which is the most penetrating, with a brief reason.</li></ol>",
 7,
 "<b>(a)</b> &alpha;: a helium nucleus (2 protons + 2 neutrons), relative mass 4, charge +2e. "
 "&beta;<sup>&minus;</sup>: a fast electron, relative mass &asymp; 1/1840, charge &minus;e. &gamma;: a "
 "high-energy electromagnetic photon, zero mass, zero charge.<br>"
 "<b>(b)</b> &alpha; is the most ionising (large charge and mass, many collisions over a short "
 "range); &gamma; is the most penetrating (no charge, interacts least, so it travels furthest).")

add(T11,
 "A nucleus of uranium <sup>238</sup><sub>92</sub>U decays by emitting an &alpha;-particle."
 "<ol class='parts'>"
 "<li>Write the nuclear equation, giving the nucleon and proton numbers of the daughter nucleus.</li>"
 "<li>Explain how nucleon number and charge are conserved in this decay.</li></ol>",
 6,
 "<b>(a)</b> <sup>238</sup><sub>92</sub>U &rarr; <sup>234</sup><sub>90</sub>Th + "
 "<sup>4</sup><sub>2</sub>&alpha;. Daughter (thorium): <b>nucleon number 234, proton number 90</b>.<br>"
 "<b>(b)</b> Nucleon number: 238 = 234 + 4 &#10003;. Charge (proton number): 92 = 90 + 2 &#10003;. "
 "Both totals are unchanged before and after the decay.")

add(T11,
 "During &beta;<sup>&minus;</sup> decay a neutron in the nucleus changes into a proton."
 "<ol class='parts'>"
 "<li>Write the equation for this change at the level of the nucleon, including the emitted "
 "particles.</li>"
 "<li>Explain why the emitted &beta;-particles have a continuous range of energies.</li></ol>",
 6,
 "<b>(a)</b> n &rarr; p + <sup>0</sup><sub>&minus;1</sub>e + &#772;&nu;<sub>e</sub> (a proton, an "
 "electron and an electron antineutrino).<br>"
 "<b>(b)</b> The available energy is shared between the &beta;-particle and the (anti)neutrino in "
 "varying proportions; because the antineutrino carries away a variable amount, the &beta;-particle "
 "can have any energy from near zero up to a maximum &mdash; a continuous spectrum.")

add(T11,
 "State the quark composition of a proton and of a neutron."
 "<ol class='parts'>"
 "<li>Give the compositions and verify the charge of each using quark charges "
 "(u = +&frac23;e, d = &minus;&frac13;e).</li>"
 "<li>State the difference between a baryon and a meson.</li></ol>",
 7,
 "<b>(a)</b> Proton = uud: (+&frac23;) + (+&frac23;) + (&minus;&frac13;) = <b>+1e</b> &#10003;. "
 "Neutron = udd: (+&frac23;) + (&minus;&frac13;) + (&minus;&frac13;) = <b>0</b> &#10003;.<br>"
 "<b>(b)</b> A baryon is made of three quarks (e.g. proton, neutron); a meson is made of one quark "
 "and one antiquark.")

add(T11,
 "During &beta;<sup>+</sup> decay a proton changes into a neutron."
 "<ol class='parts'>"
 "<li>Describe this change in terms of quarks.</li>"
 "<li>State the two particles emitted and identify them as leptons.</li></ol>",
 6,
 "<b>(a)</b> A proton (uud) becomes a neutron (udd): one <b>up quark changes to a down quark</b>.<br>"
 "<b>(b)</b> A <b>positron</b> (e<sup>+</sup>) and an <b>electron neutrino</b> (&nu;<sub>e</sub>) are "
 "emitted; both are leptons (fundamental particles).")

add(T11,
 "Explain what is meant by an antiparticle, and describe the positron."
 "<ol class='parts'>"
 "<li>Define antiparticle and state the properties of the positron relative to the electron.</li>"
 "<li>State the class of fundamental particle to which the electron and neutrino belong.</li></ol>",
 5,
 "<b>(a)</b> An antiparticle has the same mass as its corresponding particle but opposite charge "
 "(and opposite other &#39;charges&#39;). The positron is the antiparticle of the electron: same "
 "mass, but charge +e (instead of &minus;e).<br>"
 "<b>(b)</b> They are <b>leptons</b>.")

add(T11,
 "A radium nucleus <sup>226</sup><sub>88</sub>Ra decays by &alpha;-emission to radon (Rn), which "
 "then decays by &alpha;-emission to polonium (Po)."
 "<ol class='parts'>"
 "<li>Write both decay equations, giving the nucleon and proton numbers at each stage.</li></ol>",
 6,
 "First decay: <sup>226</sup><sub>88</sub>Ra &rarr; <sup>222</sup><sub>86</sub>Rn + "
 "<sup>4</sup><sub>2</sub>&alpha; (radon: <b>A = 222, Z = 86</b>).<br>"
 "Second decay: <sup>222</sup><sub>86</sub>Rn &rarr; <sup>218</sup><sub>84</sub>Po + "
 "<sup>4</sup><sub>2</sub>&alpha; (polonium: <b>A = 218, Z = 84</b>). "
 "(Each &alpha;-emission lowers A by 4 and Z by 2.)")

add(T11,
 "The six flavours of quark are up, down, strange, charm, top and bottom."
 "<ol class='parts'>"
 "<li>State the charge of the up, down and strange quarks, and of their antiquarks.</li>"
 "<li>A particle has quark composition u&#363; (an up quark and an up antiquark). State whether it is "
 "a baryon or a meson, and calculate its charge.</li></ol>",
 6,
 "<b>(a)</b> u: +&frac23;e (&#363;: &minus;&frac23;e); d: &minus;&frac13;e (d&#772;: +&frac13;e); "
 "s: &minus;&frac13;e (s&#772;: +&frac13;e).<br>"
 "<b>(b)</b> One quark + one antiquark &rArr; a <b>meson</b>. Charge = (+&frac23;e) + (&minus;&frac23;e) "
 "= <b>0</b>.")

add(T11,
 "The unified atomic mass unit (u) is used as a unit of mass in nuclear physics."
 "<ol class='parts'>"
 "<li>State the approximate value of 1 u in kilograms and explain why it is a convenient unit.</li>"
 "<li>A carbon-12 atom has a mass of exactly 12 u. Calculate its mass in kilograms.</li></ol>",
 5,
 "<b>(a)</b> 1 u = 1.66&times;10<sup>&minus;27</sup> kg (one twelfth of the mass of a carbon-12 "
 "atom). It is convenient because nucleon masses are then close to 1 u, so nuclide masses are near "
 "their nucleon numbers.<br>"
 "<b>(b)</b> Mass = 12 &times; 1.66&times;10<sup>&minus;27</sup> = <b>1.99&times;10<sup>&minus;26</sup> kg</b>.")

add(T11,
 "Explain why &alpha;-particles are emitted with discrete (specific) energies, whereas &beta;-"
 "particles from a given decay have a continuous range of energies."
 "<ol class='parts'>"
 "<li>Explain the &alpha; case.</li>"
 "<li>Explain the &beta; case, naming the additional particle involved.</li></ol>",
 6,
 "<b>(a)</b> In &alpha;-decay the energy released is shared between just two bodies (the &alpha;-"
 "particle and the recoiling daughter nucleus). Conservation of momentum and energy then fixes the "
 "&alpha;-particle&#39;s energy at one (or a few discrete) value(s) for a given transition.<br>"
 "<b>(b)</b> In &beta;-decay the energy is shared among three bodies, because a (anti)neutrino is "
 "also emitted. The neutrino carries a variable share, so the &beta;-particle&#39;s energy varies "
 "continuously from near zero up to a maximum.")
