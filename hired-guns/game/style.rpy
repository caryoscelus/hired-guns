init python:
    renpy.store._vn_mode = 'adv'
    def vn_mode(value):
        renpy.store._vn_mode = value
    
    class CombinedCharacter(object):
        def __init__(self, *args, **kwargs):
            kwargs_adv = kwargs.copy()
            kwargs_adv['kind'] = adv
            print(Character)
            self.adv = Character(*args, **kwargs_adv)
            kwargs_nvl = kwargs.copy()
            kwargs_nvl['kind'] = nvl
            self.nvl = Character(*args, **kwargs_nvl)
        def __call__(self, *args, **kwargs):
            if _vn_mode == 'nvl':
                return self.nvl(*args, **kwargs)
            elif _vn_mode == 'adv':
                return self.adv(*args, **kwargs)
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
