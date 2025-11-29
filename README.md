# RP2040 Macro Pad

Compact 8-key macro pad built around the XIAO RP2040 DIP module. Features per-key RGB backlighting using SK6812MINI LEDs, a minimal PCB, and a custom 3D-printed enclosure.

---

## Features
- 8× MX-style mechanical switches  
- 3× SK6812MINI addressable RGB LEDs  
- XIAO RP2040 microcontroller  
- Custom PCB with direct switch routing  
- Lightweight printed case with USB-C access

---

## Hardware Overview
### Microcontroller  
- Seeed Studio XIAO RP2040 (DIP package)

### Layout  
- Switches arranged in a compact 2×4 configuration  
- RGB LEDs daisy-chained: DIN → DOUT path across the PCB  
- USB-C through the case opening for programming and power

### Case  
- Two-piece shell designed for friction-fit or fastener-based closure  
- Plate openings sized for MX-compatible housings  
- Internal clearance for the XIAO and LEDs

---

## Bill of Materials (BOM)
| Quantity | Item |
|---------|------|
| 1 | XIAO RP2040 (DIP) |
| 8 | MX-style switches |
| 3 | SK6812MINI RGB LEDs |
| — | Printed case components |
| — | USB-C cable |

---

## Project Images
**Overall Build**  
<img width="680" height="576" alt="Screenshot 2025-11-29 at 11 36 38 AM" src="https://github.com/user-attachments/assets/54c05d33-3daf-44bc-b7ee-4c83069c29d1" />

**Schematic**  
![Schematic](https://github.com/user-attachments/assets/34ccb595-e5aa-442b-b44b-66e143eb0126)

**PCB Layout**  
![PCB Layout](https://github.com/user-attachments/assets/0a2f49e8-30fa-4870-81ea-2e1a07431c12)

**Case**  
![Case](https://github.com/user-attachments/assets/30c98bb7-005e-4cef-9f31-3e2d62e099c4)

---

## Firmware
Compatible with CircuitPython, MicroPython, or a custom C++/Pico-SDK firmware. QMK support is possible with additional configuration.
