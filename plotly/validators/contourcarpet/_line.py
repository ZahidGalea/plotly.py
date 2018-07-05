import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='line', parent_name='contourcarpet', **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Line',
            data_docs="""
            color
                Sets the color of the contour level. Has no if
                `contours.coloring` is set to *lines*.
            dash
                Sets the dash style of lines. Set to a dash
                type string (*solid*, *dot*, *dash*,
                *longdash*, *dashdot*, or *longdashdot*) or a
                dash length list in px (eg *5px,10px,2px,2px*).
            smoothing
                Sets the amount of smoothing for the contour
                lines, where *0* corresponds to no smoothing.
            width
                Sets the line width (in px).""",
            **kwargs
        )
