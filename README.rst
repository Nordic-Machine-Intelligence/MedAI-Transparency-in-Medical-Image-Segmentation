************************************************
MedAI-Transparency-in-Medical-Image-Segmentation
************************************************

This Github repository contains a starter code for `the Kvasir-SEG Dataset <https://datasets.simula.no/kvasir-seg/>`_ [#]_  and `the Kvasir-Instrument Dataset <https://datasets.simula.no/kvasir-instrument/>`_ [#]_

Data:
=====

Kvasir-SEG Dataset
^^^^^^^^^^^^^^^^^^

The Kvasir-SEG dataset (size 46.2 MB) contains 1000 polyp images and their corresponding ground truth from the Kvasir Dataset v2 [1].
The dataset can be downloaded here:
`https://datasets.simula.no/kvasir-seg <https://datasets.simula.no/kvasir-seg/>`_

.. image:: https://www.nora.ai/Competition/2dadc75e-8fca-4411-88a0-65a3f1cc92be.jpeg
**Figure 1:** The Kvasir-SEG Dataset contains 1000 images of segmented polyps


Kvasir-Instrument Dataset
^^^^^^^^^^^^^^^^^^^^^^^^^
The Kvasir-Instrument dataset (size 170 MB) contains 590 endoscopic tool images and their ground truth mask [2].
The dataset can be downloaded here:
`https://datasets.simula.no/kvasir-instrument/ <https://datasets.simula.no/kvasir-instrument/>`_

.. image:: https://datasets.simula.no/kvasir-instrument/static/images/example_1.jpg
**Figure 2:** The Kvasir-SEG Dataset contains 590 endoscopic tool images

Run the code:
-------------
You can run the code by follwing this steps:
#. Fork and clone this repository
#. Download the data and extract it to the same folder as the two Jupyter notebooks in this repository
    
 | hyperkvasir-starter-code.ipynb
 | kvasir-instrument-starter-code.ipynb
 | ├── kvasir-instrument         
 | │   ├── A0001.hea
 | │   ├── A0001.dat
 | │   ├── A0002.hea
 | │   ├── A0002.dat
 | │   └── Axxxx.dat
#. Run the code!

References:
===========

.. [#] Debesh Jha, Pia H. Smedsrud, Michael A. Riegler, Pål Halvorsen, Dag Johansen, Thomas de Lange, and Håvard D. Johansen, Kvasir-SEG: A Segmented Polyp Dataset, In Proceedings of the ternational conference on Multimedia Modeling, Republic of Korea, 2020.
.. [#] Jha, Debesh, et al. “Kvasir-instrument: Diagnostic and Therapeutic Tool Segmentation Dataset in Gastrointestinal Endoscopy.” OSF Preprints, 15 Aug. 2020. Web



