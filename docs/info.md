# Full Adder

## How it works

This project implements a 1-bit full adder using combinational logic.

The full adder takes three inputs:

- `A` — first input bit
- `B` — second input bit
- `Cin` — carry input

It produces two outputs:

- `Sum` — the sum bit
- `Carry` — the carry output

The logic is:

```text
Sum   = A XOR B XOR Cin
Carry = (A AND B) OR (Cin AND (A XOR B))
