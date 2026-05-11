# Robotic Actuator Validation Fixture

A CAD-based mechanical fixture concept for testing small robotic actuators under repeated motion and adjustable loading conditions. The fixture was designed to practice hardware validation workflows used in robotics: mounting an actuator, applying a controlled load, positioning a sensor near the moving arm, and logging test data for repeatability analysis.

## Overview

This project models a desktop actuator validation fixture in SolidWorks. The fixture uses a mounted actuator or servo to rotate a load arm with an adjustable weight block. A sensor bracket is positioned near the arm path to support future position, limit, or feedback sensing. A safety guard covers the moving arm area.

The goal is to create a mechanical test setup that could be used to evaluate basic actuator behavior such as repeatability, drift, loading effects, and cycle performance.

## Key Features

- SolidWorks assembly of a robotic actuator validation fixture
- Adjustable actuator mount with slotted mounting holes
- Rotating load arm with multiple load positions
- Removable weight block for varying applied load
- Adjustable sensor bracket for future feedback hardware
- Safety guard around the moving arm region
- BOM, mechanical drawings, assembly notes, and test plan
- Python logging script for cycle data and test result analysis

## CAD Design

The fixture includes:

- Base plate
- Actuator mount
- Load arm
- Adjustable weight block
- Sensor bracket
- Safety guard

The design is intended as a 3D-printable prototype using ABS plastic, with future improvements possible using machined aluminum or reinforced printed components.

## How It Works

1. The actuator or servo mounts to the vertical actuator bracket.
2. The actuator shaft connects to the load arm.
3. The adjustable weight block is mounted to one of the holes on the load arm.
4. The actuator rotates the arm through a repeated motion profile.
5. The sensor bracket holds a future sensor for measuring position, limits, or repeatability.
6. The Python logging workflow records cycle data for analysis.

## Test Workflow

The planned validation test checks whether the actuator can repeatedly move under load without major drift or failure.

Example test data includes:

- Target angle
- Measured angle
- Cycle count
- Position error
- Test status
- Failure or anomaly flag

## Repository Structure

```text
robotic-actuator-validation-fixture/
│
├── README.md
│
├── cad/
│   ├── parts/
│   ├── assembly/
│   ├── drawings/
│   └── screenshots/
│
├── docs/
│   ├── bom.csv
│   ├── assembly_procedure.md
│   ├── test_plan.md
│   └── design_notes.md
│
└── control_concept/
    ├── serial_logger.py
    ├── analyze_cycles.py
    └── sample_cycle_log.csv
