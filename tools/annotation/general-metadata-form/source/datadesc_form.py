import ipywidgets as widgets
from IPython.display import display, FileLink
from .Widgets import *

fullWidthLayout = widgets.Layout(width="auto", height="auto")
layout = widgets.Layout(width="auto", height="40px")
style_kwargs = { 'layout' : fullWidthLayout, 'style' : {'description_width': 'initial'} }
style = {'description_width' : 'initial'}
tab = widgets.Tab(layout=fullWidthLayout)
meta_file = FileLink("./meta.json", result_html_prefix="Download meta.json")
output = widgets.Textarea()
prop_names = []

smd_tab = None
allwidgets = []

def tabbed_layout():
    global fullWidthLayout
    global tab

    # Headers and Horizontal Lines
    show_headers = True
    sh_tag = "h4"
    sh_style = "style='margin-left: 0ch; margin-bottom: 0; padding-bottom: 0;'"
    header_smd = widgets.HTML(value="<h2>Software Metadata</h2>")
    header_contact = widgets.HTML(value=f"<{sh_tag} {sh_style}>Contact Info</{sh_tag}>")
    header_license = widgets.HTML(value=f"<{sh_tag} {sh_style}>License Info</{sh_tag}>")
    header_authors = widgets.HTML(value=f"<{sh_tag} {sh_style}>Authors</{sh_tag}>")
    header_cholders = widgets.HTML(value=f"<{sh_tag} {sh_style}>Copyright Holders</{sh_tag}>")
    header_funders = widgets.HTML(value=f"<{sh_tag} {sh_style}>Funders</{sh_tag}>")
    br = widgets.HTML(value="<br>")

    
    identifier = TextWidget(desc="Identifier", id="identifier", **style_kwargs)
    title = TextWidget(desc="Software Title", id="title", **style_kwargs)
    description = TextWidget(desc="Description", id="description", **style_kwargs)
    
    contact = ContactWidget(id="contact")

    license = LicenseWidget(id="license")

    version = TextWidget(desc="Version", id="version", **style_kwargs)
    codeRepository = TextWidget(desc="Code Repository", id="codeRepository", **style_kwargs)
    programmingLanguages = TextWidget(desc="Programming Languages", id="programmingLanguages", **style_kwargs)
    downloadUrl = TextWidget(desc="Download URL", id="downloadUrl", **style_kwargs)

    authors = ArrayWidget( "authors", PersonWidget )

    copyrightHolders = ArrayWidget( "copyrightHolders", [ 
                            ORWidget, 
                            PersonWidget, 
                            OrganizationWidget,
                            ["Person", "Organization"] 
                            ] )
    
    copyrightYear = TextWidget(desc="Copyright Year", id="copyrightYear", **style_kwargs)
    datePublished = DatePickerWidget(desc="Date Published", id="datePublished", **style_kwargs)
    keywords = TextWidget(desc="Keywords", id="keywords", **style_kwargs)

    funders = ArrayWidget( "funders", [ 
                            ORWidget, 
                            PersonWidget, 
                            OrganizationWidget,
                            ["Person", "Organization"]
                            ] )
    
    fundings = TextWidget(desc="Funding sources", id="fundings", **style_kwargs)
    reference_publication = TextWidget(desc="Reference Publication", id="referencePublication", **style_kwargs)
    readme = TextWidget(desc="README", id="readme", **style_kwargs)


    global smd_tab
    global allwidgets

    allwidgets += [ identifier, title, description, contact, 
                   license, version, codeRepository, programmingLanguages, 
                   downloadUrl, authors, copyrightHolders, copyrightYear, 
                   datePublished, keywords, funders, fundings, reference_publication, 
                   readme ]

    if show_headers:
        smd_tab = widgets.VBox( [
            header_smd,
            allwidgets[0].get_widget(), 
            allwidgets[1].get_widget(), 
            allwidgets[2].get_widget(), 
            header_contact, allwidgets[3].get_widget(), 
            br,
            header_license, allwidgets[4].get_widget(), 
            br,
            allwidgets[5].get_widget(), 
            allwidgets[6].get_widget(), 
            allwidgets[7].get_widget(), 
            allwidgets[8].get_widget(), 
            header_authors, allwidgets[9].get_widget(),
            br,
            header_cholders, allwidgets[10].get_widget(), 
            br,
            allwidgets[11].get_widget(), 
            allwidgets[12].get_widget(), 
            allwidgets[13].get_widget(), 
            header_funders, allwidgets[14].get_widget(), 
            br,
            allwidgets[15].get_widget(), 
            allwidgets[16].get_widget(), 
            allwidgets[17].get_widget() ], layout=fullWidthLayout )

    else:
        smd_tab = widgets.VBox( [
            identifier, 
            title, 
            description, 
            contact, 
            license, 
            version, 
            codeRepository, 
            programmingLanguages, 
            downloadUrl, 
            authors,
            copyrightHolders, 
            copyrightYear, 
            datePublished, 
            keywords, 
            funders, 
            fundings, 
            reference_publication, 
            readme ], layout=fullWidthLayout )
    
    ##smd_tab = widgets.VBox([header1, test_or, hr], layout=fullWidthLayout)

    ui = widgets.VBox([smd_tab], layout=fullWidthLayout)

    display(ui)


    setup_generate_yaml()

