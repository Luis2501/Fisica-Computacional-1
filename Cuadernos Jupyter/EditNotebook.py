from IPython.display import display, HTML
from jupyterthemes import jtplot
import sys

def Edit():

	display(HTML("""
	<style>
	.output {
	    display: flex;
	    align-items: center;
	    text-align: center;
	}
	</style>
	"""))


	jtplot.style(theme= 'onedork')
	jtplot.style(figsize = (10,10))
	
	sys.path.append("../")
