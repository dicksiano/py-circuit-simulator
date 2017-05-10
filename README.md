# Py Circuit Simulator

This project aims to develop a simulator for digital circuits that is capable of:
* Allow the user to draw digital circuits.
* Evaluate output of digital circuits.
* Draw the Timing Diagram.

## Class hierarchy

* Assets
* Editor
    * Mouse
    * Screen
    * Component (abstract)
        * MenuToolbar
        * Toolbar
            * ToolbarButton
        * Gates
            *GateFanInOne
                * IN, OUT, NOT
            * GateFanInTwo
                * OR, AND, NOR, NAND, XOR, XNOR
        * Wires
            * Wire
* Result
    * Waveform
* Simulator
    * Simulation