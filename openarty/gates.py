from myhdl import *
import argparse
clock = Signal(bool(0))
a = Signal(bool(0))
b = Signal(bool(0))
and_ = Signal(bool(0))
nand_ = Signal(bool(0))
or_ = Signal(bool(0))
nor_ = Signal(bool(0))
xor_ = Signal(bool(0))
xnor_ = Signal(bool(0))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args
     
def gates(a,b,and_,nand_,or_,nor_,xor_,xnor_):
	@always_comb
	def rtl():
		and_.next = b & a
		nand_.next = ~(b & a)
		or_.next = b | a
		nor_.next = ~(b | a)
		xor_.next =  (b ^ a)
		xnor_.next =  ~(b ^ a)
	return rtl
def tb(a,b,and_,nand_,or_,nor_,xor_,xnor_):
	instance_gates = gates(a,b,and_,nand_,or_,nor_,xor_,xnor_)

 
      	
	@instance
	def stimulus():
		a.next = 0
		
		b.next = 0
		
		a.next = 1
		
		a.next = 0
		
		b.next = 1
		
		a.next = 1
	
		b.next = 1		
	
		raise StopSimulation
	return instances()	
def convert(args):
	toVerilog(gates,a,b,and_,nand_,or_,nor_,xor_,xnor_)
def main():
	args = cliparse()
	if args.test:
		tb_fsm = traceSignals(tb,a,b,and_,nand_,or_,nor_,xor_,xnor_)
		sim = Simulation(tb_fsm)
		sim.run()  
	if args.convert:
		convert(args)

if __name__ == '__main__':
	main()
