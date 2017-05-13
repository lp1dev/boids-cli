## Boids CLI
1;2802;0c
Boids CLI is a command-line representation of the boids algorithm, used to represent flocks (of 'boids') mostly.

### Requirements

- Python3.X

### Installation

- pip install -r requirements.txt

### Usage

- ./boids-cli

boids-cli will generate a random number of animated boids with random speeds and positions, calculated based on your terminal size.

![screenshot](https://raw.githubusercontent.com/lp1dev/boids-cli/master/boids.gif)

### About

Only the two first rules of the algorithm are implemented, since we're using integers as coordinates there is no real notion of velocity in this implementation.
