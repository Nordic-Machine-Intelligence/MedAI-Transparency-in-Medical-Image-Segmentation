************************************************
MedAI-Transparency-in-Medical-Image-Segmentation
************************************************

This Github repository contains a starter code for `the Kvasir-SEG Dataset <https://datasets.simula.no/kvasir-seg/>`_ [#]_  and `the Kvasir-Instrument Dataset <https://datasets.simula.no/kvasir-instrument/>`_ [#]_



.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/github/stars/Nordic-Machine-Intelligence/MedAI-Transparency-in-Medical-Image-Segmentation
        :target: https://github.com/Nordic-Machine-Intelligence/MedAI-Transparency-in-Medical-Image-Segmentation/stargazers

.. image:: https://img.shields.io/github/forks/Nordic-Machine-Intelligence/MedAI-Transparency-in-Medical-Image-Segmentation
        :target: https://github.com/Nordic-Machine-Intelligence/MedAI-Transparency-in-Medical-Image-Segmentation/network

.. image:: https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg
   :target: https://GitHub.com/Nordic-Machine-Intelligence/MedAI-Transparency-in-Medical-Image-Segmentation/hyperkvasir-starter-code.ipynb/releases/)
   
Data:
=====

Kvasir-SEG Dataset
^^^^^^^^^^^^^^^^^^

The Kvasir-SEG dataset (size 46.2 MB) contains 1000 polyp images and their corresponding ground truth from the Kvasir Dataset v2 [1].
The dataset can be downloaded here:
`https://datasets.simula.no/kvasir-seg <https://datasets.simula.no/kvasir-seg/>`_

.. image:: https://www.nora.ai/Competition/2dadc75e-8fca-4411-88a0-65a3f1cc92be.jpeg
**Figure 1:** The Kvasir-SEG Dataset contains 1000 images of segmented polyps [1]


Kvasir-Instrument Dataset
^^^^^^^^^^^^^^^^^^^^^^^^^
The Kvasir-Instrument dataset (size 170 MB) contains 590 endoscopic tool images and their ground truth mask [2].
The dataset can be downloaded here:
`https://datasets.simula.no/kvasir-instrument/ <https://datasets.simula.no/kvasir-instrument/>`_

.. image:: https://datasets.simula.no/kvasir-instrument/static/images/example_1.jpg
**Figure 2:** The Kvasir-SEG Dataset contains 590 endoscopic tool images [2]

Starter code:
-------------
The two jupyter notebooks in this repository give you a fundament for staring the development of the polyp and instrument segmentation tasks. As a baseline model we have provided a Unet build with Keras. Finally, we run the model inside a 10-fold cross-validation loop and we encourage the participants to also use som kind of resampling methods when reporting the results on the development set in the final paper to Nordic Machine Intelligence. 

Run the code:
-------------

You can run the code by Fork and clone this repository. Then download the datasets and extract them to this cloned repository.
The folder structrure should look like this: 
    
 | ├── hyperkvasir-starter-code.ipynb
 | ├── kvasir-instrument-starter-code.ipynb
 | ├── kvasir-instrument         
 | │   ├── bboxes.json
 | │   ├── test.txt
 | │   ├── train.txt
 | │   ├── images
 | │   └── masks
 | ├── kvasir-SEG        
 | │   ├── kavsir_bboxes.json
 | │   ├── test.txt
 | │   ├── train.txt
 | │   ├── images
 | │   └── masks

 
Finally, yo should pip install the necessary python packages and then you can run the code!

References:
===========

.. [#] Debesh Jha, Pia H. Smedsrud, Michael A. Riegler, Pål Halvorsen, Dag Johansen, Thomas de Lange, and Håvard D. Johansen, Kvasir-SEG: A Segmented Polyp Dataset, In Proceedings of the ternational conference on Multimedia Modeling, Republic of Korea, 2020.
.. [#] Jha, Debesh, et al. “Kvasir-instrument: Diagnostic and Therapeutic Tool Segmentation Dataset in Gastrointestinal Endoscopy.” OSF Preprints, 15 Aug. 2020. Web



