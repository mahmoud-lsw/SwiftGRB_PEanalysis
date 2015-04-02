#ifndef __UTILS_H__
#define __UTILS_H__ 1

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>

// return an array of detected z from input array of z and detection prob, given a prob threshold
void detected(double *trigz, double *ptrig, long int ntrig, double pth, double *detz, long int *ndet);

// count lines in a file
long int countlines(char filename[]);

// read command-line options
void read_options(int argc, char **argv, double *n0, double *n1, double *n2, long int *seed, int *resume,
				  int *popsize, int *datpopsize, int *help, char *filename, int *nlive);

#endif
