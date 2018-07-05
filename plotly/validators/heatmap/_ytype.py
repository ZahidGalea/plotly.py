import _plotly_utils.basevalidators


class YtypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='ytype', parent_name='heatmap', **kwargs):
        super(YtypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+clearAxisTypes',
            role='info',
            values=['array', 'scaled'],
            **kwargs
        )
