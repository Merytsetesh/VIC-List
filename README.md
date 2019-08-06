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
---



## `VIC-List` is copyright (C) 2019 Simon Ellis.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.