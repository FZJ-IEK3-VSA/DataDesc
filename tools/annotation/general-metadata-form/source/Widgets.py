import ipywidgets as widgets
import datetime

fullWidthLayout = widgets.Layout(width="auto", height="auto")
style_kwargs = { 'layout' : fullWidthLayout, 'style' : {'description_width': 'initial'} }
prop_names = []


def label_to_prop(plaintext):
    label_dict = {
        "Identifier" : "identifier",
        "Software Title" : "title",
        "Description" : "description",
        "Contact" : "contact",
        "License" : "license",
        "Version" : "version",
        "Code Repository" : "codeRepository",
        "Programming Languages" : "programmingLanguages",
        "Download URL" : "downloadUrl",
        "Authors" : "authors",
        "Copyright Holders" : "copyrightHolders",
        "Copyright Year" : "copyrightYear",
        "Date Published" : "datePublished",
        "Keywords" : "keywords",
        "Fundings" : "fundings",
        "Funders" : "funders",
        "Reference Publication" : "referencePublication",
        "README" : "readme",
        "Given Name" : "givenName",
        "Additional Name" : "additionalName",
        "Family Name" : "familyName",
        "Honorific Prefix" : "honorificPrefix",
        "Honorific Suffix" : "honorificSuffix",
        "Affiliation" : "affiliation",
        "Job Title" : "jobTitle",
        "URL" : "url",
        "E-Mail" : "email",
        "Telephone" : "telephone",
        "Legal Name" : "legalName",
        "Alternate Name" : "alternateName",
        "Headline" : "headline",
        "Date Published" : "datePublished",
        "Journal" : "journal",
        "Volume Number" : "volumeNumber",
        "Page Start" : "pageStart",
        "Page End" : "pageEnd",
        "Name" : "name",
    }

    ret_text = label_dict[plaintext] if plaintext in label_dict else plaintext

    return ret_text
class DictObject(object):    
    def __init__(self, props, accordion=False, accordionTitle="Accordion"):
        global prop_names
        children = []


        for prop_name, prop_values in props.items():
            if prop_name in prop_names:
                prop_name = f"{prop_name}"

            prop_names.append(prop_name)

            new_child = prop_values["type"]( 
                                    description=f"{prop_values["desc"]}", 
                                    ref_title=prop_name, 
                                    **style_kwargs
                                )

            children.append( new_child )
        
        self.id = id
        self.children = children
        self.w = widgets.VBox( self.children, layout=fullWidthLayout )

        if accordion:
            #accordion_vbox = widgets.VBox( self.children, layout=fullWidthLayout )
            self.w = widgets.Accordion(
                [ self.w ], 
                titles = [ accordionTitle ],
                layout=fullWidthLayout )
        
        
    
    def get_widget(self):
        return self.w
    
    def get_tuple(self):
        return (self.id, self.w.value)
    
    def get_json(self):       
        widget_json = { label_to_prop(child.description) : child.value for child in self.children if not isinstance(child, widgets.HTML) and child.value }
        return widget_json

    def get_widget(self):
        return self.w


class TextWidget(object):
    def __init__(self, desc, id, **style_kwargs):
        self.w = widgets.Text(description=desc, ref_title=id, **style_kwargs)
        self.id = id
    
    def __str__(self):
        return self.id
    
    def get_widget(self):
        return self.w
    
    def get_tuple(self):
        return (self.id, self.w.value)
    
    def get_widget(self):
        return self.w
    
    def get_json(self):
        return { self.id : self.w.value } if self.w.value else {}
    
class DatePickerWidget(object):
    def __init__(self, desc, id, **style_kwargs):
        self.w = widgets.DatePicker(description=desc, ref_title=id, **style_kwargs)
        self.id = id

    def get_widget(self):
        return self.w
    
    def __str__(self):
        return self.id
    
    def to_tuple(self):
        return (self.id, self.w.value)
    
    def get_widget(self):
        return self.w
    
    def get_json(self):
        if self.w.value is None: return {}
        
        datetime_obj = datetime.datetime.combine(self.w.value, datetime.time())
        return { self.id : datetime_obj.strftime("%Y-%m-%d") }

