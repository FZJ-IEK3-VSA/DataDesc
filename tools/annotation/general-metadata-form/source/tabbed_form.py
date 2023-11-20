import ipywidgets as widgets
from IPython.display import display, FileLink

fullWidthLayout = widgets.Layout(width="100%", height="auto")
layout = widgets.Layout(width="auto", height="40px")
style = {'description_width' : 'initial'}
tab = widgets.Tab(layout=fullWidthLayout)
meta_file = FileLink("./meta.yaml", result_html_prefix="Download meta.yaml")

def _tab_setup(title, tab_contents, tab_contents_titles, content_types):
    global layout
    global style

    base_args = { 'layout' : layout, 'style' : style }

    children = [content_types[i](description=name, ref_title=tab_contents_titles[i], **base_args) for i, name in enumerate(tab_contents)]
    
    for i in range(len(children)):
        children[i].ref_title = tab_contents_titles[i]

    if any(isinstance(child, widgets.Button) for child in children):
        _children = []
        for child in children:
            if isinstance(child, widgets.Button):
                child.on_click(on_button_clicked_simple)
            _children.append(child)
        children = _children
    return (title, children)


def software_md():
    title = 'Software Metadata'
    tab_contents = ['Software Title', 'Description', 'Creation Date', 'First Release Date', 'License']
    tab_contents_titles = ['title', 'desc', 'cdate', 'frdate', 'license']
    content_types = [widgets.Text, widgets.Textarea, widgets.DatePicker, widgets.DatePicker, widgets.Text]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def discoverability():
    title = 'Discoverability and Citation'
    tab_contents = ['Unique Identifier', 'Application Category', 'Keywords', 'Funding', 'Funder']
    tab_contents_titles = ['uid', 'appcat', 'keywords', 'funding', 'funder']
    content_types = [widgets.Text, widgets.Text, widgets.Text, widgets.Text, widgets.Text]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def dev_community():
    title = 'Development Community / Tools'
    tab_contents = ['Code Repository', 'Continuous Integration', 'Issue Tracker', 'Related Links']
    tab_contents_titles = ['crepo', 'ci', 'issuetracker', 'related']
    content_types = [widgets.Text, widgets.Text, widgets.Text, widgets.Textarea]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def runtime():
    title = 'Run-Time Environment'
    tab_contents = ['Programming Language', 'Runtime Platform', 'Operating System', 'Other Requirements']
    tab_contents_titles = ['plang', 'rplat', 'os', 'req']
    content_types = [widgets.Text, widgets.Text, widgets.Text, widgets.Textarea]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def current_version():
    title = 'Current Software Release'
    tab_contents = ['Version Number', 'Release Date', 'Download URL', 'Release Notes']
    tab_contents_titles = ['verno', 'rdate', 'durl', 'relnotes']
    content_types = [widgets.Text, widgets.DatePicker, widgets.Text, widgets.Textarea]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def additional_info():
    title = 'Additional Info'
    tab_contents = ['Reference Publication', 'Development Status', 'Is Part Of']
    tab_contents_titles = ['refpub', 'devstatus', 'partof']
    content_types = [widgets.Text, widgets.Text, widgets.Text]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def authors():
    title = 'Authors'
    tab_contents = ['First Name', 'Last Name', 'Email Adress', 'URI', 'Affiliation', ]#'Add Author']
    tab_contents_titles = ['fname', 'lname', 'email', 'uri', 'affiliation', ]#'btn_add_author']
    content_types = [widgets.Text, widgets.Text, widgets.Text, widgets.Text, widgets.Text, widgets.Button]
    return _tab_setup(title, tab_contents, tab_contents_titles, content_types)

def on_button_clicked_simple(b):
    print("Clicked")

def tabbed_layout():
    global fullWidthLayout
    global tab
    smd = software_md()
    dis = discoverability()
    dev = dev_community()
    run = runtime()
    cur = current_version()
    add = additional_info()
    aut = authors()

    tabs = [smd, dis, dev, run, cur, add, aut]

    tab_titles = [str(t[0]) for t in tabs]
    tab_contents = [t[1] for t in tabs]

    children = []
    for i in range(len(tabs)):
        vbox = widgets.VBox(tab_contents[i], layout=fullWidthLayout)
        hbox = widgets.HBox([vbox], layout=fullWidthLayout)
        children.append(hbox)

    tab.children = children
    
    for i, title in enumerate(tab_titles):
        tab.set_title(i, title)

    display(tab)

    setup_generate_yaml()

## EXPORT TO YAML
def input_to_yaml():
    # create dict
    spec = { "openapi" : "3.0.0" }

    # fill info with input
    sinfo = {}

    global tab

    widgets_values = {}

    for child in tab.children:
        #print(child)
        for widget in child.children[0].children:
            if not isinstance(widget, widgets.Button):
                widgets_values[widget.ref_title] = widget.value if widget.value != None else ''

    sinfo["title"] = widgets_values['title']
    sinfo["version"] = str( widgets_values['verno'] )
    sinfo["description"] = widgets_values['desc']
    sinfo["contact"] = { "name" : widgets_values['fname'] + " " + widgets_values['lname'] , 
                        "email" : widgets_values['email'],
                        "url" : widgets_values['uri'],
                        "x-affiliation" : widgets_values['affiliation'] }
    sinfo["license"] = { "name" : widgets_values['license'] }
    sinfo["x-created"] = str( widgets_values['cdate'] )
    sinfo["x-first-release"] = str( widgets_values['frdate'] )
    sinfo["x-programming-lang"] = widgets_values['plang']
    sinfo["x-platform"] = widgets_values['rplat']
    sinfo["x-os"] = widgets_values['os']
    sinfo["x-id"] = str( widgets_values['uid'] )
    sinfo["x-category"] = widgets_values['appcat']
    sinfo["x-keywords"] = widgets_values['keywords']
    sinfo["x-funding"] = widgets_values['funding']
    sinfo["x-funder"] = widgets_values['funder']
    sinfo["x-repository"] = widgets_values['crepo']
    sinfo["x-ci"] = widgets_values['ci']
    sinfo["x-issue-tracker"] = widgets_values['issuetracker']
    sinfo["x-related-links"] = widgets_values['related']
    sinfo["x-download-url"] = widgets_values['durl']
    sinfo["x-release-notes"] = widgets_values['relnotes']
    sinfo["x-reference-pub"] = widgets_values['refpub']
    sinfo["x-dev-status"] = widgets_values['devstatus']
    sinfo["x-part-of"] = widgets_values['partof']

    sinfo = {key : val for key, val in sinfo.items() if (val is not None and val != '')}

    spec["info"] = sinfo

    import yaml
    with open('meta.yaml', 'w+') as f:
        yaml.dump(spec, f, allow_unicode=True)

def on_button_clicked(b):
    global meta_file
    input_to_yaml()
    display(meta_file)


def setup_generate_yaml():
    ## DISPLAY BUTTON
    button = widgets.Button(description="Generate meta.yaml")
    output = widgets.Output()

    display(button, output)
        
    button.on_click(on_button_clicked)