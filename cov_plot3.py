### Boas Pucker ###
### pucker@uni-bonn.de ###
### v0.3 ###
### reference: https://doi.org/10.3390/genes10090671 & https://doi.org/10.1186/s12864-021-07877-8 ####

__usage__ = """
					python cov_plot.py
					--in <FULL_PATH_TO_COVERAGE_FILE>
					--out <FULL_PATH_TO_OUTPUT_FILE>
					
					--res <RESOLUTION, WINDOW_SIZE_FOR_COVERAGE_CALCULATION>[1000]
					--sat <SATURATION, CUTOFF_FOR_MAX_COVERAGE_VALUE>[100]
					--cov <AVERAGE_COVERAGE>
					--name <NAME>
					
					--chr <CHROMOSOME>
					--start <REGION_START_POSITION>
					--end <REGION_END_POSITION>
					"""

import sys, os
import matplotlib.pyplot as plt
import numpy as np

# --- end of imports --- #


def load_cov( cov_file ):
	"""! @brief load all information from coverage file """
	
	cov = {}
	with open( cov_file, "r" ) as f:
		line = f.readline()
		header = line.split('\t')[0]
		tmp = []
		while line:
			parts = line.strip().split('\t')
			if parts[0] != header:
				cov.update( { header: tmp } )
				header = parts[0]
				tmp = []
			tmp.append( float( parts[-1] ) )
			line = f.readline()
		cov.update( { header: tmp } )
	return cov


def generate_specific_plot( cov, out_file, resolution, saturation, chromosome, start, end, color ):
	"""! @brief generate figure """
	
	fig, ax = plt.subplots( figsize=( 10, 3 ) )
		
	ax.scatter( range( start, end, 1), cov[ chromosome ][ start:end ], color=color, s=1 )
	
	ax.set_xlabel( "position on chromosome [ bp ]" )
	ax.set_ylabel( "coverage" )
	
	ax.set_title( chromosome )
	
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	#ax.spines['left'].set_visible(False)
	#ax.get_yaxis().set_ticks([])
	#ax.yaxis.labelpad = 10
	
	plt.subplots_adjust( left=0.05, right=0.99, top=0.85, bottom=0.2 )
	
	fig.savefig( out_file, dpi=300 )


def generate_plot( cov, out_file, resolution, saturation, name, color ):
	"""! @brief generate figure """
	
	fig, ax = plt.subplots( figsize=( 10, 7 ) )
	
	ymax = 5	#len( cov.keys() )+1
	max_value = 0
	collected_values = {}
	
	# --- generate list for plotting --- #
	for idx, key in enumerate( sorted( cov.keys() ) ):
		y = ymax-idx-1
		x = []
		blocks = [ cov[ key ] [ i : i + resolution ] for i in range( 0, len( cov[ key ] ), resolution ) ]
		for block in blocks:
			x.append( min( [ np.mean( block ), saturation ] ) )
		max_value = max( [ max_value, max( x ) ] )
		collected_values.update( { key: x } )
	
	# --- plot values --- #
	max_value = float( min( [ saturation, max_value ] ) )
	for idx, key in enumerate( sorted( cov.keys() )[:5] ):
		y = ymax - ( idx*1.3 )
		x = []
		for each in collected_values[ key ]:
			x.append( y + min( [ 1, ( each / max_value ) ] ) )
		
		ax.scatter( np.arange( 0, len( x ), 1 ), x, s=1, color=color )
		
		ax.text( 1, y, key )
		
		ax.plot( [ 0, len( x ) ], [ y+( 0 / max_value ), y+( 0 / max_value ) ], color="black" , linewidth=0.1)
		#ax.plot( [ 0, len( x ) ], [ y+( 10 / max_value ), y+( 10 / max_value ) ], color="black" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 20 / max_value ), y+( 20 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 30 / max_value ), y+( 30 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 40 / max_value ), y+( 40 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 50 / max_value ), y+( 50 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 60 / max_value ), y+( 60 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 70 / max_value ), y+( 70 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 80 / max_value ), y+( 80 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 90 / max_value ), y+( 90 / max_value ) ], color="grey" , linewidth=0.1)
		ax.plot( [ 0, len( x ) ], [ y+( 100 / max_value ), y+( 100 / max_value ) ], color="grey" , linewidth=0.1)
		
		
		ax.plot( [ 0, 0 ], [ y, y+1 ], color="black", linewidth=1, markersize=1 )
		ax.text( 0, y+1, str( int( max_value ) ), ha="right", fontsize=5 )
		ax.text( 0, y+0.5, str( int( max_value / 2 ) ), ha="right", fontsize=5 )
		ax.text( 0, y, "0", ha="right", fontsize=5 )
		
	ax.set_xlabel( "position on chromosome [ Mbp ]" )
	ax.set_ylabel( "coverage" )
	
	ax.set_xlim( 0, 30500 )
	
	ax.set_title( name )
	
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.get_yaxis().set_ticks([])
	ax.yaxis.labelpad = 10
	
	ax.xaxis.set_ticks( np.arange( 0, 31000, 1000 ) )
	labels = map( str, np.arange( 0, 31, 1 ) )
	ax.set_xticklabels( labels )	#[ "0", "5", "10", "15", "20", "25", "30" ]
	
	plt.subplots_adjust( left=0.03, right=0.999, top=0.95, bottom=0.1 )
	
	fig.savefig( out_file, dpi=300 )


def generate_hist( cov_values, outputfile, saturation, resolution, title, color ):
	"""! @brief generate coverage histogram """
	
	values = []
	blocks = [ cov_values[i : i + resolution] for i in range( 0, len(cov_values), resolution ) ]
	for block in blocks:
		values.append( min( [ np.mean( block ), saturation ] ) )
	
	fig, ax = plt.subplots()
	
	ax.set_title( title )
	ax.hist( values, bins=300, color=color )
	ax.set_xlim( 0, 300 )
	
	ax.set_xlabel( "sequencing coverage depth" )
	ax.set_ylabel( "number of positions" )
	
	fig.savefig( outputfile, dpi=300 )


def main( arguments ):
	"""! @brief runs everything """
	
	cov_file = arguments[ arguments.index( '--in' ) + 1 ]
	output_folder = arguments[ arguments.index( '--out' ) + 1 ]
	
	if not os.path.exists( output_folder ):
		os.makedirs( output_folder )
	
	if '--res' in arguments:
		resolution = int( arguments[ arguments.index( '--res' ) + 1 ] )
	else:
		resolution = 1000
	
	if '--sat' in arguments:
		saturation = int( arguments[ arguments.index( '--sat' ) + 1 ] )
	else:
		saturation = 100
	
	if '--name' in arguments:
		name = arguments[ arguments.index( '--name' ) + 1 ]
	else:
		name = ""
	
	chromosome = arguments[ arguments.index( '--chr' ) + 1 ]
	start = int( arguments[ arguments.index( '--start' ) + 1 ] )
	end = int( arguments[ arguments.index( '--end' ) + 1 ] )
	color="lime"
	
	cov = load_cov( cov_file )
	
	# --- generate specific plot --- #
	out_file = output_folder + name + ".specific_plot.pdf"
	generate_specific_plot( cov, out_file, resolution, saturation, chromosome, start, end, color )

	# --- generate coverage histograms per chromosome --- #
	for key in cov.keys():
		outputfile = output_folder + key + ".pdf"
		generate_hist( cov[ key ], outputfile, saturation, resolution, key, color )
	
	# --- generate per chromosome position coverage plot --- #
	out_file = output_folder + name + ".pdf"
	generate_plot( cov, out_file, resolution, saturation, name, color )


if '--in' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
