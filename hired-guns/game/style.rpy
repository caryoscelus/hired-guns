init python:
    class VNMode(object):
        def __init__(self, mode, **kwargs):
            self.mode = mode
            self.margins = kwargs
    
    renpy.store._mode_stack = [VNMode('adv', left=0, right=0, bottom=0, top=0)]
    def vn_mode():
        return renpy.store._mode_stack[-1]
    
    def push_mode(*args, **kwargs):
        renpy.store._mode_stack.append(VNMode(*args, **kwargs))
    
    def pop_mode():
        renpy.store._mode_stack.pop()
    
    class CombinedCharacter(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
        def __call__(self, *args, **kwargs):
            kwargs_copy = self.kwargs.copy()
            for margin in vn_mode().margins:
                kwargs_copy['window_'+margin+'_margin'] = vn_mode().margins[margin]
            if vn_mode().mode == 'nvl':
                kwargs_copy['kind'] = nvl
                return Character(*self.args, **kwargs_copy)(*args, **kwargs)
            elif vn_mode().mode == 'adv':
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
