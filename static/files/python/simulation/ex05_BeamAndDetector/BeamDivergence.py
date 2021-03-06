"""
Cylinder form factor in DWBA with beam divergence
"""
import bornagain as ba
from bornagain import deg, nm


def get_sample():
    """
    Returns a sample with uncorrelated cylinders on a substrate.
    """

    # Define materials
    material_Particle = ba.HomogeneousMaterial("Particle", 0.0006, 2e-08)
    material_Substrate = ba.HomogeneousMaterial("Substrate", 6e-06, 2e-08)
    material_Vacuum = ba.HomogeneousMaterial("Vacuum", 0.0, 0.0)

    # Define form factors
    ff = ba.FormFactorCylinder(5.0*nm, 5.0*nm)

    # Define particles
    particle = ba.Particle(material_Particle, ff)

    # Define particle layouts
    layout = ba.ParticleLayout()
    layout.addParticle(particle, 1.0)
    layout.setWeight(1)
    layout.setTotalParticleSurfaceDensity(0.01)

    # Define layers
    layer_1 = ba.Layer(material_Vacuum)
    layer_1.addLayout(layout)
    layer_2 = ba.Layer(material_Substrate)

    # Define sample
    sample = ba.MultiLayer()
    sample.addLayer(layer_1)
    sample.addLayer(layer_2)

    return sample


def get_simulation(sample):
    beam = ba.Beam(1.0, 0.1*nm, ba.Direction(0.2*deg, 0*deg))
    detector = ba.SphericalDetector(100, 2*deg, 1*deg, 1*deg)
    simulation = ba.GISASSimulation(beam, sample, detector)
    distr_1 = ba.DistributionLogNormal(0.1*nm, 0.1)
    simulation.addParameterDistribution("*/Beam/Wavelength", distr_1, 5, 0.0)
    distr_2 = ba.DistributionGaussian(0.2*deg, 0.1*deg)
    simulation.addParameterDistribution("*/Beam/InclinationAngle", distr_2, 5,
                                        0.0)
    distr_3 = ba.DistributionGaussian(0*deg, 0.1*deg)
    simulation.addParameterDistribution("*/Beam/AzimuthalAngle", distr_3, 5,
                                        0.0)
    return simulation


if __name__ == '__main__':
    import ba_plot
    sample = get_sample()
    simulation = get_simulation(sample)
    ba_plot.run_and_plot(simulation)
