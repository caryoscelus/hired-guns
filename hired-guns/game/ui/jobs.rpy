screen jobs:
    tag main_view
    default job = None
    hbox:
        ypos STATUS_PANEL_HEIGHT
        vbox:
            text "Jobs"
            viewport:
                xfill False
                draggable True
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    for mission in world.missions:
                        textbutton mission.name action SetScreenVariable('job', mission) text_bold (mission is job)
        vbox:
            if job:
                text job.name
                text "Description:"
                text "{}".format(job.description.strip())
                text "Tags: {}".format(str(list(job.tags)).replace('[', '').replace(']', ''))
                text "Reward: {}".format(job.payment)
            else:
                text "Choose mission to see its description"
