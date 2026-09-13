module tt_um_full_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Full adder inputs
    wire A;
    wire B;
    wire Cin;

    assign A   = ui_in[0];
    assign B   = ui_in[1];
    assign Cin = ui_in[2];

    // Full adder outputs
    assign uo_out[0] = A ^ B ^ Cin;
    assign uo_out[1] = (A & B) | (Cin & (A ^ B));

    // Unused output pins
    assign uo_out[7:2] = 6'b0;

    // Bidirectional pins unused
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
