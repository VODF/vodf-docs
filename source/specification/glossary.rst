Glossary
========

.. glossary::

    event-list
      A table of information about detected particles, including their
      reconstructed arrival time, position on the sky, and energy. Depending on
      the specifics of the detector that measured them, other reconstructed
      information may be included, such as signal/background classification
      parameters.

    IACT
      Short for "Imaging Atmospheric Cherenkov Telescope"

    IRF
      Short for "Instrument Response Function". The set of IRFs allows to transform the measurements in detector units/coordinates to astrophysical quantities with physical units/coordinates

    Observation
      Within our project, an observation should be seen as the minimal set of Science-Ready data (DL3/L1, ie events list
      + IRFs) that a user can fetch. This set can be discovered by users using, at minima, the instrument name, the
      observation time and a sky region. The minimal size definition is up to the observatory/experiment. It can be one
      data acquisition sequence (generally associated with an `obs_id`), a subset based on any parameter or a merge of
      sequences.

    reconstruction
      For VHE data, reconstruction is the act of estimating physical parameters of the detected particle (photon, neutrino, cosmic ray) from lower-level instrumental parameters.  For example, for an IACT, one might reconstruct a gamma ray photon's energy from the Cherenkov light intensity and geometric parameters of the detected air-shower.

    PR
      Short for "Pull Request"

    SOI
      Short for "Stable Observation Interval". It is a time interval during
      which the IRFs are considered as stable, within systematics.

    VHE
      Very-High-Energy, i.e. pertaining to particles roughly in the energy range
      of a few GeV to hundreds of TeV.

    WCD
      Short for "Water Cherenkov Detector"

