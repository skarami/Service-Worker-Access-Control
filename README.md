## Service Worker Access Control
This is a tool for implementing an access control mechanism in service workers to prevent exploiting its isolation issue.

## Research paper
This tool was proposed to prevent the History Sniffing attacks mention in the paper.

**Awakening the Web's Sleeper Agents: Misusing Service Workers for Privacy Leakage** [pdf](http://https://www.cs.uic.edu/~skarami/files/sw21/sw21.pdf "pdf")

Soroush Karami, Panagiotis Ilia, and Jason Polakis
In Proceedings of 28th Network and Distributed System Security Symposium (NDSS'21), 2021.

 ``` tex
@inproceedings {swNdss2021,
author={Karami, Soroush and Ilia, Panagiotis and Polakis, Jason},
title = {Awakening the Web's Sleeper Agents: Misusing Service Workers for Privacy Leakage},
booktitle = {28th Annual Network and Distributed System Security Symposium, {NDSS}
2021, San Diego, California, USA, February 21-24, 2021},
year = {2021},
publisher = {The Internet Society},
} 
```

## Using
`defense.py -w path_to_whiteList_file -i path_to_js_file -o output_file`
