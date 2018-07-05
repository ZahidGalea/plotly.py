import _plotly_utils.basevalidators


class NbinsyValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='nbinsy', parent_name='histogram2d', **kwargs
    ):
        super(NbinsyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='style',
            **kwargs
        )
