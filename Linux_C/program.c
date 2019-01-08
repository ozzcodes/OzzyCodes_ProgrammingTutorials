#include <stdio.h>
#include "weather.h"

int main(void) {
	double temperatures[7] = {6.9, 12.3, 9.0, 40.5, 9.8, 1.8, 0.3};
	printAverageTemp(temperatures, 7);

	return 0;
}
