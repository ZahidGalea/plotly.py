import _plotly_utils.basevalidators


class ShowaxeslabelsValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='showaxeslabels',
        parent_name='layout.scene.yaxis',
        **kwargs
    ):
        super(ShowaxeslabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='info',
            **kwargs
        )
