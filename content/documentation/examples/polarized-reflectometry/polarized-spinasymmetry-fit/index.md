+++
title = "Spin asymmetry fit example"
weight = 40
+++

### Fitting the spin-asymmetry example from NIST

This example shows how to fit the parameters in the [spin-asymmetry example]({{% ref-example "polarized-reflectometry/polarized-spinasymmetry" %}}).

For this demonstration, we choose initial parameters that are not too far from the fitting results.
In particular, the magnetization is initially set to zero, such that the spin asymmetry identically vanishes.

With the initial parameters, we obtain the following reflectivity and spin-asymmetry curves:

{{< galleryscg >}}
{{< figscg src="/files/manually-simulated/SpinAsymmetryInitial1.png" width="350px" caption="Reflectivity">}}
{{< figscg src="/files/manually-simulated/SpinAsymmetryInitial2.png" width="350px" caption="Spin Asymmetry">}}
{{< /galleryscg >}}




#### Setup of the Fit

For fitting of reflectometry data covering several orders of magnitude we use the $\chi^2$ metric

$$\chi^2 = \sum_{i = 1}^N  \frac{\left( d_i - s_i \right)^2}{\sigma_i^2}$$

Here $d_i$ is the $i$-thexperimental data point, $\sigma_i$ is its uncertainty and 
$s_i$ is the corresponding simulation result.

This is supported in BornAgain by setting

{{< highlight python>}}
fit_objective.setObjectiveMetric("chi2")
{{< /highlight >}}

It must be noted, that in order to obtain good results, one needs to provide the uncertainties 
of the reflectivity.
If no uncertainties are available, using the relative difference `fit_objective.setObjectiveMetric("reldiff")` yields better results.
If the relative difference is selected and uncertainties are provided, BornAgain automatically falls back to the above $\chi^2$ metric.

The fitting of polarized reflectometry data proceeds similar to the lines presented in
[the tutorial on multiple datasets]({{% ref-example "fitting/advanced/multiple-datasets" %}}).
We need to add the reflectivity curves for the up-up and down-down channel
to the fit objective:

{{< highlight python>}}
fit_objective.addSimulationAndData( SimulationFunctionPlusplus,
                                    r_data_pp, r_uncertainty_pp, 1.0)
fit_objective.addSimulationAndData( SimulationFunctionMinusMinus,
                                    r_data_mm, r_uncertainty_mm, 1.0)
{{< /highlight >}}

`SimulationFunctionPlusplus` and `SimulationFunctionMinusMinus` are two function objects that return a simulation result for
the up-up and down-down channels, respectively.

The fit parameters are defined in the dictionary `startParams`, where they are defined as a triple of values `(start, min, max)`.
If no fit is performed the values obtained from our own fit are stored in `fixedParams` and are subsequently used
to simulate the system.

We want to fit the following parameters:

* `q_res`: Relative $Q$-resolution
* `q_offset`: Shift of the $Q$-axis.
* `t_Mafo`: The thickness of the layer
* `rho_Mafo`: The SLD of the layer
* `rhoM_Mafo`: The magnetic SLD of the layer
* `r_Mao`: The roughness on top of the substrate
* `r_Mafo`: The roughness on top of the magnetic layer


#### Fit Result

After running the fit using

{{< highlight python>}}
python3 PolarizedSpinAsymmetryFit.py fit
{{< /highlight >}}


we get the result

{{< galleryscg >}}
{{< figscg src="/files/manually-simulated/SpinAsymmetry1.png" width="350px" caption="Reflectivity">}}
{{< figscg src="/files/simulated/PolarizedSpinAsymmetry.png" width="350px" caption="Spin Asymmetry">}}
{{< /galleryscg >}}


This result was already presented in the [spin-asymmetry]({{% ref-example "polarized-reflectometry/polarized-spinasymmetry" %}}) tutorial and
can also be obtained by runnning the example without the fit option:

{{< highlight python>}}
python3 PolarizedSpinAsymmetryFit.py
{{< /highlight >}}


Here is the complete example:

{{< highlightfile file="/static/files/python/simulation/ex06_Reflectometry/PolarizedSpinAsymmetryFit.py"  language="python" >}}
