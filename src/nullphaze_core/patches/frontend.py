# Removing attract-video files leaves their timer/relay graph behind. Keep the native script
# recipe paired with file removal, separate from MP3Update's A-button-start edit. Boundary
# names here: apply_frontend.
"""Frontend script edits paired with the exporter's attract-video removal."""

def apply_frontend(add_static):
    # Removing THPs alone leaves the timer/relay path behind. Keep the script
    # recipe paired with the file removal, independent of MP3Update's A-button edit.
    add_static('FrontEndPatches.patch_attract_videos')
