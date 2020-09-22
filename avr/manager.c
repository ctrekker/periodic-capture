#define F_CPU 10000000L
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
DDRB = 0b00010000; // PORTB is output, all pins
PORTB = 0x00; // Make pins low to start

for (;;) {
PORTB = PINB << 1; // invert all the pins
_delay_ms(100); // wait some time
}
return 0;
}
