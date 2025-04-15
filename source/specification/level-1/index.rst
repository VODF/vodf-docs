=========
 Level-1
=========

VODF Level-1 contains data products related to specific
:term:`observations<observation>`, and in particular to :term:`events<event>` detected
by the given instrument as well as :term:`IRF` that describe how the parameters
of those events map to physical quantities. It also covers related information
such as time-series tables of data quality, instrumental or atmospheric
conditions.

Level-1 data is assumed to be already *pre-processed* by the instrument that
produces it. The pre-processing must include all calibration and
:term:`reconstruction` necessary to reduce the raw data of the instrument into a
set of physical estimated parameters per detected particle.

.. note:: VODF Level-1 is equivalent to *data level 3 (DL3)* defined by CTAO,
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


Data Products
=============
