# Comprehensive Electromagnetic Theory (EMT) Course Notes

Welcome to the consolidated master documentation for **23ECE204: Electromagnetic Theory and Waves**. This document aggregates and structures the complete course material across all 11 lectures, providing mathematical derivations, key formulas, physical principles, and boundary conditions.

---

## Table of Contents
1. [Lecture 1: Scalars & Vectors](#lecture-1-scalars--vectors)
2. [Lecture 2: Coordinate Systems](#lecture-2-coordinate-systems)
3. [Lecture 3: Electrostatics](#lecture-3-electrostatics)
4. [Lecture 4: Gauss's Law](#lecture-4-gauss-law)
5. [Lecture 5: Dielectric Polarization](#lecture-5-dielectric-polarization)
6. [Lecture 6: Electric Potential & Work Done](#lecture-6-electric-potential--work-done)
7. [Lecture 7: Poisson's & Laplace's Equations](#lecture-7-poissons--laplace-equations)
8. [Lecture 8: Boundary Conditions in Electrostatics](#lecture-8-boundary-conditions-in-electrostatics)
9. [Lecture 9: Magnetostatics](#lecture-9-magnetostatics)
10. [Lecture 10: Boundary Conditions in Magnetostatics](#lecture-10-boundary-conditions-in-magnetostatics)
11. [Lecture 11: Maxwell's Equations](#lecture-11-maxwells-equations)

---

## Lecture 1: Scalars & Vectors

# Lec1_Scalars&Vectors

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Scalars & Vectors
Dr. Sreedevi K. Menon

• Scalar – a quantity whose value maybe  • Vector quantity has both magnitude and
represented  by  a  single  (positive  or  direction in space
negative) real number.
• Velocity, force, displacement, fields
• Mass, density, pressure, volume, and
volume resistivity
| • The | dot product | of two vectors | A and | B is  |       |               |            |     |              |        |
| ----- | ----------- | -------------- | ----- | ----- | ----- | ------------- | ---------- | --- | ------------ | ------ |
|       |             |                |       |       | • The | cross product | of vectors |     | A and B is a | vector |
a scalar
|                            |     |               |     |     | • The         | cross  | product                           | gives  | a vector  | that  is  |
| -------------------------- | --- | ------------- | --- | --- | ------------- | ------ | --------------------------------- | ------ | --------- | --------- |
| • The dot product measures |     | how much one  |     |     |               |        |                                   |        |           |           |
|                            |     |               |     |     | perpendicular |        | to the plane formed by vectors A  |        |           |           |
vector extends in the direction of another
and B.
(projection of one over other.
|     |     |     |     |     | •  Its                         | magnitude | equals             |         | the area        | of  the  |
| --- | --- | --- | --- | --- | ------------------------------ | --------- | ------------------ | ------- | --------------- | -------- |
|     |     |     |     |     | parallelogram                  |           | formed by A and B. |         |                 |          |
|     |     |     |     |     | • If vectors are parallel:     |           |                    | A×B = 0 |                 |          |
|     |     |     |     |     | • Direction is found using the |           |                    |         | right-hand rule |          |

Del operator (∇)
|     | ∇ Vector differential operator |           |     |                      |     |     | used in vector calculus.  |     |     |     |
| --- | ------------------------------ | --------- | --- | -------------------- | --- | --- | ------------------------- | --- | --- | --- |
|     | define                         | gradient, |     | divergence and curl. |     |     |                           |     |     |     |
Gradient:
| •   | When      |            | applied   | to      | a  scalar   |           | field,  |        | the        | del   |
| --- | --------- | ---------- | --------- | ------- | ----------- | --------- | ------- | ------ | ---------- | ----- |
|     | operator  |            | (∇)       | yields  | the         | gradient  |         | (grad  |            | φ  =  |
|     | ∇φ).      | The        | gradient  |         | represents  |           | the     |        | direction  |       |
|     | and       | magnitude  |           | of      | the         | maximum   |         |        | rate       | of    |
change of the scalar field.
| •   | A scalar  |     | field | (e.g.,  | temperature,  |     |     |     | pressure,  |     |
| --- | --------- | --- | ----- | ------- | ------------- | --- | --- | --- | ---------- | --- |
height)

Divergence:
| • When  | applied  |        | to   | a  vector  |           | field,  | the  |     |     |     |
| ------- | -------- | ------ | ---- | ---------- | --------- | ------- | ---- | --- | --- | --- |
| dot     | product  | of     | the  | del        | operator  |         | and  |     |     |     |
| the     | vector   | field  |      | (∇         | ⋅  A)     | gives   | the  |     |     |     |
divergence.
• Divergence measures the flux of the
| vector  | field  |     | through  |     |     | a  closed  |     |     |     |     |
| ------- | ------ | --- | -------- | --- | --- | ---------- | --- | --- | --- | --- |
surface.
| • The     | divergence  |      |     | is            | a   | scalar     | that  |                                         |        |           |
| --------- | ----------- | ---- | --- | ------------- | --- | ---------- | ----- | --------------------------------------- | ------ | --------- |
|           |             |      |     |               |     |            |       | • Positive divergence →                 | source | (outflow) |
| measures  |             | how  |     | much          |     | a  vector  |       |                                         |        |           |
|           |             |      |     |               |     |            |       | • Negative divergence →                 | sink   | (inflow)  |
| field     | spreads out |      |     | from a point. |     |            |       |                                         |        |           |
|           |             |      |     |               |     |            |       | • Zero divergence → incompressible flow |        |           |

Curl:
• When applied to a vector field, the cross product of the del operator and the vector
field (∇ × A) gives the curl.
• The curl is a vector that measures the rotation or circulation of a vector field around
a point.
• Curl measures how much and in what direction a field swirls.
• If curl is zero → the field is irrotational.

---

## Lecture 2: Coordinate Systems (Cartesian, Cylindrical, Spherical)

# Lec2_Coordinate System

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Coordinate Systems
Dr. Sreedevi K. Menon

Cartesian Coordinate System
Cartesian Coordinate System
• Axes: x, y, z
• The geometry is flat or rectangular
• like boxes, beams, or flat planes.
| • Examples:  | Analyzing  | a      | flat  plate  | under  | stress,   |
| ------------ | ---------- | ------ | ------------ | ------ | --------- |
| Calculating  | electric   | field  | between      | two    | parallel  |
plates, Motion in straight lines

Cylindrical Coordinate System
| • Axes:                                       | ρ(radial), | ϕ(angular),           | z (height) |
| --------------------------------------------- | ---------- | --------------------- | ---------- |
| • The object or system has                    |            | cylindrical symmetry- |            |
| •  like wires, pipes, or circular waveguides. |            |                       |            |
• Examples: Current in a coaxial cable, Heat flow in a cylinder, Magnetic field around a
wire

Spherical Coordinate System
| • Axes: | r (radius), | θ (polar angle), | ϕ (azimuthal angle) |
| ------- | ----------- | ---------------- | ------------------- |
• The system has spherical symmetry—like planets, antennas, or point charges.
• Examples:  Electric  field  of  a  point  charge,  Radiation  pattern  of  a  spherical  antenna,
Gravitational field of a planet.

| Coordinate System | Axes / Variables |                                   | Applications |
| ----------------- | ---------------- | --------------------------------- | ------------ |
| Cartesian         | x,y,z            | Rectangular shapes / flat regions |              |
| Cylindrical       | ρ,ϕ,z            | Pipes, wires, rotational systems  |              |
| Spherical         | r,θ,ϕ            | Radial/point sources, spheres     |              |

---

## Lecture 3: Electrostatics (Coulomb's Law & Electric Field)

# Lec3_Electrostatics

## Page 1

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S, B.Tech. ECE

Electrostatics

Dr. Sreedevi K. Menon

---

## Page 2

Coulomb’s Law

Coulomb stated that the force between two very small objects separated in a vacuum or free space by a
distance which is large compared to their size is proportional to the charge on each and inversely
proportional to the square of the distance between them.

a) ag) where Q1 and Q2 are the positive or negative
F=k 12 quantities of charge, R is the separation, and
R2 k is a proportionality constant.
The constant & is called the permittivity of
1 0 P y
= Gren free space and has the magnitude, measured
EO in farads per meter (F/m)

1
_ —12_ -9
€o = 8.854 x 10 = 36, 19 F/m

— O10

Fae
Are, R2

---

## Page 3

Coulomb’s Law

F,
F= 0:0) Ri2=")- 1; Pa
Arey R2 Rio QO,"
ai? r
2
oe
r \.
Origin

_ 9192
21% 4,

2—= 1

Rp Rp m-n
Rel Ri |m—r|

a12

---

## Page 4

« If there are more than two point charges, then each will exert force on the other, then the net force on
any charge can be obtained by the principle of superposition. Consider a point charge Q surrounded by
three other point charges Q;, Qo and Q3, as shown

K = 2
Q290 4ne 9R2, fe]
_ F-¥,
where a0 = ==
|F-¥, |

And force exerted due to Q3 on Q is,

E, = _sS¥ 4
Q39 2 3Q
Ane R 30
where a30 = ru

|F-¥5 |
. E — QQ _ ¢ Hence the total force on Q is,
- Q190 ~ 2 “10 _

4negRig Fo = Fo.0 + Fo.0 + Fo,0

where a19 = ae * In general if there are n other charges then force exerted on Q due to all other n charges is,

---

## Page 5

Coulomb’s Law

Two charges Q1] & Q2 are kept in vacuum. Compute the force exerted by Q2 on Q1
QO; =3 x 10-4 Cat M(I, 2, 3) Q> = —10~* Cat N(2, 0, 5)

---

## Page 6

Electric Field Intensit

F, - 2102. ap
Consider a point charge Q; as shown ? ATE, Ri,

, ; Fr = Qa e
force per unit charge can be written as, Q ~ Ane, R2.
012

force exerted per unit charge is called electric field intensity or electric field strength!

(b)

If any other similar charge Q) is brought near it, Q) experiences a force.

if Q is moved around Q,, still Qo experiences a force

fe]
il
_
aj
m
i=}
Ms
/,|!0
|
2

Thus there exists a region around a charge in which it exerts a force on any other charge. This region

where a particular charge exerts a force on any other charge located in that region is called electric field
of that charge. The electric field of Q; is shown in the Fig (b).

E due to n number of charges

---

## Page 7

Electric Field Intensity

Find E at P (1,1,1) caused by four identical 3 n C charges located at
P, (1,1,0) P, (-1,1,0), P3 (-1,-1,0), and P, (1,-1,0)

P, (-1, 1, 0)

P,(1,~1, 0) P, (1, 1,0)

---

### Extracted Text (MarkItDown)

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Electrostatics
Dr. Sreedevi K. Menon

Coulomb’s Law
Coulomb stated that the force between two very small objects separated in a vacuum or free space by a
distance which is large compared to their size is proportional to the charge on each and inversely
proportional to the square of the distance between them.
where Q1 and Q2 are the positive or negative
quantities of charge, R is the separation, and
k is a proportionality constant.
The constant ℇ is called the permittivity of
0
free space and has the magnitude, measured
in farads per meter (F/m)

Coulomb’s Law

Coulomb’s Law
Two charges Q1 & Q2 are kept in vacuum. Compute the force exerted by Q2 on Q1

Electric Field Intensity

Electric Field Intensity
Find E at P (1,1,1) caused by four identical 3 n C charges located at
| P  (1,1,0) P | (-1,1,0), P |  (-1,-1,0), and P |  (1,-1,0) |
| ------------ | ----------- | ----------------- | --------- |
| 1            | 2           | 3                 | 4         |

---

## Lecture 4: Gauss's Law & Electric Flux Density

# Lec4_Gauss’s Law

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Gauss’s Law
Dr. Sreedevi K. Menon

• Aa charge uniformly distributed along a line is called
a line charge.
|       |         |         |          |               |              |     | • In case of surface charge distribution, to find the total charge  |     |     |     |     |     |     |
| ----- | ------- | ------- | -------- | ------------- | ------------ | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| • The | charge  | density | of  the  | line  charge  | is  denoted  | as  |                                                                     |     |     |     |     |     |     |
Q consider elementary surface area dS. The charge dQ on
| ρ   | and defined as charge per unit length. |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
|     |     |     |     |     |     |     | this differential area is given by p |     |     |     |  dS.  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ----- | --- | --- |
S
| • The  | ρ is  | constant  | all  along  | the  length  | L  of  the  | line  |     |     |     |     |     |     |     |
| ------ | ----- | --------- | ----------- | ------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
L
|     |     |     |     |     |     |     | • Integrating dQ over the given surface, the total charge Q is  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
carrying the charge.
obtained.
| • To  | find  the  | total  charge  | Q   | by  considering  | differential  |     |                                |     |     |                  |     |     |     |
| ----- | ---------- | -------------- | --- | ---------------- | ------------- | --- | ------------------------------ | --- | --- | ---------------- | --- | --- | --- |
|       |            |                |     |                  |               |     | • Such an integral is called a |     |     | surface integral |     |     |     |
length dZ of the line.
• Integrate the charge dQ on dZ, for the entire length, total
charge Q is to be obtained.
| • Such an integral is called |     |     | line integral. |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• In case of volume charge distribution, the differential volume dv is
considered. The charge dQ possessed by the differential volume is
p  dV.
V
|     |     |     |     |     |     |     | • Then  | the  total  | charge  | within  the  | finite  given  | volume  | is  to  be  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------- | ------------ | -------------- | ------- | ----------- |
If the line of length L is a closed path, then integral is called
closed contour integral and denoted as, obtained by integrating the dQ throughout that volume.
• Such an integral is called volume integral.

Gauss’s Law
The  electric  flux  passing  through  any  closed  surface  (called  Gaussian  surface)  in  free
space is equal to 1 / ε  times the net charge enclosed within the surface.
0
|     |     |     | 1 n |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
∑ E
|     | Ψ  = |     |     | q   |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- |
E . dS =
|     | E   |     | ε     | i   |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     | 0 i=1 |     |     |     |     |
S
|              |     | 1   | q       |     |     | r   | dS  |
| ------------ | --- | --- | ------- | --- | --- | --- | --- |
| d Ψ = E . dS |     | =   | r . dS  | n   |     |     |     |

|     |     | 4πε | r2  |     |     | O•  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0
r
+q
|        | 1   | q dS |       |     |     |     |     |
| ------ | --- | ---- | ----- | --- | --- | --- | --- |
| d Ψ =  |     |      | r . n |     |     |     |     |
|        | 4πε | r2   |       |     |     |     |     |
0
Here,
|     | r . n | = 1 x 1  cos 0° = 1 |     |     |     |     |     |
| --- | ----- | ------------------- | --- | --- | --- | --- | --- |
1 q dS
d Ψ =
4πε
r2
0
1 q
|     |     | 1   | q   |     |     |     | q   |
| --- | --- | --- | --- | --- | --- | --- | --- |
4π r2
|       |        |     | dS  | =   |     | =   |     |
| ----- | ------ | --- | --- | --- | --- | --- | --- |
| Ψ   = | d Ψ  = |     |     |     |     |     |     |
E
|     |     | 4πε | r2  | 4πε | r2  |     | ε   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 0   |     |     | 0   |
0
S
S
3

Deduction of Coulomb’s Law from Gauss’s Theorem:
From Gauss’s law,
q
Φ =
E E . dS =
ε
0
S
Since E and dS are in the same direction,
q
Φ =
E E dS =
ε
0
S
q
or Φ = E dS =
E ε
0
S
q q
E x 4π r2 = or E =
ε 4πε r2
0 0
If a charge q is placed at a point where E is calculated, then
0
qq
0
F = which is Coulomb’s Law.
4πε r2
0

Electric Field Intensity due to an Infinitely Long Straight Charged Wire:
| Gaussian  | surface  | is  a  closed  | surface,  |
| --------- | -------- | -------------- | --------- |
around a charge distribution, such that
the electric field intensity has a single
| fixed  value  | at  | every  point  | on  the  |
| ------------- | --- | ------------- | -------- |
surface.

Electric Field Intensity due to an Infinitely Long, Thin Plane Sheet of Charge:

---

## Lecture 5: Dielectric Polarization & Boundary Behavior

# Lec5_Dielectric Polarisation

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Dielectric Polarization
Dr. Sreedevi K. Menon

When a dielectric is placed in an electric field E, the centers of positive and negative charges shift slightly in opposite
directions. This creates an electric dipole moment in the material, reducing the effective electric field inside the
dielectric. As a result, electric dipoles are induced or aligned within the material - Dielectric Polarization
Polarization Vector
Total dipole moment
The polarization of a dielectric is represented by: 𝐏 =
Unit volume
𝑃= Polarization (C/m²)
For a linear dielectric, 𝐏 = 𝜺 𝝌 𝐄
𝟎 𝒆
𝜀 = Permittivity of free space
0
𝜒 = Electric susceptibility
𝑒
𝐸= Applied electric field
• Reduces the internal electric field.
• Increases the capacitance of a capacitor.
• Enables storage of electrical energy.
• Influences the dielectric constant (relative permittivity) of the material.
2

Displacement Flux Density (D)
| The electric displacement flux density is defined as 𝐃 |     |     |     |     | = 𝜀 𝐄 | + 𝐏 |
| ------------------------------------------------------ | --- | --- | --- | --- | ----- | --- |
0
𝜀 𝐄 represents the contribution from free space.
0
𝐏 represents the contribution due to polarization of the dielectric.
For a Linear, Isotropic Dielectric
|     |     | 𝐏   | = 𝜀 𝜒 | 𝐄,  |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
0 𝑒
|     |     | 𝐃 = | 𝜀 𝐄 + 𝜀 | 𝜒 𝐄  |     |     |
| --- | --- | --- | ------- | ---- | --- | --- |
|     |     |     | 0       | 0 𝑒  |     |     |
|     |     | 𝐃 = | 𝜀 1 +   | 𝜒 𝐄  |     |     |
|     |     |     | 0       | 𝑒    |     |     |
|     |     | 𝜀   | = 1 +   | 𝜒    |     |     |
|     |     | 𝑟   |         | 𝑒    |     |     |
|     |     | 𝐃 = | 𝜀 𝜀 𝐄   | = 𝜀𝐄 |     |     |
0 𝑟
• Polarization (𝐏) measures how strongly the dielectric material becomes polarized.
• Displacement flux density (𝐃) accounts for both the applied electric field and the
effect of the material's polarization.
| • In vacuum, 𝐏 | = 0, so 𝐃 | =   | 𝜀 𝐄.  |     |     |     |
| -------------- | --------- | --- | ----- | --- | --- | --- |
0
• In a dielectric, polarization increases 𝐃 above its vacuum value.
3

---

## Lecture 6: Electric Potential & Work Done

# Lec6_Potential & Work done

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Potential & Work done
Dr. Sreedevi K. Menon

Line Integral of Electric Field (Work Done by Electric Field):
𝐵
Negative Line Integral of Electric Field represents the work
𝑊 = −𝑄 න 𝐸. 𝑑𝑙
done by the electric field on a unit positive charge in moving it
𝐴
from one point to another in the electric field.
𝐵
𝑊 = − න 𝐹. 𝑑𝑙
𝐵 𝐴
θ = 0° : Maximum positive work
න 𝐸. 𝑑𝑙 = 𝐸 𝑑𝑙 𝑐𝑜𝑠𝜃
θ = 90° : Zero work W = Work done (J)
𝐴
q = Charge (C)
θ = 180° : Negative work
E = Electric field (N/C or V/m)
F = Force (N)
dl = Infinitesimal displacement
1. The equation shows that the work done in moving a test charge q from point A to another point B along any
0
path AB in an electric field due to +q charge depends only on the positions of these points and is independent
of the actual path followed between A and B.
2. That is, the line integral of electric field is path independent.
3. Therefore, electric field is ‘conservative field’.
4. Line integral of electric field over a closed path is zero. This is another condition satisfied by conservative field.
ර𝐸. 𝑑𝑙 = 0
2

Electric Potential:
Electric potential is a physical quantity which determines the flow of charges from one body to another.
Electric Potential at a point in the electric field is defined as the work done in moving (without any acceleration) a
unit positive charge from infinity to that point against the electrostatic force irrespective of the path followed.
𝐵
| 𝑉 − 𝑉 | = − න | 𝐸. 𝑑𝑙 |     |
| ----- | ----- | ----- | --- |
| 𝐵     | 𝐴     |       |     |
Electric field does positive work when a positive
𝐴
charge moves from higher to lower potential
| 𝑊 = −𝑄 (𝑉 |     | 𝑉 ) = 𝑄 (𝑉 | 𝑉 )  |
| --------- | --- | ---------- | ---- |
|           | 𝐵 − | 𝐴 𝐴 −      | 𝐵    |
Electric potential at a point is one volt if one joule of work is done in moving one coulomb charge from
infinity to that point in the electric field.
Electrostatic Potential Energy:
The work done in moving a charge q from infinity to a point in the field against the electric force is called
electrostatic potential energy.
𝑊 = 𝑄 𝑉
3

Electric Potential Difference:
Electric Potential Difference between any two points in the electric field is defined as the work done in
moving (without any acceleration) a unit positive charge from one point to the other against the
electrostatic force irrespective of the path followed.
| W   | q   |     | q   |     |
| --- | --- | --- | --- | --- |
|     |     | 1   |     | 1   |
AB
| =   |     | -   |     |     |
| --- | --- | --- | --- | --- |
| q   |     | r   |     | r   |
|     | 4πε | B   | 4πε |     |
| 0   |     |     |     | A   |
|     | 0   |     | 0   |     |
W
AB
V  - V   =  ∆V  =
|     | B A |     | q   |     |
| --- | --- | --- | --- | --- |
0
1. Electric potential and potential difference are scalar quantities.
2. Electric potential at infinity is zero.
3. Electric potential near an isolated positive charge (q > 0) is positive and that near an isolated
negative charge (q < 0) is negative.
4

Electric Potential due to a Single Point Charge:
|        |                                                  |     |     |     |     |     |     |     |     |     |     |     |     | q E |
| ------ | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Let +q |  be the test charge placed at P at a distance x  |     |     |     |     |     |     | E   |     |     |     | dx  |     |     |
|        |                                                  |     |     |     |     |     |     |     |     |     |     | +q  |     | 0   |
|        | 0                                                |     |     |     |     |     |     |     |     |     |     |     | 0   |     |
from the source charge +q. ∞
B
|     |     |     |     |     |     |     | + q |     |     |     |     | Q P |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
| The force F = +q |     | E  is radially outward and tends to  |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x
0
accelerate the test charge.
To prevent this acceleration, equal and opposite force –q E has to be applied on the test charge.
0
| Work done to move q |     |     |  from P to Q through ‘dx’ against q |     |     |     | E is |                  |     |        |     |     |     |     |
| ------------------- | --- | --- | ----------------------------------- | --- | --- | --- | ---- | ---------------- | --- | ------ | --- | --- | --- | --- |
|                     |     |     |                                     |     |     |     |      | dW = F . dx  = q |     | E . dx |     |     |     |     |
|                     |     |     | 0                                   |     |     |     | 0    |                  |     | 0      |     |     |     |     |
E dx cos 180°  =  - q
|     | dW = q |     |     | E dx   |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |        | 0   |     | 0      |     |     |     |     |     |     |     |     |     |     |
q
q q
E =
0
|     | dW = - |     |     | dx  |     |     |            |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     |        |     |     |     |     |     | 4πε   x2   |     |     |     |     |     |     |     |
0
4πε   x2
0
| Total work done to move q |     |     |  from A to B (from ∞ to r ) is |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
B
|     |     | r   |     |     |     | r   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | q q |     | q q |     | 1   |     |     |     | q   |     |     | q   |
W
|        |        |     | 0          |        | 0          |     |      |     |     |     |        |     |      |        |
| ------ | ------ | --- | ---------- | ------ | ---------- | --- | ---- | --- | --- | --- | ------ | --- | ---- | ------ |
| W  =   | dW = - |     |            | dx = - |            |     | dx   |     | ∞B  |     |        |     |      |        |
| ∞B     |        |     |            |        |            |     |      |     |     | =   |        |     | V  = |        |
|        |        |     | 4πε   x2   |        | 4πε   x2   |     |      |     | q   |     |        |     |      |        |
|        | ∞      |     |            |        |            |     | x2   |     |     |     | 4πε  r |     |      | 4πε  r |
|        |        |     | 0          |        | 0          |     |      |     | 0   |     |        |     |      |        |
|        |        | ∞   |            |        |            | ∞   |      |     |     |     | 0      |     |      | 0      |
5

Equipotential Surfaces:
A surface at every point of which the potential due to charge distribution is the same is called equipotential surface.
i) For a uniform electric field:
E
V
V V 3
1 2 E
+
Plane Equipotential Surfaces
Spherical Equipotential Surfaces
ii) For an isolated charge:
6

Properties of Equipotential Surfaces:
W
AB
1. No work is done in moving a test charge from one point to another on an equipotential surface. V - V = ∆V =
B A
q
0
W
If A and B are two points on the equipotential surface, then V = V . AB W = 0
B A = 0 AB
q
0
2. The electric field is always perpendicular to the element dl of the equipotential surface.
B
Since no work is done on equipotential surface,
W = - = 0
AB E . dl
A
3. Equipotential surfaces indicate regions of strong or weak electric fields.
dV
Electric field is defined as the negative potential gradient. E = -
dr
If E is strong (large), dr will be small, i.e. the separation of equipotential surfaces will be smaller (i.e. equipotential
surfaces are crowded) and vice versa.
4. Two equipotential surfaces can not intersect.
If two equipotential surfaces intersect, then at the points of intersection, there will be two values of the electric potential
which is not possible.
7

---

## Lecture 7: Poisson's & Laplace's Equations

# Lec7_Poissons & Laplaces equatin

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Poisson's & Laplace’s Equation
Dr. Sreedevi K. Menon
Associate Professor
Department of Electronics and Communication Engineering
Amrita Vishwa Vidyapeetham
Amritapuri

| Stokes theorem |             | Divergence theorem |     |         |
| -------------- | ----------- | ------------------ | --- | ------- |
| ර 𝐸. 𝑑𝑙        | = න  𝐸 𝑑𝑆 | ර 𝐸. 𝑑𝑆            | = න | . 𝐸 𝑑𝑣 |
| 𝑙              | 𝑆           | 𝑆                  | 𝑉   |         |
B
Integral form
E . dl = 0
A
𝑄
 𝐸 = 0
|     |     | . 𝐸 | =   |     |
| --- | --- | ---- | --- | --- |

Point form
0
|  𝐷 | = 0  |     |       |     |
| ---- | ---- | --- | ----- | --- |
|      |      | .  | 𝐷 = Q |     |
2

3

|     | Feature | Poisson's Equation |     | Laplace's Equation |     |
| --- | ------- | ------------------ | --- | ------------------ | --- |
𝜌
∇2𝑉
|     | Equation | ∇2𝑉 | = − |     | = 0 |
| --- | -------- | --- | --- | --- | --- |
𝜖
| Charge Density |     | Present   0 |     |     | = 0 |
| -------------- | --- | ------------- | --- | --- | ---- |
Absent
| Applicable Region |             | Charged region |        | Charge-free region |      |
| ----------------- | ----------- | -------------- | ------ | ------------------ | ---- |
|                   | Source Term |                | Exists |                    | Zero |
Potential Depends On Charges + Boundary Conditions Boundary Conditions only
• Poisson's equation: Describes the potential in regions where charge is present.
• Laplace's equation: A special case of Poisson's equation when 𝜌 = 0.
• Electric field is obtained from potential using
|     |     |     | 𝐄 = −∇𝑉. |     |     |
| --- | --- | --- | -------- | --- | --- |
4

---

## Lecture 8: Boundary Conditions in Electrostatics

# Lec8_Boundary Conditions_Electrostatics

## Page 1

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S, B.Tech. ECE

Boundary Condition

Dr. Sreedevi K. Menon

---

## Page 2

B c ws Two Perfect Diel. . Both E, and E, in the respective dielectrics have both the
oundary Conditions between Two Perfect Dielectrics components, normal and tangential.
Region 1} &

