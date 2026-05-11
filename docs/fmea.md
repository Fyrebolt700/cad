# Failure Mode and Effects Analysis

## Project
Robotic Actuator Validation Fixture

## Scope
This FMEA identifies likely failure modes for a future actuator endurance test setup using the CAD-designed fixture.

| Failure Mode | Possible Cause | Effect | Detection Method | Acceptance Criteria | Mitigation |
|---|---|---|---|---|---|
| Positional drift | Actuator backlash, shaft slip, sensor noise | Measured response moves away from commanded position over cycles | Compare commanded position and measured response in CSV logs | Drift must remain below 5 degrees over endurance test | Add encoder feedback, improve shaft coupling, tighten mount |
| Thermal rise | Actuator overloaded or run continuously | Reduced actuator performance or shutdown | Future temperature sensor or manual temperature checks | Temperature must stay within actuator-rated operating range | Reduce load, reduce duty cycle, add cooling time |
| Bearing wear | Repeated load cycles or poor shaft support | Increased play, noise, or inconsistent position | Position error trend, inspection after test | No visible looseness or increasing position error trend | Add bearing support, reduce radial load, improve alignment |
| Load arm slip | Weak shaft connection or loose fastener | Incorrect load arm position | Sudden increase in position error | No sudden position shift during test | Use keyed hub, clamp collar, or set screw |
| Weight block loosening | Fastener vibration during repeated cycles | Changing load condition or unsafe operation | Visual inspection before and after test | Weight block remains fixed through full test | Use lock nut, washer, or threadlocker |
| Sensor misalignment | Bracket movement or poor setup | Incorrect measured response or missed limit | Compare sensor reading with expected arm position | Sensor triggers consistently at expected position | Use slotted adjustment, tighten bracket, add alignment marks |
| Guard interference | Guard placed too close to moving arm | Arm collision or failed motion | Visual clearance check before test | No contact between arm and guard | Increase guard clearance, adjust guard position |
| Base flex | Printed base not stiff enough | Inconsistent actuator alignment | Visual deflection or increasing position error | No visible flex during test | Use thicker base or aluminum revision |
| Wiring interference | Wires enter arm sweep path | Motion blocked or wire damage | Pre-test inspection | Wires remain outside moving area | Add wire routing clips and strain relief |

## Primary Failure Indicators

The primary failure indicators for this fixture are:

1. Positional drift  
2. Thermal rise  
3. Bearing wear  

These were selected because they are common indicators of actuator degradation during repeated motion and endurance testing.

## Future Improvements

- Add encoder feedback for direct position measurement
- Add temperature sensing for thermal monitoring
- Add current sensing to estimate actuator load
- Add bearing support for the rotating shaft
- Replace printed load-bearing components with aluminum
- Add hard stops for controlled range-of-motion testing