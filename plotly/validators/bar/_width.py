import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='width', parent_name='bar', **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='calc',
            min=0,
            role='info',
            **kwargs
        )