[Ext] = Etanty | Eot| = Brana

Ein] = Ein — | Eon |= Eon

c a b d
Ah > 0,f and J become zero J EedL+/ EedL=0
b d

a c

b b
[Region 2] e, J Eedl = Bani d= Euan Aw
a a
E and D 2 to be obtained again by resolving each into two components, tangential to boundary
and normal to the surface.

Consider a closed path abcda rectangular in shape

Etant AW - Etano AW = 0
f EedL = 0

b _ ¢ _ d _ a _ Fran! =
-. [ EedL+[ EedL+/ EedL+/ EedL=0

a b © a D=ecE — Drani = &1 Etani and Dtan2 =€2 Etana
Now E, = Ey, +E

1 at + Ein Diant _ Dian? Diant ~ &_ fn

and E, = Ey +Eon €) se Dian2 Eo Ey

---

## Page 3

Consider a Gaussian surface in the form of right circular cylinder, placed in such a way that half of it lies in dielectric 1
while the remaining half in dielectric 2. The height Ah — 0 hence flux leaving from its lateral surface is zero. The surface

area of its top and bottom is AS.
f Deds =Q
f+ f + f DedS=Q

top bottom _ lateral

J DedS=0 as Ah0
lateral

J Deas + f DedS=Q
top bottom

bottom bottom ,
Dyy AS — Dyn AS = Q no free charge available in perfect dielectric Dui =€1 En; and Dyp =€2 Exp
hence no free charge can exist on the surface.
Q = pg AS Ps = 0 Dui _ &Eni _ 4 Eni - 2 _'&2
Dni-Dy2 = Ps Dyi-Dyo = 0 Dni = Dyno Dyo___€2 Enp Eno 81 €n

---

## Page 4

Boundary Conditions between Conductor and Free Space

1. The component tangential to the surface (Etan ).

2. The component normal to the surface (En ).

Consider a rectangular closed path traced in clockwise direction as a-b- c-d-a

Boundary

b c d a

f EedL=[ EedL+/ EedL+{ EedL+{ EedL=0
a b c d

* The closed contour is placed in such a way that its two sides a-b and c-d are parallel to tangential

direction to the surface while the other two are normal to the surface, at the boundary.

The rectangle is an elementary rectangle with elementary height A and elementary width Aw

the portion c-d is in the conductor where — = 0 hence the corresponding integral is zero.

b c a
f EedL+/ EedL+/ EedL=0
a b d

As the width Aw is very small, E over it can be assumed constant and hence can be taken out of bb _b _
; ; J EedL = Ef dL = E(aw)
integration.

a a

---

## Page 5

b
Aw is along tangential direction to the boundary in which direction _— = E,,. f EedL = Ejay (Aw) where Etan =| Etan |
a

Now b-c is parallel to the normal component so we have E = Ey along this direction.
Ex =| En}
Over the small height Ah, Ey can be assumed constant and can be taken out of integration.

EedL = E

dL =Ey

d

o—
_
on

‘b-c, b-2 is in free space and 2-c is in the conductor where — = 0.

for path d-a, the condition is same as for the path b-c, only direction is opposite.

jt = Ah
¢c 2 c EedL = -E
- fae — Ah, Ah x( 2 }
fa = Jats Jat=s0=y a ws
Fag dwt By (2P) EQS) =o
c
[ Beak = Ey {% . En = 0
> Eitan AW = 0 Aw#0 as finite

the tangential component of the electric field intensity is zero at
the boundary between conductor and free space.

---

## Page 6

_ To find normal component of [, , select a closed Gaussian surface in the form of right circular cylinder
D As

Its axis is in the normal direction to the surface.

Gaussian

According to Gauss's law, f DedS=Q
Ss
surface

The surface integral must be evaluated over three surfaces,

i) Top, ii) Bottom and iii) Lateral.

Let the area of top and bottom is same equal to AS.

J Deas + f DedS + f DedS=Q
top bottom lateral

The bottom surface is in the conductor where J, = 0 hence corresponding integral is zero.

The top surface is in the free space and we are interested in the boundary condition hence top surface

Its height is Ah and is placed in such a way that Ah/2 is in the conductor and remaining Ah/2 is in the free space.

J Deas + f DedS=Q
can be shifted at the boundary with Ah — 0.

top lateral
The lateral surface area is 2 tr Ah where r is the radius of the cylinder. But as Ah — 0, this area reduces
to zero and corresponding integral is zero.

While only component of , present is the normal component having magnitude Dy The top surface is f DedS = Dy f dS =
very small over which Dy can be assumed constant and can be taken out of integration. top

---

## Page 7

From Gauss's law, Dy AS=Q
But at the boundary, the charge exists in the form of surface charge density pS C / m2. Q=psS AS

Dy AS = pS AS

Dy = pS

The flux leaves the surface normally and the normal component of flux density is equal to the surface charge density.

Dy = €0 En = pS

EN =pS/ €

boundary is between conductor and dielectric with € = €y €,.

---

### Extracted Text (MarkItDown)

23ECE204 Electromagnetic Theory and Waves
 (3-1-0-4)
S3 B.Tech. ECE

Boundary Condition

Dr. Sreedevi K. Menon

Boundary Conditions between Two Perfect Dielectrics

Both
components, normal and tangential.

in the respective dielectrics have both the

2

Consider a Gaussian surface in the form of right circular cylinder, placed in such a way that half of it lies in dielectric 1
while the remaining half in dielectric 2. The height Δh → 0 hence flux leaving from its lateral surface is zero. The surface
area of its top and bottom is ΔS.

no free charge available in perfect dielectric
hence no free charge can exist on the surface.

3

Boundary Conditions between Conductor and Free Space

4

the tangential component of the electric field intensity is zero at
the boundary between conductor and free space.

5

6

The flux leaves the surface normally and the normal component of flux density is equal to the surface charge density.

boundary is between conductor and dielectric with Ɛ = Ɛ0 Ɛr.

7

---

## Lecture 9: Magnetostatics (Biot-Savart Law & Ampere's Circuital Law)

# Lec9_Magnetostatics

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S B.Tech. ECE
3
Steady State Magnetic Filed
Dr. Sreedevi K. Menon

| Electric force | 𝐹 = | 𝑞 𝐸 |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑒
|     |     |     | Electromagnetic force |     |     | 𝐹 = | 𝐹 + 𝐹 |     |
| --- | --- | --- | --------------------- | --- | --- | --- | ----- | --- |
𝑒 𝑚
Magnetic force
|     | 𝐹 = | 𝑞 𝑣  × 𝐵 |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- |
𝑚
|     |     |     | 𝐹  = 𝑞 | 𝐸 + | 𝑣  × 𝐵 | Lorentz’s force equation |     |     |
| --- | --- | --- | ------ | --- | ------ | ------------------------ | --- | --- |
Fundamental Postulates of Magnetostatics in Free Space
| Gauss's law for magnetism  |       |     | Ampère's circuital law  |     |     |     |       |     |
| -------------------------- | ----- | --- | ----------------------- | --- | --- | --- | ----- | --- |
|                            | ∇ ⋅ 𝐁 | = 0 |                         |     |     |     | ∇ × 𝐇 | = 𝐉 |
The magnetic flux density 𝐁 has zero
where 𝐇 is the magnetic field intensity and 𝐉 is the current density. In
divergence.
| Equivalently, for a closed surface 𝑆, |          |     | integral form, |     |     |     |         |     |
| ------------------------------------- | -------- | --- | -------------- | --- | --- | --- | ------- | --- |
|                                       |  ර𝐁 ⋅ 𝑑𝐒 | = 0 |                |     |     |     | ර𝐇 ⋅ 𝑑𝐥 | = 𝐼 |
|                                       | 𝑆        |     |                |     |     |     | 𝐶       |     |
This implies that magnetic monopoles do not  where 𝐼 is the total steady current enclosed by the closed contour 𝐶.
exist; magnetic field lines always form closed  In free space, 𝐁 = 𝜇 𝐇
0
| loops. |     |     | Ampère's law : ∇ |     |     | × 𝐁 = 𝜇 | 𝐉   |     |
| ------ | --- | --- | ---------------- | --- | --- | ------- | --- | --- |
0
The two fundamental differential postulates of magnetostatics in free space
|     |     |     |     |     | ∇ ⋅ 𝐁 = | 0   |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- |
|     |     |     |     |     | ∇ × 𝐁 = | 𝜇 𝐉 |     |     |
0
Apply to steady (time-independent) currents and magnetic fields.
2

Magnetic Vector Potential 𝐀
|     |     | ∇ ⋅ 𝐁 = | 0,  |     |     |
| --- | --- | ------- | --- | --- | --- |
the magnetic flux density 𝐁can be expressed as the curl of a
vector field 𝐀:
|     |     | 𝐁 = ∇ × | 𝐀   |     |     |
| --- | --- | ------- | --- | --- | --- |
The vector 𝐀is called the magnetic vector potential.
Electric Scalar Potential
| In electrostatics, the electric field 𝐄is irrotational: ∇ |     |     |     | × 𝐄 | = 0 |
| --------------------------------------------------------- | --- | --- | --- | --- | --- |
The electric field can be expressed as the negative gradient of a scalar function 𝑉: 𝐄 = −∇𝑉
where 𝑉is called the electric scalar potential or simply electric potential.
𝐵
The potential difference between two points 𝐴and 𝐵 is 𝑉 − 𝑉 = − 𝐄 ⋅ 𝑑𝐥
׬
|     |     |     |     |     | 𝐵 𝐴 |
| --- | --- | --- | --- | --- | --- |
𝐴
The electric potential at a point is the work done per unit positive charge in bringing a test charge from a
reference point (usually infinity) to that point.
𝑃
| Taking 𝑉 | = 0at infinity, 𝑉 | = −׬ | 𝐄 ⋅ 𝑑𝐥 |     |     |
| -------- | ----------------- | ---- | ------ | --- | --- |
∞
3

Biot-Savart Law
Total Magnetic Field
The magnetic field 𝑑𝐁 at a point due to a current element 𝐼 𝑑𝐥 is:
For a complete current-carrying conductor,
𝜇 𝐼 𝑑𝐥 × 𝐫ො
0
𝑑𝐁 = integrate over its length:
4𝜋 𝑟2
𝜇 𝐼 𝑑𝐥 × 𝐫ො
0
or, in magnitude, 𝐁 = න
4𝜋 𝑟2
𝜇 𝐼 𝑑𝑙 sin 𝜃
0
𝑑𝐵 =
4𝜋 𝑟2
• 𝑑𝐵= small magnetic field due to the current element
• 𝜇 = 4𝜋 × 10−7 T ⋅ m/A
0
• 𝐼= current in the conductor
• 𝑑𝑙= infinitesimal length element of the conductor
• 𝑟= distance from the current element to the observation point
• 𝜃= angle between 𝑑𝐥and the position vector 𝐫
• 𝐫ො= unit vector from the current element to the observation point
The direction of the magnetic field is given by the right-hand rule:
• Point your thumb in the direction of the current.
• Curl your fingers toward the observation point; the magnetic
field direction is perpendicular to both the current element and
the position vector.
4

Magnetic Field Due to a Straight Current-Carrying Wire Using Biot–Savart Law
Consider a long straight wire carrying a current 𝐼.
Calculate the magnetic field at a point 𝑃, located at a perpendicular distance
𝑎from the wire.
According to the Biot–Savart law,
𝜇 𝐼 𝑑𝑙 sin𝜃
0
𝑑𝐵 =
4𝜋 𝑟2
Let 𝑥 be the distance of the current element 𝑑𝑙from the foot of the
perpendicular drawn from 𝑃.
𝑟 = 𝑎2 + 𝑥2
𝑎
sin 𝜃 =
𝑟
𝜇 𝐼 𝑑𝑙 𝑎
0
𝑑𝐵 =
4𝜋 𝑟2 𝑟
Since 𝑑𝑙 = 𝑑𝑥,
𝜇 𝐼𝑎 𝑑𝑥
0
𝑑𝐵 =
4𝜋 𝑎2 + 𝑥2 3/2
5

Magnetic Field Due to a Straight Current-Carrying Wire Using Biot–Savart Law
For an infinitely long wire, 𝑥varies from −∞to +∞.
+∞
| 𝜇 𝐼𝑎 | 𝑑𝑥  |     |
| ---- | --- | --- |
0
| 𝐵 = | න    |        |
| --- | ---- | ------ |
| 4𝜋  | 𝑎2 + | 𝑥2 3/2 |
−∞
| +∞  | 𝑑𝑥       | 2   |
| --- | -------- | --- |
| න   | =        |     |
| 𝑎2  | + 𝑥2 3/2 | 𝑎2  |
−∞
𝜇 𝐼𝑎 2
0
𝐵 =
4𝜋 𝑎2
𝜇 𝐼
0
𝐵 =
2𝜋𝑎
𝜇 𝐼
0
| 𝐵   | =   |     |
| --- | --- | --- |
2𝜋𝑎
6

Magnetic Field at the Centre of a Circular Current Loop
Consider a circular loop of radius 𝑅carrying a current 𝐼.
According to the Biot–Savart law, the magnetic field
produced by a small current element is
𝜇 𝐼 𝑑𝑙 sin 𝜃
0
𝑑𝐵 =
4𝜋 𝑅2
At the center of the circular loop, 𝜃 = 90∘ , so sin 𝜃 = 1.
Every current element produces a magnetic field in the same
direction at the center.
Integrating around the entire circumference, ׯ𝑑 𝑙 = 2𝜋𝑅,
gives
𝜇 𝐼
0
𝐵 =
2𝑅
The direction of the magnetic field is
For a coil of 𝑁turns,
determined by the right-hand thumb
𝜇 𝑁𝐼
0
𝐵 = rule
2𝑅
7

Magnetic Field at the Center of a Square Current Loop
Consider a square loop of side a carrying current I. Let O be the center of the square.The magnetic field at O is the sum
of the magnetic fields produced by the four straight sides.
Magnetic field due to one side
For a finite straight current-carrying conductor, the magnetic
field at a perpendicular distance 𝑟is
𝜇 𝐼
0
𝐵 = sin𝜃 + sin 𝜃
side 1 2
4𝜋𝑟
For a square of side 𝑎, the perpendicular distance from the
𝑎
center to any side is 𝑟 =
2
From the geometry of the square, 𝜃 = 𝜃 = 45∘
1 2
Therefore,
𝜇 𝐼
0
𝐵 = sin45∘ + sin 45∘
side
4𝜋 𝑎/2
1
sin45∘ = ,
2
𝜇 𝐼 2
0
𝐵 =
side
2𝜋𝑎 2
2 𝜇 𝐼
0
𝐵 =
side
2𝜋𝑎
8

Magnetic Field at the Center of a Square Current Loop
Magnetic field due to all four sides
By the right-hand rule, the magnetic fields produced by all four
sides at the center are in the same direction, perpendicular to the
plane of the square.
Therefore,𝐵 = 4 𝐵
side
Substituting,
2 𝜇 𝐼
0
𝐵 = 4
2𝜋𝑎
Thus, the magnetic field at the center of a square current loop is
2 2 𝜇 𝐼
0
𝐵 =
𝜋𝑎
For a square coil having 𝑁turns
2 2 𝜇 𝑁𝐼
𝐵 = 0
𝜋𝑎
The direction of 𝐵is perpendicular to the plane of the loop and is
determined using the right-hand thumb rule.
9

---

## Lecture 10: Boundary Conditions in Magnetostatics

# Lec10_Boundary Condtions_Mag

## Page 1

23ECE204 Electromagnetic Theory and Waves
(3-1-0-4)
S, B.Tech. ECE

Boundary Conditions

Dr. Sreedevi K. Menon

---

## Page 2

* According to the Gauss's law for the magnetic field,

Boundary Conditions for Magnetostatic Fields

§ Beds =0
s

The surface integral must be evaluated over three surfaces,
i) Top, ii) Bottom and iii) Lateral.

