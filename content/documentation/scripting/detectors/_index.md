+++
title = "Detectors"
weight = 25
+++

## Detectors

Every GISAS or off-specular simulation in BornAgain carries a detector object representing the real x-ray/neutron detector. The detector object has to be properly initialized before the simulation can start. Each detector is characterized by its size, the number of pixels and their shapes and finally by the detector's position/rotation with respect to the sample coordinate system.

There are two major types of detectors in BornAgain.

{{< figscg src="two_detectors.png" class="center">}}

The `SphericalDetector` object represents a portion of a sphere, whose center is located at the origin of the sample coordinate system. The spherical detector has a simple interface and serves as a good approximation of real detectors for the majority of small angle experimental setups.

The `RectangularDetector` object represents a more realistic, rectangular 2D detector. In particular, it allows to define an arbitrary position/orientation with respect to the sample and/or the beam.

Both detector types are explained in detail in the following sections of the tutorial.

* [Spherical detector]({{% relref "documentation/scripting/detectors/spherical-detector/index.md" %}})
* [Rectangular detector]({{% relref "documentation/scripting/detectors/rectangular-detector/index.md" %}})

### Masks

When fitting theoretical models to measured diffraction images,
it can be helpful to mask part of the detector area.
See

* [Fit with masks]({{% ref-example "fitting/advanced/fit-with-masks" %}})

### Resolution

For modeling the detector resolution, see

* [Detector resolution example]({{% ref-example "beam-and-detector/detector-resolution" %}})
