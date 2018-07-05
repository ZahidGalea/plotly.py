import _plotly_utils.basevalidators


class TicksuffixValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='ticksuffix',
        parent_name='contour.colorbar',
        **kwargs
    ):
        super(TicksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            **kwargs
        )
