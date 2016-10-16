"""10/09/16
The example is from the openarty 
Now a test bench is being generated to test
using myhdl & iverilog 
"""
from __future__ import division
from __future__ import print_function
from myhdl import *
import os
import argparse
from argparse import Namespace
def test_bench(args):
    """Need to create the signals that are to be test
    """
 
    i_clk = Signal(bool(0))
    i_reset = Signal(bool(0))
    i_break = Signal(bool(0))
    o_wr = Signal(bool(0))
    i_uart = Signal(bool(0))
    o_break = Signal(bool(0))
    o_parity_err = Signal(bool(0))
    o_frame_err = Signal(bool(0))
    i_setup = Signal(intbv(0)[30:])
    o_data = Signal(intbv(0)[8:])
    o_ck_uart = Signal(bool(0))
	    
    """Need to define stimlus"""
    @instance
    def stimlus():
		i_reset.next = 1
		for i in range(10):
			yield i_clk.posedge
		for i in range(10):
			yield i_clk.posedge
		i_reset.next = 0
		yield i_clk.posedge
		
		i_setup.next = 0x6c8
		yield i_clk.posedge
		for i in range(300):
			yield i_clk.posedge	
 
  	
 
		raise StopSimulation
    """Need to create a clkgen that will be returned to simulation
    """ 

    @always(delay(4))
    def clkgen():
		i_clk.next = not i_clk

    """Need an instance of the test code"""
     
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_reset=i_reset,i_setup=i_setup, \
    i_uart=i_uart,o_wr=o_wr,o_data=o_data,o_break=o_break, \
    o_parity_err=o_parity_err,o_frame_err=o_frame_err,o_ck_uart=o_ck_uart)

     
    print("back from prep cosim")
    print("start (co)simulation ...")
    Simulation((tb_dut, clkgen, stimlus)).run()
    
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    print ("  *%s" %  (sigs))   
    print("compiling ...")
    cmd = "iverilog -o rxuart ../rxuart.v ./tb_rxuart.v"
    print("  %s" %  (cmd))
    os.system(cmd)
    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi rxuart"
    print("  %s" %  (cmd))
    cosim = Cosimulation(cmd, **sigs)
    print("  %s" %  (cosim))
    return cosim
 
if __name__ == '__main__':
	print("Running test...")
	test_bench(Namespace())
