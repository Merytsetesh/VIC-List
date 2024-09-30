# VIC-List

## The Little VIC-20 Program Listing Tool


### 1. Introduction

Thank you for visiting!

VIC-List is a suite of Python modules for working with VIC-20 programs. Its current functionality is as follows:

* Loads and saves programs in `.PRG` format.
* Loads and saved programs in plain text.
* A _renumber_ module which can renumber destinations after `ON..GOTO` and `ON..GOSUB`.
* Print program listings to PDF documents.

---


### 2. Setup

1. Download the VIC-List suite from GitHub to some convenient location.

2. Install the `reportlab` package.

3. Download and install the PetMe font from http://www.kreativekorp.com/software/fonts/c64.shtml. VIC-List expects the font files to be in a directory within its own installation directory.

---


### 3. Using `Vic-List`

Example code can be found in `mainprog.py`.

---


### 4. Sample output

Sample `VIC-List` output has been included.

1. `Dungeon.prg` has been printed and saved in plain text twice, both before and after renumbering.

2. `Glyphs.pdf` displays the entire VIC-20 character set.

The _Dungeon_ game remains copyright (C) Clifford Marshall and Melbourne House; no intent to infringe copyright is intended.

---

### 5. Known issues

1. Generating a PDF when a document with the same name is currently open will cause a crash.

---

### 6. Contributing

I would love your help! Contribute by forking the repo and opening pull requests.

All pull requests should be submitted to the `main` branch.

Thank you. :-)


---
---



## `VIC-List` is copyright (C) 2019 Merytsetesh.

License (OLC-3)

Copyright 2019- Merytsetesh

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions or derivations of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions or derivative works in binary form must reproduce the above copyright notice. This list of conditions and the following disclaimer must be reproduced in the documentation and/or other materials provided with the distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
