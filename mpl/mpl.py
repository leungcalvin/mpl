import matplotlib
matplotlib.style.use('./lm.mplstyle')

journal_textwidths = {'prd': 6.50127,
                      'none': 8.5} # Latex's \textwidth in inches

def get_size(fraction_of_textwidth = 0.45,height_per_width  = 1 / 1.61803399,journal = 'prd'):
    textwidth = journal_textwidths[journal]
    width_in = textwidth * fraction_of_textwidth
    height_in = height_per_width * width_in
    return (width_in, height_in)
