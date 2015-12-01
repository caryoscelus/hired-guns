init python:
    PORTRAIT_ZOOM = 0.3333

init -1 python:
    from style import apply_margins, VNMode, init_vn_modes, vn_mode, push_mode, set_window_margins, set_window_position, set_text_color, pop_mode, CombinedCharacter

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
