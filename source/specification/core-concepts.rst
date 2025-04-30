Core Concepts
=============

This describes the overall data model of VODF and how its  component parts are
inter-related.

Data Levels
-----------

.. todo::

   Describe high-level relationship between L1 to L4

Common Types
------------

.. uml::

   !include common.inc
   class TimeStamp

Maps and N-Dimensional Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




PDGID
~~~~~

.. uml::

   !include common.inc
   class PDGID <<integer>>


Particle ids used in VODF shall follow the integer `https://particle.wiki/wiki/PDG_particle_numbering_scheme <Particle Data Group Numbering Scheme>`_, e.g.:


.. csv-table:: Some example PDGIDs
   :header: "Particle","ID"
   :widths: 1,5

   ":math:`\gamma`", 22
   ":math:`e-`", 11
   ":math:`p`", 2212
   ":math:`\nu_e`", 12
   ":math:`\nu_\mu`", 14
   ":math:`\nu_\tau`",16
