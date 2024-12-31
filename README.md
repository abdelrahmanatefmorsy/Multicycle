# Team Project

This project is a simulator for a custom assembly language with a GUI built using Tkinter. It simulates the working of registers, assembly instructions, and cycles of an MIPS-like architecture.

## Project Structure

1. Main Application (main.py): The core of the program, responsible for creating the GUI and handling user input for assembly code execution.
2. Classes (classes.py): Contains custom classes for various components of the GUI, including the text area with line numbers, registers, and graphical components like lines and rectangles.
3. Code Check (code_check.py): Handles the validation and parsing of assembly code.
4. Run (Run.py): Responsible for executing the assembly code, simulating cycles, and updating the state of the registers.

## Features

Register Table: Displays a list of registers with their current values.
Dynamic Entry System: Users can add new entries and simulate different assembly operations.
Code Editor: A text editor with line numbers where users can input assembly code.
Cycle Simulation: Simulates the execution of assembly instructions and updates the register values accordingly.
Reset: Allows users to reset the register values to their initial state.

## How to Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:

bash
git clone https://github.com/abdelrahmanatefmorsy/Multicycle/tree/main/multicycle


## How to Compile and Run



## Usage
1. Register Table: The table shows a list of registers with their values. You can simulate changes to these values by executing assembly code.
2. Code Editor: Write assembly code in the provided text editor and click "Run Code" to simulate the execution.
3. Cycle Simulation: Use the "Cycle" button next to each register entry to simulate a cycle for that particular instruction.
4. Reset: Click the "Reset" button to clear all register values and reset the simulation.
