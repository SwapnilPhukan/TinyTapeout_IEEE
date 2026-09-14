import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_full_adder(dut):

    test_cases = [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 0, 1),
        (1, 0, 0, 1, 0),
        (1, 0, 1, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1),
    ]

    for A, B, Cin, expected_sum, expected_carry in test_cases:

        # Put A, B and Cin onto ui_in
        dut.ui_in.value = A | (B << 1) | (Cin << 2)

        # Give the combinational logic time to respond
        await Timer(1, units="ns")

        # Read outputs
        result = int(dut.uo_out.value)

        actual_sum = result & 1
        actual_carry = (result >> 1) & 1

        assert actual_sum == expected_sum, (
            f"A={A}, B={B}, Cin={Cin}: "
            f"expected Sum={expected_sum}, got {actual_sum}"
        )

        assert actual_carry == expected_carry, (
            f"A={A}, B={B}, Cin={Cin}: "
            f"expected Carry={expected_carry}, got {actual_carry}"
        )