## EXPORT TO YAML
def input_to_json():
    # create dict
    spec = { "openapi" : "3.0.0", "dataDescVersion" : "1.0" }

    # fill info with input
    sinfo = {}

    global smd_tab
    global output
    global allwidgets

    widgets_values = {}

    try:
        for w in allwidgets:
            if isinstance(w, (TextWidget, 
                              DatePickerWidget, 
                              )):
                if w.id in ["identifier", "title", "description", "contact", "license", "version", "codeRepository",
                            "programmingLanguages", "downloadUrl", "authors", "copyrightHolders", "copyrightYear",
                            "datePublished", "keywords", "funders", "fundings", "reference_publication", "readme"]:
                    w_json = w.get_json()
                    w_json = { k : v for k,v in w_json.items() if v }
                    
                    sinfo |= w_json
                #output.value += f"{str( w.id )}({str(type(w).__name__)}) : { w.get_widget().value } \n"

            elif isinstance(w, (ContactWidget, 
                              LicenseWidget, 
                              PersonWidget, 
                              OrganizationWidget, 
                              ScholarlyArticle)):
                if w.id in ["contact", "license", "authors", "copyrightHolders", "funders"]:
                    w_json = w.get_json()
                    w_json = { k : v for k,v in w_json.items() if v }

                    sinfo[w.id] = {}
                    sinfo[w.id] = w_json

            elif isinstance(w, ORWidget):
                output.value += "OR"
                try:
                    w_json = w.get_json()
                    w_json = { k : v for k,v in w_json.items() if v }
                    sinfo[w.id] = w_json[w.id]
                    #output.value += str( w_json ) + "\n"
                except Exception as e:
                    output.value += str(e)
            
            elif isinstance(w, ArrayWidget):
                try:
                    w_json = w.get_json()
                    w_json = { k : v for k,v in w_json.items() if v }
                    sinfo[w.id] = w_json[w.id]
                except Exception as e:
                    output.value += str(e)
    except Exception as e:
        output.value = str(e)

    sinfo = { k : v for k,v in sinfo.items() if v }
    
    spec["info"] = sinfo
    output.value = str(spec)

    import json
    with open('meta.json', 'w+') as f:
        json.dump(spec, f, indent=4)

def on_button_clicked(b):
    global meta_file
    input_to_json()
    display(meta_file)


def setup_generate_yaml():
    ## DISPLAY BUTTON
    button = widgets.Button(description="Generate meta.json")

    display(button, output)
        
    button.on_click(on_button_clicked)