# -*- coding: utf-8 -*-
"""PACK 2 - Multiple-choice questions, topics 7-11. AS 9702."""
from engine import mcq as M

MT7 = "7&nbsp;&nbsp;Waves"
MT8 = "8&nbsp;&nbsp;Superposition"
MT9 = "9&nbsp;&nbsp;Electricity"
MT10 = "10&nbsp;&nbsp;D.C. circuits"
MT11 = "11&nbsp;&nbsp;Particle physics"


def add(topic, q, options, correct, ans, svg=""):
    M.append({"topic": topic, "q": q, "options": options, "correct": correct,
              "ans": ans, "svg": svg})


# ===========================================================================
# TOPIC 7
# ===========================================================================
add(MT7, "A wave has frequency 200 Hz and wavelength 1.5 m. Its speed is:",
 ["133 m s<sup>&minus;1</sup>", "300 m s<sup>&minus;1</sup>", "0.0075 m s<sup>&minus;1</sup>",
  "201.5 m s<sup>&minus;1</sup>"], 1,
 "v = f&lambda; = 200 &times; 1.5 = 300 m s<sup>&minus;1</sup>.")

add(MT7, "The period of a wave of frequency 50 Hz is:",
 ["50 s", "0.02 s", "0.5 s", "2.0 s"], 1,
 "T = 1/f = 1/50 = 0.02 s.")

add(MT7, "A sound wave of speed 340 m s<sup>&minus;1</sup> has a frequency of 680 Hz. Its wavelength "
 "is:",
 ["0.5 m", "2.0 m", "1.0 m", "0.25 m"], 0,
 "&lambda; = v/f = 340/680 = 0.5 m.")

add(MT7, "Which of the following is a longitudinal wave?",
 ["light", "a wave on a string", "sound in air", "a water surface wave"], 2,
 "In sound the air particles oscillate along the direction of travel &mdash; longitudinal. The "
 "others are transverse.")

add(MT7, "Which region of the electromagnetic spectrum has the longest wavelength?",
 ["ultraviolet", "X-rays", "radio waves", "infrared"], 2,
 "Radio waves have the longest wavelengths (&gt; 0.1 m) of the listed regions.")

add(MT7, "Polarisation can occur only with:",
 ["longitudinal waves", "transverse waves", "sound waves", "all waves"], 1,
 "Polarisation requires oscillations perpendicular to the direction of travel, which only transverse "
 "waves have.")

add(MT7, "Plane-polarised light passes through a filter whose axis is at 60&deg; to the polarisation "
 "plane. The fraction of intensity transmitted is:",
 ["0.87", "0.75", "0.50", "0.25"], 3,
 "Malus: I/I<sub>0</sub> = cos&sup2;60&deg; = (0.5)&sup2; = 0.25.")

add(MT7, "If the amplitude of a progressive wave is doubled, its intensity is:",
 ["halved", "doubled", "quadrupled", "unchanged"], 2,
 "I &prop; amplitude&sup2;, so doubling the amplitude multiplies the intensity by 4.")

add(MT7, "A source of sound moves towards a stationary observer. Compared with the emitted sound, the "
 "observer hears a frequency that is:",
 ["higher", "lower", "the same", "zero"], 0,
 "For an approaching source the wavefronts bunch up, so the observed frequency is higher (Doppler "
 "effect).")

add(MT7, "Two points on a progressive wave are separated by a quarter of a wavelength. Their phase "
 "difference is:",
 ["45&deg;", "90&deg;", "180&deg;", "360&deg;"], 1,
 "Phase difference = (&frac14;) &times; 360&deg; = 90&deg; (&pi;/2 rad).")

add(MT7, "In free space, all electromagnetic waves have the same:",
 ["frequency", "wavelength", "speed", "amplitude"], 2,
 "All EM waves travel at c = 3.0 &times; 10<sup>8</sup> m s<sup>&minus;1</sup> in free space.")

