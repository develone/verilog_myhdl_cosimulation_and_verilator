module tb_gates;

reg a;
reg b;
wire and_;
wire nand_;
wire or_;
wire nor_;
wire xor_;
wire xnor_;

initial begin
    $from_myhdl(
        a,
        b
    );
    $to_myhdl(
        and_,
        nand_,
        or_,
        nor_,
        xor_,
        xnor_
    );
end

gates dut(
    a,
    b,
    and_,
    nand_,
    or_,
    nor_,
    xor_,
    xnor_
);

endmodule
