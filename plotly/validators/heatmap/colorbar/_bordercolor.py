import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='bordercolor',
        parent_name='heatmap.colorbar',
        **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            **kwargs
        )