* Let the area of the top and bottom is same, equal to AS.

Medium
surface He

Boundary between two magnetic materials of different permeabilities top bottom lateral

f BedS+ § BedS+ f BedS = 0

For top surfaces
* As we are very much interested in the boundary conditions, reduce Ah to zero. As Ah — 0, the cylinder

tends to boundary and only top and bottom surfaces contribute in the surface integral. Thus surface f BedS = By, § dS =By AS
integrals are calculated for top and bottom surfaces only. These surfaces are very small. Let the magnitude

: . 7 " F f
of normal component of B be By; and By» in medium | and medium 2 respectively. As both the or bottom surface

f BedS = By, $ dS=By,as

surfaces are very small, we can assume B y; and B yp constant over their surfaces.
Bottom Bottom

For lateral surface

§ BedS = 0

By, AS-By,, AS = 0

---

## Page 3

Byni AS =By? AS

By

By
* Thus the normal component of B is continuous at the boundary.

+ As the magnetic flux density and the magnetic field intensity are related by, B = nH

Bui=By

Hy Hy, = Hon,

* Hence the normal component of { is not continuous at the boundary. The field strengths in two media

are inversely proportional to their relative permeabilities.

---

## Page 4

* According to Ampere's circuital law,
§ Hed =I

* Consider a rectangular closed path abeda as shown in the Fig. 8.8.1. It is traced in clockwise direction as
a-b-c-d-a. This closed path is placed in a plane normal to the boundary surface. Hence $ HedL canbe

divided into 6 parts.

§ Heal - [HedL+|HedL+] Heal +] Heat sf Heals | Heat =I
a b 1 d