add(MT7, "On a CRO, one complete cycle of a signal spans 5.0 divisions with the time-base at 2.0 ms "
 "per division. The frequency is:",
 ["50 Hz", "100 Hz", "200 Hz", "500 Hz"], 1,
 "T = 5.0 &times; 2.0&times;10<sup>&minus;3</sup> = 1.0&times;10<sup>&minus;2</sup> s; f = 1/T = "
 "100 Hz.")

add(MT7, "The intensity of light from a point source at distance r is I. At distance 3r it is:",
 ["I/3", "I/6", "I/9", "3I"], 2,
 "Inverse-square law: I &prop; 1/r&sup2;, so at 3r the intensity is I/9.")

add(MT7, "The approximate range of wavelengths of visible light in free space is:",
 ["40&ndash;70 nm", "400&ndash;700 nm", "4&ndash;7 &micro;m", "4&ndash;7 mm"], 1,
 "Visible light spans about 400 nm (violet) to 700 nm (red).")

add(MT7, "In a longitudinal wave, the regions where particles are furthest apart are called:",
 ["compressions", "rarefactions", "nodes", "crests"], 1,
 "Rarefactions are the low-density regions where particles are furthest apart; compressions are "
 "high-density.")

# ===========================================================================
# TOPIC 8
# ===========================================================================
add(MT8, "In a double-slit experiment the fringe separation is given by:",
 ["ax/D", "&lambda;D/a", "&lambda;a/D", "aD/&lambda;"], 1,
 "x = &lambda;D/a, where a is slit separation and D the slit-to-screen distance.")

add(MT8, "For a diffraction grating, the maxima occur where:",
 ["a sin&theta; = n&lambda;", "d sin&theta; = n&lambda;", "d cos&theta; = n&lambda;",
  "d sin&theta; = &lambda;/n"], 1,
 "d sin&theta; = n&lambda;, where d is the grating spacing and n the order.")

add(MT8, "Adjacent nodes on a stationary wave are separated by:",
 ["&lambda;", "&lambda;/2", "&lambda;/4", "2&lambda;"], 1,
 "Nodes are half a wavelength apart (as are adjacent antinodes).")

add(MT8, "Two sources are coherent if they have:",
 ["the same amplitude only", "a constant phase difference", "different frequencies",
  "the same colour only"], 1,
 "Coherence means a constant phase difference (and the same frequency).")

add(MT8, "Constructive interference occurs when the path difference is:",
 ["an odd number of half-wavelengths", "a whole number of wavelengths",
  "a quarter of a wavelength", "zero only"], 1,
 "Path difference = n&lambda; gives waves in phase &rArr; constructive interference.")

add(MT8, "A stationary wave, compared with a progressive wave, transfers:",
 ["more energy", "no net energy along the wave", "energy faster", "energy only at nodes"], 1,
 "A stationary wave stores energy and transfers none along its length (energy sloshes between KE and "
 "PE).")

add(MT8, "A grating has 400 lines per mm. Its slit spacing is:",
 ["2.5 &times; 10<sup>&minus;6</sup> m", "4.0 &times; 10<sup>&minus;4</sup> m",
  "2.5 &times; 10<sup>&minus;3</sup> m", "4.0 &times; 10<sup>5</sup> m"], 0,
 "d = 1/(400&times;10<sup>3</sup> per m) = 2.5 &times; 10<sup>&minus;6</sup> m.")

add(MT8, "Which condition is essential to observe stable two-source interference fringes?",
 ["sources of different frequency", "coherent sources",
  "sources very far apart", "white light only"], 1,
 "The sources must be coherent (constant phase difference) for a stable, observable pattern.")

add(MT8, "In a double-slit experiment, moving the screen further away (increasing D) makes the "
 "fringes:",
 ["closer together", "further apart", "unchanged", "disappear"], 1,
 "x = &lambda;D/a &prop; D, so increasing D increases the fringe separation.")

add(MT8, "At an antinode of a stationary wave, the amplitude of oscillation is:",
 ["zero", "a maximum", "half the maximum", "equal to that at a node"], 1,
 "Antinodes are points of maximum amplitude; nodes have zero amplitude.")

