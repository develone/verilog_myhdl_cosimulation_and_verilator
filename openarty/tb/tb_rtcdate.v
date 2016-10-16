
`timescale 1ns/10ps

 

module tb_rtcdate1;

reg i_clk;
reg i_ppd;

reg i_wb_cyc;
reg i_wb_stb;
reg i_wb_we;
reg [31:0] i_wb_data;

output wire o_wb_ack;
output wire [31:0] o_wb_data;
output wire o_wb_stall;

initial begin
    $dumpfile("vcd/rtcdate1.vcd");
    $dumpvars(0, tb_rtcdate1);
end

initial begin
    $from_myhdl(
        i_clk,
        i_ppd,
        i_wb_cyc,
        i_wb_stb,
        i_wb_we,
        i_wb_data
    );
    $to_myhdl(
        o_wb_ack,
        o_wb_stall,
        o_wb_data
    );
end
 

 

rtcdate dut_rtcdate(i_clk, i_ppd, i_wb_cyc, i_wb_stb, i_wb_we, i_wb_data,o_wb_ack, o_wb_stall, o_wb_data);   

endmodule
