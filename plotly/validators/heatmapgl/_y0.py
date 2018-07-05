import _plotly_utils.basevalidators


class Y0Validator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(self, plotly_name='y0', parent_name='heatmapgl', **kwargs):
        super(Y0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={'ytype': 'scaled'},
            role='info',
            **kwargs
        )