add(MT8, "Light of wavelength 5.0 &times; 10<sup>&minus;7</sup> m strikes a grating of spacing 2.0 "
 "&times; 10<sup>&minus;6</sup> m. The angle of the first-order maximum is:",
 ["7.2&deg;", "14.5&deg;", "30&deg;", "45&deg;"], 1,
 "sin&theta; = &lambda;/d = 5.0&times;10<sup>&minus;7</sup>/2.0&times;10<sup>&minus;6</sup> = 0.25 "
 "&rArr; &theta; = 14.5&deg;.")

add(MT8, "A string fixed at both ends vibrates in its fundamental mode. The wavelength equals:",
 ["L", "2L", "L/2", "4L"], 1,
 "The fundamental fits half a wavelength between the ends: L = &lambda;/2, so &lambda; = 2L.")

add(MT8, "Light of wavelength 600 nm strikes a grating of spacing 2.0 &times; 10<sup>&minus;6</sup> m. "
 "The highest order observable is:",
 ["2", "3", "4", "5"], 1,
 "n &le; d/&lambda; = 2.0&times;10<sup>&minus;6</sup>/6.0&times;10<sup>&minus;7</sup> = 3.3 &rArr; "
 "n<sub>max</sub> = 3.")

add(MT8, "Destructive interference between two coherent waves occurs when the path difference is:",
 ["n&lambda;", "(n + &frac12;)&lambda;", "&lambda;/4", "2n&lambda;"], 1,
 "An odd number of half-wavelengths, (n + &frac12;)&lambda;, gives antiphase &rArr; destructive "
 "interference.")

# ===========================================================================
# TOPIC 9
# ===========================================================================
add(MT9, "A current of 3.0 A flows for 20 s. The charge transferred is:",
 ["0.15 C", "6.7 C", "60 C", "23 C"], 2,
 "Q = It = 3.0 &times; 20 = 60 C.")

add(MT9, "The current in a conductor is given by I = Anvq. Here v represents the:",
 ["speed of light", "drift velocity of charge carriers", "wave speed", "potential difference"], 1,
 "v is the mean drift velocity of the charge carriers.")

add(MT9, "The potential difference across a component is defined as the:",
 ["charge per unit energy", "energy transferred per unit charge",
  "power per unit current", "current per unit resistance"], 1,
 "V = W/Q: energy transferred per unit charge.")

add(MT9, "A 12 V supply drives a current of 0.50 A through a lamp. The power dissipated is:",
 ["6.0 W", "24 W", "0.042 W", "12.5 W"], 0,
 "P = VI = 12 &times; 0.50 = 6.0 W.")

add(MT9, "The resistance of a uniform wire is given by R = &rho;L/A. Doubling the length and doubling "
 "the area changes R by a factor of:",
 ["4", "2", "1 (unchanged)", "&frac12;"], 2,
 "R &prop; L/A; doubling both L and A leaves L/A unchanged, so R is unchanged.")

add(MT9, "The SI unit of resistivity is:",
 ["&Omega;", "&Omega; m", "&Omega; m<sup>&minus;1</sup>", "&Omega; m&sup2;"], 1,
 "From R = &rho;L/A, &rho; = RA/L has units &Omega; &times; m&sup2; / m = &Omega; m.")

add(MT9, "As the current through a filament lamp increases, its resistance:",
 ["decreases", "increases", "stays constant", "becomes zero"], 1,
 "More current heats the filament; the higher temperature increases the resistance.")

add(MT9, "The resistance of a negative-temperature-coefficient thermistor, as temperature rises:",
 ["increases", "decreases", "stays constant", "first rises then falls"], 1,
 "For an NTC thermistor, resistance decreases as temperature increases.")

add(MT9, "The resistance of an LDR when the light intensity falling on it increases:",
 ["increases", "decreases", "stays constant", "becomes infinite"], 1,
 "More light frees more charge carriers, so the LDR&#39;s resistance decreases.")

