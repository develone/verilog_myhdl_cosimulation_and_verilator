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
    i_ppd = Signal(bool(0))
    i_wb_cyc = Signal(bool(0))
    i_wb_stb = Signal(bool(0))
    i_wb_we = Signal(bool(0))
    o_wb_ack = Signal(bool(0))
    o_wb_stall = Signal(bool(0))
    o_wb_data = Signal(intbv(0)[32:])
    i_wb_data = Signal(intbv(0)[32:])
	    
    """Need to define stimlus"""
    @instance
    def stimlus():
		i_ppd.next = 1
		for i in range(10):
			yield i_clk.posedge
		for i in range(10):
			yield i_clk.posedge
		i_ppd.next = 0
		yield i_clk.posedge

		i_wb_stb.next = 1
		yield i_clk.posedge
		
		o_wb_ack.next = i_wb_stb
		yield i_clk.posedge
		
		o_wb_stall.next = 0
		yield i_clk.posedge
		
				
 
		raise StopSimulation
    """Need to create a clkgen that will be returned to simulation
    """ 

    @always(delay(4))
    def clkgen():
		i_clk.next = not i_clk

    """Need an instance of the test code"""
     
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_ppd=i_ppd,i_wb_cyc=i_wb_cyc, \
    i_wb_stb=i_wb_stb,i_wb_we=i_wb_we,i_wb_data=i_wb_data, \
    o_wb_ack=o_wb_ack,o_wb_stall=o_wb_stall,o_wb_data=o_wb_data)
     
    print("back from prep cosim")
    print("start (co)simulation ...")
    Simulation((tb_dut, clkgen, stimlus)).run()
    
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    print ("  *%s" %  (sigs))   
    print("compiling ...")
    cmd = "iverilog -o rtcdate ../rtcdate.v ./tb_rtcdate.v"
    print("  %s" %  (cmd))
    os.system(cmd)
    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi rtcdate"
    print("  %s" %  (cmd))
    cosim = Cosimulation(cmd, **sigs)
    print("  %s" %  (cosim))
    return cosim
 
if __name__ == '__main__':
	print("Running test...")
	test_bench(Namespace())
