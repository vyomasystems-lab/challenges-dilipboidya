# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/WashingMachine.v  # provide your design path

TOPLEVEL :=  WashingMachine       # design file
MODULE   :=  tb_WashingMachine    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
