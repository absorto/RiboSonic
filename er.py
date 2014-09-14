# coding: utf8

import pyglet


from loop import DnaLoop
import scales




b_loop = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

a_loop = loop_from_dna("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# create a loop object
l = Loop( a_loop,
          scales.persian,
          bpm = 120.0,
          x = 0, y=400,
          height=100, width=1140, midi_chan=14)

# create a loop object
ll = Loop( b_loop,
           scales.persian,
           bpm = 120.0,
           x = 0, y=0,
           height=100, width=1140, midi_chan=34, midi_port=u'TiMidity port 1')


# main window, move to EndoplasmicReticulum init?
window = pyglet.window.Window(height=800, width=1280)

er = EndoplasmicReticulum()

er.riboplayers.append( DnaLoop( abo_fasta,
                                midi_sink,
                                bpm=120.0 ) )
                                
pyglet.clock.schedule_interval(er.update_displays, 1/60.0) # Update at 60Hz = 1/60

# move this to loop init?
# pyglet.clock.schedule_interval(er.play_at_heads, l.bpm)               


pyglet.clock.schedule_interval(l.update_playhead_display, 1/60.0) # Update at 60Hz = 1/60
pyglet.clock.schedule_interval(l.play_at_head, l.bpm)

pyglet.clock.schedule_interval(ll.update_playhead_display, 1/60.0) # Update at 60Hz = 1/60
pyglet.clock.schedule_interval(ll.play_at_head, ll.bpm)



pyglet.app.run()
