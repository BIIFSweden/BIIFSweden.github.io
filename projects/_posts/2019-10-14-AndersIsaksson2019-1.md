---
# Fill out as many of these as you can, and delete the rest.
# Text on a line after a "#" is a comment and is ignored for the published page.

title: "Feature extraction from tissue section output images"
author: ["Petter Ranefall"]
external: "Anders Isaksson, Padraic Corcoran, Department of Medical Sciences, UU"
keywords: "Light microscopy, Model organisms and tissues"
funding: "SciLifeLab BioImage Informatics Facility (www.scilifelab.se/facilities/bioimage-informatics)"
initdate: "2019-10-14"
lastdate: "Current"
tags_: "None"
thumbnail_override: "/images/projects/2019-10-14-AndersIsaksson2019-1/5e2074cb59378.png"

# author: [ "" ] # your GitHub user name
# or make a list if there is more than one author
# author: [ "@person1", "@person2", "person without GitHub account" ]

# project_homepage_url: "http://example.com/my-super-cool-project" # Homepage for this project
# source_code_url: "https://github.com/myuser/myrepo" # Provide a link to your code
# building_instructions_url: "http://example.com/building-instructions.pdf" # how to build the model out of LEGO (*not* how to build the source code)

excerpt: "Sectioning of formalin fixed tissues is a convenient way of obtaining image information on cell morphology and how cells make up tissues. The sections are usually stained with hematoxylin and eosin to..."
---

![Feature extraction from tissue section output images](/images/projects/2019-10-14-AndersIsaksson2019-1/5e2074cb59378.png){: .img-responsive}
## Project Description
Sectioning of formalin fixed tissues is a convenient way of obtaining image information on cell morphology and how cells make up tissues. The sections are usually stained with hematoxylin and eosin to facilitate the identification of cells etc. Additional information on the expression of specific proteins can be obtained by immunohistochemical staining procedures.<br/><br/>Traditionally these stained sections have been analyzed manually looking through a microscope. That is a laborious process that is hard to standardize. With the development of new imaging technology high resolution image scans can now be recorded for such sections. That also allows the automated analysis of such digital images. Many such analyses results in an output image where the locations of particular cells or groups of cells are marked.<br/><br/>This project deals with how to extract relevant spatial information from those patterns of areas with particular cellular characteristics. Thus, we have decided on collecting basic statistical information from these patterns, such as homogeneity and granularity on different scales using CellProfiler. The extraction of such features can subsequently be used for unsupervised image analysis leading to identification of subgroups of samples with distinct patterns in the output images. This analysis could for instance be used for the identification of
