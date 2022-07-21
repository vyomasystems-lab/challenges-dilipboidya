# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    initial begin

	clk = 0;
		reset = 1;
		start = 0;
		door_close = 0;
		filled = 0;
		drained = 0;
		detergent_added = 0;
		cycle_timeout = 0;
		spin_timeout = 0;

        await Timer(5, units='ns')
        reset=0;
        
        await Timer(5, units='ns')
		start=1;door_close=1;
        
        await Timer(10, units='ns')
		filled=1;
        
        await Timer(10, units='ns')
		detergent_added=1;
        

		#//filled=0;
        await Timer(10, units='ns')
		cycle_timeout=1;
        

		#//detergent_added=0;
        await Timer(10, units='ns')
		drained=1;
        

		#//cycle_timeout=0;
        await Timer(10, units='ns')
		spin_timeout=1;
        

		//drained=0;
    end

    	always
	begin
        await Timer(5, units='ns')
		clk = ~clk;
	end


# See LICENSE.cocotb for details
# See LICENSE.vyoma for details




@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')

    assert dut.sum.value == A+B, f"Adder result is incorrect: {dut.X.value} != 15"


@cocotb.test()
async def adder_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)

