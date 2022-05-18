image sam 1a:
    "mod-assets/Jetstream_sam.webp"
    zoom 2

image raiden 1a:
    "mod-assets/Raiden.png"
    zoom 1.4

image armstrong 1a:
    "mod-assets/Armstrong.webp"

image bladewolf 1a:
    "mod-assets/bladewolf.png"
    zoom 1
    xzoom -1.00

transform tcommonraiden(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.2
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.2

transform tcommonblade(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 0.9
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 0.9

transform tr41:
    tcommonraiden(200)
transform tr42:
    tcommonraiden(493)
transform tr43:
    tcommonraiden(786)
transform tr44:
    tcommonraiden(1080)
transform tr31:
    tcommonraiden(240)
transform tr32:
    tcommonraiden(640)
transform tr33:
    tcommonraiden(1040)
transform tr21:
    tcommonraiden(400)
transform tr22:
    tcommonraiden(880)
transform tr11:
    tcommonraiden(640)

transform tb41:
    tcommonblade(200)
transform tb42:
    tcommonblade(493)
transform tb43:
    tcommonblade(786)
transform tb44:
    tcommonblade(1080)
transform tb31:
    tcommonblade(240)
transform tb32:
    tcommonblade(640)
transform tb33:
    tcommonblade(1040)
transform tb21:
    tcommonblade(400)
transform tb22:
    tcommonblade(880)
transform tb11:
    tcommonblade(640)

#Music
define audio.totikfr = "mod-assets/totikfr.wav"
define audio.rules = "<from 54.1>mod-assets/ron.wav"

#Characters
define sam = DynamicCharacter('sam_name', image='sam', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define raiden = DynamicCharacter('raiden_name', image='raiden', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define armstrong = DynamicCharacter('arm_name', image='armstrong', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define bladewolf = DynamicCharacter('blade_name', image='bladewolf', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
