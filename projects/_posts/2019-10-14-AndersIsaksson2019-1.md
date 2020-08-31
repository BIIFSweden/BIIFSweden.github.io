---
# Fill out as many of these as you can, and delete the rest.
# Text on a line after a "#" is a comment and is ignored for the published page.

title: "Feature extraction from tissue section output images"
author: ["Petter Ranefall"]
external: "Anders Isaksson, Padraic Corcoran, Department of Medical Sciences, UU"
excerpt: "Sectioning of formalin fixed tissues is a convenient way of obtaining image information on cell morphology and how cells make up tissues. The sections are usually stained with hematoxylin and eosin to..."
image: "/images/projects/2019-10-14-AndersIsaksson2019-1.png" # Image should be pushed to /images/projects/YYYY-MM-DD-projectid/ before
keywords: "Light microscopy, Model organisms and tissues"
funding: "SciLifeLab BioImage Informatics Facility (www.scilifelab.se/facilities/bioimage-informatics)"
initdate: "2019-10-14"
lastdate: "Current"
tags_: "None"
# project_homepage_url: "http://example.com/external-project-page" # Optional external homepage for this project
---

## Project Description
Sectioning of formalin fixed tissues is a convenient way of obtaining image information on cell morphology and how cells make up tissues. The sections are usually stained with hematoxylin and eosin to facilitate the identification of cells etc. Additional information on the expression of specific proteins can be obtained by immunohistochemical staining procedures.<br/><br/>Traditionally these stained sections have been analyzed manually looking through a microscope. That is a laborious process that is hard to standardize. With the development of new imaging technology high resolution image scans can now be recorded for such sections. That also allows the automated analysis of such digital images. Many such analyses results in an output image where the locations of particular cells or groups of cells are marked.<br/><br/>This project deals with how to extract relevant spatial information from those patterns of areas with particular cellular characteristics. Thus, we have decided on collecting basic statistical information from these patterns, such as homogeneity and granularity on different scales using CellProfiler. The extraction of such features can subsequently be used for unsupervised image analysis leading to identification of subgroups of samples with distinct patterns in the output images. This analysis could for instance be used for the identification of
