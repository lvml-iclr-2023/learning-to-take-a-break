import base64
import functools
import io

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

from IPython.display import HTML,display

__all__=[
    'lv_eq_f',
    'p_opt_f',
    'myopic_eq_f',
    'opt_eq_f',
    'quantize',
    'create_fig',
    'confidence_interval',
    'series_confidence_interval',
    'plot_line_with_ci',
]

# Convenience functions for LV equilibrium analysis

lv_eq_f = lambda ab, gd, p_fb: np.clip(
    (gd/(1-p_fb))*(1-ab/(1-p_fb)),
    a_min=0,
    a_max=None,
)
p_opt_f = lambda ab: np.clip(1-2*ab,a_min=0,a_max=None)
myopic_eq_f = lambda ab, gd: lv_eq_f(ab,gd,p_fb=0)
opt_eq_f = lambda ab, gd: lv_eq_f(ab,gd,p_fb=p_opt_f(ab))

# Quantization

def quantize(x, res):
    """
    Quantize vector x to the given resolution.
    """
    return np.round(x/res)*res

# Graph plotting

class DownloadableIO(io.BytesIO):
    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._download_filename = filename
        
    def _repr_html_(self):
        buf = self.getbuffer()
        buf_enc = base64.b64encode(buf).decode('ascii')
        return f'<a href="data:text/plain;base64,{buf_enc}" download="{self._download_filename}">Download {self._download_filename}</a>'

def download_fig(fig, fname):
    fig_out = DownloadableIO(filename=fname)
    fig.savefig(fname=fig_out, format=fname.split('.')[-1])
    display(fig_out)

@functools.wraps(plt.subplots)
def create_fig(*args, **kwargs):
    args_dct = {}
    if 'figsize' not in kwargs:
        args_dct['figsize'] = (10,3)
    if 'tight_layout' not in kwargs:
        args_dct['tight_layout'] = dict(
            w_pad=3,
        )
    fig, ax = plt.subplots(*args, **kwargs, **args_dct)
    fig.download = lambda filename: download_fig(fig, filename)
    return fig,ax

# Statistical analysis

confidence_interval = lambda mu, std, count: scipy.stats.norm.interval(
    0.95,
    loc=mu,
    scale=std/np.sqrt(count),
)

series_confidence_interval = lambda s: confidence_interval(s.mean(), s.std(), s.count())

def plot_line_with_ci(df, ax, label=None, color=None, linestyle=None):
    assert len({'mean','ci'} - set(df.columns))==0
    df['mean'].plot.line(
        ax=ax,
        label=label,
        color=color,
        linestyle=linestyle,
    ),
    ax.fill_between(
        df.index,
        df['ci'].map(lambda t: t[0]),
        df['ci'].map(lambda t: t[1]),
        alpha=0.2,
        color=color,
    )
    return ax