class ContactWidget(object):
    def __init__(self, id):
        contact_props = {
            "name" : {
                "desc" : "Name",
                "type" : widgets.Text,
                },
            "email" : {
                "desc" : "E-Mail",
                "type" : widgets.Text,
                },
            "url" : {
                "desc" : "URL",
                "type" : widgets.Text,
                },
        }
        
        self.w = DictObject(contact_props, accordion=True, accordionTitle="Contact")
        self.id = id

    def get_widget(self):
        return self.w.get_widget()
    
    def get_tuple(self):
        return (self.id, self.w.get_json())
    
    def get_json(self):
        return self.w.get_json()
    
class LicenseWidget(object):
    def __init__(self, id):
        license_props = {
            "name" : {
                "desc" : "Name",
                "type" : widgets.Text,
                },
            "identifier" : {
                "desc" : "Identifier",
                "type" : widgets.Text,
                },
            "url" : {
                "desc" : "URL",
                "type" : widgets.Text,
                },
        }
        
        self.w = DictObject(license_props, accordion=True, accordionTitle="License")
        self.id = id

    def get_widget(self):
        return self.w.get_widget()
    
    def get_tuple(self):
        return (self.id, self.w.get_json())
    
    def get_json(self):
        return self.w.get_json()
    

class PersonWidget(object):
    def __init__(self, id=None):
        person_props = {
            "identifier" : {
                "desc" : "Identifier",
                "type" : widgets.Text,
                },
            "givenName" : {
                "desc" : "Given Name",
                "type" : widgets.Text,
                },
            "additionalName" : {
                "desc" : "Additional Name",
                "type" : widgets.Text,
                },
            "familyName" : {
                "desc" : "Family Name",
                "type" : widgets.Text,
                },
            "honorificPrefix" : {
                "desc" : "Honorific Prefix",
                "type" : widgets.Text,
                },
            "honorifixSuffix" : {
                "desc" : "Honorific Suffix",
                "type" : widgets.Text,
                },
            "affiliation" : {
                "desc" : "Affiliation",
                "type" : widgets.Text,
                },
            "jobTitle" : {
                "desc" : "Job Title",
                "type" : widgets.Text,
                },
            "url" : {
                "desc" : "URL",
                "type" : widgets.Text,
                },
            "email" : {
                "desc" : "E-Mail",
                "type" : widgets.Text,
                },
            "telephone" : {
                "desc" : "Telephone",
                "type" : widgets.Text,
                },
        }
        
        self.w = DictObject(person_props, accordion=True, accordionTitle="Person")
        self.id = id

    def get_widget(self):
        return self.w.get_widget()
    
    def get_tuple(self):
        return (self.id, self.w.get_json())
    
    def get_json(self):
        return self.w.get_json()
    
class OrganizationWidget(object):
    def __init__(self, id=None):
        organization_props = {
            "legalName" : {
                "desc" : "Legal Name",
                "type" : widgets.Text,
                },
            "alternateName" : {
                "desc" : "Alternate Name",
                "type" : widgets.Text,
                },
            "url" : {
                "desc" : "URL",
                "type" : widgets.Text,
                },
            "email" : {
                "desc" : "E-Mail",
                "type" : widgets.Text,
                },
            "telephone" : {
                "desc" : "Telephone",
                "type" : widgets.Text,
                },
        }
        
        self.w = DictObject(organization_props, accordion=True, accordionTitle="Organization")
        self.id = id

    def get_widget(self):
        return self.w.get_widget()
    
    def get_tuple(self):
        return (self.id, self.w.get_json())
    
    def get_json(self):
        return self.w.get_json()
    

class ScholarlyArticle(object):
    def __init__(self, id):
        scholarly_article_props = {
            "identifier" : {
                "desc" : "Identifier",
                "type" : widgets.Text,
                },
            "headline" : {
                "desc" : "Headline",
                "type" : widgets.Text,
                },
            "authors" : {
                "desc" : "Authors",
                "type" : widgets.Text,
                },
            "datePublished" : {
                "desc" : "Date Published",
                "type" : widgets.DatePicker,
                },
            "journal" : {
                "desc" : "Journal",
                "type" : widgets.Text,
                },
            "volumeNumber" : {
                "desc" : "Volume Number",
                "type" : widgets.Text,
                },
            "pageStart" : {
                "desc" : "Page Start",
                "type" : widgets.Text,
                },
            "pageEnd" : {
                "desc" : "Page End",
                "type" : widgets.Text,
                },
        }
        
        self.w = DictObject(scholarly_article_props, accordion=True, accordionTitle="Scholarly Article")
        self.id = id

    def get_widget(self):
        return self.w.get_widget()
    
    def get_tuple(self):
        return (self.id, self.w.get_json())
    
    def get_json(self):
        return self.w.get_json()
    
