init python:
    PORTRAIT_ZOOM = 0.3333

init -1 python:
    class VNMode(object):
        def __init__(self, mode, **kwargs):
            self.mode = mode
            self.margins = kwargs
    
    def init_vn_modes():
        renpy.store._mode_stack = [VNMode('adv', left=0, right=0)]
    
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

define narrator = CombinedCharacter(
            None,
            what_color='#000',
        )
define mission_chapter = Character(
            None,
            kind=adv,
            what_size=40,
            what_prefix="{cps=0}",
            what_suffix="{/cps}",
            what_outlines=[(1, "#000000", 0, 0)],
            window_background=None,
            window_yminimum=0,
            window_xfill=False,
            window_xalign=0.5,
            window_yalign=0.5,
        )

style simple_frame:
    background Frame('images/ui/frame.png', 8, 8)

style filled_frame:
    background Frame('images/ui/filledframe.png', 8, 8)

style empty:
    background None
    foreground None

style ui_small is text:
    size 16
