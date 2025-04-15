Level-1
=======

VODF Level-1 contains data products related to specific
:term:`observations<observation>`, in particular: an :term:`event-list`
:term:`IRF`, and time-series tables of instrumental or atmospheric conditions.

Level-1 data is assumed to be already pre-processed by the instrument that
produces it. The pre-processing is assumed to include all calibration and
:term:`reconstruction` necessary to reduce the raw data of the instrument into a
set of physical estimated parameters per detected particle.

.. note:: VODF Level-1 is equivalent to *data level 3 (DL3)* defined by CTAO,
          also called "science-ready data". In CTAO, levels DL0-DL2 constitute
          the *raw* and *pre-processed* data levels that are out of scope for
          VODF.

The **Observation** forms the core of the `Level-1` data model. Note that we use
the term "Observation" more generally than one might expect: an observation is
not simply related to the act of recording data with a telescope, but rather to
the process of *recording and processing* the data. Therefore each new *Data
Release* results in new *Observations*. This might seem strange, but it ensures
there is a unique link to data products when the lower-level processing of them
changes or improves. One way to think about it is that :term:`VHE` instruments
are not purely hardware, but a combination of hardware and software, and the
details of the *low-level data processing changes the characteristics of the
instrument*. With improvements to this low-level processing, the sensitivity,
angular resolution, energy resolution, and other factors can change.

.. uml:: level-1.plantuml
   :caption: VODF **Level-1** Data Model


Data Products
-------------
