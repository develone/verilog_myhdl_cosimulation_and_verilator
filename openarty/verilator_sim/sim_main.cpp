#include <stdio.h>
#include "Vtxuart.h"
#include "verilated_vcd_c.h"
struct rec {
	char raw_buf[1];
};
int main(int argc, char **argv)
{
    Verilated::commandArgs(argc, argv);
    Vtxuart* top = new Vtxuart;
    int i,ii0;
    struct rec my_record;
    Verilated::traceEverOn(true);
    VerilatedVcdC* tfp = new VerilatedVcdC;
    top->trace (tfp, 99);
    tfp->open ("simx.vcd");

    if (argc != 2) {
      fprintf(stderr, "usage: sim <hex-file>\n");
      exit(1);
    }

 
    FILE *hex = fopen(argv[1], "r");
    char v[10],c;
    for (i = 0; i < 10; i++) {
      fread(&my_record,sizeof(struct rec),1,hex);
      ii0 = (int)my_record.raw_buf[0];
      v[i] = ii0;
      //printf("%d\n",v[i]);
      
    }

    FILE *log = fopen("log", "w");
    int t = 0;

    top->i_reset = 1;
    top->i_wr = 1;
    top->i_data = 0x55;
    top->i_setup = 0x6c8;
    for (i = 0; i < 10; i++) {
	    top->i_data = v[i];
	    printf("%d\n",v[i]);
    }
}
/* 

    for (i = 0; i < 100000000; i++) {
      uint16_t a = top->mem_addr;
      uint16_t b = top->code_addr;
      if (top->mem_wr)
        ram32[(a & 16383) / 4] = top->dout;
      top->clk = 1;
      top->eval();
      t += 20;

      top->mem_din = ram32[(a & 16383) / 4];
      top->insn = ram16[b];
      top->clk = 0;
      top->eval();
      t += 20;
      if (top->io_wr) {
        putchar(top->dout);
        putc(top->dout, log);
        if (top->dout == '#')
          break;
      }
#if 0
      if (top->io_inp && (top->io_n == 2)) {
        top->io_din = getchar();
      }
#endif
    }
    printf("\nSimulation ended after %d cycles\n", i);
    delete top;
    // tfp->close();
    fclose(log);

    exit(0);

}*/
