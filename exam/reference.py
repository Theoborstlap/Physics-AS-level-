"""Concise, syllabus-scoped reference sheet (AS 9702, topics 1-11)."""

REFERENCE_HTML = r"""
<div class='topic-head first'>Reference sheet &mdash; what you actually need (AS, topics 1&ndash;11)</div>

<b>Data &amp; useful constants</b>
<table class='ref'>
<tr><th>Quantity</th><th>Value</th><th>Quantity</th><th>Value</th></tr>
<tr><td>acceleration of free fall, <span class='eq'>g</span></td><td>9.81 m s<sup>&minus;2</sup></td>
    <td>speed of light in vacuum, <span class='eq'>c</span></td><td>3.00 &times; 10<sup>8</sup> m s<sup>&minus;1</sup></td></tr>
<tr><td>elementary charge, <span class='eq'>e</span></td><td>1.60 &times; 10<sup>&minus;19</sup> C</td>
    <td>unified atomic mass unit, <span class='eq'>u</span></td><td>1.66 &times; 10<sup>&minus;27</sup> kg</td></tr>
<tr><td>electron mass</td><td>9.11 &times; 10<sup>&minus;31</sup> kg</td>
    <td>proton mass</td><td>1.67 &times; 10<sup>&minus;27</sup> kg</td></tr>
</table>

<b>SI base units</b>: mass (kg), length (m), time (s), current (A), temperature (K).
Every equation must be <i>homogeneous</i> &mdash; base units on both sides match.

<b>Prefixes</b>:
p 10<sup>&minus;12</sup>, n 10<sup>&minus;9</sup>, &micro; 10<sup>&minus;6</sup>, m 10<sup>&minus;3</sup>,
c 10<sup>&minus;2</sup>, d 10<sup>&minus;1</sup>, k 10<sup>3</sup>, M 10<sup>6</sup>, G 10<sup>9</sup>, T 10<sup>12</sup>.

<b>Uncertainties</b>: for <span class='eq'>y = a&plusmn;b</span> add <i>absolute</i> uncertainties;
for products/quotients (<span class='eq'>y = a<sup>m</sup>b<sup>n</sup></span>) add <i>percentage</i> uncertainties
(&times; the power). Precision = spread of repeats (random); accuracy = closeness to true value (systematic/zero errors).

<table class='ref'>
<tr><th>Topic</th><th>Key relationships</th></tr>
<tr><td>Kinematics</td><td><span class='eq'>v = u + at &nbsp;&middot;&nbsp; s = ut + &frac12;at&sup2; &nbsp;&middot;&nbsp;
    v&sup2; = u&sup2; + 2as &nbsp;&middot;&nbsp; s = &frac12;(u+v)t</span>. Area under <span class='eq'>v&ndash;t</span> = displacement;
    gradient of <span class='eq'>v&ndash;t</span> = acceleration; gradient of <span class='eq'>s&ndash;t</span> = velocity.
    Projectiles: independent horizontal (constant v) and vertical (a = g) motions.</td></tr>
<tr><td>Dynamics</td><td><span class='eq'>F = ma</span> (constant mass) &nbsp;=&nbsp; rate of change of momentum,
    <span class='eq'>F = &Delta;p/&Delta;t</span>. Momentum <span class='eq'>p = mv</span>. Weight <span class='eq'>W = mg</span>.
    Conservation of momentum in all collisions; elastic &rArr; KE conserved and relative speed of approach =
    relative speed of separation. Terminal velocity when drag = weight.</td></tr>
<tr><td>Forces</td><td>Moment = <span class='eq'>F &times; d</span> (perp. distance). Torque of a couple =
    <span class='eq'>F &times; d</span> (separation). Principle of moments: &Sigma;CW = &Sigma;ACW about any point.
    Density <span class='eq'>&rho; = m/V</span>; pressure <span class='eq'>p = F/A</span>;
    hydrostatic <span class='eq'>&Delta;p = &rho;g&Delta;h</span>; upthrust <span class='eq'>F = &rho;gV</span>.</td></tr>
<tr><td>Work / energy / power</td><td><span class='eq'>W = Fs cos&theta;</span>;
    <span class='eq'>&Delta;E<sub>P</sub> = mg&Delta;h</span>; <span class='eq'>E<sub>K</sub> = &frac12;mv&sup2;</span>;
    efficiency = useful out / total in; <span class='eq'>P = W/t = Fv</span>.</td></tr>
<tr><td>Deformation</td><td>Hooke: <span class='eq'>F = kx</span>. Stress <span class='eq'>&sigma; = F/A</span>,
    strain <span class='eq'>&epsilon; = x/L</span>, Young modulus <span class='eq'>E = &sigma;/&epsilon;</span>.
    Elastic PE = area under <span class='eq'>F&ndash;x</span> = <span class='eq'>&frac12;Fx = &frac12;kx&sup2;</span>.</td></tr>
<tr><td>Waves</td><td><span class='eq'>v = f&lambda;</span>; <span class='eq'>T = 1/f</span>;
    intensity = power/area, <span class='eq'>I &prop; A&sup2;</span>. Doppler (moving source):
    <span class='eq'>f<sub>o</sub> = f<sub>s</sub>v /(v &plusmn; v<sub>s</sub>)</span>.
    Malus: <span class='eq'>I = I<sub>0</sub>cos&sup2;&theta;</span>. Visible 400&ndash;700 nm; all EM waves transverse, speed c.</td></tr>
<tr><td>Superposition</td><td>Two-source: <span class='eq'>&lambda; = ax/D</span>.
    Grating: <span class='eq'>d sin&theta; = n&lambda;</span>. Stationary waves: nodes/antinodes,
    adjacent nodes <span class='eq'>&lambda;/2</span> apart. Coherence = constant phase difference.</td></tr>
<tr><td>Electricity</td><td><span class='eq'>Q = It</span>; <span class='eq'>I = Anvq</span>;
    <span class='eq'>V = W/Q</span>; <span class='eq'>R = V/I</span>;
    <span class='eq'>P = VI = I&sup2;R = V&sup2;/R</span>; <span class='eq'>R = &rho;L/A</span>.</td></tr>
<tr><td>D.C. circuits</td><td>e.m.f. <span class='eq'>&epsilon; = I(R + r)</span>; terminal p.d.
    <span class='eq'>V = &epsilon; &minus; Ir</span>. Series <span class='eq'>R = R<sub>1</sub>+R<sub>2</sub>+&hellip;</span>;
    parallel <span class='eq'>1/R = 1/R<sub>1</sub>+1/R<sub>2</sub>+&hellip;</span>. Kirchhoff I (charge), II (energy).
    Potential divider <span class='eq'>V<sub>out</sub> = V R<sub>2</sub>/(R<sub>1</sub>+R<sub>2</sub>)</span>.</td></tr>
<tr><td>Particle physics</td><td>Nuclide <span class='eq'><sup>A</sup><sub>Z</sub>X</span>; A &amp; charge conserved.
    &alpha; = <span class='eq'><sup>4</sup><sub>2</sub>He</span>, &beta;<sup>&minus;</sup> = electron + antineutrino,
    &beta;<sup>+</sup> = positron + neutrino, &gamma; = photon. Quarks: u,d,s,c,t,b
    (u,c,t = +&frac23;e; d,s,b = &minus;&frac13;e). p = uud, n = udd. Baryon = 3 quarks, meson = q&qbar;.
    Leptons (e, &nu;) are fundamental.</td></tr>
</table>
<p class='note'>&beta;<sup>&minus;</sup>: d &rarr; u (n&rarr;p). &beta;<sup>+</sup>: u &rarr; d (p&rarr;n).
&alpha;-particles: discrete energies; &beta;-particles: continuous spectrum (energy shared with the (anti)neutrino).</p>
"""
