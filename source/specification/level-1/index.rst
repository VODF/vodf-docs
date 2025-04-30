=========
 Level-1
=========

VODF Level-1 contains data products related to specific
:term:`observations<observation>`, and in particular to :term:`events<event>` detected
by a given instrument as well as :term:`IRF` that describe how the parameters
of those events map to physical quantities. This data level may contain extra information on
the instrument pointing, provenance information, :term:`stable time intervals or instrumental good time intervals<SOI>`, systematics error or quality estimation of the :term:`IRF`. It also covers related information
such as time-series tables of data quality, instrumental or atmospheric conditions.

Level-1 data products are assumed to be already *pre-processed* by the instrument that
produces them. The pre-processing must include all calibration and
:term:`reconstruction` necessary to reduce the raw data of the instrument into a
set of physical estimated parameters per detected particle.

.. tip:: VODF Level-1 is equivalent to *data level 3 (DL3)* defined by CTAO,
          also called "science-ready data". In CTAO, levels DL0-DL2 constitute
          the *raw* and *pre-processed* data levels that are out of scope for
          VODF.

Data Model
==========

.. uml:: level-1.plantuml
   :caption: VODF **Level-1** Data Model

Observations
------------

The **Observation** forms the core of the `Level-1` data model. Note that we use
the term "Observation" more generally than one might expect: an :term:`observation` is
not simply related to the act of recording data with a telescope, but rather to
the process of *recording and processing* the data. Therefore each new *Data
Release* results in new *Observations*. This might seem strange, but it ensures
there is a unique link to data products when the lower-level processing of them
changes or improves. One way to think about it is that :term:`VHE` instruments
are not purely hardware, but a combination of hardware and software, and the
details of the *low-level data processing changes the characteristics of the
instrument*. With improvements to this low-level processing, the sensitivity,
angular resolution, energy resolution, and other factors can change. A second
consequence of :term:`observations<observation>` being software-defined is that the
minimal duration is therefore up to the observatory. It can be directly related
to one *data acquisition interval*, but can also be a subset or concatenation of
many.

A critical point is that an *Observation* is the minimum unit of what may be
discovered by users knowing only the instrument name, a data release name, a
time interval, and a sky region.

Data Releases
-------------

TBD


Coverage
--------

.. uml:: coverage.plantuml
   :caption: VODF **Level-1 Coverage** Data Model

EventList
----------

.. uml:: eventlist.plantuml
   :caption: VODF **Level-1 EventList** Data Model

IRF
---

.. uml:: irf.plantuml
   :caption: VODF **Level-1 IRF** Data Model

The :term:`IRF` contains the information necessary to map instrumental
:term:`reconstructed <reconstruction>` parameters of the event to *physical*
parameters, i.e. it allows one to transform from a physical *flux* in a given
space-time-spectral interval into a predicted number of detected *counts* for a
given instrument. The IRF is often decomposed into a set of independent
``IRFComponents``, e.g. by separating spatial and spectral aspects. An IRF may
also vary in time, due to changing observation conditions, or instrumental
degradation. The assumption in VODF is that time variations are ignored and
therefore an :term :`observation` is broken into pieces where the IRF remains
stable, and residual variations are handled by adding instrumental parameters.

.. tip::

   Science analysis with event-counting instruments often involves fitting a
   physical model to observed data. The standard technique is a *maximum
   likelihood fit* using *forward folding*, where the physical model is passed
   through the IRF to transform flux (physical units) into predicted counts
   (instrumental units), and the fit is performed on this transformed quantity
   by comparing the predicted to measured counts. The opposite process,
   *unfolding*, where instrumental uncertainties are removed by deconvolution
   and the model is fit in physical units gives unstable results when data or
   IRFs contain instrumental or statistical noise.


StandardIRF
~~~~~~~~~~~

For VODF, we provide a commonly used decomposition of the :term:`IRF` that
separates the response :math:`\hat R` from the background rate :math:`B`. This
is convenient since :math:`\hat R` is usually computed from simulations, while
:math:`B` can be computed from observed data using blank fields. Then, the
predicted instrumental counts :math:`N` can be computed for a given flux
:math:`F` as:

.. math::

   N(\vec{p}', E' | \vec{p}, E) = \int d\Omega dE \;  \hat{R}(\vec{p}',E'|\vec{p},E) \, F(\vec{p}, E)  +  \int d\Omega dE \; B(\vec{p}', E')

where :math:`(\vec{p}, E)` are the *true* primary particle point of origin and
its energy, and :math:`(\vec{p}',E')` are the corresponding :term:`reconstructed
<reconstruction>` quantities. The coordinate system for :math:`\vec p` is
usually represented in polar coordinates relative to the FOV center, though
other representations are possible. Then, we decompose :math:`R` into the
following components:

.. math::

    R(E', {\vec{p'}} | E, \vec{p}, t) =
    \underbrace{A_\text{eff}(E, \vec{p}, t)}_{{\text{Effective Area}}}
    \cdot \overbrace{M(E' | E, \vec{p}, t)}^{{\text{Energy Migration}}}
    \cdot \underbrace{P(\vec{p'} | E, \vec{p}, t)}_{{\text{Point Spread Function}}}.


Effective Collection Area Function (:math:`A_\mathrm{eff}`, ``EffectiveArea``)
    Given a set of physical parameters, provides the collection area of the
    instrument, computed usually from detailed simulations as the ratio of the
    number of detected events to the total simulated multiplied by the area over
    which they were simulated, for given true position in the field of view and
    true energy.

Point-Spread Function (:math:`P`, ``PSF``)
    The probability to reconstruct an event a point :math:`\vec p'` in the FOV
    if it had a true position :math:`\vec p`. Positional bias is ignored,
    therefore it represents only the dispersion, i.e. the mean reconstructed
    position is assumed equal to the true position.

Energy Migration Function (:math:`M`, ``EnergyMigration``)
    The probability to reconstruct the energy as :math:`E'` for a given true
    energy :math:`E`, including both dispersion and bias. This sometimes called
    the *energy redistribution matrix*, or the *redistribution matrix file
    (RMF)*.

Background Rate Function (:math:`B`, ``BackgroundRate``)
    The expected rate of background events (in counts/second) at a given point
    :math:`\vec p` and energy `E`. Often, the real rate is difficult to compute
    correctly without real data due to e.g. atmospheric uncertainties, and
    therefore it is important to note that it may need to be calibrated using
    real data. I.e. the shape should be correct, but the normalization may need
    to be refined.

.. note::

   This decomposition ignores cross-terms, like the correlation between spectral
   and spatial resolution, which can be important in some cases. Future versions
   of VODF may include more detailed decompositions.


.. todo::

   Discuss event types here?


OnTime
------

.. uml:: ontime.plantuml
   :caption: VODF **Level-1 OnTime** Data Model


Pointing
--------

.. uml:: pointing.plantuml
   :caption: VODF **Level-1 Pointing** Data Model




Data Products
=============
