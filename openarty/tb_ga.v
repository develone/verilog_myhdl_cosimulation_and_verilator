module tb_ga;

reg a;
reg b;
wire and_;
wire nand_;
wire or_;
wire nor_;

initial begin
    $from_myhdl(
        a,
        b
    );
    $to_myhdl(
        and_,
        nand_,
        or_,
        nor_
    );
end

ga dut(
    a,
    b,
    and_,
    nand_,
    or_,
    nor_
);

endmodule
