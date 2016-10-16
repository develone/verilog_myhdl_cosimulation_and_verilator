
`timescale 1ns/10ps

 

module tb_rxuart1;

reg i_clk;
reg i_reset;
reg i_uart;
reg [29:0] i_setup;


output wire o_wr;
 
output wire o_ck_uart;
output wire [7:0] o_data;
output wire o_break;
output wire o_parity_err;
output wire o_frame_err;

initial begin
    $dumpfile("vcd/rxuart1.vcd");
    $dumpvars(0, tb_rxuart1);
end

initial begin
    $from_myhdl(
        i_clk,
        i_reset,
        i_setup,
        i_uart
 
    );
    $to_myhdl(
		o_wr,
		o_data,
		o_break,
		o_parity_err,
		o_frame_err,
        o_ck_uart
        
    );
end
 
			
rxuart dut_rxuart(i_clk,i_reset,i_setup,i_uart,o_wr,o_data,o_break,o_parity_err,o_frame_err,o_ck_uart);   

endmodule
