# EMT-Sims: Future Roadmap & Computational Physics Evolution

EMT-Sims provides browser-native 3D interactive visualizations of classical electrodynamics, vector calculus, and Maxwell's equations using Three.js and WebGL. This document outlines computational extensions.

---

## 1. WebGPU Finite-Difference Time-Domain (FDTD) Engine

- **High-Performance WebGPU FDTD Solver**:
  - Implement Yee's algorithm in WebGPU compute shaders, enabling real-time transient electromagnetic wave propagation through arbitrary dielectric and magnetic obstacles at 60 FPS.
  - Interactive boundary condition toggles: Perfectly Matched Layers (PML) vs Perfect Electric Conductors (PEC).
- **Near-to-Far Field Transformation (NTFF)**:
  - Calculate 3D far-field radiation patterns and antenna directivity/gain plots directly from near-field time-domain boundaries.

---

## 2. RF Engineering & Guided Wave Labs

- **Interactive Smith Chart & Impedance Matching**:
  - Full-featured, drag-and-drop Smith chart visualizer computing VSWR, reflection coefficient ($\Gamma$), and single/double-stub matching circuits in real time.
- **Waveguide Cutoff & Mode Explorer**:
  - 3D field distributions for Rectangular ($TE_{10}, TE_{20}, TM_{11}$) and Circular ($TE_{11}, TM_{01}$) waveguides with adjustable guide dimensions and excitation frequencies.

---

## 3. Pedagogical Tools & VR Support

- **WebXR Immersive Physics Classroom**:
  - Enable WebXR headset navigation (Meta Quest / Apple Vision Pro) allowing students to walk around 3D vector fields, flux surfaces, and equipotential contour clouds.