class ORWidget(object):
    def __init__(self, option1, option2, option_labels = ["Option 1", "Option 2"]):
        btn_opt1 = widgets.Button(description=option_labels[0])
        btn_opt2 = widgets.Button(description=option_labels[1])
        self.active_option = ORWidget.create_instance(option1)

        btn_list = widgets.HBox( [ btn_opt1, btn_opt2 ])##, layout=fullWidthLayout )

        switch_list = widgets.VBox( [ btn_list, widgets.HTML("<div></div>"), self.active_option.get_widget() ], **style_kwargs)##, layout=fullWidthLayout )

        def on_btn1_clicked(arg):
            self.active_option = ORWidget.create_instance(option1)
            switch_list.children = list( switch_list.children[:2] ) + [ self.active_option.get_widget() ]

        def on_btn2_clicked(arg):
            self.active_option = ORWidget.create_instance(option2)
            switch_list.children = list( switch_list.children[:2] ) + [ self.active_option.get_widget() ]

        btn_opt1.on_click( on_btn1_clicked )
        btn_opt2.on_click( on_btn2_clicked )

        self.w = switch_list

    @staticmethod
    def create_instance(of):
        return of() if callable(of) else of

    def get_widget(self):
        return self.w
    
    def get_json(self):
        return { "a" : "b" }
        return { self.active_option.id : self.active_option.get_json() }
        return self.w.children[2].get_json()
    
class ArrayWidget(object):
    def __init__(self, id, of):
        self.instance_list = []
        btn_expand = widgets.Button(description="+")
        
        of_instance = ArrayWidget.create_instance( of )

        of_list = widgets.VBox( [ of_instance.get_widget(), btn_expand ])## layout=fullWidthLayout)

        def on_btn_clicked(arg):
            new_instance = ArrayWidget.create_instance( of )
            self.instance_list += [ new_instance ]
            #of_list.children = list( of_list.children[:-1] ) + [widgets.HTML("<hr>")] + [ new_instance.get_widget() ] + [ btn_expand ]
            of_list.children = list( of_list.children[:-1] ) + [ new_instance.get_widget() ] + [ btn_expand ]


        btn_expand.on_click( on_btn_clicked )

        self.w = of_list
        self.id = id

    @staticmethod
    def create_instance(obj):
        if isinstance(obj, list):
            inst = ArrayWidget.create_instance(obj[0](ArrayWidget.create_instance(obj[1]), ArrayWidget.create_instance(obj[2]), obj[3]))
            #inst = ArrayWidget.create_instance( obj[0]( obj[1], obj[2] ), obj[3] )
            return inst
        return obj() if callable(obj) else obj
        

    def get_widget(self):
        return self.w
    
    @staticmethod
    def __get_json( obj ):
        widget_json = {}

        if isinstance(obj, (widgets.HTML, widgets.Button)):
            return
        
        if isinstance( obj, (widgets.VBox, widgets.Accordion) ):
            for c in obj.children:
                if isinstance( c, (widgets.HTML, widgets.Button) ):
                    continue

                elif isinstance( c, (widgets.VBox, widgets.Accordion) ):
                    widget_json.update( ArrayWidget.__get_json(c) )

                elif isinstance( c, ORWidget ):
                    widget_json.update( c.get_json() )

                elif isinstance( c, (widgets.Text, widgets.Textarea, widgets.DatePicker) ):
                    widget_json[ label_to_prop(c.description) ] = c.value

        widget_json = { k : v for k,v in widget_json.items() if v }
        return widget_json
    
    def get_json(self):
        json_list = [ ArrayWidget.__get_json(child) for child in self.w.children[:-1] ]           
        json_list = [ j for j in json_list if j ]
        return { self.id :  json_list }