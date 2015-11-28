init python:
    PORTRAIT_ZOOM = 0.3333

init -1 python:
    def apply_margins(kwargs, margins):
        if margins:
            for margin in margins:
                kwargs['window_'+margin+'_margin'] = margins[margin]
    
    class VNMode(object):
        def __init__(self, mode, margins, **kwargs):
            self.mode = mode
            apply_margins(kwargs, margins)
            self.kwargs = kwargs
    
    def init_vn_modes():
        renpy.store._mode_stack = [VNMode('adv', None)]
    
    def vn_mode():
        return renpy.store._mode_stack[-1]
    
    def push_mode(*args, **kwargs):
        renpy.store._mode_stack.append(VNMode(*args, **kwargs))
    
    def set_window_margins(**margins):
        apply_margins(renpy.store._mode_stack[-1].kwargs, margins)
    
    def set_window_position(x, y):
        renpy.store._mode_stack[-1].kwargs['window_xalign'] = 0
        renpy.store._mode_stack[-1].kwargs['window_yalign'] = 0
        renpy.store._mode_stack[-1].kwargs['window_xoffset'] = x
        renpy.store._mode_stack[-1].kwargs['window_yoffset'] = y
    
    def set_text_color(color):
        renpy.store._mode_stack[-1].kwargs['what_color'] = color
    
    def pop_mode():
        renpy.store._mode_stack.pop()
    
    class CombinedCharacter(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = dict({
                'what_prefix' : '"',
                'what_suffix' : '"',
            })
            self.kwargs.update(kwargs)
        def __call__(self, *args, **kwargs):
            kwargs_copy = self.kwargs.copy()
            kwargs_copy.update(vn_mode().kwargs)
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
            what_color='#333',
            what_size=26,
            what_prefix='',
            what_suffix='',
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
