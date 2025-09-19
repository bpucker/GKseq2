# GKseq2
This script allows to plot the coverage of _Arabidopsis thaliana_ re-sequencing data mapped to the TAIR10 reference genome sequence. The input is a TAB-separated coverage (COV) file, which has three columns (sequenceID, position, coverage).

## Usage

```
Usage:
  python3 cov_plot.py --in <FILE> --out <DIR>

Mandatory:
--in     STR     Coverage file (COV) created by construct_cov_file.py
--out    STR     Output folder
		
Optional:
--res    INT     Resolution[1000]
--sat    INT     Saturation for max coverage[100]
--cov    INT     Averge coverage
--name   STR     Name of dataset

--chr    STR   SequenceID
--start  INT   Start position
--end    INT   End position
```
				
`--in` speciefies the coverage input file.

`--out` speciefies the output folder. This will be created if it does not exist already.

`--res` speciefies the resolution for the coverage plot i.e. number of base pairs to be summarized as one dot. Default: 1000.

`--sat` speciefies a saturation for high coverage. Default: 100.

`--cov` speciefies the average coverage.

`--name` speciefies the name of the analyzed dataset.

`--chr` speciefies the name of the sequence harboring the region of interest.

`--start` speciefies the start of the region of interest.

`--end` speciefies the end of the region of interest.


## Reference
This script is based on a previously developed Python2 script (https://github.com/bpucker/GKseq), which was developed for the analysis of _Arabidopsis thaliana_ re-sequencing data (https://doi.org/10.1186/s12864-021-07877-8).