c 2

Ke dw = Hani (AW) - Htan2 (Aw)
assume that Kis the surface current normal to the path.
Heant - Htan2
Ah Ah
Kedw = Hyg (QW)# Hy ( J} "| — — - =
Heant —Htanz = @Ny X* K
Ah Ah
Fa (40") Ha *} Ha 5") - ; a ; ;
* where 4/4, is the unit vector in the direction normal at the boundary from medium | to medium 2.

* To get conditions at boundary, Ah — 0. * For B, the tangential components can be related with permeabilities of two media

---

## Page 5

* Consider a special case that the boundary is free of current. K = 0.

Hiani - Htan2 = 0

+ For tangential components of B

---

## Page 6

Given that H1=—2ax +6ay +4az in region y - x - 2 < 0 where ul = 5u0, calculate

H2 and Bp inthe region y -x—2> Owhere 1 = 2u0

As y—X—2<0isa plane, the region | is givenasy-x<2,ie.y<x+2

Let the surface be defined as,
fix.y)=y-x-2

Then the unit vector normal to the plane is given by,

Then the normal component of H is given by,

Hi, - + a,)a, -|(-2a, +64, +4a,) «{ 2% || [2¥ =
1 = (Hin * @_) An =|(-2 a, +6 ay + am i Il Tz |

5 [0+2+6+0+0+0] (@y ~ax) = 4(@y ax)

Hy, - -4a,+4ay A/m
But H, - Hy, +Hy

Ay = Hy Ain

Hy = (-28, +6ay +4a,)-(4a, +44) = 24, +2a, +4, A/m

---

## Page 7

Using boundary conditions,
Hy = Hy =2a,+2a,+4a, A/m
Also Bon = By, ie. > Hop =H) Hin

7 His 5g
Now H = 1H, =—24
‘2n HM In 2H

[-4a, +4a,]=-10a, +10a, A/m

Hence Hy = Hoy +H =(-10 a, +10 ay)+(2a, +2 ay +42,)

an H, = —8a, +12a,+4a, A/m

But B= uH , hence we get,

By = > Hy =2u9 Hy = 2x4xnx107 [-8 a, +12 ay +4a,]
o B, = 2.5132x10-°(-8a, +124, +4a,)

” B, = —20.1056 a, +30.1584 ay +10.0528 a, wWb/m?

---

### Extracted Text (MarkItDown)

23ECE204 Electromagnetic Theory and Waves
 (3-1-0-4)
S3 B.Tech. ECE

Boundary Conditions

Dr. Sreedevi K. Menon

2

3

4

5

6

7

---

## Lecture 11: Maxwell's Equations & Time-Varying Electromagnetic Fields

# Lec11_Maxwell's Equation

23ECE204 Electromagnetic Theory and Waves
 (3-1-0-4)
S3 B.Tech. ECE

Maxwell’s Equations –
Static Field

Dr. Sreedevi K. Menon

1. Faraday’s Law of  Electrostatics

∇   × 𝑬 = 0

𝑬. 𝑑𝑙 = 0

ර
𝐶

•

Since the magnetic field is constant with time, it does not induce an
electric field.

• The electric field is conservative.
• Therefore, the work done in moving a charge around any closed path is

zero.

• Electric field can be expressed as
• Electrostatics, Potential difference calculations , Capacitor analysis

𝑬 = −∇𝑉

2. Ampère's Circuital Law

∇   × 𝑯 = 𝐽

𝑯. 𝑑𝑙 = 𝐼

ර
𝐶

Steady electric currents produce magnetic fields.

•
• The circulation of  the magnetic field around a closed path

equals the total current enclosed by that path.
Long straight conductors, Solenoids, Toroids, Electromagnets

•

2

3. Gauss's Law for Electric Fields

∇ . 𝑫 = 𝑣

𝑫. 𝑑𝑆 = 𝑄

ර
𝑆

• Electric charges are the sources (or sinks) of  electric fields.
• The total electric flux leaving a closed surface equals the charge enclosed

by that surface.
If  no charge exists inside the surface, the net electric flux is zero.

•
• Determining electric fields of  symmetric charge distributions
• Designing capacitors and insulation systems.

4. Gauss's Law for Magnetism

• Magnetic field lines always form closed loops.
• No isolated magnetic poles (magnetic monopoles) have been

∇ . 𝑩 = 0

𝑩. 𝑑𝑆 = 0

ර
𝐶

observed.

• The net magnetic flux through any closed surface is always zero.
• Magnetic circuit analysis.
• Transformer and motor design.

𝑩 = 0

𝑯

𝑫 = 0

𝑬

3

---

