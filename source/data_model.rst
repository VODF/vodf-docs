.. Licensed under a 3-clause BSD style license - see LICENSE.rst

==========
Data Model
==========

Diagram(s) of top-level model
-----------------------------

Glossary
--------

.. glossary::

    IACT
      Short for "Imaging Atmospheric Cherenkov Telescope"
    
    IRF
      Short for "Instrument Response Function". The set of IRFs allows to transform the measurements in detector units/coordinates to astrophysical quantities with physical units/coordinates

    Observation
      Within our project, an observation should be seen as the minimal set of Science-Ready data (DL3/L1, ie events list + IRFs) that a user can fetch. This set can be discovered by users using the instrument name, the observation time and a sky region. The minimal size definition is up to the observatory/experiment. It can be one  data acquisition sequence (associated with an `obs_id`), a subset based on any parameter or a merge of sequences.
    
    PR
      Short for "Pull Request"
    
    SOI
      Short for "Stable Observation Interval". It is a time interval during which the IRFs are considered as stable, within systematics.

    WCD
      Short for "Water Cherenkov Detector"
