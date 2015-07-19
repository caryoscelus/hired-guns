init python:
    renpy.store._vn_mode = 'adv'
    renpy.store._margins = {
        'left' : 0,
        'right' : 0,
        'bottom' : 0,
        'top' : 0
    }
    def vn_mode(value, **kwargs):
        renpy.store._vn_mode = value
        renpy.store._margins.update(kwargs)
    
    class CombinedCharacter(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
        def __call__(self, *args, **kwargs):
            kwargs_copy = self.kwargs.copy()
            for margin in renpy.store._margins:
                kwargs_copy['window_'+margin+'_margin'] = renpy.store._margins[margin]
            if _vn_mode == 'nvl':
                kwargs_copy['kind'] = nvl
                return Character(*self.args, **kwargs_copy)(*args, **kwargs)
            elif _vn_mode == 'adv':
                kwargs_copy['kind'] = adv
                return Character(*self.args, **kwargs_copy)(*args, **kwargs)
            else:
                raise ValueError('unknown mode {}'.format(_vn_mode))

define narrator = CombinedCharacter(None, what_color='#000')

style simple_frame:
    background Frame('images/ui/frame.png', 8, 8)

style filled_frame:
    background Frame('images/ui/filledframe.png', 8, 8)

style empty:
    background None
    foreground None
