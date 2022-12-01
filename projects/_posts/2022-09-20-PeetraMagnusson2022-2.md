---
# Fill out as many of these as you can, and delete the rest.
# Text on a line after a "#" is a comment and is ignored for the published page.

title: "DL segmentation for immunofluorescent imaging of mouse brains"
author: ["Robert Welch"]
external: "Ross Smith"
# excerpt: ""
keywords: "Immunofluorescent, cerebral cavernous malformations, deep learning, segmentation"
funding: "SciLifeLab BioImage Informatics Facility (www.scilifelab.se/facilities/bioimage-informatics)"
initdate: "2022-09-20"
lastdate: "2022-11-08"
# tags_: ""
github: "https://github.com/BIIFSweden/PeetraMagnusson2022-2"
image: "/images/projects/2022-09-20-PeetraMagnusson2022-2.png"


---

## Project Description
In this project, we are looking at immunofluorescent staining of mouse brain cryosections for the study of cerebral cavernous malformations. A necessary task for analysing each image is marking the cerebellum, in effect differentiating this brain region from other neighbouring brain structures present in the image. A U-Net model with a ResNet-50 encoder was trained with previously generated manual annotations to automate this process. The resulting python-based tool carries out cerebellum segmentation, generating a predicted region of interest (ROI) from a supplied DAPI image.