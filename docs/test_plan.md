# Test Plan

## Project
Robotic Actuator Validation Fixture

## Objective
Evaluate actuator repeatability and endurance under adjustable loading conditions using a fixture-mounted load arm, sensor feedback, and Python-based data logging.

## Test Setup

The actuator is mounted below the base plate and drives a horizontal load arm through the center clearance hole. A weight block is mounted at different positions on the load arm to change the applied load. A sensor mounted on the adjustable bracket is used to measure or verify arm position.

## Data to Record

- Cycle count
- Commanded position
- Measured response
- Position error
- Fault condition
- Test status
- Optional future data: temperature, current draw, vibration, bearing condition

## Test 1: No-Load Motion Check

### Purpose
Confirm that the actuator can move the load arm through the expected range of motion without added load.

### Procedure
1. Remove the weight block from the load arm.
2. Command the actuator through the planned motion profile.
3. Record commanded position, measured response, and position error.
4. Repeat for 10 cycles.

### Acceptance Criteria
- No mechanical interference
- Position error remains within ±3 degrees
- No fault condition is recorded

## Test 2: Adjustable Load Test

### Purpose
Evaluate actuator response with the weight block mounted at different load positions.

### Procedure
1. Mount the weight block at the closest load position.
2. Run 10 cycles.
3. Move the weight block to a farther load position.
4. Run another 10 cycles.
5. Compare position error between load conditions.

### Acceptance Criteria
- Load arm rotates without slipping
- Weight block remains secured
- Position error remains within ±5 degrees under load
- No repeated fault condition occurs

## Test 3: Endurance Cycle Test

### Purpose
Check actuator performance over repeated motion cycles.

### Procedure
1. Mount the weight block at the selected test position.
2. Run 100 repeated motion cycles.
3. Log commanded position, measured response, cycle count, and fault conditions.
4. Analyze position error over time.

### Acceptance Criteria
- At least 95% of cycles pass
- Position error does not show consistent drift greater than 5 degrees
- No mechanical loosening is observed
- No repeated fault condition occurs

## Test 4: Fault Detection Check

### Purpose
Confirm that the logging workflow can capture failed cycles.

### Procedure
1. Run the actuator through a short test sequence.
2. Introduce or simulate a position error above the allowed threshold.
3. Confirm that the Python workflow records the fault condition.

### Acceptance Criteria
- Fault condition is recorded in the CSV file
- Failed cycle is identifiable during post-test analysis

## Planned Failure Indicators

- Positional drift over repeated cycles
- Thermal rise during endurance testing
- Bearing or shaft wear
- Load arm slip
- Sensor misalignment
- Weight block loosening
- Guard or bracket interference

## Notes
This test plan describes the intended validation workflow for a future physical prototype. The current CAD revision defines the fixture geometry and documentation package.