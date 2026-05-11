# Robotic Actuator Validation Fixture

A SolidWorks actuator endurance test fixture designed for adjustable loading, sensor mounting, safety guarding, and future data acquisition. This project focuses on the mechanical design and documentation package for a robotic actuator validation setup, including CAD models, a mechanical drawing, BOM, tolerances, assembly procedure, test plan, FMEA, and a Python DAQ workflow.

This fixture is intended to support future testing of small rotary actuators by applying a configurable load, tracking commanded versus measured position, and identifying early signs of actuator degradation such as positional drift, thermal rise, and bearing wear.

## Project Overview

The fixture is designed around a vertical-axis rotary actuator mounted below the base plate. The actuator shaft passes through the center clearance hole and drives a horizontal load arm. An adjustable weight block can be mounted at different locations on the arm to change the applied loading condition.

A sensor bracket sits near the load arm path to support future position, limit, or feedback sensing. A safety guard covers the moving arm region.

The current revision is a CAD and documentation project. The actuator, sensor, and DAQ hardware are represented as planned purchased components and are not fully modeled in this CAD revision.

## Assembly Preview

![Full assembly isometric view](cad/screenshots/full_assembly_iso.png)

![Top view](cad/screenshots/top_view.png)

![Load arm close-up](cad/screenshots/load_arm_closeup.png)

![Sensor bracket close-up](cad/screenshots/sensor_bracket_closeup.png)

## What I Designed

### Base Assembly

The base assembly acts as the main structure for the fixture. It supports the actuator shaft path, sensor bracket, safety guard, and load arm motion area. The design includes mounting holes and slots to keep the setup modular and adjustable.

### Load Arm

The load arm attaches to the actuator shaft and rotates in the horizontal plane. Multiple holes along the arm allow the weight block to be mounted at different positions, changing the applied loading condition during testing.

### Adjustable Weight Block

The weight block mounts to the load arm and is used to vary the load applied to the actuator. Moving the block farther from the shaft increases the moment applied during repeated motion cycles.

### Sensor Bracket

The sensor bracket uses slotted mounting features so the sensor position can be adjusted during setup. It is intended for a future limit switch, encoder, potentiometer, or other position feedback device.

### Safety Guard

The safety guard covers the moving arm region and was added to show safety consideration around rotating test equipment. In a future physical prototype, this part would be made from clear acrylic or transparent plastic.

## Mechanical Documentation

The design package includes:

* SolidWorks part files
* SolidWorks assembly file
* Mechanical drawing
* Bill of materials
* Assembly procedure
* Test plan
* FMEA
* Python DAQ workflow
* Sample cycle log

## Mechanical Drawing

The drawing includes main dimensions, material notes, and a general tolerance note.

[View mechanical drawing](cad/drawings/actuator_validation_fixture_drawing.pdf)

Drawing note:

Material: ABS plastic
Manufacturing method: 3D printed prototype
General tolerance: ±0.2 mm unless otherwise specified

## Bill of Materials

The BOM includes the fixture components, planned purchased components, and fastening hardware.

[View BOM](docs/bom.csv)

## Test Plan

The test plan defines how the fixture would be used to evaluate actuator performance under repeated motion and adjustable loading.

Planned tests include:

1. No-load motion check
2. Adjustable load test
3. Endurance cycle test
4. Fault detection check

The main data recorded during testing would include:

* Cycle count
* Commanded position
* Measured response
* Position error
* Fault condition
* Test status

Acceptance criteria include limits on position error, drift, mechanical loosening, and repeated fault conditions.

[View full test plan](docs/test_plan.md)

## FMEA

The FMEA focuses on likely failure modes for an actuator endurance test setup.

Primary failure indicators:

1. Positional drift
2. Thermal rise
3. Bearing wear

Other failure modes considered include:

* Load arm slip
* Weight block loosening
* Sensor misalignment
* Guard interference
* Base flex
* Wiring interference

[View FMEA](docs/fmea.md)

## Python DAQ Workflow

The Python workflow supports future actuator validation testing by logging cycle data to CSV and analyzing post-test behavior.

The logger records:

* Commanded position
* Measured response
* Cycle count
* Fault condition
* Test status

The analysis script calculates position error, pass/fail count, and summary statistics for post-test failure analysis.

Example CSV format:

timestamp,cycle_count,commanded_position_deg,measured_response_deg,position_error_deg,fault_condition,test_status
2026-05-11T10:00:00,1,0,0.4,0.4,NONE,PASS
2026-05-11T10:00:02,2,45,44.2,-0.8,NONE,PASS
2026-05-11T10:00:04,3,90,91.1,1.1,NONE,PASS
2026-05-11T10:00:06,4,135,138.6,3.6,POSITION_ERROR_WARNING,PASS
2026-05-11T10:00:08,5,180,186.2,6.2,POSITION_DRIFT,FAIL

Files:

* [Serial logger](control_concept/serial_logger.py)
* [Cycle analysis script](control_concept/analyze_cycles.py)
* [Sample cycle log](control_concept/sample_cycle_log.csv)

## Assembly Procedure

The assembly procedure explains how the fixture components would be assembled for a future physical prototype.

Main steps:

1. Prepare the base plate
2. Mount the rotary actuator below the base plate
3. Attach the load arm to the actuator shaft
4. Install the adjustable weight block
5. Mount and position the sensor bracket
6. Install the selected sensor
7. Place the safety guard over the moving arm area
8. Complete final inspection

[View assembly procedure](docs/assembly_procedure.md)

## Design Intent

This project was built to practice the workflow behind robotic hardware validation: designing a fixture, documenting the mechanical system, defining test procedures, identifying failure modes, and preparing a data logging workflow for future testing.

The fixture is not meant to be a final industrial test stand. It is a prototype-level design package for evaluating small rotary actuators and demonstrating how a validation setup could be planned before physical fabrication.

## Future Improvements

* Add a physical actuator and encoder for closed-loop testing
* Add a load cell or torque sensor
* Add current and temperature measurement
* Add bearing support for the rotating shaft
* Replace ABS load-bearing components with aluminum
* Add adjustable hard stops for range-of-motion testing
* Run longer endurance tests and compare actuator performance over time

## Skills Demonstrated

* SolidWorks CAD design
* Mechanical fixture design
* Mechanical drawing and tolerancing
* BOM creation
* Assembly procedure writing
* Actuator test planning
* FMEA and failure mode analysis
* Python data logging
* Post-test failure analysis