add(MT9, "For the same current, a thinner wire (smaller area) of the same material has a drift "
 "velocity that is:",
 ["smaller", "larger", "the same", "zero"], 1,
 "v = I/(nAq); for fixed I, smaller A gives a larger drift velocity.")

add(MT9, "A current of 2.0 A flows through a 5.0 &Omega; resistor. The power dissipated is:",
 ["10 W", "20 W", "2.5 W", "40 W"], 1,
 "P = I&sup2;R = (2.0)&sup2;(5.0) = 20 W.")

add(MT9, "A p.d. of 6.0 V is applied across a 3.0 &Omega; resistor. The power dissipated is:",
 ["2.0 W", "12 W", "18 W", "1.5 W"], 1,
 "P = V&sup2;/R = 6.0&sup2;/3.0 = 36/3.0 = 12 W.")

add(MT9, "Ohm&#39;s law applies to a metallic conductor provided that:",
 ["the current is very large", "the temperature is constant",
  "the p.d. is very small", "it is connected in parallel"], 1,
 "Ohm&#39;s law (I &prop; V) holds only if physical conditions, especially temperature, are constant.")

add(MT9, "Electric current is best defined as the:",
 ["number of electrons in a wire", "rate of flow of charge",
  "energy per unit charge", "force on a charge"], 1,
 "I = &Delta;Q/&Delta;t: the rate of flow of electric charge.")

add(MT9, "That charge is quantised means that charge:",
 ["can take any value", "exists only in whole multiples of e",
  "is always negative", "cannot be measured"], 1,
 "Charge comes in integer multiples of the elementary charge e = 1.60 &times; 10<sup>&minus;19</sup> C.")

add(MT9, "A charge of 0.32 C passes a point. The number of electrons is (e = 1.6 &times; "
 "10<sup>&minus;19</sup> C):",
 ["2.0 &times; 10<sup>18</sup>", "5.0 &times; 10<sup>18</sup>", "2.0 &times; 10<sup>19</sup>",
  "5.1 &times; 10<sup>&minus;20</sup>"], 0,
 "N = Q/e = 0.32/1.6&times;10<sup>&minus;19</sup> = 2.0 &times; 10<sup>18</sup>.")

# ===========================================================================
# TOPIC 10
# ===========================================================================
add(MT10, "Three 6.0 &Omega; resistors in series have a combined resistance of:",
 ["2.0 &Omega;", "6.0 &Omega;", "18 &Omega;", "0.5 &Omega;"], 2,
 "Series: R = 6.0 + 6.0 + 6.0 = 18 &Omega;.")

add(MT10, "Two 6.0 &Omega; resistors in parallel have a combined resistance of:",
 ["12 &Omega;", "6.0 &Omega;", "3.0 &Omega;", "1.5 &Omega;"], 2,
 "Parallel of two equal resistors = R/2 = 3.0 &Omega;.")

add(MT10, "A cell of e.m.f. 6.0 V and internal resistance 1.0 &Omega; is connected to a 2.0 &Omega; "
 "resistor. The current is:",
 ["3.0 A", "2.0 A", "6.0 A", "1.0 A"], 1,
 "I = &epsilon;/(R + r) = 6.0/(2.0 + 1.0) = 2.0 A.")

add(MT10, "For the cell in the previous style (E = 6.0 V, r = 1.0 &Omega;, I = 2.0 A), the terminal "
 "p.d. is:",
 ["6.0 V", "4.0 V", "2.0 V", "8.0 V"], 1,
 "V = &epsilon; &minus; Ir = 6.0 &minus; 2.0 &times; 1.0 = 4.0 V.")

add(MT10, "Kirchhoff&#39;s first law is a consequence of the conservation of:",
 ["energy", "charge", "momentum", "mass"], 1,
 "The junction rule (sum of currents in = sum out) follows from conservation of charge.")

add(MT10, "Kirchhoff&#39;s second law is a consequence of the conservation of:",
 ["charge", "energy", "power", "voltage"], 1,
 "The loop rule (&Sigma;E = &Sigma;IR) follows from conservation of energy.")

