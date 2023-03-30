import os
import matplotlib.pyplot as plt
path_to_style = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'lm.mplstyle'))
print(f'Using style file at: {path_to_style}')
plt.style.use(path_to_style)

journal_textwidths = {'prd': 6.50127,
                      'none': 8.5,
                      'kaobook':6.5, # just a guess
                      'apj':6.0, # from \textwidth in aastex631.cls
                      'aj': 6.0, # from \textwidth in aastex631.cls
                      } # Latex's \textwidth in inches

def figsize(fraction_of_textwidth = 0.45,height_per_width  = 1 / 1.61803399,journal = 'prd'):
    """When making your figure, decide its aspect ratio and your journal and its width as a fraction of the \textwidth of the journal. Then use matplotlib.pyplot.Figure(figsize = ...) to specify the right size"""
    textwidth = journal_textwidths[journal]
    width_in = textwidth * fraction_of_textwidth
    height_in = height_per_width * width_in
    return (width_in, height_in)
