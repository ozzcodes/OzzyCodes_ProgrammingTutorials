#include <stdio.h>
#include "weather.h"

double averageTemp(double *temps, int numOfTemps) {
	double result = 0.0;
	int i;

	for(i = 0; i < numOfTemps; i++) {
		result = result + temps[i];
	}
	result = result / (double) numOfTemps;

	return result;
}

void printAverageTemp(double *temps, int numOfTemps) {
	double average = averageTemp(temps, numOfTemps);
	printf("The average 7-day temp: %.2lf\n", average);
}