add(MT10, "A potential divider has two equal resistors across a 10 V supply. The output across one "
 "resistor is:",
 ["10 V", "5.0 V", "2.5 V", "0 V"], 1,
 "Equal resistors share the p.d. equally: V<sub>out</sub> = 10/2 = 5.0 V.")

add(MT10, "A potentiometer is balanced when the galvanometer reads zero. At balance, the current "
 "drawn from the cell under test is:",
 ["maximum", "zero", "half the driver current", "equal to the driver current"], 1,
 "At balance no current flows through the tested cell, so its true e.m.f. is measured.")

add(MT10, "The &#39;lost volts&#39; in a circuit with internal resistance are equal to:",
 ["IR", "Ir", "&epsilon;", "V/R"], 1,
 "Lost volts = Ir, the p.d. across the internal resistance.")

add(MT10, "In a parallel circuit, a 6.0 V supply is connected across a 3.0 &Omega; resistor. The "
 "current in that resistor is:",
 ["0.5 A", "2.0 A", "18 A", "9.0 A"], 1,
 "I = V/R = 6.0/3.0 = 2.0 A (each parallel branch has the full supply p.d.).")

add(MT10, "Two resistors, 4.0 &Omega; and 8.0 &Omega;, are in series across 12 V. The p.d. across the "
 "8.0 &Omega; resistor is:",
 ["4.0 V", "8.0 V", "6.0 V", "12 V"], 1,
 "I = 12/12 = 1.0 A; V<sub>8</sub> = IR = 1.0 &times; 8.0 = 8.0 V.")

add(MT10, "The e.m.f. of a source is the energy transferred per unit charge:",
 ["to the external resistor only", "in driving charge round the whole circuit",
  "lost in the internal resistance", "when no charge flows"], 1,
 "E.m.f. is the total energy per unit charge supplied by the source to drive charge around the "
 "complete circuit.")

add(MT10, "Two identical resistors R in parallel give a combined resistance of:",
 ["2R", "R", "R/2", "R/4"], 2,
 "Two equal resistors in parallel combine to R/2.")

add(MT10, "A galvanometer is used in a null method because it:",
 ["measures large currents accurately", "indicates precisely when the current is zero",
  "has a very high resistance", "measures power"], 1,
 "In null methods the galvanometer detects the balance point (zero deflection = zero current) very "
 "sensitively.")

add(MT10, "A cell of e.m.f. 1.5 V has internal resistance 0.30 &Omega;. The maximum (short-circuit) "
 "current is:",
 ["5.0 A", "0.45 A", "0.20 A", "4.5 A"], 0,
 "I = &epsilon;/r = 1.5/0.30 = 5.0 A.")

add(MT10, "A 4.0 &Omega; resistor carries a current of 1.5 A. The power dissipated is:",
 ["6.0 W", "9.0 W", "2.7 W", "0.38 W"], 1,
 "P = I&sup2;R = (1.5)&sup2;(4.0) = 2.25 &times; 4.0 = 9.0 W.")

# ===========================================================================
# TOPIC 11
# ===========================================================================
add(MT11, "In the notation <sup>A</sup><sub>Z</sub>X, Z represents the:",
 ["nucleon number", "proton number", "neutron number", "mass in u"], 1,
 "Z is the proton (atomic) number; A is the nucleon number.")

add(MT11, "Isotopes of an element have the same number of:",
 ["neutrons", "protons", "nucleons", "electrons in the nucleus"], 1,
 "Isotopes have the same proton number but different numbers of neutrons.")

add(MT11, "An &alpha;-particle consists of:",
 ["2 protons and 2 neutrons", "1 proton and 1 neutron", "2 electrons",
  "2 protons only"], 0,
 "An &alpha;-particle is a helium nucleus: 2 protons and 2 neutrons (charge +2e, mass 4 u).")

add(MT11, "During &beta;<sup>&minus;</sup> decay, within the nucleus:",
 ["a proton changes into a neutron", "a neutron changes into a proton",
  "an electron changes into a proton", "a neutron is destroyed"], 1,
 "&beta;<sup>&minus;</sup> decay: a neutron &rarr; proton + electron + antineutrino.")

