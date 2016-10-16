
$(SUBDIRS):
	$(MAKE) -C $@

all: obj_dir/Vtxuart $(SUBDIRS)

VERILOGS=verilog/txuart.v verilog/rxuart.v

obj_dir/Vtxuart: $(VERILOGS) sim_main.cpp Makefile
	verilator -Wall --cc --trace -Iverilog/ $(VERILOGS) --top-module txuart --exe sim_main.cpp
	# verilator --cc --trace $(VERILOGS) --top-module txuart --exe sim_main.cpp
	$(MAKE) -C obj_dir OPT_FAST="-O2" -f Vtxuart.mk Vtxuart

.PHONY: all
