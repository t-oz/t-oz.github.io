---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

PDF version [here]({{ base_path }}/files/tyler-osborne-cv.pdf).

Education
======
* Ph.D. in Computer Science, Stony Brook University, 2028 (expected), advised by [Prof. Fusheng Wang](https://www3.cs.stonybrook.edu/~fuswang/)
* B.A. in Computer Science, Boston College, 2023, advised by [Prof. Amittai Aviram](http://www.amittai.com)
* B.S. in Management, Boston College, 2023

Work experience
======
* Spring 2024 -- Present: Research Assistant in BMIDB Lab at Stony Brook University
  * First-author journal article in *npj Digital Medicine*; collaborated with over a dozen internal medicine and primary care physicians.
  * Implemented HIPAA-compliant pipelines for large-scale processing of real-world clinical notes, resulting in high-quality automated discharge summary generation as evaluated by over a dozen internal medicine and primary care physicians.
  * Designed and built HIPAA-compliant full-stack applications for study data collection.

* Spring 2026 -- Fall 2026: Machine Learning Engineering Intern at Kouper Health (Since acquired by [Ellipsis Health](https://ellipsishealth.com))
  * Designed, implemented and benchmarked a referral extraction pipeline to ingest faxed referral forms and start agentic outbound calls to patients to schedule appointments, generating significant interest from clients.
  * Iterated inbound phone call quality assurance agent, resulting in improved precision and recall across metrics such as patient intent and frustration and better containment rates.
  * Evaluated various models and prompts to potentially upgrade components of inbound call agent and ruling out models which appeared superior on the surface but introduced behavioral regressions, resulting in organizational restraint on model upgrades and maintaining product reliability.

* Fall 2021 -- Spring 2024: Research Assistant for Cognitive States Project
  * Second-author publication in MIT’s ACL conference proceedings.
  * Designed unified database schema for training and testing examples extracted from said corpora.
  * Fine-tuned deep learning model to perform experiments as the lone undergrad on a team of professors and Ph.D. students.

* Spring 2021 -- Spring 2023: Information Technology Services Intern at Boston College
  * Assisted with organization of internal decision support website and University-wide SQL tutorial rollout.
  * Led numerous beginner/intermediate SQL workshops for audiences of various professional staff throughout the University.
  * Trained AI-powered course registration chatbot for the University to answer FAQs and reduce strain on help staff.

* Fall 2020 -- Fall 2021: Computer Science Instructor at Juni Learning
  * Guided 6+ students per week to achieve challenging programming curriculum via Zoom.
  * Conceived, developed and produced educational video explaining blockchain for national campaign.
  * Communicated professionally with parents, supervisors and peers.

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
* Fall 2023 -- Fall 2024: Graduate Teaching Assistant at Stony Brook University
  * Compilers (2 terms)
  * Computer Networks (1 term)
* Spring 2021 -- Summer 2023: Undergraduate Teaching Assistant at Boston College
  * Computer Systems (3 terms)
  * Compilers (2 terms)
  * Computer Networks (1 term)
  * Computer Architecture (1 term)