add(MT11, "The quark composition of a proton is:",
 ["udd", "uud", "uds", "uuu"], 1,
 "Proton = uud, giving charge (+&frac23; +&frac23; &minus;&frac13;) = +1e.")

add(MT11, "The quark composition of a neutron is:",
 ["uud", "udd", "uus", "ddd"], 1,
 "Neutron = udd, giving charge (+&frac23; &minus;&frac13; &minus;&frac13;) = 0.")

add(MT11, "When <sup>238</sup><sub>92</sub>U emits an &alpha;-particle, the daughter nucleus is:",
 ["<sup>234</sup><sub>90</sub>Th", "<sup>238</sup><sub>90</sub>Th",
  "<sup>234</sup><sub>92</sub>U", "<sup>236</sup><sub>91</sub>Pa"], 0,
 "&alpha;-emission lowers A by 4 and Z by 2: <sup>234</sup><sub>90</sub>Th.")

add(MT11, "When a nucleus <sup>A</sup><sub>Z</sub>X emits a &beta;<sup>&minus;</sup> particle, the "
 "daughter nucleus is:",
 ["<sup>A</sup><sub>Z+1</sub>Y", "<sup>A</sup><sub>Z&minus;1</sub>Y",
  "<sup>A&minus;1</sup><sub>Z</sub>Y", "<sup>A&minus;4</sup><sub>Z&minus;2</sub>Y"], 0,
 "&beta;<sup>&minus;</sup> decay: Z increases by 1, A unchanged.")

add(MT11, "An antiparticle has, compared with its particle, the same mass but:",
 ["the same charge", "opposite charge", "no mass", "half the charge"], 1,
 "An antiparticle has equal mass and opposite charge (e.g. positron vs electron).")

add(MT11, "Which of these is a lepton?",
 ["proton", "neutron", "electron", "&alpha;-particle"], 2,
 "The electron (and neutrino) are leptons &mdash; fundamental particles. Protons and neutrons are "
 "hadrons.")

add(MT11, "A meson is composed of:",
 ["three quarks", "one quark and one antiquark", "two quarks",
  "three antiquarks"], 1,
 "A meson = one quark + one antiquark; a baryon = three quarks.")

add(MT11, "The charge on an up quark is:",
 ["+&frac13;e", "+&frac23;e", "&minus;&frac13;e", "&minus;&frac23;e"], 1,
 "The up quark carries +&frac23;e (its antiquark carries &minus;&frac23;e).")

add(MT11, "In any nuclear decay, which quantities are always conserved?",
 ["mass and charge", "nucleon number and charge", "kinetic energy only",
  "number of protons only"], 1,
 "Nucleon number and charge (proton number balance) are conserved in nuclear processes.")

add(MT11, "An electron antineutrino is emitted during:",
 ["&alpha;-decay", "&gamma;-emission", "&beta;<sup>&minus;</sup> decay",
  "&beta;<sup>+</sup> decay"], 2,
 "&beta;<sup>&minus;</sup> decay emits an (electron) antineutrino; &beta;<sup>+</sup> decay emits a "
 "neutrino.")

add(MT11, "The &alpha;-particle scattering experiment provided evidence that the atom has a:",
 ["uniform distribution of charge", "small, dense, positive nucleus",
  "negative core", "solid structure"], 1,
 "The rare large-angle deflections showed a tiny, massive, positively charged nucleus with mostly "
 "empty space around it.")

add(MT11, "&beta;-particles are emitted with a continuous range of energies because:",
 ["they lose energy in the nucleus", "a neutrino shares the energy",
  "the nucleus recoils fully", "they are not fundamental"], 1,
 "The decay energy is shared with an emitted (anti)neutrino, so the &beta;-particle energy varies "
 "continuously up to a maximum.")

add(MT11, "How many flavours of quark are there?",
 ["three", "four", "six", "eight"], 2,
 "Six: up, down, strange, charm, top and bottom.")
