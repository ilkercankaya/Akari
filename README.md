# Akari
Akari is a game which consists of black boxes, white boxes and light bulbs. Each of the light bulbs lightens the white boxes to a block or the outer frame along x-axis and y-axis.  

![Boloxorz](https://www.researchgate.net/profile/Andrew_Parkes/publication/220174445/figure/fig5/AS:277313137725445@1443128012478/A-completed-Light-Up-Puzzle.png)

##### [You can play Akari here](https://www.puzzle-light-up.com)

## Goal

_Modeling Akari as a CSP to solve a given stage._

Akari player has 3 goals:  
* Each black box that has a number inside it must have specified amount of light bulb around it. (Must be within x-axis or y-axis)  
* Each white box must be enlightened by a light bulb
* No light bulbs can be placed in the same row and column if there is no black box between them.

## The Files

`SolveAkari.py:` Contains a board representaion of Akari as well as constraint representation implementation with akari.


## Library used

[python-constraint](https://pypi.org/project/python-constraint)

## Example solutions found by the algorithm

- `xij` represents a white box location with matrix indexing. `i:` row number, `j:` column number.
- 1's indicate white bulbs and zero's indicate no light bulbs president in that white box.

`[{'x22': 0, 'x42': 1, 'x12': 0, 'x25': 0, 'x32': 0, 'x41': 0, 'x43': 0, 'x44': 0, 'x23': 0, 'x24': 0,  
'x34': 1, 'x51': 0, 'x53': 0, 'x54': 0, 'x31': 1, 'x03': 0, 'x30': 0, 'x35': 0, 'x36': 0,   
'x11': 0, 'x13': 1, 'x55': 1, 'x01': 0, 'x16': 0, 'x15': 1, 'x50': 1, 'x63': 1, 'x62': 0, 'x65': 0,  
 'x60': 0, 'x20': 1, 'x46': 1, 'x66': 1, 'x00': 1, 'x04': 1, 'x06': 1}]`


## More Information with A Report
[Report](ReportAkari.pdf)
