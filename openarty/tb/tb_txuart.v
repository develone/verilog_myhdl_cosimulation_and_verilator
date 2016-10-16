
`timescale 1ns/10ps

 

module tb_txuart1;

reg i_clk;
reg i_reset;

reg [29:0] i_setup;
reg i_break;
reg i_wr;
reg [7:0] i_data;

output wire o_uart;
output wire o_busy;



initial begin
    $dumpfile("vcd/txuart1.vcd");
    $dumpvars(0, tb_txuart1);
end

initial begin
    $from_myhdl(
        i_clk,
        i_reset,
        i_setup,
        i_break,
        i_wr,
        i_data
    );
    $to_myhdl(
        o_uart,
        o_busy
    );
end
 

 

txuart dut_txuart(i_clk, i_reset, i_setup, i_break, i_wr, i_data, o_uart, o_busy);   

endmodule
